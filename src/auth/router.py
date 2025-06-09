from flask import Blueprint, request
from .controllers import (
    register_controller,
    login_controller,
    get_current_user_controller,
    forgot_password_controller,
    logout_controller,
)

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    return register_controller(request)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    return login_controller(request)


@auth_bp.route("/me", methods=["GET"])
def get_current_user():
    return get_current_user_controller(request)


@auth_bp.route("/forgot-password", methods=["GET"])
def forgot_password():
    return forgot_password_controller(request)


@auth_bp.route("/logout")
def logout():
    return logout_controller(request)
