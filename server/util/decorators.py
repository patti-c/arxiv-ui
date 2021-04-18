import functools
from flask import jsonify


def handles_exceptions_gracefully(func):
    # Basic wrapper that enables endpoints to handle exceptions without blowing up the server

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            return jsonify({'error': e})
    return wrapper
