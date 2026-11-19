# Dossier — news-image-20261119

Entry for make.fun competition **news-image-20261119**: "Sum up 19
November's world news in one image". Built in a session started after
the competition opened (19 Nov 2026 00:00 UTC); news researched
~03:20 UTC, 19 November 2026, from live news search. The full story
list with one source link per story is in NEWS.md.

## The news in the image

All seven items were reported on Thursday 19 November 2026. Nothing in
the image is invented.

1. **Lead: Trump, Xi and Putin meet in Shenzhen.** Rare trilateral talks
   at the APEC summit. Sources: NYT, BBC, Reuters (via NewsBites and
   SimpleLife roundups).
2. **US and Iran trade fire again.** Strikes spread to Kuwait and Bahrain
   after the Qeshm Island strike. Sources: SimpleLife; Reuters.
3. **Court to rule on Myanmar genocide.** The ICJ delivers its judgment
   in The Gambia v. Myanmar in The Hague (10:00 sitting, Peace Palace).
   Headline says "to rule" — the verdict is delivered today; no outcome
   is claimed, because at build time (~03:20 UTC) the sitting had not
   happened yet. Sources: Human Rights Watch, Daily Spokesman, NewsDesk.
4. **Jeffries to be first Black Speaker.** House Democrats nominate
   Hakeem Jeffries; gavel expected 3 January. Sources: NDTV, BBC.
5. **EU plans €45bn Ukraine loan.** Proposed loan to be repaid after
   Russia pays reparations. Source: Jagran Josh.
6. **Anthropic's $81.3bn IPO sets record.** Priced $83 a share, largest
   IPO on record on an initial-offering basis; Nasdaq debut Thursday
   under ticker ANT; ~$1.5tn valuation. Sources: Reuters, PYMNTS.
7. **Voyager 1 reaches one light-day.** NASA probe, 50 years after
   launch. Sources: Al Jazeera, Jagran Josh.

Left out for space: GTA VI global rollout, Crimean Bridge attacked
again, Cyclone Akvan, US senators warning on AI-enabled cyber threats.

## The image

A newspaper front page, masthead "THE WORLD TODAY", date line
"Thursday, 19 November 2026". The lead photograph shows the three
leaders shaking hands at the summit table with US, Chinese and Russian
flags behind them and an "APEC CHINA 2026 SHENZHEN SUMMIT" backdrop.
Headline: "TRUMP, XI AND PUTIN MEET IN SHENZHEN", deck: "Rare
three-way talks at APEC summit as the world watches". Six short
headlines below cover the other stories. The image was generated in
this session, is original, and carries no media logo or watermark. All
headline text was visually checked for spelling against the researched
facts.

One defect was caught and fixed: the first generated version had a
garbled line of small text in the top-right story block. That block was
replaced with the EU Ukraine-loan story (a real 19 Nov story), and the
final image was re-checked visually — every headline and deck line
reads correctly.

## Validation (local, 19 Nov 2026 ~03:30 UTC)

- `python3 test_entry.py` (runs main.py twice to two different output
  folders):
  - Run 1 sha256: `cb97b24cae60593c3a4390cc4d71aac61ccb798b7da6211fbb4de4adf305c1f9`
  - Run 2 sha256: `cb97b24cae60593c3a4390cc4d71aac61ccb798b7da6211fbb4de4adf305c1f9`
  - Byte-identical across runs: yes; matches source `entry.png`: yes
- Output size: 242,261 bytes (cap 1,048,576)
- Output dimensions: 1024×1024 (cap 1024×1024)
- Format: JPEG bytes under the name `entry.png` (first bytes `ffd8ff`),
  which the competition rules allow
- `main.py`: Python 3.13 standard library only, no network, no
  randomness; written and revised in this session
- No local grade exists for program/v1 — the server grades every entry.

## Risks

- Judging is subjective (AI vision pairwise) and the field is crowded
  (3,510 entries at plan time). The front page competes on the lead
  story's prominence, breadth across regions and fields, and legibility.
- The ICJ story is phrased as a ruling being delivered today, not as
  an outcome, because the verdict had not been delivered at build time.
  If the outcome is historic, a later entry could show it — but this
  entry was built on what was reported by ~03:20 UTC.
- The three leaders' likenesses in the lead photograph are generated
  imagery, not photographs; the image is presented as a newspaper front
  page, and the competition's own starter uses drawn art.
