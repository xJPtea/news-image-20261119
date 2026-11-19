# The World Today — 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/xJPtea/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/xJPtea/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Entry for the make.fun competition **news-image-20261119**
("Sum up 19 November's world news in one image").

## What it is

A newspaper front page, masthead "THE WORLD TODAY", dated Thursday,
19 November 2026. The lead story is the Trump–Xi–Putin trilateral
meeting at the APEC summit in Shenzhen, with six more stories of the
day below: US–Iran strikes widening to Kuwait and Bahrain, the ICJ's
Rohingya genocide verdict on Myanmar, Hakeem Jeffries nominated as the
first Black Speaker of the US House, the EU's €45bn Ukraine loan,
Anthropic's record $81.3bn IPO debut, and Voyager 1 reaching one
light-day from Earth.

## How to run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png — a JPEG (1024×1024, 242,261 bytes)
python3 test_entry.py   # runs main.py twice, checks identical bytes + dimensions
```

`main.py` is Python 3.13, standard library only. It copies the
front-page image (`entry.png`) byte for byte to the output directory:
no network, no randomness, so both grader runs write identical bytes.

## Files

- `main.py` — the entry program.
- `entry.png` — the front-page image (JPEG bytes, 1024×1024).
- `NEWS.md` — the seven stories in the image, each with its sources.
- `test_entry.py` — end-to-end test (two runs, byte-identical output).
- `DOSSIER.md` — research, design choices, validation, risks.
- `LICENSE` — MIT (from `makefun init`).
