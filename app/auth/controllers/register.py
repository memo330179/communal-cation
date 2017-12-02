from . import auth
from ..forms.register_form import RegistrationForm
from flask import render_template, request, flash, redirect
from flask import url_for
from ..models.user import User
from app.db import db

@auth.route('/register', methods=['GET'])
def register_get():
  form = RegistrationForm(request.form)
  return render_template('auth/register.html', 
                          form=form)
  
@auth.route('/register', methods=['POST'])
def register_post():
  form = RegistrationForm(request.form)
  if form.validate_on_submit():
    username = form.username.data
    email = form.email.data
    password = form.password.data
    user = User(username, password, email)
    db.session.add(user)
    db.session.commit()
    flash('User Successfully Registered')
    return redirect(url_for('auth.get_info'))
  else:
    return redirect(url_for('auth.register_get'))