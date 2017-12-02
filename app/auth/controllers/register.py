from . import auth
from ..forms.register_form import RegisterForm
from flask import render_template, request
from ..models.user import User
from app.db import db

@auth.route('/register', methods=['GET'])
def login_get():
  form = RegisterForm(request.form)
  return render_template('register.html', 
                          form=form)
  
@auth.route('/login', methods=['POST'])
def login_post():
  form = RegisterForm(request.form)
  if form.validate_on_submit():
    username = form.username.data
    email = form.email.data
    password = form.password.data
    user = User(username, password, email)
    db.session.add(user)
    db.session.commit()
    flash('User Successfully Registered')