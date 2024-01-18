import telebot

def send_msg_tg(text: str, bot: telebot.TeleBot):
    bot.send_message('367757357', text)
