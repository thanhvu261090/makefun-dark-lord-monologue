#!/usr/bin/env python3
"""The Tired Dark Lord: a 100-word villain monologue.

Entry for the make.fun bounty of the same name. This program holds one
fixed monologue, checks it against the bounty gate, and then prints it
to stdout exactly as written -- no trailing newline, no extra text --
and writes the identical bytes to /output/entry.txt.

Python 3, standard library only, no network access.

Usage:
    python3 main.py              # print the monologue, write entry.txt
    python3 main.py --self-test  # validate the entry and report counts
"""

import os
import sys

# The entry: 102 words, 545 characters. The tiredness lives in the
# voice, the rhythm and the small deflections, never in a plain claim
# of weariness -- and the speaker is still a villain, with a scheme
# (the crown, the curse, the surrender) and a history (three centuries
# on the mountain).
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

OUTPUT_PATH = "/output/entry.txt"
EXPECTED_WORDS = 102
EXPECTED_CHARS = 545


def check_entry(text):
    """Validate one entry string against the bounty gate.

    Raises ValueError with a plain message when the gate fails.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    text.encode("utf-8")  # raises if the text is not valid UTF-8
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= 600:
        raise ValueError(
            "entry is %d characters; the gate allows 1-600" % len(text)
        )


def word_count(text):
    return len(text.split())


def run():
    """Validate the entry, write it to disk, print it to stdout."""
    check_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    # Read the file back and make sure what landed on disk is byte for
    # byte the entry we validated -- a partial or recoded write must
    # fail loudly here instead of silently shipping a wrong entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != ENTRY:
            raise ValueError("entry.txt on disk does not match ENTRY")
    # stdout carries the monologue alone, byte for byte; the status
    # line goes to stderr so nothing else pollutes the output.
    sys.stdout.write(ENTRY)
    sys.stdout.flush()
    print(
        "wrote %s: %d chars, %d words"
        % (OUTPUT_PATH, len(ENTRY), word_count(ENTRY)),
        file=sys.stderr,
    )


def self_test():
    """Run the entry checks and report the counts."""
    check_entry(ENTRY)
    words = word_count(ENTRY)
    chars = len(ENTRY)
    assert words == EXPECTED_WORDS, "word count is %d, expected %d" % (
        words,
        EXPECTED_WORDS,
    )
    assert chars == EXPECTED_CHARS, "char count is %d, expected %d" % (
        chars,
        EXPECTED_CHARS,
    )
    assert ENTRY.encode("utf-8")
    print(
        "self-test passed: %d words, %d chars, UTF-8, no trailing newline"
        % (words, chars)
    )


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
    else:
        run()
