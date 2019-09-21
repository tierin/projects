import random
import logging
import re
from datetime import date

import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

REQUEST_KWARGS = {
    'proxy_url': 'http://bot1:45rrtx32@zhum-eu.freeddns.org:3128/'}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

with open('token_name') as bot_key:
    bot_key = bot_key.read()
    print(bot_key)


def greet_user(bot, update):
    print('Вызван /start')
    text = 'I\'m back baby!'
    update.message.reply_text(text)


def constellation(bot, update):
    user_text = update.message.text.split(' ')
    if len(user_text) >= 2:
        planet_name = user_text[1]
        try:
            chosen_planet = getattr(ephem, planet_name)
            if planet_name == 'Pluto':
                update.message.reply_text('My dear meatbag, Pluto is not a planet anymore!')
            else:
                today = date.today()
                planet_const_today = ephem.constellation(chosen_planet(today))[1]
                planet_answer = 'Planet {} is in the constellation {} today'.format(planet_name, planet_const_today)
                update.message.reply_text(planet_answer)
        except AttributeError:
            if planet_name == 'Earth':
                update.message.reply_text('Where are you from, alien?')
            else:
                update.message.reply_text('I don\'t understand what you want. Ask Google about it')

    elif len(user_text) < 2:
        update.message.reply_text('We need more words!')


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    items = ['Well, everybody, I just saved a turtle. What have you done with your lives?',
             'Kill all humans!',
             'I love you, meatbag!',
             'Bite my shiny metal ass!',
             'Game’s over, losers! I have all the money. Compare your lives to mine and then kill yourselves.!',
             'Hasta la vista, meatbag!',
             'I’m so embarrassed. I wish everybody else was dead.',
             'My story is a lot like yours, only more interesting ‘cause it involves robots.']
    update.message.reply_text(items[random. randrange(len(items))])


def read_token():
    with open('token_name', 'r') as f:
        token = f.readline()
        return str(token)


def word_counter(bot, update):
    user_text = update.message.text.split(' ')[1:]
    print(user_text)
    words_count = 0
    if len(user_text) == 0:
        update.message.reply_text('Их нет!')
    else:
        for element in user_text:
            if re.search('[a-zA-Zа-яА-Я0-9]', element):
                words_count += 1
        if str(words_count)[-1] == '1':
            update.message.reply_text(f'{words_count} слово')
        else:
            update.message.reply_text(f'{words_count} слова')


def next_full_moon(bot, update):
    user_text = update.message.text.split(' ')[1]
    user_text = user_text.replace('.', '/')
    if re.search('(\d\d).(\d\d).(\d{4})', user_text):
        pattern = re.search('(\d\d).(\d\d).(\d{4})', user_text)
        user_text = f'{pattern[3]}/{pattern[2]}/{pattern[1]}'
    full_moon = ephem.next_full_moon(user_text)
    update.message.reply_text(f'Ближайшее полнолуние: {full_moon}')


#def cities(bot, update):
#    while True:
#        user_text = ' '.join(update.message.text.split(' ')[1:])
#        if user_text == 'Хорош':
#            break
#        user_cities = []
#        with open('cities', 'r', encoding='utf-8') as f:
#            # The protocol version used is detected automatically, so we do not
#            # have to specify it.
#            city = ''
#            for line in f:
#                if user_text == line:
#                    city = user_text
#                    print(city)
#            if city != '':
#                for line in f:
#                    if line[0] == user_text[0].upper():
#                        update.message.reply_text(line)


def main():
    mybot = Updater(
        token=read_token(),
        request_kwargs=REQUEST_KWARGS,
    )
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler('planet', constellation))
    dp.add_handler(CommandHandler('wordcount', word_counter))
    dp.add_handler(CommandHandler('next_full_moon', next_full_moon))
#    dp.add_handler(CommandHandler('cities', cities))


    mybot.start_polling()
    mybot.idle()


main()
