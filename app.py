from telebot import TeleBot, types

from setting import bot_token
from user_data import User

from servise.auxiliaryFunctions import WorcUser, AdminPanel
from servise.returnText import text_user, not_registered_text, admin_text



bot = TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start_bot_worc(message):
    user = User.get_user(message.chat.id, message.chat.username, message.from_user.first_name, message.from_user.last_name)
    WorcUser(user).check_user()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if user.rights == 'not_registered':
        button_1 = types.KeyboardButton('Авторизация')
        markup.add(button_1)
        bot.send_message(message.chat.id, not_registered_text, reply_markup=markup)

    elif user.rights == 'user':
        button_1 = types.KeyboardButton('Подать заявку')
        button_2 = types.KeyboardButton('Отменить заявку')
        button_3 = types.KeyboardButton('Перенос заявки')
        button_4 = types.KeyboardButton('Просмотреть мои заявки')

        markup.add(button_1, button_2, button_3)
        markup.add(button_4)
        bot.send_message(message.chat.id, text_user, reply_markup=markup)

        markup.add(button_3)
    elif user.rights == 'admin':
        button_1 = types.KeyboardButton('Просмотр заявок')
        button_2 = types.KeyboardButton('Увеличение количества заявок')
        button_3 = types.KeyboardButton('Уменьшение количества заявок')
        button_4 = types.KeyboardButton('Отметить заявку как выполненную')
        button_5 = types.KeyboardButton('Отмениить заявку')
        button_6 = types.KeyboardButton('Перенос заявки')
        button_7 = types.KeyboardButton('Блокировка дня')
        button_8 = types.KeyboardButton('Разблокировка дня')
        button_9 = types.KeyboardButton('Изменить права')

        markup.add(button_1, button_6)
        markup.add(button_2, button_3)
        markup.add(button_4, button_5)
        markup.add(button_7, button_8)
        markup.add(button_9)
        bot.send_message(message.chat.id, admin_text, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    user = User.get_user(message.chat.id, message.chat.username, message.from_user.first_name, message.from_user.last_name)
    WorcUser(user).check_user()

    if user.rights == 'not_registered':
        result = WorcUser(user).authorization()
        if result:
            bot.send_message(message.chat.id, "Авторизация пройдена успешно.")
            start_bot_worc(message)
        else:
            bot.send_message(message.chat.id, "Во время авторизации произошла ошибка.\n"
                                              "Повторите попытку.")
            start_bot_worc(message)

    elif user.rights == 'user':
        pass
    elif user.rights == 'admin':
        if message.text == 'Изменить права':
            AdminPanel(user, bot, message).replacement_rights()




if __name__ == '__main__':
    bot.polling()
