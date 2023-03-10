from flask import Flask
from flask.testing import FlaskClient
from pytest import fixture, fail


@fixture
def app():
    try:
        return __import__("app").create_app()
    except ModuleNotFoundError:
        fail("Verifique se o arquivo principal está nomeado como `app`")
    except AttributeError:
        fail("Verifique se a instancia de Flask está sendo servida pelo `create_app`")


@fixture
def client(app: Flask) -> FlaskClient:
    with app.test_client() as client:
        yield client
