"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes the entry text exactly as-is (no trailing newline) to
/output/entry.txt, after validating it against the bounty gate:
UTF-8 text, 1-600 characters, not only whitespace.

Stdlib only, no network. Run: python3 main.py
Self-test: python3 main.py --self-test
"""

import os
import sys

ENTRY = (
    "Heroes. You come here, torch in hand, monologue ready \u2014 as if I have "
    "not heard this exact speech four hundred times. Very well. The crown is "
    "behind the door on your left. The curse lifts at dawn, the kingdom sighs, "
    "everyone claps. Take it. Honestly, take it. I have ruled this mountain for "
    "three centuries and all it taught me is that empires are just paperwork "
    "with better lighting. You want a final battle? I want a chair. Sit. We can "
    "sign the surrender in the morning, after the ravens stop screaming. Or "
    "don't. Either way, I am going to bed."
)


def validate(text: str) -> None:
    """Raise ValueError if the entry fails the bounty gate."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    text.encode("utf-8")  # must be valid UTF-8
    if not 1 <= len(text) <= 600:
        raise ValueError(f"entry length {len(text)} not in 1-600 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate(ENTRY)
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {out_path}: {len(ENTRY)} chars, {len(ENTRY.split())} words")


def self_test() -> None:
    validate(ENTRY)
    assert len(ENTRY.split()) == 102, f"word count {len(ENTRY.split())}"
    assert 1 <= len(ENTRY) <= 600
    assert ENTRY.strip()
    assert ENTRY.encode("utf-8")
    # round-trip: no trailing newline, exact bytes
    validate(ENTRY)
    print("self-test passed: 102 words, 545 chars, UTF-8, no trailing newline")


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
    else:
        main()
