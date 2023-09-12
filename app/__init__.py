from flask import Flask
from config import Config
from app.extensions import db
from app.extensions import migrate
from app.jwt_handlers import jwt, refresh


def create_app(config_class=Config):
	app = Flask(__name__, static_folder='/home/francium/my_dir/dev/Basic-crud-flask/static')
	app.config.from_object(config_class)
	jwt.init_app(app)
	
	db.init_app(app)
	migrate.init_app(app, db, render_as_batch=True)

	from app.auth import bp as auth_bp
	app.register_blueprint(auth_bp)

	from app.main import bp as main_bp
	app.register_blueprint(main_bp)
	
	from app.create import bp as create_bp
	app.register_blueprint(create_bp)

	from app.update import bp as update_bp
	app.register_blueprint(update_bp)
	 
	@app.route('/test/')
	def test_page():
		return '<h1>Testing the Flask Application Factory Pattern</h1>'
	
	@app.route('/token/refresh')
	def token_refresh():
		return refresh()
	
	return app

