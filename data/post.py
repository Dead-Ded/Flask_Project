import sqlalchemy
from flask_login import UserMixin
from .db_session import SqlAlchemyBase


class Post(SqlAlchemyBase, UserMixin):
    __tablename__ = 'post'  # Подключение к таблице 'users' базы данных

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)  # Выбор столбца
    topic_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('topics.id'), nullable=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'),
                                nullable=True)
    message = sqlalchemy.Column(sqlalchemy.String)
    post_date = sqlalchemy.Column(sqlalchemy.TIMESTAMP, nullable=True)
    deleted = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

    def __repr__(self):
        return f'{self.message}'
