import asyncio
import random

import aiofiles
import aioschedule
from selenium.webdriver.chrome.webdriver import WebDriver

# file = open('../data/draft.txt')
# links: list = [x for x in file]

global counter1, counter2, counter3

async def init_list() -> list[str]:
    async with aiofiles.open('data/draft.txt') as file:
        links: list[str] = [x.strip() for x in await file.readlines()]
    return links

async def init_counters() -> None:
    global counter1, counter2, counter3
    counter1 = 0
    counter2 = 10
    counter3 = 20


async def increase_counters() -> None:
    global counter1, counter2, counter3
    counter1 += 30
    counter2 += 30
    counter3 += 30


async def send_message(start: int, nums: list) -> None:
    try:
        for i in range(start, start + 10):
            sleep_duration = random.uniform(40 * 60, 60 * 60)
            print(sleep_duration)
            await asyncio.sleep(sleep_duration)
            print(nums[i])
            await asyncio.sleep(1)
    except Exception as e:
        print(e)


async def func(nums: list) -> None:
    await asyncio.gather(
        send_message(counter1, nums),
        send_message(counter2, nums),
        send_message(counter3, nums),
    )
    await increase_counters()


async def main() -> None:
    global counter3
    links: list[str] = await init_list()
    await init_counters()
    # schedule.every(30).seconds.do(func(links))

    aioschedule.every(30).seconds.do(func, links)

    while counter3 < 120:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(main())
