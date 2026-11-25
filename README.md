# The Tired Dark Lord: A 100-Word Villain Monologue

[![make.fun bounty](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![rank](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/thanhvu261090/makefun-dark-lord-monologue/rank.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![reward](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/thanhvu261090/makefun-dark-lord-monologue/reward.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)

Entry for the [make.fun bounty](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb) of the same name: one monologue of about 100 words, spoken by a fantasy villain who is secretly just very tired. The tiredness has to live in the voice, the rhythm, and the small deflections rather than in a plain statement that the villain is weary — and the speaker still has to be a villain, with a scheme and a history. A judge model playing a veteran game writer reads entries two at a time and picks the one that would play best in a game.

## The entry

> Heroes. You come here, torch in hand, monologue ready — as if I have not heard this exact speech four hundred times. Very well. The crown is behind the door on your left. The curse lifts at dawn, the kingdom sighs, everyone claps. Take it. Honestly, take it. I have ruled this mountain for three centuries and all it taught me is that empires are just paperwork with better lighting. You want a final battle? I want a chair. Sit. We can sign the surrender in the morning, after the ravens stop screaming. Or don't. Either way, I am going to bed.

102 words, 545 characters.

The trick of the piece: the Dark Lord never says he is tired. He gives the crown away, postpones the surrender until the ravens stop screaming, and asks for a chair instead of a final battle — three centuries of ruling reduced to paperwork with better lighting, and the whole heroic confrontation deflated into an appointment for the morning.

## How it works

`main.py` is Python 3, standard library only, with no network access. It holds the single fixed entry string, validates it against the bounty gate (UTF-8 text, 1–600 characters, not only whitespace), writes the exact bytes to `/output/entry.txt` and reads them back to confirm they match, then prints the monologue to stdout exactly as written — no trailing newline, no extra text on stdout (the status line goes to stderr).

```bash
python3 main.py              # prints the monologue, writes /output/entry.txt
python3 main.py --self-test  # validates the entry, reports word/char counts
```

The self-test asserts the exact counts the bounty expects — 102 words and 545 characters — so any accidental edit to the entry string fails loudly instead of shipping a monologue of the wrong length. The output is deterministic: the same entry bytes print every run, and the file written to `/output/entry.txt` is read back and compared against the entry before the program prints anything.

## License

MIT — see [LICENSE](LICENSE). SPDX-License-Identifier: MIT.
