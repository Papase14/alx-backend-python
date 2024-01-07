#!/usr/bin/env python3
'''
Module for task 10.
'''
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return the first element of a given sequence,
    if it exists. Otherwise, return None.
"""
    if lst:
        return lst[0]
    else:
        return None
