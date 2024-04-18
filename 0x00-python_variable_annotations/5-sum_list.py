#!/usr/bin/env python3
"""
  function:
    sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
      function that returns the sum of inputs as a float.
      Args:
        input_list
    """
    result: float = 0.0
    for num in input_list:
        result += num
    return result
