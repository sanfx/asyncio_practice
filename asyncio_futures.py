import asyncio

from asyncio import Future

async def my_task(number: int) -> dict:
    print('Starting task...')
    await asyncio.sleep(2)
    return {'task': number}

async def  main() -> None:
    tasks: Future = asyncio.gather(
        my_task(1),
        my_task(2),
        my_task(3)
    )
    results: list[dict] = await tasks
    print(results)

if __name__ == '__main__':
    asyncio.run(main())