import asyncio
import random
import aiofiles
import aioschedule
from selenium.webdriver.chrome.webdriver import WebDriver
from functions.get_messages import init_list
from functions.get_msg_text import get_msg_text
from functions.send_tg_msg import send_msg_tg
from functions.send_msg_selenium import send_message_selenium


class Counters:
    def __init__(self):
        self.counter1 = 0
        self.counter2 = 10
        self.counter3 = 20


counters = Counters()

async def init_msg() -> str:
    return await get_msg_text()

async def init_counters() -> Counters:
    return Counters()


async def increase_counters() -> None:
    counters.counter1 += 30
    counters.counter2 += 30
    counters.counter3 += 30


async def send_message(start: int, links: list, driver: WebDriver, text: str) -> None:
    try:
        for i in range(start, start + 10):
            sleep_duration = random.uniform(1 * 60, 2 * 60)
            await asyncio.sleep(sleep_duration)
            print(sleep_duration)
            await send_message_selenium(links[i], driver, text)
            print(f'Was sent to {links[i]}')
            await asyncio.sleep(1)
    except Exception as e:
        send_msg_tg(e)


async def func(links: list, driver1: WebDriver, driver2: WebDriver, text: str) -> None:
    print('started fir')
    await asyncio.gather(
        send_message(counters.counter1, links, driver1, text),
        send_message(counters.counter2, links, driver2, text),
    )
    await increase_counters()


async def main_send(driver1: WebDriver, driver2: WebDriver) -> None:
    # Use the returned values instead of global variables
    links: list[str] = await init_list()
    text_msg: str = await init_msg()
    counters: Counters = await init_counters()

    aioschedule.every().day.at('15:45').do(func, links, driver1, driver2, text_msg)

    while counters.counter3 < 60:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
