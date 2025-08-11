import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-fixed-secret-key'

# Environment-aware database config
if os.getenv("RENDER") == "true":
    # Use Render's environment variables for DB (set these in Render dashboard)
    DB_USER = os.getenv("DB_USER", "your_user")
    DB_PASS = os.getenv("DB_PASS", "your_pass")
    DB_HOST = os.getenv("DB_HOST", "your_host")
    DB_NAME = os.getenv("DB_NAME", "your_dbname")

    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
else:
    # Local development DB config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/movies'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Import routes relatively to avoid module errors
from routes import *  
