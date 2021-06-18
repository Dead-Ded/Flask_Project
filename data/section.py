import sqlalchemy
from flask_login import UserMixin
from .db_session import SqlAlchemyBase


class Section(SqlAlchemyBase, UserMixin):
    __tablename__ = 'sections'  # Подключение к таблице 'users' базы данных

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)
    deleted = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

    def __repr__(self):
        return f'{self.name}'