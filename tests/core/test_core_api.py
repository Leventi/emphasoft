import pytest as pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_user(client, user_data):
    url = reverse("users-list")
    response = client().post(url, user_data)

    assert response.status_code == 201
