from flask import render_template, Request, jsonify, Response
from flask_jwt_extended import jwt_required
from .service import (
    login_user_service,
    get_current_user_service,
    logout_user_service,
    create_first_admin_service,
)
from .validation import (
    LoginSchema,
    CreateFirstAdminSchema,
)
from pydantic import ValidationError
from typing import Dict, Any, Union, Tuple


def login_user_controller(
    request: Request,
) -> Union[Response, Tuple[Dict[str, Any], int]]:
    try:
        validated = LoginSchema(**request.get_json())
        return login_user_service(validated, request)
    except ValidationError as e:
        return {"error": str(e)}, 400
    except Exception as e:
        return {"error": str(e)}, 500


@jwt_required()
def get_current_user_controller(
    request: Request,
) -> Union[Response, Tuple[Dict[str, Any], int]]:
    try:
        return get_current_user_service(request)
    except Exception as e:
        return {"error": str(e)}, 500


# def forgot_password_controller(request: Request) -> Response:
#     return render_template("auth/forgot_password.html")


@jwt_required()
def logout_user_controller(
    request: Request,
) -> Union[Response, Tuple[Dict[str, Any], int]]:
    try:
        return logout_user_service(request)
    except Exception as e:
        return {"error": str(e)}, 500


def create_first_admin_controller(
    request: Request,
) -> Union[Response, Tuple[Dict[str, Any], int]]:
    try:
        validated = CreateFirstAdminSchema(**request.get_json())
        return create_first_admin_service(validated, request)
    except ValidationError as e:
        return {"error": str(e)}, 400
    except Exception as e:
        return {"error": str(e)}, 500
