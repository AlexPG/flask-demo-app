import json

class TestAuthor:
    '''Test Author API'''
    def test_api_author_cant_get_author_detail(self, app_client, session):
        response = app_client.get('/api/admin/authors/1')
        assert response.status_code == 404

    def test_api_author_can_get_author_index(self, app_client, session):
        response = app_client.get('/api/admin/authors/')
        assert response.status_code == 200

    def test_api_author_can_post(self, app_client, session):
        response = app_client.post('/api/admin/authors/',
            data=json.dumps({
                'name': 'John',
                'description': 'Hi, I am John Doe',
                'email': 'john@example.com'
            }),
            content_type='application/json'
        )
        assert response.status_code == 201

    def test_api_author_cant_post_with_name_longer_than_50(self, app_client, session):
        response = app_client.post('/api/admin/authors/',
            data=json.dumps({
                'name': 'loremipsumdolorsitametconsecteturadipiscingelitmorb',
                'description': 'Hi, I am John Doe',
                'email': 'lorem@example.com'
            }),
            content_type='application/json'
        )
        assert response.status_code == 404
        
    def test_api_author_cant_post_with_duplicate_email(self, app_client, session):
        response = app_client.post('/api/admin/authors/',
            data=json.dumps({
                'name': 'John',
                'description': 'Hi, I am John Doe',
                'email': 'john@example.com'
            }),
            content_type='application/json'
        )
        assert response.status_code == 404

    def test_api_author_cant_post_with_email_longer_than_120(self, app_client, session):
        response = app_client.post('/api/admin/authors/',
            data=json.dumps({
                'name': 'loremipsumdolorsitametconsecteturadipiscingelitmorbivelauguemalesuadatempornislettempuseratsedsedloremipsumdl',
                'description': 'Hi, I am John Doe',
                'email': 'lorem@example.com'
            }),
            content_type='application/json'
        )
        assert response.status_code == 404

    def test_api_author_can_post_another_author(self, app_client, session):
        response = app_client.post('/api/admin/authors/',
            data=json.dumps({
                'name': 'Jane',
                'description': 'Hi, I am Jane Doe',
                'email': 'jane@example.com'
            }),
            content_type='application/json'
        )
        assert response.status_code == 201

    def test_api_author_can_get_author_detail(self, app_client, session):
        response = app_client.get('/api/admin/authors/1')
        assert response.status_code == 200

    def test_api_author_cant_update_author_with_duplicate_email(self, app_client, session):
        response = app_client.put('/api/admin/authors/1',
            data=json.dumps({
                'name': 'Mike',
                'description': 'Hi, I am John Doe',
                'email': 'jane@example.com'
            }),
            content_type='application/json'
        )
        assert response.status_code == 404

    def test_api_author_cant_update_author_with_name_longer_than_50(self, app_client, session):
        response = app_client.put('/api/admin/authors/1',
            data=json.dumps({
                'name': 'loremipsumdolorsitametconsecteturadipiscingelitmorb',
                'description': 'Hi, I am John Doe',
                'email': 'mike@example.com'
            }),
            content_type='application/json'
        )
        assert response.status_code == 404

    def test_api_author_cant_update_author_with_email_longer_than_120(self, app_client, session):
        response = app_client.put('/api/admin/authors/1',
            data=json.dumps({
                'name': 'Mike',
                'description': 'Hi, I am John Doe',
                'email': 'loremipsumdolorsitametconsecteturadipiscingelitmorbivelauguemalesuadatempornislettempuseratsedsedloremipsumdl@example.com'
            }),
            content_type='application/json'
        )
        assert response.status_code == 404

    def test_api_author_can_update_author(self, app_client, session):
        response = app_client.put('/api/admin/authors/1',
            data=json.dumps({
                'name': 'Mike',
                'description': 'Hi, I am Mike Doe',
                'email': 'mike@example.com'
            }),
            content_type='application/json'
        )
        assert response.status_code == 204

    def test_api_author_can_delete_author(self, app_client, session):
        response = app_client.delete('/api/admin/authors/1')
        assert response.status_code == 204

    def test_api_author_cant_delete_already_deleted_author(self, app_client, session):
        response = app_client.delete('/api/admin/authors/1')
        assert response.status_code == 404
