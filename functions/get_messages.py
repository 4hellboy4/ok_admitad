import asyncio
import aiofiles

async def init_list() -> list[str]:
    async with aiofiles.open('data/draft.txt', 'r', encoding='utf-8') as file:
        links: list[str] = [x.strip() for x in await file.readlines()]
    return links
