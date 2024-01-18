import aiofiles


async def get_msg_text() -> str:
    async with aiofiles.open('data/msg.txt') as f:
        message: str = ''.join([string for string in await f.readlines()])
    return message