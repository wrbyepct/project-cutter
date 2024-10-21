"""Test utils."""

from __future__ import annotations

import subprocess
from typing import TYPE_CHECKING

from tests.consts import PROJECT_DIR
from tests.utils.misc import create_json_file_from_dict

if TYPE_CHECKING:
    from pathlib import Path


def generate_project(cookiecutter_test_config: dict[str, dict]) -> Path:
    """
    Generate cookiecutter project.

    Args:
        cookiecutter_test_config (dict[str, dict]): Test template config values for \
        cookiecutter.

    Returns:
        Generated project Path object.

    """
    from tests.consts import PROJECT_OUTPUT_DIR

    # Parallels test will create folder every time regarless fixture 'project_dir' is
    # session-wide.
    # To prevent path exist error we create project using unique path name.

    cookiecutter_test_config_fpath = create_json_file_from_dict(
        path_obj=PROJECT_OUTPUT_DIR / "cookiecutter.json",
        some_dict=cookiecutter_test_config,
    )

    cmd = [
        "cookiecutter",
        PROJECT_DIR,  # location of template folder
        "--output-dir",
        PROJECT_OUTPUT_DIR,
        "--no-input",
        "--config-file",
        str(cookiecutter_test_config_fpath),
        "--verbose",
    ]

    subprocess.run(cmd, check=True)  # noqa: S603
    return PROJECT_OUTPUT_DIR / cookiecutter_test_config["default_context"]["repo_name"]
