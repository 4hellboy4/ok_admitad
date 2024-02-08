from components.bot_telebot import bot


def send_msg_tg(text: str):
    bot.send_message('367757357', text)
