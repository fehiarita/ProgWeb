from extensions import db

class profile(db.Model):

    id = db.collumn(db.Integer,primary_key=True, unique= True)
    user_id = db.collumn(db.Integer, db.ForeingKey("user_id"), unique= True)
    telefone = db.collumn(db.String(20), nullable=False)
    instituicao = db.collumn(db.String(100), nullable=False)
    cargo = db.collumn(db.String(100), nullable=False, default = "aluno")
    bio = db.collumn(db.Text)
    foto = db.collumn(db.String(300))
    foto_thumb = db.collumn(db.String(300))

    
