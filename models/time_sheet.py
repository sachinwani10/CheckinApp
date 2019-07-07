from db import db

class TimeSheetModel(db.Model):
    __tablename__ = 'time_sheet'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    timestamp_in = db.Column(db.DateTime)
    timestamp_out = db.Column(db.DateTime)

    def __init__(self, username, timestamp_in, timestamp_out):
        self.username = username
        self. timestamp_in = timestamp_in
        self.timestamp_out = timestamp_out

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
