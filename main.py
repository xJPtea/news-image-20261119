"""Entry for make.fun competition news-image-20261119.

The repository holds a single front-page image next to this program.
Running the program copies that image, unchanged, into the output
directory, so the grader's two runs produce identical bytes. The
program uses only the Python standard library, reaches no network,
and makes no random choices.

Local run:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import sys
from pathlib import Path

IMAGE_FILE = "entry.png"
JPEG_PREFIX = b"\xff\xd8\xff"
JPEG_SUFFIX = b"\xff\xd9"
SIZE_LIMIT = 1_048_576


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    return 1


def main():
    here = Path(__file__).resolve().parent
    source = here / IMAGE_FILE
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination = output_dir / IMAGE_FILE

    try:
        image_bytes = source.read_bytes()
    except OSError as exc:
        return fail(f"cannot read {source}: {exc}")

    if not image_bytes.startswith(JPEG_PREFIX):
        return fail(f"{source} does not start with the JPEG magic bytes")

    if not image_bytes.endswith(JPEG_SUFFIX):
        return fail(f"{source} lacks the JPEG end marker, so it is truncated")

    if len(image_bytes) > SIZE_LIMIT:
        return fail(
            f"{source} is {len(image_bytes)} bytes, over the 1 MiB limit"
        )

    output_dir.mkdir(parents=True, exist_ok=True)
    try:
        destination.write_bytes(image_bytes)
    except OSError as exc:
        return fail(f"cannot write {destination}: {exc}")

    if destination.read_bytes() != image_bytes:
        return fail(f"{destination} differs from {source} after writing")

    digest = hashlib.sha256(image_bytes).hexdigest()
    print(f"wrote {destination} ({len(image_bytes)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
