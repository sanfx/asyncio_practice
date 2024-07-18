import asyncio
import time


async def use_api(x: int):
    await asyncio.sleep(0.1)  # fake lag
    return 2 * x


async def main():
    awaitables = (use_api(x) for x in range(10))
    start = time.perf_counter()
    for awaitable in awaitables:
        result = await awaitable
        elapsed = time.perf_counter() - start
        print(f"[{elapsed:.2f}s] Got result: {result}")


if __name__ == "__main__":
    asyncio.run(main())