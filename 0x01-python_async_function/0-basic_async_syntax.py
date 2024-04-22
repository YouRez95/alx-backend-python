#!/usr/bin/env python3
"""
  function:
    wait_random
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
       asynchronous coroutine that takes in an integer argument
       named wait_random that waits for a random delay
       between 0 and max_delay
    """
    random_num = random.uniform(0, max_delay)
    await asyncio.sleep(random_num)
    return random_num
