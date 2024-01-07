#!/usr/bin/env python3
'''
Module for task 10.
'''
from typing import Sequence, Any, Union, Optional

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None
