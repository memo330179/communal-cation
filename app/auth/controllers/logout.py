from . import auth
from flask_login import logout_user, login_required
from flask import url_for, redirect

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('login'))