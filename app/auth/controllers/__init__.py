from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import login
from . import register
from . import logout