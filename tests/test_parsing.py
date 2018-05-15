"""Tests parsing files"""


import pytest
from typing import (
    Any
)

from json_datatypes import parse_string


@pytest.mark.parametrize('data_spec, json_, value', [
    (str, 'hello', 'hello'),
    (str, '5', '5'),
    (str, '1.5', '1.5'),
    (int, '1', 1),
    (float, '1', 1.0),
    (float, '1.5', 1.5)
])
def test_parse_basic_value(data_spec: type, json_: str, value: Any) -> None:
    """Ensure a basic value is parsed according to the data_spec."""
    result = parse_string(data_spec, json_)
    assert isinstance(result, data_spec)
    assert result == value
