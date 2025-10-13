from flask import Blueprint
from views import users as users_views

users_bp = Blueprint("users",__name__, url_prefix="/users")

users_bp.add_url_rule("/", view_func=users_views)
users_bp.add_url_rule("/create", view_func=users_views.create, methods=["GET","POST"])
users_bp.add_url_rule("/<int:user_id>", view_func=users_views.show)
users_bp.add_url_rule("/<int:user_id>/edit", view_func=users_views.edit, methods=["GET","POST"])
users_bp.add_url_rule("/<int:user_id/delete>", view_func=users_views.delete, methods=["POST"])
users_bp.add_url_rule("/profile", view_func=users_views.profile, methods=["GET", "POST"])
