import asyncio

import aioschedule

from functions.login_account import login
from functions.initialization import init
from functions.send_tg_msg import send_msg_tg
from components.bot_telebot import bot
from functions.send_message import main_send
from classes.counters import Counters, init_counters
from functions.send_message import init_msg
from functions.get_messages import init_list


async def main_func(counters: Counters, text: list[str], links: list[str]) -> None:
    driver1, driver2, driver3 = await init()
    try:
        await asyncio.gather(
            login('79258789353', 'qwerty23017', driver1),
            login('89381414996', '1fJskl23', driver2),
            login('89880267156', 'fSDf123aAsdq', driver3)
        )
        send_msg_tg('All accounts are logged in')
        await main_send(driver1, driver2, driver3, counters, text, links)
    except Exception as e:
        send_msg_tg(e)
    finally:
        driver1.quit()
        driver2.quit()
        driver3.quit()
        send_msg_tg('the work is done for this day')


async def main() -> None:
    text_msg: list[str] = await init_msg()
    my_counters: Counters = await init_counters()
    links: list[str] = await init_list()

    aioschedule.every().day.at('07:00').do(main_func, my_counters, text_msg, links)

    while my_counters.counter3 < 7200:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


if __name__ == '__main__':
    asyncio.run(main())
    bot.infinity_polling()
