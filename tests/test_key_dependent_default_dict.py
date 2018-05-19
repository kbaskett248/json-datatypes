"""Tests the KeyDependentDefaultDict class."""


import pytest

from json_datatypes.utils import KeyDependentDefaultDict


@pytest.mark.parametrize('key', ['yellow', 'orange', 'purple'])
def test_raises_key_error_with_no_default_factory(key: str) -> None:
    """Ensure the dictionary raises a key error if no default factory was
    specified."""
    kdict = KeyDependentDefaultDict(None, {'red': 1, 'blue': 2, 'green': 3})
    with pytest.raises(KeyError):
        kdict[key]


@pytest.mark.parametrize('key, value', [
    ('red', 1),
    ('blue', 2),
    ('green', 3)
])
def test_returns_value_from_dict(key: str, value: int) -> None:
    """Ensure the dictionary still functions like a dictionary."""
    kdict = KeyDependentDefaultDict(None, {'red': 1, 'blue': 2, 'green': 3})
    assert kdict[key] == value


@pytest.mark.parametrize('key, value', [
    ('red', 1),
    ('blue', 2),
    ('green', 3),
    ('yellow', 4),
    ('orange', 5),
    ('purple', 6)
])
def test_returns_key_value_if_missing(key: str, value) -> None:
    """Ensure the dictionary invokes the default factory for missing keys."""
    kdict = KeyDependentDefaultDict(lambda key: key)

    assert kdict[key] == key
    kdict[key] = value
    assert kdict[key] == value
