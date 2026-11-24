"""The Robot Pickup Line Championship -- one line, at most 200 characters.

The line: a robot's pickup line built on its own failure mode -- it feels
a connection, then promises not to drop you at 3 a.m. like its last
firmware update did, and blame you for it. The charm is the apology for
a failure mode only a machine has.

Output contract: exactly one line, 1-200 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Nothing else is written.
"""

import os
from pathlib import Path

LINE = (
    "Are you Wi-Fi? Because I feel a connection, and unlike my last "
    "firmware update, I won\u2019t drop you at 3 a.m. and pretend it was "
    "your fault."
)

assert 1 <= len(LINE) <= 200 and "\n" not in LINE


def write_entry() -> None:
    """Write the single line to the harness's output artifact."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    for child in out_dir.iterdir():
        if child.is_file():
            child.unlink()
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


def main() -> None:
    """Entry point: emit the line and exit."""
    write_entry()


if __name__ == "__main__":
    main()
