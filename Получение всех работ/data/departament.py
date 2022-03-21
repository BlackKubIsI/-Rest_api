import datetime
import sqlalchemy
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from .db_session import SqlAlchemyBase
from flask_login import UserMixin


class Departament(SqlAlchemyBase, UserMixin):
    __tablename__ = "departament"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    chief = sqlalchemy.Column(sqlalchemy.String)
    members = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String)