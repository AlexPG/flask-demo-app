from flask import url_for

# Main views
class TestApp: 
    '''Test App'''
    def test_app_is_running(self, app_client):
        response = app_client.get(url_for('main.hello'))
        assert response.status_code == 200

# Admin views
class TestAdmin:
    '''Test Admin'''
    def test_admin_index_view(self, app_client):
        response = app_client.get(url_for('admin.index'))
        assert response.status_code == 200

# Admin views authors
class TestAuthor:
    '''Test Author CRUD'''
    def test_admin_author_can_get_index_view(self, app_client, session):
        response = app_client.get(url_for('admin.authors'))
        assert response.status_code == 200

    def test_admin_author_cant_get_detail_view_when_no_author(self, app_client, session):
        response = app_client.get(url_for('admin.author_detail', author_id=11))
        assert response.status_code == 404

    def test_admin_author_can_get_create_view(self, app_client, session):
        response = app_client.get(url_for('admin.author_create'))
        assert response.status_code == 200

    def test_admin_author_can_post_create_view(self, app_client, session):
        response = app_client.post(url_for('admin.author_create'), data={
            'name': 'John Doe',
            'description': 'Hi, I am John Doe',
            'email': 'john@example.com'
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_admin_author_cant_post_create_view_with_duplicate_email(self, app_client, session):
        response = app_client.post(url_for('admin.author_create'), data={
            'name': 'John Doe',
            'description': 'Hi, I am John Doe',
            'email': 'john@example.com'
        }, follow_redirects=True)
        assert response.status_code == 404

    def test_admin_author_can_post_another_author(self, app_client, session):
        response = app_client.post(url_for('admin.author_create'), data={
            'name': 'Jane Doe',
            'description': 'Hi, I am Jane Doe',
            'email': 'jane@example.com'
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_admin_author_can_get_detail_view_when_author(self, app_client, session):
        response = app_client.get(url_for('admin.author_detail', author_id=1))
        assert response.status_code == 200

    def test_admin_author_can_get_update_view(self, app_client, session):
        response = app_client.get(url_for('admin.author_update', author_id=1))
        assert response.status_code == 200

    def test_admin_author_cant_get_update_view_when_author_does_not_exist(self, app_client, session):
        response = app_client.get(url_for('admin.author_update', author_id=11))
        assert response.status_code == 404

    def test_admin_author_can_post_update_view_new_data(self, app_client, session):
        response = app_client.post(url_for('admin.author_update', author_id=1), 
        data={
            'name': 'Mike Doe',
            'description': 'Hi, I am John Doe',
            'email': 'john@example.com'
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_admin_author_cant_post_update_view_when_email_is_duplicated(self, app_client, session):
        response = app_client.post(url_for('admin.author_update', author_id=1), 
        data={
            'name': 'John Doe',
            'description': 'Hi, I am John Doe',
            'email': 'jane@example.com'
        }, follow_redirects=True)
        assert response.status_code == 404

    def test_admin_author_can_delete_author(self, app_client, session):
        response = app_client.get(url_for('admin.author_delete', author_id=3))
        assert response.status_code == 302

    def test_admin_author_cant_delete_author_already_deleted(self, app_client, session):
        response = app_client.get(url_for('admin.author_delete', author_id=3))
        assert response.status_code == 404

# Admin views categories
class TestCategory:
    '''Test Category CRUD'''
    def test_admin_category_can_get_index_view(self, app_client, session):
        response = app_client.get(url_for('admin.categories'))
        assert response.status_code == 200

    def test_admin_category_can_get_create_view(self, app_client, session):
        response = app_client.get(url_for('admin.category_create'))
        assert response.status_code == 200

    def test_admin_category_can_post_create_view(self, app_client, session):
        response = app_client.post(url_for('admin.category_create'), data={
            'name': 'IT'
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_admin_category_cant_post_create_view_with_duplicate_name(self, app_client, session):
        response = app_client.post(url_for('admin.category_create'), data={
            'name': 'IT'
        }, follow_redirects=True)
        assert response.status_code == 404

    def test_admin_category_can_post_another_category(self, app_client, session):
        response = app_client.post(url_for('admin.category_create'), data={
            'name': 'Sport'
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_admin_category_can_get_update_view(self, app_client, session):
        response = app_client.get(url_for('admin.category_update', category_id=1))
        assert response.status_code == 200

    def test_admin_category_cant_get_update_view_when_category_does_not_exist(self, app_client, session):
        response = app_client.get(url_for('admin.category_update', category_id=11))
        assert response.status_code == 404

    def test_admin_category_can_post_update_view_new_data(self, app_client, session):
        response = app_client.post(url_for('admin.category_update', category_id=1),
        data={
            'name': 'Flask'
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_admin_category_cant_post_update_view_when_name_is_duplicated(self, app_client, session):
        response = app_client.post(url_for('admin.category_update', category_id=1),
        data={
            'name': 'Sport'
        }, follow_redirects=True)
        assert response.status_code == 404

    def test_admin_category_can_delete_category(self, app_client, session):
        response = app_client.get(url_for('admin.category_delete', category_id=3))
        assert response.status_code == 302

    def test_admin_category_cant_delete_category_already_deleted(self, app_client, session):
        response = app_client.get(url_for('admin.category_delete', category_id=3))
        assert response.status_code == 404

# Admin views entries
class TestEntry:
    '''Test Entry CRUD'''
    def test_admin_entry_can_get_index_view(self, app_client, session):
        response = app_client.get(url_for('admin.entries'))
        assert response.status_code == 200

    def test_admin_author_cant_get_detail_view_when_no_entry(self, app_client, session):
        response = app_client.get(url_for('admin.entry_detail', entry_id=11))
        assert response.status_code == 404

    def test_admin_entry_can_get_create_view(self, app_client, session):
        response = app_client.get(url_for('admin.entry_create'))
        assert response.status_code == 200

    def test_admin_entry_can_post_create_view(self, app_client, session):
        response = app_client.post(url_for('admin.entry_create'), data={
            'title': 'Hello World',
            'body': 'This is my first entry',
            'author': 1,
            'category': [1, ]
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_admin_entry_cant_post_create_view_non_existing_author(self, app_client, session):
        response = app_client.post(url_for('admin.entry_create'), data={
            'title': 'Hello World',
            'body': 'This is my second entry',
            'author': 2
        }, follow_redirects=True)
        assert response.status_code == 200
    
    def test_admin_author_can_get_detail_view_when_entry(self, app_client, session):
        response = app_client.get(url_for('admin.entry_detail', entry_id=1))
        assert response.status_code == 200
