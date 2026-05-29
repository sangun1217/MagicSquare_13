#!/usr/bin/env python3
"""Generate Golden Master baseline from live Magic Square Solver output."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
if str(PROJECT_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT / "src"))

from tests.golden_master.approve import approve_or_assert  # noqa: E402
from tests.golden_master.capture import render_golden_master_document  # noqa: E402

DEFAULT_OUTPUT = PROJECT_ROOT / "tests" / "golden_master_expected.txt"


def main() -> int:
    """Generate or approve the Golden Master baseline file."""
    parser = argparse.ArgumentParser(
        description="Generate Golden Master baseline from solver output.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output path (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--approve",
        action="store_true",
        help="Force-write baseline even when file already exists.",
    )
    args = parser.parse_args()

    document = render_golden_master_document()
    force_approve = args.approve or not args.output.is_file()
    approve_or_assert(document, args.output, approve=force_approve)
    if force_approve:
        print(f"Golden Master baseline written to {args.output}")
    else:
        print(f"Golden Master baseline matches {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
