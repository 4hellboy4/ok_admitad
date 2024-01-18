import time

import asyncio
import webdriver_manager
from selenium.webdriver.common.by import By


async def parse_users(url: str, driver: webdriver_manager) -> list:
    main_list: list = []
    try:
        # heading to the page
        driver.get(url)
        await asyncio.sleep(2)

        # scrolling the page till the end to update the page source code
        while True:
            for i in range(0, 8):
                await driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                await asyncio.sleep(1)
            if driver.find_element(By.CLASS_NAME, 'link-show-more').text == '':
                break
            await driver.find_element(By.CLASS_NAME, 'link-show-more').click()

        # saving all groups to the list
        users: list = await driver.find_elements(By.CLASS_NAME, "ugrid_i")
        users.pop(0)
        for user in users:
            ls: dict = {}
            user_name = await user.find_element(By.CLASS_NAME, "ellip").find_element(By.TAG_NAME, "a").text
            temp = await user.find_element(By.CLASS_NAME, 'user-grid-card_img')
            link = await temp.get_attribute('href')
            ls['user_name'] = user_name
            ls['link'] = link
            main_list.append(ls)
        print(f'{len(main_list)} users found')
        return main_list

    except Exception as e:
        print(e)
        print(f'{len(main_list)} users has been parsed')
        return main_list
