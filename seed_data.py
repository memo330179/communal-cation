from app.db import db
from app.auth.models.user import User
from app.assign.models.user_info import UserInfo
from app import create_app

app = create_app()
with app.app_context():
  db.create_all()
  
  memo = User('memo', 'pass', 'example@example.com')
  
  memow = User('memo2', 'pass', 'example2@example2.com')
  
  db.session.add(memo)
  db.session.add(memow)
  
  db.session.commit()
  
  memo_info = UserInfo(memo, 30, "pass", "pass")
  memow_info = UserInfo(memow, 60, "pass", "pass")
  
  db.session.add(memo_info)
  db.session.add(memow_info)
  
  db.session.commit()
