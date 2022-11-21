import telebot
import config
import random
 
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Вітаю, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот для гри:Hello".format(message.from_user, bot.get_me()),
        parse_mode='html' )
    bot.send_message(message.chat.id, "Як справи?".format(message.from_user, bot.get_me()),
        parse_mode='html' )
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Добре':
            bot.send_message(message.chat.id, "добре що добре")
        elif message.text == 'Погано':
            bot.send_message(message.chat.id, 'Хуйово')
        else:
            bot.send_message(message.chat.id, 'Не лізь . Кіт бити буде!')
@bot.message_handler()
def welcomes(message):
    bot.send_message(message.chat.id, "Що робиш?".format(message.from_user, bot.get_me()),
        parse_mode='html' )

@bot.message_handler(content_types=['text'])
def lalalal(message):
    if message.chat.type == 'private':
        if message.text == 'Добре':
            bot.send_message(message.chat.id, "добре що добре")
        elif message.text == 'Погано':
            bot.send_message(message.chat.id, 'Хуйово')
        else:
            bot.send_message(message.chat.id, 'Не лізь . Кіт бити буде!')



bot.polling(none_stop=True)
"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Грати у групі")
    item2 = types.KeyboardButton("🎲 Грати з ботом")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Вітаю, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот для гри: Крокодил. у Телеграм ".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Грати у групі':
            bot.send_message(message.chat.id, "Грв в групі. в розробці")
        elif message.text == '🎲 Грати з ботом':
            bot.send_message(message.chat.id, 'Грв з ботом. в розробці')
        else:
            bot.send_message(message.chat.id, 'Не лізь . Кіт бити буде!')
# RUN
bot.polling(none_stop=True)
"""



"""


import telebot
from telebot import types
import config
import random
version = "1.0.0 beta"
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Грати у групі")
    item2 = types.KeyboardButton("🎲 Грати з ботом")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Вітаю, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот для гри: Крокодил. у Телеграм ".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text == '🎲 Грати з ботом':
        wordlist = '''Кіт Капуста Водій Призидент'''.split()
        dbword = random.choice(wordlist)
        bot.send_message(message.chat.id, "Бот загадує слово".format(message.from_user, bot.get_me()))
        bot.send_message(message.chat.id, "Бот загадав слово")
        if dbword == "Кіт":
            bot.send_message(message.chat.id, "Підказка: Видає звуки м'яв та мур")
        elif dbword == "Водій":
            bot.send_message(message.chat.id, "Підказка: Керує авто")
        elif dbword == "Президент":
            bot.send_message(message.chat.id, "Підказка: Найвища посда")
        elif dbword == "Капуста":
            bot.send_message(message.chat.id, "Підказка: Зелена рослина-овоч з неї беруть дітей")
        bot.send_message(message.chat.id,"Введи слово")
        @bot.message_handler()
        def ustext(message):
           if message.text == dbword:
               bot.send_message(message.chat.id,"Вітаю ви вгадали")
           elif message.text != dbword:
               bot.send_message(message.chat.id,"Помилка! ви не вгадали слово")
           if dbword == "Кіт":
               bot.send_message(message.chat.id, "Підказка: Чотирьох лапе створіння")
           elif dbword == "Водій":
               bot.send_message(message.chat.id, "Підказка: Возить людей")
           elif dbword == "Президент":
               bot.send_message(message.chat.id, "Підказка: За нього голосую раз у 5 років")
           elif dbword == "Капуста":
               bot.send_message(message.chat.id, "Підказка: Овоч листям якого загортають голубці")
           bot.send_message(message.chat.id,"Введи слово")
           if message.text == dbword:
               bot.send_message(message.chat.id,"Вітаю ви вгадали")
           elif message.text != dbword:
               bot.send_message(message.chat.id,f"Помилка! ви програли Вірне слово:{dbword}")
#run
bot.polling(none_stop=True)
"""