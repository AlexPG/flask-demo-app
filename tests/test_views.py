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
def test_admin_author_can_get_index_view(app_client, session):
    response = app_client.get(url_for('admin.authors'))
    assert response.status_code == 200

def test_admin_author_cant_get_detail_view_when_no_user(app_client, session):
    response = app_client.get(url_for('admin.author_detail', author_id=11))
    assert response.status_code == 404

def test_admin_author_can_get_create_view(app_client, session):
    response = app_client.get(url_for('admin.author_create'))
    assert response.status_code == 200

def test_admin_author_can_post_create_view(app_client, session):
    response = app_client.post(url_for('admin.author_create'), data={
        'name': 'John Doe',
        'description': 'Hi, I am John Doe',
        'email': 'john@example.com'
    }, follow_redirects=True)
    assert response.status_code == 200

def test_admin_author_cant_post_create_view_with_duplicate_email(app_client, session):
    response = app_client.post(url_for('admin.author_create'), data={
        'name': 'John Doe',
        'description': 'Hi, I am John Doe',
        'email': 'john@example.com'
    }, follow_redirects=True)
    assert response.status_code == 200

def test_admin_author_can_get_create_view_when_user(app_client, session):
    response = app_client.get(url_for('admin.author_detail', author_id=1))
    assert response.status_code == 200
