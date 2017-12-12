from . import assign
from flask import flash, redirect, url_for, render_template
from ..models.user_info import UserInfo
from app.models.room import Room
from app.auth.models.user import User
from ..models.request_partner import Request_Partner
from app.db import db
from flask_login import current_user, login_required
import random


@assign.route('/profile/<int:user_id>', methods=['GET'])
@login_required
def profile(user_id):
  user = User.query.get(user_id)
  return render_template('profile.html', user=user)

@assign.route('/find_partner', methods=['GET'])
@login_required
def find_people():
  if current_user.user_info[0].spectrum > 50:
    other_users = UserInfo.query.filter(UserInfo.spectrum < 50).filter(UserInfo.user_id != current_user.id)
  elif current_user.user_info[0].spectrum <= 50:
    other_users = UserInfo.query.filter(UserInfo.spectrum > 50).filter(UserInfo.user_id != current_user.id)
    
  return render_template('assign/find_people.html', users = other_users)
  
  
@assign.route('/request_partner/<int:user_id>', methods=['GET'])
@login_required
def request_partner(user_id):
  has_requested = Request_Partner.query.filter(Request_Partner.requester_id == current_user.id).filter(Request_Partner.user_id == user_id)
  
  if not has_requested.count():
    request_partner_obj = Request_Partner(user_id, current_user.id)
    db.session.add(request_partner_obj)
    db.session.commit()
    return redirect(url_for('main.index'))
    
  return "You have already sent a request to this person."
  

@assign.route('/assign_partner/<int:user_id>', methods=['GET'])
@login_required
def assign_partner(user_id):
    user = User.query.get(user_id)
    room = Room('name')
    db.session.add(room)
    db.session.commit()
    current_user.room_id = room.id
    user.room_id = room.id
    db.session.commit()
    
    
  
    return redirect(url_for('main.index'))
  
