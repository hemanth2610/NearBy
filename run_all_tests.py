#!/usr/bin/env python3
"""
Root-level shortcut for Master Unified Enterprise Test Runner
"""
import sys
import io

# Force UTF-8 stdout/stderr on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from automation.run_all_tests import main

if __name__ == "__main__":
    sys.exit(main())
