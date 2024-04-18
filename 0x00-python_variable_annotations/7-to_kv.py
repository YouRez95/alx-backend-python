#!/usr/bin/env python3
"""
  function:
    sum_mixed_list
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
      returns a tuple.
      The first element of the tuple is the string k.
      The second element is the square of the int/float v
      and should be annotated as a float.
      Args:
        k, v
    """
    return (k, v*v)
