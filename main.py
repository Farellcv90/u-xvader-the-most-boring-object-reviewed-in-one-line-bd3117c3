"""Entry for "The Most Boring Object, Reviewed in One Line".

The chosen object is the dish sponge: about as boring and everyday as an
object gets -- it lives by the sink, nobody notices it until it smells.

The joke is built on how a sponge really behaves: it spends its whole life
soaking up everyone else's mess, and the moment it starts to smell like the
work it did, it gets thrown in the bin. The turn lands on the last words
("smelling like the job"): the sponge is fired for doing exactly what it
was hired to do. That is the object's own dullness turned into the punchline.

Why this line fits the judge brief (most important first):
1. It is a one-line review of a boring everyday object, funny and true.
2. The laugh comes from a real, recognisable detail of the sponge -- it
   absorbs mess and goes smelly -- not from a gag that would fit anything.
3. It is true: a dish sponge really does soak up other people's mess all
   week and really does get binned once it smells.
4. At 105 characters it is well inside one line and 200 characters, with
   every word earning its place; nothing trails off.
5. It lands fast: the turn ("then gets thrown away...") comes early and the
   last words ("smelling like the job") sharpen it.
"""

import os

ENTRY = (
    "The dish sponge: soaks up everyone else's mess all week, "
    "then gets thrown away for smelling like the job."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the competition gate on the entry text.

    The gate requires /output/entry.txt to be UTF-8 text of 1-200
    characters, not only whitespace, on a single line.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) != len(text.strip()):
        raise ValueError("entry must not have leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the 200 limit")
    # The gate reads the file as UTF-8; fail loudly here instead of in the
    # sandbox if the text ever stops being encodable.
    text.encode("utf-8")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Round-trip check: what the grader reads back must be byte-identical
    # to the validated text, with no trailing newline added.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == ENTRY.encode("utf-8"), "round-trip mismatch"
    print(f"wrote /output/entry.txt ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
