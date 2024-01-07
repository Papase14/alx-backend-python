#!/usr/bin/env python3
'''
Module for task 12.
'''
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on an array by repeating each element a specified number of times.

    Args:
        lst (Tuple): The input array.
        factor (int, optional): The number of times each element should be repeated. Defaults to 2.

    Returns:
        List: The zoomed-in array.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
