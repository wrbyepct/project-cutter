"""Pytest project setup fixtures."""

import shutil
from pathlib import Path
from unittest.mock import patch

import pytest

from tests.consts import PROJECT_OUTPUT_DIR
from tests.utils.misc import generate_session_id
from tests.utils.project import generate_project


@pytest.fixture
def temp_project_dir():
    """Create temporary project folder by replacing tests.consts.PROJECT_DIR value."""
    my_temp_dir = Path(f"{PROJECT_OUTPUT_DIR}-{generate_session_id()}")
    with patch(
        "tests.consts.PROJECT_OUTPUT_DIR",
        new=my_temp_dir,
    ):
        yield
        shutil.rmtree(my_temp_dir)


@pytest.fixture
def project_dir(temp_project_dir) -> Path:  # noqa: ARG001
    """
    ookiecutter Project fixture.

    1. Generate cookiecutter template project from test config.
    2. Return project direcototry as Path object.
    3. Teardown by recursive deleteing the proejct direcototry.

    """
    template_values = {"repo_name": "test_repo"}
    cookiecutter_test_config: dict[str, dict] = {
        "default_context": template_values,
    }

    generated_repo_dir: Path = generate_project(
        cookiecutter_test_config,
    )

    return generated_repo_dir
