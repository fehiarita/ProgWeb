from flask import Flask, render_template 

app = Flask(__name__)

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

@app.route("/login")
def login():
    return render_template("lauth/login.html")