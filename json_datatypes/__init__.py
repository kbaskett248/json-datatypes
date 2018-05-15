"""json_datatypes - A json parser, validator and serializer based on type annotations"""

__version__ = '0.1.0'
__author__ = 'Kenny Baskett <kbaskett248@gmail.com>'
__all__ = []


import json


def parse_string(data_spec: type, json_: str):
    return data_spec(json_)
