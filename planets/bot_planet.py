from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename="bot.log"
                    )

PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(bot, update):
    text = "Hello"
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def give_me_planets():
    list_planet_all = ephem._libastro.builtin_planets()
    list_planet_only = []
    for p_tuple in list_planet_all:
        if p_tuple[1] == "Planet":
            list_planet_only.append(p_tuple[2]) 
    return list_planet_only     

def print_new_planet(bot, update):
    user_text = update.message.text
    planet_name = user_text.split(' ')[1]
    print(planet_name)
    year = "2019"
    list_planets = give_me_planets()
    if planet_name in list_planets:
        if planet_name == "Mars":
            m = ephem.Mars(year)
        elif planet_name == "Mercury":
            m = ephem.Mercury(year)
        elif planet_name == "Venus":
            m = ephem.Venus(year)
        elif planet_name == "Jupiter":
            m = ephem.Jupiter(year)
        elif planet_name == "Saturn":
            m = ephem.Saturn(year)
        elif planet_name == "Uranus":
            m = ephem.Uranus(year)
        elif planet_name == "Neptune":
            m = ephem.Neptune(year)
        elif planet_name == "Pluto":
            m = ephem.Pluto(year)
        elif planet_name == "Sun":
            m = ephem.Sun(year)
        elif planet_name == "Moon":
            m = ephem.Moon(year)
        constell_name = ephem.constellation(m)
        print(constell_name)
        update.message.reply_text(constell_name)    
    else:
        update.message.reply_text('Not a planet!') 


def main():
    mybot = Updater("753185034:AAFp2AC87A3HxQjl7bsfifedB_78rE4et-0", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", print_new_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

main()


