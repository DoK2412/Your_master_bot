import datetime


from telegram_bot_calendar import WYearTelegramCalendar
from sqlmodel import Session, select

from database.connection_db import engin
from database.sql_requests import Calendar


def get_year(bot, message):
    calendar, step = WYearTelegramCalendar(calendar_id=1,
                                           locale='ru', min_date=datetime.date.today()).build()
    bot.send_message(message.from_user.id,
                          'Укажите месяц.',
                          reply_markup=calendar)

# def get_days_for_calendar(month, user):
#
#     list_day = list()
#     month = str(month.split('_')[-2])
#
#     with Session(engin) as session:
#         all_day = session.exec(select(Calendar).where(Calendar.month == month, Calendar.actively==True)).all()
#     for day in all_day:
#         list_day.append(day.day[:2])
#     user.day = True
#
#     return list_day