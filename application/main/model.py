from application import app, db
from datetime import datetime


class Mayfarm(db.Model):
    __tablename__ = 'token'
    id = db.Colmun(db.Integer, primary_key=True)
