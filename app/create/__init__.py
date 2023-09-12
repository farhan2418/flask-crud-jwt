from flask import Blueprint

bp = Blueprint('create',__name__)

from app.create import routes

