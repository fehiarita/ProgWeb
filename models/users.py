from extensions import db

class users:
    id = db.collumn(db.Interger, primary_key=True)
    nome = db.collumn(db.String(150), nullable= True)
    email = db.collumn(db.String(150), nullable= True)
    password_hash = db.collumn(db.String(255), nullable= True)
    role = db.collumn(db.String(100))
    ativo = db.collumn(db.boolean)

    users = db.relationship("users",back_templates="profile")

    