from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    amount = db.Column(db.Float)
    description = db.Column(db.String(255))

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    amount = db.Column(db.Float)
    description = db.Column(db.String(255))