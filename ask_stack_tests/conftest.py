import pytest

from ask_stack_app import create_app


@pytest.fixture
def app():
    yield create_app


@pytest.fixture
def client(app):
    return app.test_client()
