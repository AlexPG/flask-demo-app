from flask import url_for

def test_app_is_running(app_client):
    response = app_client.get(url_for('blog.hello'))
    assert response.status_code == 200