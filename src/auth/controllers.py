from flask import (
    render_template,
    redirect,
    url_for,
    flash
)
from .service import (
    register_user_service,
    login_user_service,
    get_current_user_service,
    logout_user_service,
)
from .validation import RegisterSchema, LoginSchema
from pydantic import ValidationError
from flask import Request, Response


def register_controller(request: Request) -> Response | tuple[dict, int]:
    if request.method == "GET":
        return render_template("auth/register.html")
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()
    try:
        validated = RegisterSchema(**data)
    except ValidationError as e:
        if request.is_json:
            return {"error": e.errors()}, 400
        flash("Datos inválidos: " + str(e), "danger")
        return redirect(url_for("auth.register"))
    return register_user_service(validated, request)


def login_controller(request: Request) -> Response | tuple[dict, int]:
    if request.method == "GET":
        return render_template("auth/login.html")
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()
    try:
        validated = LoginSchema(**data)
    except ValidationError as e:
        if request.is_json:
            return {"error": e.errors()}, 400
        flash("Datos inválidos: " + str(e), "danger")
        return redirect(url_for("auth.login"))
    return login_user_service(validated, request)


def get_current_user_controller(request: Request) -> tuple[dict, int]:
    return get_current_user_service(request)


def forgot_password_controller(request: Request) -> Response:
    return render_template("auth/forgot_password.html")


def logout_controller(request: Request) -> Response:
    return logout_user_service(request)
