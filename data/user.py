import sqlalchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'  # Подключение к таблице 'users' базы данных

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)  # Выбор столбца
    login = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True)  # __||__
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # __||__

    def __repr__(self):
        return f'{self.login}'  # возвращает логин

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)  # Генерация шифрованного ключа к паролю

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)  # Проверка ключа к паролю

