import sqlalchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .db_session import SqlAlchemyBase
from sqlalchemy.orm import relationship
from .user_status import UserStatus


class Comment(SqlAlchemyBase, UserMixin):
    __tablename__ = 'comments'  # Подключение к таблице 'users' базы данных

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)  # Выбор столбца
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    section_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('sections.id'),
                                   nullable=True)
    topic_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('topics.id'), nullable=True)
    post_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('posts.id'), nullable=True)
    discussion_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('discussions.id'),
                                      nullable=True)
    message = sqlalchemy.Column(sqlalchemy.String)
    date = sqlalchemy.Column(sqlalchemy.TIMESTAMP, nullable=True)
    replyed = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    parrent_comment_id = sqlalchemy.Column(sqlalchemy.Integer,
                                           # sqlalchemy.ForeignKey('comments.id'),
                                                    nullable=True)

    def __repr__(self):
        return f'{self.message}'
