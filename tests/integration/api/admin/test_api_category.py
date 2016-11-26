import json

class TestCategory:
    '''Test Category API'''
    def test_api_category_cant_get_category_detail(self, app_client, session):
        response = app_client.get('/api/admin/categories/1')
        assert response.status_code == 404

    def test_api_category_can_get_category_index(self, app_client, session):
        response = app_client.get('/api/admin/categories/')
        assert response.status_code == 200

    def test_api_category_can_post(self, app_client, session):
        response = app_client.post('/api/admin/categories/',
            data=json.dumps({
                'name': 'IT'
            }),
            content_type='application/json'
        )
        assert response.status_code == 201

    def test_api_category_cant_post_with_duplicate_name(self, app_client, session):
        response = app_client.post('/api/admin/categories/',
            data=json.dumps({
                'name': 'IT'
            }),
            content_type='application/json'
        )
        assert response.status_code == 404

    def test_api_category_cant_post_with_name_longer_than_50(self, app_client, session):
        response = app_client.post('/api/admin/categories/',
            data=json.dumps({
                'name': 'loremipsumdolorsitametconsecteturadipiscingelitmorb'
            }),
            content_type='application/json'
        )
        assert response.status_code == 404

    def test_api_category_can_post_another_category(self, app_client, session):
        response = app_client.post('/api/admin/categories/',
            data=json.dumps({
                'name': 'Flask'
            }),
            content_type='application/json'
        )
        assert response.status_code == 201

    def test_api_category_can_get_category_detail(self, app_client, session):
        response = app_client.get('/api/admin/categories/1')
        assert response.status_code == 200

    def test_api_category_cant_update_category_with_duplicate_name(self, app_client, session):
        response = app_client.put('/api/admin/categories/1',
            data=json.dumps({
                'name': 'Flask'
            }),
            content_type='application/json'
        )
        assert response.status_code == 404

    def test_api_category_cant_update_category_with_name_longer_than_50(self, app_client, session):
        response = app_client.put('/api/admin/categories/1',
            data=json.dumps({
                'name': 'loremipsumdolorsitametconsecteturadipiscingelitmorb'
            }),
            content_type='application/json'
        )
        assert response.status_code == 404

    def test_api_category_can_update_category(self, app_client, session):
        response = app_client.put('/api/admin/categories/1',
            data=json.dumps({
                'name': 'Python'
            }),
            content_type='application/json'
        )
        assert response.status_code == 204

    def test_api_category_can_delete_category(self, app_client, session):
        response = app_client.delete('/api/admin/categories/1')
        assert response.status_code == 204

    def test_api_category_cant_delete_category_already_deleted(self, app_client, session):
        response = app_client.delete('/api/admin/categories/1')
        assert response.status_code == 404
