"""Test to build package."""

import subprocess
from pathlib import Path


def test__can_build_package(project_dir: Path):
    """
    Test can build package using 'build' successfully.

    Args:
        project_dir (Path): Test generated cookiecutter template project folder.

    """
    subprocess.run(args=["just", "build_package"], cwd=project_dir, check=True)
    dist_dir = project_dir / "src/dist"

    assert dist_dir.exists()
