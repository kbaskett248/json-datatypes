"""json_datatypes - A json parser, validator and serializer based on type annotations"""

__version__ = '0.1.0'
__author__ = 'Kenny Baskett <kbaskett248@gmail.com>'
__all__ = ['parse_string']


from functools import partial
import json
from typing import (
    Any,
    Text,
    TypeVar
)

from .utils import (
    KeyDependentDefaultDict
)


T = TypeVar('T')


def default_converter(type_: T, value: Any) -> T:
    """Generic validator that ensures value is of the specified type."""
    if isinstance(value, bool):
        if type_ is not bool:
            raise ValueError()
        else:
            return value
    if isinstance(value, type_):
        return value
    else:
        raise ValueError()


def float_converter(value: Any) -> float:
    """Validator that ensures value is a float."""
    if isinstance(value, bool):
        raise ValueError()
    if isinstance(value, float):
        return value
    elif isinstance(value, int):
        return float(value)
    else:
        raise ValueError()


CONVERTERS = KeyDependentDefaultDict(
    lambda key: partial(default_converter, key),
    {float: float_converter}
)


def parse_string(data_spec: type, json_: str):
    """Parse a string according to the data_spec provided."""
    return CONVERTERS[data_spec](json.loads(json_))
