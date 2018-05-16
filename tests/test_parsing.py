"""Tests parsing files"""


from typing import (
    Any
)

import pytest

from json_datatypes import parse_string


@pytest.mark.parametrize('data_spec, json_, value', [
    (str, 'hello', 'hello'),
    (str, '5', '5'),
    (str, '1.5', '1.5'),
    (str, 'true', 'true'),
    (str, 'false', 'false'),
    (int, '1', 1),
    (float, '1', 1.0),
    (float, '1.5', 1.5),
    (bool, 'true', True),
    (bool, 'false', False)
])
def test_parse_basic_value(data_spec: type, json_: str, value: Any) -> None:
    """Ensure a basic value is parsed according to the data_spec."""
    result = parse_string(data_spec, json_)
    assert isinstance(result, data_spec)
    assert result == value


@pytest.mark.parametrize('data_spec, json_', [
    (int, 'hello'),
    (float, 'hello'),
    (bool, 'hello'),
    (int, '1.5'),
    (bool, '1.5'),
    (float, 'true'),
    (float, 'false')
])
def test_throws_error_on_incompatible_basic_values(
        data_spec: type, json_: str) -> None:
    with pytest.raises(ValueError):
        parse_string(data_spec, json_)
