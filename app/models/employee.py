from app.extensions import db
from datetime import datetime

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    e_name = db.Column(db.String[50])
    e_email = db.Column(db.String[100], unique = True)

    date_joined = db.Column(db.Date, default=datetime.utcnow)
    comp_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    company  = db.relationship('Company', backref='employees')
    password = db.Column(db.String[200])

    def __repr__(self):
        return '<Email %r>' % self.e_email 
