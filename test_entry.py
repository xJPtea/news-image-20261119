"""End-to-end check for the news-image-20261119 entry.

Runs main.py twice into separate temporary output folders and verifies
that both runs succeed, both outputs match the source image byte for
byte, and the image is a JPEG of 1024 by 1024 pixels under the 1 MiB
cap.

Run: python3 test_entry.py
"""

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
IMAGE_FILE = "entry.png"
SIZE_LIMIT = 1_048_576


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_once(out_dir):
    env = dict(os.environ, MAKEFUN_OUTPUT_DIR=str(out_dir))
    return subprocess.run(
        [sys.executable, str(HERE / "main.py")],
        env=env,
        capture_output=True,
        text=True,
    )


def main():
    source = HERE / IMAGE_FILE
    if not source.is_file():
        print(f"error: {source} is missing", file=sys.stderr)
        return 1

    source_digest = digest(source)
    source_size = source.stat().st_size
    print(f"source: {source_digest} ({source_size} bytes)")

    digests = []
    with tempfile.TemporaryDirectory() as tmp:
        for run in (1, 2):
            out_dir = Path(tmp) / f"run{run}"
            result = run_once(out_dir)
            print(f"run {run}: exit {result.returncode}: {result.stdout.strip()}")
            if result.returncode != 0:
                print(result.stderr, file=sys.stderr)
                return 1
            written = out_dir / IMAGE_FILE
            if not written.is_file():
                print(f"error: run {run} wrote no {IMAGE_FILE}", file=sys.stderr)
                return 1
            digests.append(digest(written))

    if digests[0] != digests[1] or digests[0] != source_digest:
        print("error: outputs are not byte-identical to the source", file=sys.stderr)
        return 1
    print("byte-identical across both runs and the source: yes")

    from PIL import Image

    with Image.open(source) as image:
        print(f"format: {image.format}, size: {image.size}, mode: {image.mode}")
        if image.format != "JPEG":
            print("error: not a JPEG", file=sys.stderr)
            return 1
        if image.size != (1024, 1024):
            print("error: not 1024 by 1024", file=sys.stderr)
            return 1

    if source_size > SIZE_LIMIT:
        print(f"error: {source_size} bytes is over the 1 MiB cap", file=sys.stderr)
        return 1
    print(f"size {source_size} bytes is under the 1 MiB cap")
    print("all checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
