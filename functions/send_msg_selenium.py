import asyncio
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from functions.send_tg_msg import send_msg_tg


async def send_message_selenium(user: str, driver: WebDriver, text: list[str]) -> None:
    try:
        driver.get(user)
        await asyncio.sleep(10)
        input_field: WebElement = driver.find_element(By.XPATH, '//msg-input[@class="js-empty"]')
        send_button: WebElement = driver.find_element(By.XPATH, '//button[@class="primary-okmsg"]')

        for line in text:
            input_field.send_keys(line)
            input_field.send_keys(Keys.SHIFT + Keys.ENTER)
            await asyncio.sleep(5)
            input_field.send_keys(Keys.SHIFT + Keys.ENTER)
            await asyncio.sleep(5)
        await asyncio.sleep(5)
        send_button.click()
    except Exception as e:
        send_msg_tg(e)