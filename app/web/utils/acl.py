from flask import abort
from flask_login import current_user
from functools import wraps


def roles_required(required_roles: list[str]):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.is_authenticated and current_user.role in required_roles:
                return func(*args, **kwargs)
            else:
                abort(403)  # Forbidden

        return wrapper

    return decorator


def permissions_required(permission: list[str]):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.is_authenticated and current_user.has_permission(
                permission
            ):
                return func(*args, **kwargs)
            else:
                abort(403)

        return wrapper

    return decorator
