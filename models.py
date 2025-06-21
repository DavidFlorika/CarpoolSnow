from flask_login import UserMixin
from app import db, login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    default_location = db.Column(db.String(150))

class CarpoolPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    resort = db.Column(db.String(100))
    time = db.Column(db.String(100))
    pickup_location = db.Column(db.String(100))
    status = db.Column(db.String(20))  # Posted, Scheduled, Completed

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))