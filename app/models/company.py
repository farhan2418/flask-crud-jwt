from app.extensions import db
from datetime import datetime

class Company(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    c_name = db.Column(db.String[50])
    c_address = db.Column(db.String[100])
    date_opened = db.Column(db.Date, default = datetime.utcnow)

    def __repr__(self):
        return '<Name: %r>' % self.c_name