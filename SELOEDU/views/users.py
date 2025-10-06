from flask import render_template


users = [
{"id":1, "nome":"Jose",    "email": "jose@gmail.com","role":"Coordenador", "status":"ativo"},
{"id":2, "nome": "Maria",  "email": "mariazinha@gmail.com","role": "Supervizor", "status":"inativo"},
{"id":3, "nome": "Carla",  "email": "carlinha@gmail.com","role": "Desenvolvedor", "status":"ativo"},
{"id":4, "nome": "Pablo",  "email": "pablinho@gmail.com","role": "Analista de Dados", "status":"inativo"},
{"id":5, "nome": "Wesley", "email": "wesley@gmail.com","role": "Designer", "status":"ativo"},
{"id":6, "nome": "Amina",  "email": "Amina@gmail.com","role": "QA", "status":"ativo"}]

def render_show_users_page():

    return render_template("users/show.html", user=users[1])

def render_edit_user_page(id):
    return render_template("users/form.html", user=users[id-1])

def render_list_user_page():
    return render_template("users/index.html", users=users)