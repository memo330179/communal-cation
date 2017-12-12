from app.db import db

class Room(db.Model):
  __tablename__ = 'rooms'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column('name', db.String())
  
  def __init__(self, name):
    self.name = name
