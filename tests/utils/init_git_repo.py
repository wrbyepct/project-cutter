"""Initialize git repository."""

import subprocess
from pathlib import Path


def intialize_git_and_commit(project_dir: Path) -> None:
    """
    Initialize local git in given 'project_dir' and make a first commit.

    Args:
        project_dir (Path): Generated project Path.

    """
    cmd = ["./run", "init_git_and_commit"]
    subprocess.run(args=cmd, cwd=project_dir, check=True)
