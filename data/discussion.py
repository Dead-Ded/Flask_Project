import sqlalchemy
from flask_login import UserMixin
from .db_session import SqlAlchemyBase


class Discussion(SqlAlchemyBase, UserMixin):
    __tablename__ = 'discussions'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    topic_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('topics.id'))
    description = sqlalchemy.Column(sqlalchemy.String)
    date = sqlalchemy.Column(sqlalchemy.TIMESTAMP, nullable=True)
    deleted = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

    def __repr__(self):
        return f'{self.name}'
