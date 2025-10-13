from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bd = SQLAlchemy()
Login_Manager = LoginManager()
Login_Manager.login_view = "auth.login"