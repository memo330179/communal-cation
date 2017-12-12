from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm
from flask_login import login_required, current_user
from app.models.room import Room
from app.assign.models.request_partner import Request_Partner

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    """Login form to enter a room."""
    room_id = current_user.room_id
    user_requests = Request_Partner.query.filter(Request_Partner.user_id == current_user.id)
    return render_template('index.html', room_id=room_id, current_user=current_user, user_requests=user_requests)


@main.route('/chat/<int:room_id>')
@login_required
def chat(room_id):
    """Chat room. The user's name and room must be stored in
    the session."""
    name = current_user.username
    room = Room.query.get(room_id)
    session['name'] = name
    session['room'] = str(room)
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=room)
