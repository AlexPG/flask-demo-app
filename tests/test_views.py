from flask import url_for

# Main views

def test_app_is_running(app_client):
    response = app_client.get(url_for('main.hello'))
    assert response.status_code == 200

# Admin views

def test_admin_index_view(app_client):
    response = app_client.get(url_for('admin.index'))
    assert response.status_code == 200

# Admin views authors
def test_admin_author_index_view(app_client, db):
    response = app_client.get(url_for('admin.authors'))
    assert response.status_code == 200