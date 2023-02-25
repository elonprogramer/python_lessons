import telebot

TOKEN = 2414112 = '6255138350:AAFo9OdDpLSr4Mhjv3a3qzh6eoPtGx3INF8'
bot = telebot.TeleBot(TOKEN = 2414112)


bot.message_handler(content_types=['text'])


def ustext(message):
    bot.send_message(message.chat.id,"Привет")
    if message.text == "Привет":
        bot.send_message(message.chat.id,"Hello!!")


# run


bot.polling(none_stop=True)
