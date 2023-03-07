from flask import Flask
from app import routes


# DESIGN PATTER - Factory
def create_app():
    app = Flask(__name__)

    # Inicializando rotas
    routes.init_app(app)

    return app
