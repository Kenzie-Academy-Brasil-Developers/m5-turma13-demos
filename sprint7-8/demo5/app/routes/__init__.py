from flask import Flask

from app.routes.pet_route import pet_routes


def init_app(app: Flask):
    pet_routes(app)
