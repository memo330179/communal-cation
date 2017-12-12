from flask import Flask
from flask_socketio import SocketIO
from flask_login import LoginManager
from .db import db

socketio = SocketIO()
login_manager = LoginManager()


def create_app(debug=True):
    """Create an application."""
    app = Flask(__name__)
    app.config['DEBUG'] = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ubuntu/workspace/Flask-SocketIO-Chat-master/db.sqlite'
    
    import chat
    from .main import main as main_blueprint
    from .auth.controllers import auth as auth_blueprint
    from .assign.controllers import assign as assign_blueprint
    
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(assign_blueprint)

    socketio.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login_get'
    db.init_app(app)
    
    
    return app

