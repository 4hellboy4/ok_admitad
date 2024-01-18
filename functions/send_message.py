import asyncio
import random
import aiofiles
import aioschedule
import telebot
from selenium.webdriver.chrome.webdriver import WebDriver
from functions.get_messages import init_list
from functions.get_msg_text import get_msg_text
from functions.send_tg_msg import send_msg_tg
from functions.send_msg_selenium import send_message_selenium

global counter1, counter2, counter3
global text

async def init_msg() -> str:
    global text
    text: str = await get_msg_text()

async def init_counters() -> None:
    global counter1, counter2, counter3
    counter1: int = 0
    counter2: int = 10
    counter3: int = 20


async def increase_counters() -> None:
    global counter1, counter2, counter3
    counter1 += 30
    counter2 += 30
    counter3 += 30


async def send_message(start: int, links: list, driver: WebDriver) -> None:
    try:
        for i in range(start, start + 10):
            sleep_duration = random.uniform(40 * 60, 60 * 60)
            await asyncio.sleep(sleep_duration)
            send_message_selenium(links[i], )
            await asyncio.sleep(1)
    except Exception as e:
        send_msg_tg(e)


async def func(links: list, driver1: WebDriver, driver2: WebDriver, driver3: WebDriver, text: str) -> None:
    await asyncio.gather(
        send_message(counter1, links),
        send_message(counter2, links),
        send_message(counter3, links),
    )
    await increase_counters()


async def main_send(driver1: WebDriver, driver2: WebDriver, driver3: WebDriver) -> None:
    global counter3
    links: list[str] = await init_list()
    await init_counters()
    text_msg: str = await init_msg()

    aioschedule.every().day.at('10:00', tz='Europe/Moscow').do(func, links, driver1, driver2, driver3)

    while counter3 < 60:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(main_send())
