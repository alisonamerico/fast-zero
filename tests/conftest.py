import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app, database
from fast_zero.schemas import UserDB


@pytest.fixture(autouse=True)
def clean_database():
    database.clear()


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def client_with_user():
    database.append(
        UserDB(
            id=1,
            username='alice',
            email='alice@example.com',
            password='secret',
        )
    )
    return TestClient(app)
