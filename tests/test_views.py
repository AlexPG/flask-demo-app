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

def test_admin_author_can_get_create_view(app_client, db):
    response = app_client.get(url_for('admin.create_author'))
    assert response.status_code == 200

def test_admin_author_can_post_create_view(app_client, db):
    response = app_client.post(url_for('admin.create_author'), data={
        'name': 'John Doe',
        'description': 'Hi, I am John Doe',
        'email': 'john@example.com'
    }, follow_redirects=True)
    assert response.status_code == 200
