from flask import url_for

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

    def test_admin_category_cant_post_create_view_with_name_longer_than_50(self, app_client, session):
        response = app_client.post(url_for('admin.category_create'), data={
            'name': 'loremipsumdolorsitametconsecteturadipiscingelitmorb'
        }, follow_redirects=True)
        assert response.status_code == 200

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
