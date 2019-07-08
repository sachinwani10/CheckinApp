from db import db

class TimeSheetModel(db.Model):
    __tablename__ = 'time_sheet'

    id = db.Column(db.Integer, primary_key=True)
    timestamp_in = db.Column(db.DateTime)
    timestamp_out = db.Column(db.DateTime)

    username = db.Column(db.String(80), db.ForeignKey('users.username'))
    user = db.relationship('UserModel')

    def __init__(self, username, timestamp_in, timestamp_out):
        self.username = username
        self.timestamp_in = timestamp_in
        self.timestamp_out = timestamp_out

    def json(self):
        return {"username": self.username,
                "timestamp_in": str(self.timestamp_in),
                "timestamp_out": str(self.timestamp_out)
        }

    @classmethod
    def find_in_db(cls, username, timestamp_in, timestamp_out):
        return cls.query.filter_by(username=username). \
        filter(timestamp_in>=timestamp_in). \
        filter(timestamp_out<=timestamp_out)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
