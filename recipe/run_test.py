import subprocess
import sys
import os

from importlib.metadata import version


def do(args: list[str], expect_stdout: str = "") -> int:
    print(">>>", *args, flush=True)
    out = subprocess.check_output(args, encoding="utf-8")
    if expect_stdout:
        assert expect_stdout in out
    return 0


def check_versions() -> int:
    out = subprocess.check_output(["jupyter-book", "--version"], encoding="utf-8")
    versions = {
        out.strip().replace("v", ""),
        version("jupyter-book"),
        os.environ["PKG_VERSION"],
    }
    print(versions)
    assert len(versions) == 1, f"expected one version, got: {versions}"
    return 0


if __name__ == "__main__":
    sys.exit(
        do(["jupyter-book", "--version"])
        or do(["jupyter-book", "--help"])
        or check_versions()
    )
