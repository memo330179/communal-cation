from . import assign
from flask import render_template, request, flash, redirect
from flask import url_for
from ..models.user_info import UserInfo
from app.db import db
from flask_login import current_user, login_required

@assign.route('/get_info', methods=['GET'])
@login_required
def info_get():
  return render_template('assign/user_info.html')
  
@assign.route('/get_info', methods=['POST'])
@login_required
def info_post():
  data = request.form
  spectrum = data['spectrum']
  user_story = data['about_me']
  goal = data['hope']
  user =  current_user
  user_info = UserInfo(user, spectrum, user_story, goal)
  
  db.session.add(user_info)
  db.session.commit()
  flash('Info Successfully Captured')
  return redirect(url_for('main.index'))
  