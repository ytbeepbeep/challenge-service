from datetime import datetime
from decimal import Decimal
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


# add the table Challenge
class Challenge(db.Model):
    __tablename__ = 'challenge'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    run_one = db.Column(db.Integer)
    name_run_one = db.Column(db.Unicode(128))
    run_two = db.Column(db.Integer)
    name_run_two = db.Column(db.Unicode(128))
    id_user = db.Column(db.Integer)

    def to_json(self):
        res = {}
        for attr in ('id', 'run_one', 'name_run_one', 'run_two',
                     'name_run_two', 'id_user'):
            res[attr] = getattr(self, attr)
        return res
