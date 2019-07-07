from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), index=True, nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    _session = db.relationship('SessionModel')
    work_record = db.relationship('TimeSheetModel')

    def __init__(self, username, password):
        self.password = password
        self.username = username

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
