import asyncio
import time

from client import fake_file_data

async def main():
    async for chunk in fake_file_data():
        print(chunk)

if __name__ == "__main__":
    asyncio.run(main())