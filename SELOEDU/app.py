from flask import Flask, render_template 
from routes.auth import auth_bp
from routes.users import users_bp
app = Flask(__name__)



app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)

# @app.route("/")
# def home():
#     return render_template("home.html")

# # @app.route("/login")
# # def login():
# #     return render_template("lauth/login.html")

# @app.route("/show")
# def show():
#     return render_template("users/show.html", users=users)