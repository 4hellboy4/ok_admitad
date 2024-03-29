from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent

def init() -> webdriver:
    options: Options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f"user-agent={UserAgent().random}")
    service: Service = Service(ChromeDriverManager().install())
    driver1: webdriver = WebDriver(options=options, service=service)
    driver2: webdriver = WebDriver(options=options, service=service)
    driver3: webdriver = WebDriver(options=options, service=service)
    return driver1, driver2, driver3
