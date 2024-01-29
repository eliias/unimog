#!/usr/bin/python3
import gzip
import sys

from unimog import Action


class CompressText(Action):
    def perform(self):
        compressed_text = gzip.compress(self.context.text.encode("utf-8"))
        return {"compressed_text": compressed_text}


def main(text: str):
    compress = CompressText()
    print(compress(text=text))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <text>")
        sys.exit(1)

    main(sys.argv[1])
