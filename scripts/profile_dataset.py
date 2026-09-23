from __future__ import annotations

import argparse
import re
from pathlib import Path


WORD_RE = re.compile(r"\S+")
PERSIAN_RE = re.compile(r"[\u0600-\u06FF]")


def iter_documents(file_path: Path):
    text = file_path.read_text(encoding="utf-8")

    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    documents = text.split("\n\n")

    for document in documents:
        document = document.strip()

        if document:
            yield document


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "path",
        type=Path,
    )

    args = parser.parse_args()

    if not args.path.is_dir():
        raise ValueError(f"Not a directory: {args.path}")

    files = sorted(args.path.rglob("*.txt"))

    if not files:
        print("No .txt files found.")
        return

    document_count = 0
    total_chars = 0
    total_words = 0
    estimated_tokens = 0

    min_chars = None
    max_chars = 0

    persian_chars = 0
    letter_chars = 0

    for file_path in files:
        for document in iter_documents(file_path):
            document_count += 1

            chars = len(document)
            words = len(WORD_RE.findall(document))
            tokens = estimate_tokens(document)

            total_chars += chars
            total_words += words
            estimated_tokens += tokens

            min_chars = (
                chars
                if min_chars is None
                else min(min_chars, chars)
            )

            max_chars = max(max_chars, chars)

            persian_chars += len(PERSIAN_RE.findall(document))
            letter_chars += sum(
                1
                for char in document
                if char.isalpha()
            )

    if document_count == 0:
        print("No documents found.")
        return

    average_chars = total_chars / document_count
    average_words = total_words / document_count
    average_tokens = estimated_tokens / document_count

    persian_ratio = (
        persian_chars / letter_chars
        if letter_chars
        else 0
    )

    print()
    print("Dataset Profile")
    print("================")

    print(f"Path:               {args.path}")
    print(f"Shards:             {len(files):,}")
    print(f"Documents:          {document_count:,}")
    print()

    print(f"Characters:         {total_chars:,}")
    print(f"Words:              {total_words:,}")
    print(f"Estimated tokens:   {estimated_tokens:,}")
    print()

    print(f"Min chars/doc:      {min_chars:,}")
    print(f"Average chars/doc:  {average_chars:,.2f}")
    print(f"Max chars/doc:      {max_chars:,}")
    print()

    print(f"Avg words/doc:      {average_words:,.2f}")
    print(f"Avg tokens/doc:     {average_tokens:,.2f}")
    print()

    print(f"Persian char ratio: {persian_ratio:.2%}")


if __name__ == "__main__":
    main()