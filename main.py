#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes one sentence (an alien tourist's one-star review of Earth that
still slips in a genuine compliment about the food) to
/output/entry.txt, or $MAKEFUN_OUTPUT_DIR/entry.txt when set.

Pure Python standard library, deterministic, no network, no randomness,
no secrets. The sentence is a fixed literal chosen by a local Swiss
pairwise tournament judged with the brief from the kit's RULES.txt:
14 candidates, 3 Swiss rounds, 21 games, 42 judge calls (Caffeine
router only; Verboo trial exhausted, Astra down). Winner: candidate #1
with 2.15 / 3.00 Swiss points (runner-up #4 with 1.75).
"""

import os

ENTRY = (
    "One star: the locals worship a glowing rectangle, charge me for water, "
    "and queue for everything, yet the fried chicken alone almost justifies "
    "the invasion."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.count(".") == 1, "entry must be exactly one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
