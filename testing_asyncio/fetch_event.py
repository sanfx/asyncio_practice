import json
import random
import asyncio

from pathlib import Path
from aiohttp import ClientSession


async def read_data(
    path: str="./data/fictional_events.json",
) -> dict[str, dict[str, str]]:
    await asyncio.sleep(random.choice([0.125, 0.5, 0.75, 0.1]))
    json_path = Path(__file__).parent.joinpath(path)
    with open(json_path) as file:
        data = json.load(file)
    return data


async def fetch_event(
    event_id: str, session: ClientSession | None = None
) -> dict[str, str]:
    json_data = await read_data()

    try:
        event = json_data[event_id]
        return event
    except KeyError:
        return {"error": "Event not found."}