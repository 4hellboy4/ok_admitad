import asyncio
import telebot
from functions.login_account import login
from functions.initialization import init
from functions.users_parsing import parse_users
from functions.send_tg_msg import send_msg_tg
from functions.send_message import main_send
from components.bot_telebot import bot

async def main() -> None:
    send_msg_tg('The start of a program')
    try:
        driver1, driver2 = await init()
        await asyncio.gather(
            login('89381414996', '1fJskl23', driver1),
            login('89880267156', 'fSDf123aAsdq', driver2),
        )
        await main_send(driver1, driver2)
        send_msg_tg('Done without errors')
    except Exception as e:
        send_msg_tg(e)
    finally:
        send_msg_tg('The end of a program')
        driver1.quit()
        driver2.quit()



if __name__ == '__main__':
    asyncio.run(main())

bot.infinity_polling()
