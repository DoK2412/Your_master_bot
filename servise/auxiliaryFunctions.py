import datetime

from sqlmodel import Session, select

from database.connection_db import engin
from database.sql_requests import Users



class WorcUser(object):
    def __init__(self, user):
        self.user = user

    def check_user(self):

        with (Session(engin) as session):
            user_view = session.exec(
                select(Users).where(Users.telegram_id == self.user.telegram_id)).first()
            print(user_view)
            if user_view is None:
                self.user.rights = 'not_registered'
            elif user_view.rights == 'admin':
                self.user.user_id_db = user_view.telegram_id
                self.user.rights = user_view.rights
            elif user_view.rights == 'user':
                self.user.user_id_db = user_view.telegram_id
                self.user.rights = user_view.rights

    def authorization(self):
        date = datetime.datetime.now()
        with Session(engin) as session:
            add_useer = Users(telegram_id=self.user.telegram_id,
                              telegram_teg=self.user.telegram_tag,
                              registration_date=str(date),
                              rights='user',
                              user_name=self.user.user_name,
                              surname=self.user.surname)
            session.add(add_useer)
            session.commit()
            return True


class AdminPanel(object):

    bot = None
    user = None
    message = None
    def __init__(self, user, bot, message):
        self.user = user
        self.bot = bot
        self.message = message

    def replacement_rights(self):

        AdminPanel.bot = self.bot
        AdminPanel.user = self.user
        AdminPanel.message = self.message
        with (Session(engin) as session):
            user_view = session.exec(
                select(Users)).all()
            self.bot.send_message(self.message.chat.id, "Выберите и введите id пользователя и укажите права (admin/user) через пробел")

            for user in user_view:
                self.bot.send_message(self.message.chat.id, f"id: {user.id},\nИмя: {user.user_name},\nФамилия: {user.surname}, \nПрава: {user.rights}.")
            self.bot.register_next_step_handler(self.message, AdminPanel.update_rights)

    def update_rights(self):
        data_us = self.text.split()
        if data_us[1] not in ['admin', 'user']:
            AdminPanel.bot.send_message(self.from_user.id,
                                        "Указаны неверные права.\nПовторите ввод.")
            AdminPanel.bot.register_next_step_handler(AdminPanel.message, AdminPanel.update_rights)

        else:
            with Session(engin) as session:
                user_view = session.exec(
                    select(Users).where(Users.id == data_us[0])).one()
                user_view.rights = data_us[1]
                session.add(user_view)
                session.commit()
                session.refresh(user_view)
            AdminPanel.bot.send_message(self.from_user.id,
                                  "Права изменены.")







