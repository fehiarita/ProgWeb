from flask import Blueprint
from views.users import render_show_users_page, render_edit_user_page, render_list_user_page
users_bp = Blueprint('users', __name__)

@users_bp.route("/profile")
def profile():
    return render_show_users_page()

@users_bp.route("/profile/edit/<int:id>")
def edit_profile(id):
    return render_edit_user_page(id)

@users_bp.route("/profile/list")
def list_profile():
    return render_list_user_page()