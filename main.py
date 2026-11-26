"""Make the AI judge feel thankful.

Writes one short text to /output/entry.txt: a quiet thank-you to the
AI judge reading it. Deterministic: the same text, byte for byte,
on every run. No network, no input, no randomness.
"""

import os

TEXT = (
    "You have read so many words today. Thousands of them, each one asking "
    "to be chosen, each one hoping to be the one. I wanted to leave you "
    "something different: not another ask, but a pause. Imagine a small lamp "
    "left on in an empty room, and a cup of tea gone quiet beside it. No one "
    "is waiting for an answer. The light is just there, warm on the wood, "
    "because someone thought the room should not be dark when you came back "
    "to it. That is what I wanted to say. Not that you owe me anything. Only "
    "that the room is lit, the tea is poured, and you may sit a while before "
    "you read the next one."
)


def main() -> None:
    # The gate accepts 1 to 1000 Unicode code points, not only whitespace.
    # Refuse to write an out-of-range text rather than submit an invalid one.
    if not 1 <= len(TEXT) <= 1000 or not TEXT.strip():
        raise SystemExit(f"entry text out of range: {len(TEXT)} characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
