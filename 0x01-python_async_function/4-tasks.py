#!/usr/bin/env python3
"""
  function:
    task_wait_n
"""

from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
      The code is nearly identical to wait_n
      except task_wait_random is being called
    """
    my_list = []
    for i in range(n):
        random_num = await task_wait_random(max_delay)
        my_list.append(random_num)
    return sorted(my_list)
