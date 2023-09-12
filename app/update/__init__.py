from flask import Blueprint

bp = Blueprint('update', __name__)
from app.update import routes