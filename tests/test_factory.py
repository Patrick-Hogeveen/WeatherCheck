from weather import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/')
    print(response.data)
    assert response.data == b'Hello, World!'