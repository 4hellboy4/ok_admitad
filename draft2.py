import aiofiles
import asyncio
from fake_useragent import UserAgent
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager



async def get_msg() -> list[str]:
    async with aiofiles.open('data/msg.txt') as f:
        msg: list[str] = [string.strip() for string in await f.readlines()]
        return msg


async def init() -> WebDriver:
    options: Options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f"user-agent={UserAgent().random}")
    service: Service = Service(ChromeDriverManager().install())
    driver1: WebDriver = WebDriver(options=options, service=service)
    return driver1


async def send(user: str, driver: WebDriver, text: list[str]) -> None:
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
        print(e)


async def log_in(driver: WebDriver) -> None:
    driver.get('https://ok.ru')
    await asyncio.sleep(2)
    s_username: WebElement = driver.find_element(By.XPATH, '//input[@name="st.email"]')
    s_password: WebElement = driver.find_element(By.XPATH, '//input[@name="st.password"]')
    s_continue: WebElement = driver.find_element(By.XPATH, '//div[@class="login-form-actions"]/input['
                                                           '@type="submit"]')
    s_username.clear()
    s_password.clear()
    s_username.send_keys('89880267156')
    await asyncio.sleep(1)
    s_password.send_keys('fSDf123aAsdq')
    s_continue.click()
    await asyncio.sleep(1)




async def main() -> None:
    driver: WebDriver = await init()
    await log_in(driver)
    msg: list[str] = await get_msg()
    await send('https://ok.ru/messages/604892728361', driver, msg)

    driver.close()


if __name__ == '__main__':
    asyncio.run(main())

