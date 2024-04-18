#!/usr/bin/env python3
"""
  function:
    safe_first_element
"""
from typing import Union, Sequence, Any
from types import NoneType


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
      duck-typed annotations
    """
    if lst:
        return lst[0]
    else:
        return None
