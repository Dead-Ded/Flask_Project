import sqlalchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .db_session import SqlAlchemyBase
from sqlalchemy.orm import relationship


class UserStatus(SqlAlchemyBase, UserMixin):
    __tablename__ = 'user_status'  # Подключение к таблице 'users_status' базы данных

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)  # Выбор столбца
    status = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    users = relationship("User")

    def __repr__(self):
        return f'{self.status}'  # возвращает статус
