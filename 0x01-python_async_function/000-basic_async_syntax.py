import random
import asyncio

async def wait_random(max_delay=10):
    wait = random.uniform(0, max_delay);
    await asyncio.sleep(wait)
    return wait

