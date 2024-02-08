import aiofiles


async def get_msg_text() -> list[str]:
    async with aiofiles.open('data/msg.txt') as f:
        message: list[str] = [string.strip() for string in await f.readlines()]
        return message