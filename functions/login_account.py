import asyncio
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from functions.send_tg_msg import send_msg_tg


async def login(username: str, password: str, driver: WebDriver) -> None:
    try:
        driver.get('https://ok.ru')
        await asyncio.sleep(2)
        s_username: WebElement = driver.find_element(By.XPATH, '//input[@name="st.email"]')
        s_password: WebElement = driver.find_element(By.XPATH, '//input[@name="st.password"]')
        s_continue: WebElement = driver.find_element(By.XPATH, '//div[@class="login-form-actions"]/input['
                                                                '@type="submit"]')
        s_username.clear()
        s_password.clear()
        s_username.send_keys(username)
        await asyncio.sleep(1)
        s_password.send_keys(password)
        s_continue.click()
        await asyncio.sleep(1)
    except Exception as e:
        send_msg_tg(e)
        print('login error')