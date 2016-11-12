from flask import url_for

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

    def test_admin_author_cant_post_create_view_with_name_longer_than_50(self, app_client, session):
        response = app_client.post(url_for('admin.author_create'), data={
            'name': 'Lorem ipsum dolor sit amet, consectetur massa nunc.',
            'description': 'Hi, I am Lorem',
            'email': 'lorem@example.com'
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_admin_author_cant_post_create_view_with_duplicate_email(self, app_client, session):
        response = app_client.post(url_for('admin.author_create'), data={
            'name': 'John Doe',
            'description': 'Hi, I am John Doe',
            'email': 'john@example.com'
        }, follow_redirects=True)
        assert response.status_code == 404

    def test_admin_author_cant_post_create_view_with_email_longer_than_120(self, app_client, session):
        response = app_client.post(url_for('admin.author_create'), data={
            'name': 'Lorem',
            'description': 'Hi, I am Lorem',
            'email': 'loremipsumdolorsitametconsecteturadipiscingelitmorbivelauguemalesuadatempornislettempuseratsedsedloremipsumdl@example.com'
        }, follow_redirects=True)
        assert response.status_code == 200

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
