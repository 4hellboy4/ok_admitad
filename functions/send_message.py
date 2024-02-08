import asyncio
import random
from selenium.webdriver.chrome.webdriver import WebDriver
from functions.get_msg_text import get_msg_text
from functions.send_tg_msg import send_msg_tg
from functions.send_msg_selenium import send_message_selenium
from classes.counters import Counters, increment_counters


async def init_msg() -> list[str]:
    return await get_msg_text()


async def send_message(start: int, links: list, driver: WebDriver, text: list[str]) -> None:
    try:
        for i in range(start, start + 20):
            sleep_duration = random.uniform(15 * 60, 25 * 60)
            await asyncio.sleep(sleep_duration)
            await send_message_selenium(links[i], driver, text)
            send_msg_tg(f'Was sent to {links[i]}')
            await asyncio.sleep(2)
    except Exception as e:
        send_msg_tg(e)


async def main_send(driver1: WebDriver, driver2: WebDriver, driver3: WebDriver, counters: Counters, text: list[str],
                    links: list[str]) -> None:
    send_msg_tg('The sending has started')
    await asyncio.gather(
        send_message(counters.counter1, links, driver1, text),
        send_message(counters.counter2, links, driver2, text),
        send_message(counters.counter3, links, driver3, text)
    )
    await increment_counters(counters)
