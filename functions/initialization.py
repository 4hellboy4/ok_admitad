from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent


async def init() -> tuple[WebDriver, WebDriver, WebDriver]:
    options: Options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f"user-agent={UserAgent().random}")
    service: Service = Service(ChromeDriverManager().install())
    driver1: WebDriver = WebDriver(options=options, service=service)
    driver2: WebDriver = WebDriver(options=options, service=service)
    driver3: WebDriver = WebDriver(options=options, service=service)
    return driver1, driver2, driver3
