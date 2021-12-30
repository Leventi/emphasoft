from rest_framework.test import APIClient
import pytest


@pytest.fixture
def client():
    return APIClient


@pytest.fixture
def user_data():
    return {
        "username": "user1",
        "first_name": "Alex",
        "last_name": "Zii",
        "password": "321"
    }




