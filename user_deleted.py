import sqlalchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .db_session import SqlAlchemyBase
from sqlalchemy.orm import relationship


class UserDeleted(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)  # Выбор столбца
    login = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True)  # __||__
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # __||__
    status_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('user_status.id'),
                                  nullable=True)
    registration_date = sqlalchemy.Column(sqlalchemy.TIMESTAMP, nullable=True)
    deleted = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

    status = relationship("UserStatus", foreign_keys=[status_id])