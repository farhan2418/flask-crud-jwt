import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config: 
	SECRET_KEY = os.environ.get('SECRET_KEY')
	JWT_SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
	JWT_TOKEN_LOCATION = os.environ.get('JWT_TOKEN_LOCATION')
	JWT_COOKIE_CSRF_PROTECT = True
	JWT_CSRF_CHECK_FORM = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	