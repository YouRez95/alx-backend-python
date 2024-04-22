#!/usr/bin/env python3
"""
  function:
    wait_n
"""

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
      async routine called wait_n that takes in 2 int arguments
      n and max_delay. You will spawn wait_random n times with
      the specified max_delay.
    """
    my_list = []
    for i in range(n):
        random_num = await wait_random(max_delay)
        my_list.append(random_num)
    return sorted(my_list)
