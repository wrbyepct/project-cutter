"""Test main functions."""

from greeting_mf.main import return_greeting


def test__return_greeting():
    """Test return greeting."""
    assert return_greeting() == "{{ cookiecutter.greeting }}"
