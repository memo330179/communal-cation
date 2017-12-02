from . import auth
from flask import request, render_template
from flask import url_for, redirect, flash, abort
from ..forms.login_form import LoginForm
from flask_login import login_user
from ..models.user import User
from app import login_manager

@auth.route('/login', methods=['GET'])
def login_get():
  form = LoginForm(request.form)
  return render_template('login.html', 
                          form=form)
  
@auth.route('/login', methods=['POST'])
def login_post():
  form = LoginForm(request.form)
  if form.validate_on_submit():
    user = User.query.get(form.username.data)
    if user is not None and user.check_password_hash(form.password.data):
      login_user(user)
      
      flash('Logged in successfully.')
      
      next = request.args.get('next')
      # we should use safe redirects here
      redirect(next or url_for('index'))
    else:
      abort(403)
      
@login_manager.user_loader
def load_user(user_id):
  return User.get(user_id)
  
  