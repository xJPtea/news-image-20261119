"""End-to-end test for the news-image-20261119 entry.

Runs main.py twice to two different output folders and checks:
- both runs exit 0,
- both outputs are byte-identical to each other and to entry.png,
- the output is a JPEG, 1024x1024, under the 1 MiB cap.

Run: python3 test_entry.py
"""

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAX_BYTES = 1_048_576


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    source = HERE / "entry.png"
    if not source.exists():
        print("error: entry.png missing", file=sys.stderr)
        return 1

    digests = []
    with tempfile.TemporaryDirectory() as tmp:
        for i in (1, 2):
            out_dir = Path(tmp) / f"out{i}"
            env = dict(os.environ, MAKEFUN_OUTPUT_DIR=str(out_dir))
            result = subprocess.run(
                [sys.executable, str(HERE / "main.py")],
                env=env, capture_output=True, text=True, check=False,
            )
            print(f"run {i}: exit={result.returncode} {result.stdout.strip()}")
            if result.returncode != 0:
                print(result.stderr, file=sys.stderr)
                return 1
            target = out_dir / "entry.png"
            if not target.exists():
                print(f"error: run {i} wrote no entry.png", file=sys.stderr)
                return 1
            digests.append(sha256(target))

    source_digest = sha256(source)
    print(f"source sha256: {source_digest}")
    print(f"run 1 sha256:  {digests[0]}")
    print(f"run 2 sha256:  {digests[1]}")
    assert digests[0] == digests[1] == source_digest, "outputs differ"
    print("byte-identical across runs: yes")

    from PIL import Image

    with Image.open(source) as im:
        print(f"format: {im.format}, dimensions: {im.size}, mode: {im.mode}")
        assert im.format == "JPEG", "not a JPEG"
        assert im.size == (1024, 1024), "not 1024x1024"
    size = source.stat().st_size
    print(f"size: {size} bytes (cap {MAX_BYTES})")
    assert size <= MAX_BYTES, "over the 1 MiB cap"
    print("all checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
