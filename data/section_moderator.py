import sqlalchemy
from flask_login import UserMixin
from .db_session import SqlAlchemyBase


class Section_moderator(SqlAlchemyBase, UserMixin):
    __tablename__ = 'section_moderators'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    section_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('sections.id'))

    def __repr__(self):
        return f'{self.name}'
