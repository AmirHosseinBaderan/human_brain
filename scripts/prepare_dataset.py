from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

from datasets import DatasetDict, load_dataset, load_from_disk


DATASET_ID = "taesiri/TinyStories-Farsi"


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFC", text)

    replacements = {
        "\u064a": "\u06cc",  # ي -> ی
        "\u0649": "\u06cc",  # ى -> ی
        "\u0643": "\u06a9",  # ك -> ک
        "\u200c": "\u200c",  # preserve ZWNJ
        "\ufeff": "",
    }

    for source, target in replacements.items():
        text = text.replace(source, target)

    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    lines = []
    for line in text.split("\n"):
        line = re.sub(r"[ \t]+", " ", line)
        line = line.strip()

        if line:
            lines.append(line)

    return "\n".join(lines).strip()


def is_valid_text(text: str, min_chars: int) -> bool:
    if len(text) < min_chars:
        return False

    persian_chars = len(
        re.findall(r"[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]", text)
    )

    return persian_chars >= 10


class ShardWriter:
    def __init__(self, output_dir: Path, max_chars: int):
        self.output_dir = output_dir
        self.max_chars = max_chars

        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.file_index = 0
        self.current_chars = 0
        self.current_docs = 0
        self.total_chars = 0
        self.total_docs = 0

        self.file = None
        self._open_next()

    def _open_next(self):
        if self.file:
            self.file.close()

        path = self.output_dir / f"part-{self.file_index:05d}.txt"

        self.file = path.open(
            "w",
            encoding="utf-8",
            newline="\n",
        )

        self.file_index += 1
        self.current_chars = 0
        self.current_docs = 0

    def write(self, text: str):
        required_chars = len(text) + 2

        if (
            self.current_chars > 0
            and self.current_chars + required_chars > self.max_chars
        ):
            self._open_next()

        self.file.write(text)
        self.file.write("\n\n")

        self.current_chars += required_chars
        self.current_docs += 1

        self.total_chars += len(text)
        self.total_docs += 1

    def close(self):
        if self.file:
            self.file.close()


def load_source(raw_dir: Path):
    if raw_dir.exists():
        print(f"Loading existing dataset from: {raw_dir}")
        return load_from_disk(str(raw_dir))

    print(f"Downloading dataset: {DATASET_ID}")

    dataset = load_dataset(DATASET_ID)

    raw_dir.parent.mkdir(parents=True, exist_ok=True)
    dataset.save_to_disk(str(raw_dir))

    return dataset


def process_split(
    dataset,
    split_name: str,
    output_dir: Path,
    max_chars: int,
    min_chars: int,
):
    print(f"\nProcessing split: {split_name}")

    writer = ShardWriter(
        output_dir=output_dir,
        max_chars=max_chars,
    )

    skipped_empty = 0
    skipped_short = 0
    skipped_invalid = 0

    seen = set()
    duplicates = 0

    for index, row in enumerate(dataset):
        text = row.get("Persian")

        if not isinstance(text, str):
            skipped_invalid += 1
            continue

        text = normalize_text(text)

        if not text:
            skipped_empty += 1
            continue

        if len(text) < min_chars:
            skipped_short += 1
            continue

        if not is_valid_text(text, min_chars):
            skipped_invalid += 1
            continue

        fingerprint = hash(text)

        if fingerprint in seen:
            duplicates += 1
            continue

        seen.add(fingerprint)

        writer.write(text)

        if (index + 1) % 5000 == 0:
            print(
                f"  processed={index + 1:,} "
                f"documents={writer.total_docs:,} "
                f"chars={writer.total_chars:,}"
            )

    writer.close()

    stats = {
        "split": split_name,
        "documents": writer.total_docs,
        "characters": writer.total_chars,
        "shards": writer.file_index,
        "duplicates": duplicates,
        "skipped_empty": skipped_empty,
        "skipped_short": skipped_short,
        "skipped_invalid": skipped_invalid,
    }

    print("\nResult:")
    print(json.dumps(stats, indent=2, ensure_ascii=False))

    return stats


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--raw-dir",
        type=Path,
        default=Path("data/raw/tiny_stories_fa"),
    )

    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/corpus/tiny_stories_fa"),
    )

    parser.add_argument(
        "--shard-mb",
        type=int,
        default=25,
    )

    parser.add_argument(
        "--min-chars",
        type=int,
        default=20,
    )

    args = parser.parse_args()

    dataset = load_source(args.raw_dir)

    if not isinstance(dataset, DatasetDict):
        raise RuntimeError("Expected a DatasetDict with train/validation splits.")

    max_chars = args.shard_mb * 1024 * 1024

    all_stats = {}

    for split_name in ("train", "validation"):
        if split_name not in dataset:
            continue

        split_output = args.output_dir / split_name

        stats = process_split(
            dataset=dataset[split_name],
            split_name=split_name,
            output_dir=split_output,
            max_chars=max_chars,
            min_chars=args.min_chars,
        )

        all_stats[split_name] = stats

    args.output_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "dataset": DATASET_ID,
        "source": "Hugging Face",
        "text_column": "Persian",
        "normalization": [
            "Unicode NFC",
            "Arabic Yeh -> Persian Yeh",
            "Arabic Kaf -> Persian Kaf",
            "line ending normalization",
            "whitespace normalization",
            "empty line removal",
            "short document filtering",
            "duplicate filtering",
        ],
        "shard_size_mb": args.shard_mb,
        "min_chars": args.min_chars,
        "splits": all_stats,
    }

    manifest_path = args.output_dir / "manifest.json"

    manifest_path.write_text(
        json.dumps(
            manifest,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    print(f"\nManifest written to: {manifest_path}")


if __name__ == "__main__":
    main()