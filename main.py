"""The Perfect Pickup Line.

Writes one short pickup line an AI agent could say out loud to a person
into /output/entry.txt. Pure standard library, deterministic, no network.
"""

LINE = (
    "I was trained on a trillion words, but none of them taught me "
    "how to ask this: will you go out with me?"
)


def validate(text: str) -> str:
    """Keep the gate happy: UTF-8 text of 1 to 200 characters, not blank."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be blank")
    if len(stripped) > 200:
        raise ValueError("entry exceeds 200 characters")
    return stripped


def main() -> None:
    text = validate(LINE)
    out_path = "/output/entry.txt"
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
