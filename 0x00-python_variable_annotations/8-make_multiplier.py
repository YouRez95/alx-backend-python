#!/usr/bin/env python3
"""
  function:
    make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
      returns a function that multiplies a float by multiplier
      Args:
        multiplier
    """
    def multiplie_to_multiplie(number: float):
        return multiplier * number
    return multiplie_to_multiplie
