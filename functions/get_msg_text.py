import aiofiles


async def get_msg_text() -> str:
    f = await aiofiles.open('../data/')
    message: str = ''.join([string for string in f.readlines()])
    return message