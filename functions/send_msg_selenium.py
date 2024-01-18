import asyncio

import aiofiles
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from functions.send_tg_msg import send_msg_tg

async def send_message_selenium(user: str, driver: WebDriver, text: str) -> None:
    try:
        driver.get(user)
        await asyncio.sleep(2)
        input_field: WebDriver = driver.find_element(By.XPATH, '//msg-input[@class="js-empty"]')
        send_button: WebDriver = driver.find_element(By.XPATH, '//button[@class="primary-okmsg"]')
        input_field.send_keys(text)
        await asyncio.sleep(1)
        send_button.click()
        send_msg_tg(f'Message was sent to {user}')
    except Exception as e:
        send_msg_tg(e)