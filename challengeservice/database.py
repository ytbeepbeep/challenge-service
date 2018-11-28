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

    def set_challenge_user(self,id_usr):
        self.id_user = id_user


    def set_challenge1_run(self,run_one):
        self.run_one = run_one


    def set_challenge2_run(self,run_two):
        self.run_two = run_two


    def set_challenge1_name(self,name_one):
        self.name_run_one = name_one


    def set_challenge2_name(self,name_two):
        self.name_run_two = name_two


    def to_json(self):
        res = {}
        for attr in ('id', 'run_one', 'name_run_one', 'run_two',
                     'name_run_two', 'id_user'):
            value = getattr(self, attr)
            if isinstance(value, datetime):
                value = value.timestamp()
            res[attr] = value
        return res
