import aiofiles


async def init_list() -> list[str]:
    async with aiofiles.open('data/members.txt') as file:
        links: list[str] = [x.strip() for x in await file.readlines()]
    return links
