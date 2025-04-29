#!/usr/bin/python3

import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def talk():
    print("Hello World")

async def run():
    print("Runnning...About to sleep")
    await asyncio.sleep(1)
    print("Just Woke Up")
    

async def main():
    await asyncio.gather(count(), run(), talk())

if __name__ == '__main__':
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} exexuted in {elapsed:0.2f} seconds.")

