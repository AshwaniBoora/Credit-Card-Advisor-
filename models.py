from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    issuer = db.Column(db.String(50))
    joining_fee = db.Column(db.Integer)
    annual_fee = db.Column(db.Integer)
    reward_type = db.Column(db.String(50))
    reward_rate = db.Column(db.Float)
    lounge_accesses = db.Column(db.Integer)
    min_income = db.Column(db.Integer)
    perks = db.Column(db.Text)
    image_url = db.Column(db.String(200))
    apply_link = db.Column(db.String(200))