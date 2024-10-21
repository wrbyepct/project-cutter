"""Tests for justfile file commands."""

import subprocess
from pathlib import Path

from tests.utils.init_git_repo import intialize_git_and_commit


def test__linting_passes(project_dir: Path):
    """
    Test Linting in generated cookiecutter project.

    Args:
        project_dir (Path): Test generated cookiecutter template project folder.

    """
    intialize_git_and_commit(project_dir)
    cmd = ["just", "lint"]
    subprocess.run(args=cmd, cwd=project_dir, check=True)


def test__tests_pass(project_dir: Path):
    """
    Test project depencies install and run test successfully.

    Args:
        project_dir (Path): Test generated cookiecutter template project folder.

    """
    subprocess.run(args=["just", "build_package"], cwd=project_dir, check=True)
    subprocess.run(args=["just", "install_package"], cwd=project_dir, check=True)
    subprocess.run(args=["just", "test"], cwd=project_dir, check=True)
