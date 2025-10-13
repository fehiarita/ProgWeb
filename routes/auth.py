from flask import Blueprint
from views.auth import render_auth_page
auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login")
def login():
    return render_auth_page()
