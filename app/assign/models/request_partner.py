from app.db import db
from sqlalchemy.orm import relationship, backref
import datetime


class Request_Partner(db.Model):
  __tablename__ = 'request_partner'
  id = db.Column(db.Integer, primary_key = True)
  requester_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  date_sent = db.Column(db.DateTime)
  
  
  def __init__(self, user_id, requester_id):
    self.requester_id = requester_id
    self.user_id = user_id
    self.date_sent = datetime.datetime.now()
    