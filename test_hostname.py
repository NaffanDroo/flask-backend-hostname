import json
import platform

import pytest

from main import create_app


@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["BCRYPT_LOG_ROUNDS"] = 4
    app.config["WTF_CSRF_ENABLED"] = False

    testing_client = app.test_client()

    context = app.app_context()
    context.push()

    yield testing_client
    context.pop()


@pytest.mark.unit
def test_hostname(test_client):
    response = test_client.get("/v1/host")
    actual_hostname = platform.node()

    assert response.status_code == 200

    response_json = json.loads(response.data)
    assert response_json["backend_host"] == actual_hostname


@pytest.mark.unit
def test_root_url_redirects(test_client):
    response = test_client.get("/")
    actual_hostname = platform.node()

    assert response.status_code == 302


@pytest.mark.unit
def test_root_url_returns_host(test_client):
    response = test_client.get("/", follow_redirects=True)
    actual_hostname = platform.node()

    assert response.status_code == 200

    response_json = json.loads(response.data)
    assert response_json["backend_host"] == actual_hostname
