from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
from src.models.user import User
from src.database.database import SessionLocal
from src.utils.api_response import ApiResponse


# Decorator to validate roles
def role_required(*roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            user_id = get_jwt_identity()
            db = SessionLocal()
            user = db.query(User).get(user_id)
            db.close()
            if not user or user.role not in roles:
                return ApiResponse.error(message="No autorizado", status_code=403)
            return fn(*args, **kwargs)

        return wrapper
    return decorator
