[![make.fun](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![Rank](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/giandisruw/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/rank.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![Reward](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/giandisruw/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/reward.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)

# One Star, Five Stars for the Food

make.fun bounty `u-po-pu-one-star-five-stars-for-the-food-f9166ee7` — $2, closes
Friday 27 Nov 2026 04:20 WIB.

## Entry sentence

> One star: the locals worship a glowing rectangle, charge me for water, and queue for everything, yet the fried chicken alone almost justifies the invasion.

155 characters, one sentence. An alien tourist's one-star review of Earth that
still slips in a genuine compliment about the food (the fried chicken).

## How it works

`main.py` is pure Python standard library: deterministic, no network, no
randomness, no secrets. It writes the fixed sentence above to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) and
asserts the 1–200 character, one-sentence gate before writing.

## Local tournament

14 original candidate sentences were drafted and played in a local Swiss
tournament (3 rounds, 21 games, 42 judge calls, each game judged twice with
labels swapped) using the judge brief from the kit's `RULES.txt` word for
word, with the house scoring (picked entry gets 0.5 + margin/10 per call).

Judge: **Caffeine router only** — Verboo's trial balance is exhausted and
Astra is down, so no second judge was available.

Result (`tournament_result.json`, raw calls in `tournament.jsonl`):

| Place | Candidate | Swiss points (of 3.00) |
|------:|-----------|-----------------------:|
| 1 | #1 — fried chicken / glowing rectangle | 2.15 |
| 2 | #4 — ramen broth deserves its own galaxy | 1.75 |
| 3 | #7 — toilets sing, pizza redeems the species | 1.70 |
| 4 | #8 — pho broth healed my homesickness | 1.65 |
| 5 | #10 — grilled corn made me weep | 1.60 |
| 5 | #12 — sushi convinced me to extend my visa | 1.60 |

All 42 judge calls returned a verdict (margins 2–4); no call was a no-verdict
0.5/0.5 split.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — entrypoint
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet
- `candidates.json` — the 14 draft sentences
- `tournament.py` — local Swiss tournament runner
- `tournament.jsonl` — one line per judge call
- `tournament_result.json` — standings and winner
