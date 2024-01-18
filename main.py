import asyncio
import telebot
from functions.login_account import login
from functions.initialization import init
from functions.users_parsing import parse_users
from functions.send_tg_msg import send_msg_tg

async def main() -> None:
    try:
        driver1, driver2, driver3 = init()
        await asyncio.gather(
            login('1', '2', driver1),
            login('1', '2', driver2),
            login('1', '2', driver3),
        )
    except Exception as e:
        send_msg_tg(e)
    finally:
        driver1.quit()
        driver2.quit()
        driver3.quit()



if __name__ == '__main__':
    asyncio.run(main())
    bot.infinity_polling()
