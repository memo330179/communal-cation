from app.db import db
import datetime

from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column('username', db.String(80), unique=True, nullable=False)
  pw_hash = db.Column('password', db.String())
  email = db.Column('email', db.String())
  has_info = db.Column('has_info', db.Boolean())
  room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
  
  
  def __init__(self, username, password, email):
    self.username = username
    self.email = email
    self.set_password(password)
    
  def is_active(self):
    """All users will be active"""
    return True
    
  def set_password(self, password):
    self.pw_hash = generate_password_hash(password)
    
  def check_password_hash(self, password):
    return check_password_hash(self.pw_hash, password)
  
  def get_id(self):
    return unicode(self.id)
    
  def is_authenticated(self):
    """We don't support users that aren't 
        logged if the object is in memory 
        they will be authenticated
    """
    return True
    
  def is_anonymous(self):
    """We do not support anonymous users"""
    return False
  
  def __repr__(self):
    return '<User {0}>'.format(self.username)