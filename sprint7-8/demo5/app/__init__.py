from flask import Flask

from app import exceptions, routes


# DESIGN PATTERN - Factory
def create_app():
    app = Flask(__name__)

    # Inicializando rotas
    routes.init_app(app)

    # Inicializando gerenciador de erros
    exceptions.init_app(app)

    return app
