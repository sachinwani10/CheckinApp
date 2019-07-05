import sqlite3
from db import db

class TimeSheetModel(db.Model):
    __tablename__ = 'time_sheet'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    date = db.Column(db.String(80))
    day = db.Column(db.String(80))
    timee = db.Column(db.String(80))

    def __init__(self, date, day, username, timee):
        self.date = date
        self.day = day
        self.username = username
        self.timee = timee
        # self.id = id

    def json(self):
        return {"username": self.username, "date": self.date,
                "day": self.day,
                "time": self.timee
        }

    @classmethod
    def find_in_db(cls, username):
        return cls.query.filter_by(username=username).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
