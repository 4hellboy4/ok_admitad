import asyncio

import aiofiles
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


async def send_message(user: str, driver: WebDriver, text: str) -> None:
    try:
        f = await aiofiles.open('../data/')
        message: str = ''.join([string for string in f.readlines()])
        driver.get(user)
        await asyncio.sleep(2)
        input_field = driver.find_element(By.XPATH, '//msg-input[@class="js-empty"]')
        send_button = driver.find_element(By.XPATH, '//button[@class="primary-okmsg"]')
        # input_field.clear()
        input_field.send_keys('Hi, pupururp')
        time.sleep(1)
        send_button = driver.find_element(By.XPATH, '//button[@class="primary-okmsg"]')
        send_button.click()

    except Exception as e:
        print(e)