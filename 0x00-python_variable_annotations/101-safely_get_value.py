#!/usr/bin/env python3
'''
Module for task 11.
'''
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Return the value associated with the given key in the provided 
    dictionary, or a default value if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
