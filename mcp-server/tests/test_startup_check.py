#!/usr/bin/env python3
"""
Unit tests for startup_check.run_indexing.

startup-check.log (supervisord's capture of this script's stdout and stderr) is the only
production log of the indexer, so every line the indexer prints must reach it: each file
left out of the index and why, and the cause of a failed run, which comes after the
summary table.
"""

import subprocess
import sys
from pathlib import Path
from typing import Any, List
from unittest.mock import patch

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
import startup_check  # noqa: E402

# Stands in for the indexer: 30 lines on stdout (more than any tail), one on stderr
FAKE_INDEXER = """
import sys
print("Skipping Zz/long.md: file_path is 482 bytes")
for n in range(28):
    print(f"summary line {n}")
print("Indexing aborted: add 10 documents: task 7 failed (missing_document_id: x)")
print("traceback line", file=sys.stderr)
sys.exit(int(sys.argv[1]))
"""


def run_with_fake_indexer(exit_code: int) -> List[Any]:
    real_run = subprocess.run
    seen: List[Any] = []

    def fake_run(cmd: List[str], **kwargs: Any) -> Any:
        seen.append(cmd)
        return real_run([sys.executable, "-c", FAKE_INDEXER, str(exit_code)], **kwargs)

    with patch("subprocess.run", fake_run):
        seen.append(startup_check.run_indexing())
    return seen


@pytest.mark.parametrize("exit_code", [0, 1])
def test_every_line_of_the_indexer_output_reaches_the_log(capfd: pytest.CaptureFixture[str], exit_code: int) -> None:
    cmd, ok = run_with_fake_indexer(exit_code)
    out, err = capfd.readouterr()
    assert ok is (exit_code == 0)
    assert "Skipping Zz/long.md: file_path is 482 bytes" in out
    assert all(f"summary line {n}\n" in out for n in range(28))
    assert "Indexing aborted: add 10 documents: task 7 failed" in out
    assert "traceback line" in err
    assert ("Indexing completed successfully!" if exit_code == 0 else "Indexing failed with return code 1") in out
    # never --force: the indexer decides between an update and a rebuild by swap
    assert cmd == [sys.executable, "/app/scripts/index_to_meilisearch.py", "--docs-path", "/data/documentation"]
