from flask import Flask, render_template,login_manager
import os
from extensions import db
from models.users import User
from routes.auth import auth_bp 
from routes.users import users_bp

app = Flask(__name__,static_folder="static",template_fouder="templates")
app.config.from_object("config.Config")

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok= True)
os.makedirs("instance",exist_ok=True)

db.init_app(app)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()
    if not User.query.filter_by(email= "admin@seloedu.com").first():
        master = User(
            nome= "user",
            email = "admin@seloedu.com",
            role = "master"
        )
        master.set_password("1234")
        db.session.add(master)
        db.session.commit()
        print("Usuario masterr criado")





users = [
{"id":1, "nome":"Jose",    "email": "jose@gmail.com","perfil":"Coordenador", "status":"ativo"},
 {"id":2, "nome": "Maria",  "email": "mariazinha@gmail.com","perfil": "Supervizor", "status":"inativo"},
 {"id":3, "nome": "Carla",  "email": "carlinha@gmail.com","perfil": "Desenvolvedor", "status":"ativo"},
 {"id":4, "nome": "Pablo",  "email": "pablinho@gmail.com","perfil": "Analista de Dados", "status":"inativo"},
 {"id":5, "nome": "Wesley", "email": "wesley@gmail.com","perfil": "Designer", "status":"ativo"},
 {"id":6, "nome": "Amina",  "email": "Amina@gmail.com","perfil": "QA", "status":"ativo"}]


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard(params):
    return render_template("dashboard.html")

app.register_blueprint(auth_dp)
app.register_blueprint(users_bp)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/login")
def login():
    return render_template("auth/login.html")

@app.route("/profile")
def profile():
    return render_template("users/profile.html")

