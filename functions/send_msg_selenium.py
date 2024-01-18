import asyncio

import aiofiles
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from functions.send_tg_msg import send_msg_tg
from selenium.webdriver.common.keys import Keys

async def send_message_selenium(user: str, driver: WebDriver, text: list[str]) -> None:
    try:
        driver.get(user)
        await asyncio.sleep(2)
        input_field: WebDriver = driver.find_element(By.XPATH, '//msg-input[@class="js-empty"]')
        send_button: WebDriver = driver.find_element(By.XPATH, '//button[@class="primary-okmsg"]')

        for line in text:
            print(text)
            input_field.send_keys(line)
            input_field.send_keys(Keys.SHIFT + Keys.ENTER)
            await asyncio.sleep(1)
            input_field.send_keys(Keys.SHIFT + Keys.ENTER)
            await asyncio.sleep(1)
        await asyncio.sleep(1)
        send_button.click()
    except Exception as e:
        send_msg_tg(e)