from app.db import db
from sqlalchemy.orm import relationship, backref
import datetime


class UserInfo(db.Model):
  __tablename__ = 'userinfo'
  id = db.Column(db.Integer, primary_key = True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  user = relationship('User', backref=db.backref('user_info', lazy='dynamic'))
  spectrum = db.Column('spectrum', db.Integer())
  user_story = db.Column('user_story', db.String())
  goal = db.Column('goal', db.String())
  
  def __init__(self, user, spectrum, user_story, goal):
    self.user = user
    self.spectrum = spectrum
    self.user_story = user_story
    self.goal = goal
    
