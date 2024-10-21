"""Test misclleneous helper functions."""

import json
from pathlib import Path
from uuid import uuid4


def generate_session_id() -> str:
    """Return first 6 digits of uuid4 string."""
    return str(uuid4())[:6]


def create_json_file_from_dict(path_obj: Path, some_dict: dict) -> Path:
    """
    Ensure create a JSON file from dictionary by any given path return file path object.

    Args:
        path_obj (Path): Path object.
        some_dict (dict): Python dictionary

    Returns:
        Path: A path object of the created JSON file.

    """
    path_obj.parent.mkdir(parents=True, exist_ok=True)
    path_obj.write_text(json.dumps(some_dict))
    return path_obj
