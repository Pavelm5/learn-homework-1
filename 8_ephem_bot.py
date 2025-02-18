"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime
from eph import planet_const
import settings
import ephem

dt_now = datetime.now()
#print(dt_now) 


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

#list_planets = ['Mercury', 'Venus', 'Mars','Jupiter', 'Saturn', 'Uranus', 'Neptune']

PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
         'password': settings.PROXY_PASSWORD}
    }

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Привет! Введите данные - название планеты (например Mars), латиницей, в формате "/planet Mars"') 


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planet(update, context):
    user_text = update.message.text
    print(user_text)
    planet_name = update.message.text.split()[1]
    planet_name = planet_name
    update.message.reply_text(f'Сегодня планета {planet_name} находится в созвездии {planet_const(planet_name)}')



def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
