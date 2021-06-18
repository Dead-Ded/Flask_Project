import sqlalchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .db_session import SqlAlchemyBase
from sqlalchemy.orm import relationship
from .user_status import UserStatus


class Topic(SqlAlchemyBase, UserMixin):
    __tablename__ = 'topics'  # Подключение к таблице 'users' базы данных

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)  # Выбор столбца
    name = sqlalchemy.Column(sqlalchemy.String)
    section_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('sections.id'),
                                   nullable=True)
    unlock = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String)
    deleted = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

    def __repr__(self):
        return f'{self.name}'
