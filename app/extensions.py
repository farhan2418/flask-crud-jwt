from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import check_password_hash, generate_password_hash


db = SQLAlchemy()
migrate = Migrate()
class HashPassword:
    
    @staticmethod
    def generate_hash(password):
        return generate_password_hash(password, "sha256")
        
        
    
    @staticmethod
    def validate_hash(hashed_pw, input_pw):
        return check_password_hash(hashed_pw, input_pw)
        
    


