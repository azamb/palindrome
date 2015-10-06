from functools import wraps
from werkzeug.exceptions import HTTPException
from api.resources.exceptions import (
    MessageNotFound
)


def api_error_handler(func):
    @wraps(func)
    def handle_errors(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except MessageNotFound as e:
            return e.message, 404
        except HTTPException:
            raise
        except Exception:
            return "API Internal error", 500

    return handle_errors
