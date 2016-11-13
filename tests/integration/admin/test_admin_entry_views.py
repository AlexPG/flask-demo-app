from flask import url_for

class TestEntry:
    '''Test Entry CRUD'''
    def test_admin_entry_can_get_index_view(self, app_client, session):
        response = app_client.get(url_for('admin.entries'))
        assert response.status_code == 200

    def test_admin_entry_cant_get_detail_view_when_no_entry(self, app_client, session):
        response = app_client.get(url_for('admin.entry_detail', entry_id=11))
        assert response.status_code == 404

    def test_admin_entry_can_get_create_view(self, app_client, session):
        response = app_client.get(url_for('admin.entry_create'))
        assert response.status_code == 200

    def test_admin_entry_can_post_create_view(self, app_client, session, create_authors, create_categories):
        response = app_client.post(url_for('admin.entry_create'), data={
            'title': 'Hello World',
            'body': 'This is my first entry',
            'author': 1,
            'category': [1, ]
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_admin_entry_cant_post_create_view_with_title_longer_than_50(self, app_client, session):
        response = app_client.post(url_for('admin.entry_create'), data={
            'title': 'loremipsumdolorsitametconsecteturadipiscingelitmorb',
            'body': 'This is my second entry',
            'author': 1
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_admin_entry_cant_post_create_view_with_non_existing_author(self, app_client, session):
        response = app_client.post(url_for('admin.entry_create'), data={
            'title': 'Hello World',
            'body': 'This is my second entry',
            'author': 3
        }, follow_redirects=True)
        assert response.status_code == 200
    
    def test_admin_entry_can_get_detail_view_when_entry(self, app_client, session):
        response = app_client.get(url_for('admin.entry_detail', entry_id=1))
        assert response.status_code == 200

    def test_admin_entry_can_get_update_view(self, app_client, session):
        response = app_client.get(url_for('admin.entry_update', entry_id=1))
        assert response.status_code == 200

    def test_admin_entry_cant_get_update_view_when_entry_does_not_exist(self, app_client, session):
        response = app_client.get(url_for('admin.entry_update', entry_id=11))
        assert response.status_code == 404

    def test_admin_entry_can_post_update_view_new_data(self, app_client, session):
        response = app_client.post(url_for('admin.entry_update', entry_id=1),
        data={
            'title': 'New Title',
            'body': 'New content',
            'author': 2,
            'category': [1, 2]
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_admin_entry_can_delete_entry(self, app_client, session):
        response = app_client.get(url_for('admin.entry_delete', entry_id=1))
        assert response.status_code == 302

    def test_admin_entry_cant_delete_entry_already_deleted(self, app_client, session):
        response = app_client.get(url_for('admin.entry_delete', entry_id=1))
        assert response.status_code == 404
