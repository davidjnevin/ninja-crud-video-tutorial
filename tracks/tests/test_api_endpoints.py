"""Place here tests for tracks related endpoints. """
import typing as t

import pytest
import requests
# from django.conf import settings
from django.urls import resolve, reverse, reverse_lazy

# from api import success_message

# from api import success_message


def test_success_message(client):
    # Arrange
    # url = "http://127.0.0.1:8000/api/tracks/success"
    url = reverse_lazy("tracks_api:success")
    print(url)
    # Action
    res = client.get(url)

    # Assert
    assert res.status_code == 200


@pytest.mark.django_db
def test_tracks(client):
    # Arrange
    # url = "http://127.0.0.1:8000/api/tracks/tracks"
    url = reverse_lazy("tracks_api:tracks")
    # Action
    res = client.get(url)

    # Assert
    assert res.status_code == 200
