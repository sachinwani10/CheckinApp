from db import db
from models.time_sheet import TimeSheetModel as TS

class SessionModel(db.Model):
    __tablename__ = 'active_sessions'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    timestamp_in = db.Column(db.String(80))
    timestamp_out = db.Column(db.String(80))

    def __init__(self, username, timestamp_in, timestamp_out):
        self.username = username
        self.timestamp_in = timestamp_in
        self.timestamp_out = timestamp_out

    def json(self):
        return {"username": self.username, "timestamp_in": self.timestamp_in,
                "timestamp_out": self.timestamp_out}

    @classmethod
    def find_in_db(cls, username):
        return cls.query.filter_by(username=username).all()

    def save_checkin(self):
        db.session.add(self)
        db.session.commit()

    def save_checkout(self):
        row = self.query.filter_by(username=self.username).first()
        row.timestamp_out = self.timestamp_out
        db.session.commit()
        record = self.query.filter_by(username=self.username).first()
        self.move_to_ts(record)
        self.delete_session(record)

    def move_to_ts(self, record):
        row = TS(record.username, record.timestamp_in, record.timestamp_out)
        row.save_to_db()

    def delete_session(self, record):
        db.session.delete(record)
        db.session.commit()


# https://stackoverflow.com/questions/6699360/flask-sqlalchemy-update-a-rows-information
