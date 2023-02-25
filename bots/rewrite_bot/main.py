import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


bot.message_handler(content_types=['text'])
def ustext(message):
    bot.send_message(message.chat.id,"Привіт")
    if message_text == "привіт":
        bot.send_message(message.chat.id,"І тобі привіт")
#run
bot.polling(none_stop=True)
