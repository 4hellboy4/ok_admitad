import asyncio
from draft2 import send

async def main() -> None:
    # await asyncio.gather(*[senddd(0, 20), send(5, 20)])
    await asyncio.gather(send(0), send(5))



if __name__ == '__main__':
    asyncio.run(main())