import datetime


from telegram_bot_calendar import WYearTelegramCalendar


def get_year(bot, message):
    calendar, step = WYearTelegramCalendar(calendar_id=1,
                                           locale='ru', min_date=datetime.date.today()).build()
    bot.send_message(message.from_user.id,
                          'Укажите месяц.',
                          reply_markup=calendar)
