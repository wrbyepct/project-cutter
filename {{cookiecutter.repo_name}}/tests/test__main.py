"""Test main functions."""

from {{ cookiecutter.example_pkg }}.main import return_greeting


def test__return_greeting():
    """Test return greeting."""
    assert return_greeting() == "{{ cookiecutter.greeting }}"
