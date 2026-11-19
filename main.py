"""news-image-20261119 entry (Python 3.13, standard library only).

The entry image is the file ``entry.png`` beside this program: a newspaper
front page summing up the world news of Thursday 19 November 2026
(masthead "THE WORLD TODAY", lead story the Trump-Xi-Putin meeting in
Shenzhen, plus six more stories of the day). The program copies that file
byte for byte to the output directory, so both grader runs write
identical bytes — the competition runs the program twice and requires
both runs to produce the same file. No network, no randomness, no
dependencies.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
JPEG_MAGIC = b"\xff\xd8\xff"
MAX_BYTES = 1_048_576  # competition cap: image at most 1 MiB


def main() -> int:
    source = Path(__file__).resolve().parent / SOURCE_NAME
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = out_dir / SOURCE_NAME

    data = source.read_bytes()
    if not data.startswith(JPEG_MAGIC):
        print(f"error: {source} is not a JPEG image", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"error: {source} is {len(data)} bytes, over the 1 MiB cap",
              file=sys.stderr)
        return 1

    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)

    written = target.read_bytes()
    if written != data:
        print("error: output bytes differ from source", file=sys.stderr)
        return 1

    print(f"wrote {target} ({len(written)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
