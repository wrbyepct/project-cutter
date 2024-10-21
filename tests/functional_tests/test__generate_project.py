"""Test generate project from cookicutter template."""


def test__can_generate_project(project_dir):
    """Test generate project from cookicutter template."""
    assert project_dir.exists()
