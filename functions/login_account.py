import asyncio
# import webdriver_manager
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


async def login(username: str, password: str, driver: webdriver) -> None:
    try:
        await driver.get('https://ok.ru')
        await asyncio.sleep(2)
        s_username: WebElement = await driver.find_element(By.XPATH, '//input[@name="st.email"]')
        s_password: WebElement = await driver.find_element(By.XPATH, '//input[@name="st.password"]')
        s_continue: WebElement = await driver.find_element(By.XPATH, '//div[@class="login-form-actions"]/input['
                                                                '@type="submit"]')
        s_username.clear()
        s_password.clear()
        s_username.send_keys(username)
        await asyncio.sleep(1)
        s_password.send_keys(password)
        s_continue.click()
        await asyncio.sleep(1)
    except Exception as e:
        print(e)