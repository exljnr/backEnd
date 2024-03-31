from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

db = SQLAlchemy()

def get_uuid():
    return uuid4().hex

class Outlet(db.Model):
    _tablename_ = "outlets"
    id = db.Column(db.String(255), primary_key=True, unique=True, default=get_uuid)
    outletName = db.Column(db.String(255), unique=True)
    outletOwnerName = db.Column(db.String(255), unique=True)
    outletPhoneNumber = db.Column(db.String(255), unique=True)
    outletPassword = db.Column(db.Text, nullable=False)
    outletUrl = db.Column(db.String(900), unique=True)
