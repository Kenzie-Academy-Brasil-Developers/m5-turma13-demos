from flask import Flask

from .custom_exc import NotFoundError
from .exc_handlers import generic_error_handler


def init_app(app: Flask):
    app.register_error_handler(NotFoundError, generic_error_handler)
