"""Write one short text for make.fun bounty u-gudril-cool-one-line-best-line-b8c41f4d."""

import os
import sys
from pathlib import Path

TEXT = "The waiting-room fish has a name tag on his bowl: Gerald. Gerald has been dead since Tuesday. The tag is new."


def output_dir() -> Path:
    chosen = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    return Path(chosen)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text must be 1..280 characters, got {len(TEXT)}"
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    path = target / "entry.txt"
    path.write_bytes(TEXT.encode("utf-8"))
    print(f"wrote {path} ({len(TEXT)} characters)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
