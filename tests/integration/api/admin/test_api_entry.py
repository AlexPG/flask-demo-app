import json

class TestAuthor:
    '''Test Entry API'''
    def test_api_entry_cant_get_entry_detail(self, app_client, session):
        response = app_client.get('/api/admin/entries/1')
        assert response.status_code == 404

    def test_api_entry_can_get_entry_index(self, app_client, session):
        response = app_client.get('/api/admin/entries/')
        assert response.status_code == 200

    def test_api_entry_can_post(self, app_client, session, create_authors, create_categories):
        response = app_client.post('/api/admin/entries/',
            data=json.dumps({
                'title': 'Hello World',
                'body': 'This is my first entry',
                'author_id': 1,
                'en_ca': [
                    {
                      'id': 1,
                      'name': 'Python'
                    },
                    {
                      'id': 2,
                      'name': 'Javascript'
                    }
                ]
            }),
            content_type='application/json'
        )
        assert response.status_code == 201

    def test_api_entry_cant_post_with_title_longer_than_50(self, app_client, session):
        response = app_client.post('/api/admin/entries/',
            data=json.dumps({
                'title': 'loremipsumdolorsitametconsecteturadipiscingelitmorb',
                'body': 'This is my first entry',
                'author_id': 1,
            }),
            content_type='application/json'
        )
        assert response.status_code == 404

    def test_api_entry_cant_post_with_non_existing_author(self, app_client, session):
        response = app_client.post('/api/admin/entries/',
            data=json.dumps({
                'title': 'Hello World',
                'body': 'This is my first entry',
                'author_id': 3
            }),
            content_type='application/json'
        )
        assert response.status_code == 404

    def test_api_entry_can_get_entry_detail(self, app_client, session):
        response = app_client.get('/api/admin/entries/1')
        assert response.status_code == 200

    def test_api_entry_can_update_entry(self, app_client, session):
        response = app_client.put('/api/admin/entries/1',
            data=json.dumps({
                'title': 'Hello World again',
                'body': 'This is my first updated entry',
                'author_id': 1,
                'en_ca': [
                    {
                      'id': 1,
                      'name': 'Python'
                    }
                ]
            }),
            content_type='application/json'
        )
        assert response.status_code == 204

    def test_api_entry_cant_update_entry_with_title_longer_than_50(self, app_client, session):
        response = app_client.put('/api/admin/entries/1',
            data=json.dumps({
                'title': 'loremipsumdolorsitametconsecteturadipiscingelitmorb',
                'body': 'This is my first updated entry',
                'author_id': 1
            }),
            content_type='application/json'
        )
        assert response.status_code == 404

    def test_api_entry_can_delete_entry(self, app_client, session):
        response = app_client.delete('/api/admin/entries/1')
        assert response.status_code == 204

    def test_api_entry_cant_delete_already_deleted_entry(self, app_client, session):
        response = app_client.delete('/api/admin/entries/1')
        assert response.status_code == 404