from flask import Blueprint

assign = Blueprint('assign', __name__)

from . import get_info
from . import assign_partner