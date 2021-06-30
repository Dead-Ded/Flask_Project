import sqlalchemy
from flask_login import UserMixin
from .db_session import SqlAlchemyBase


class Like(SqlAlchemyBase, UserMixin):
    __tablename__ = 'likes'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    post_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('posts.id'), nullable=True)
    comment_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('comments.id'),
                                                                                        nullable=True)

    def __repr__(self):
        pass
