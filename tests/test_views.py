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
    assert response.status_code == 404

def test_admin_author_can_post_another_author(app_client, session):
    response = app_client.post(url_for('admin.author_create'), data={
        'name': 'Jane Doe',
        'description': 'Hi, I am Jane Doe',
        'email': 'jane@example.com'
    }, follow_redirects=True)
    assert response.status_code == 200

def test_admin_author_can_get_create_view_when_user(app_client, session):
    response = app_client.get(url_for('admin.author_detail', author_id=1))
    assert response.status_code == 200

def test_admin_author_can_get_update_view(app_client, session):
    response = app_client.get(url_for('admin.author_update', author_id=1))
    assert response.status_code == 200

def test_admin_author_cant_get_update_view_when_user_does_not_exist(app_client, session):
    response = app_client.get(url_for('admin.author_update', author_id=11))
    assert response.status_code == 404

def test_admin_author_can_post_update_view_new_data(app_client, session):
    response = app_client.post(url_for('admin.author_update', author_id=1), 
    data={
        'name': 'Mike Doe',
        'description': 'Hi, I am John Doe',
        'email': 'john@example.com'
    }, follow_redirects=True)
    assert response.status_code == 200

def test_admin_author_cant_post_update_view_when_email_is_duplicated(app_client, session):
    response = app_client.post(url_for('admin.author_update', author_id=1), 
    data={
        'name': 'John Doe',
        'description': 'Hi, I am John Doe',
        'email': 'jane@example.com'
    }, follow_redirects=True)
    assert response.status_code == 404

def test_admin_author_can_delete_user(app_client, session):
    response = app_client.get(url_for('admin.author_delete', author_id=2))
    assert response.status_code == 302

def test_admin_author_cant_delete_user_already_deleted(app_client, session):
    response = app_client.get(url_for('admin.author_delete', author_id=2))
    assert response.status_code == 404
