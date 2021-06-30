import sqlalchemy
from flask_login import UserMixin
from .db_session import SqlAlchemyBase
from sqlalchemy.orm import relationship


class Post(SqlAlchemyBase, UserMixin):
    __tablename__ = 'posts'  # Подключение к таблице 'users' базы данных

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)  # Выбор столбца
    topic_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('topics.id'))
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    message = sqlalchemy.Column(sqlalchemy.String)
    date = sqlalchemy.Column(sqlalchemy.TIMESTAMP, nullable=True)
    deleted = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

    user = relationship('User', foreign_keys=[user_id])

    def __repr__(self):
        return f'{self.message}'
