#!/usr/bin/env python3
"""
  function:
    sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
      function that returns the sum of inputs as a float.
      Args:
        mxd_lst
    """
    result: float = 0.0
    for num in mxd_lst:
        result += num
    return result
