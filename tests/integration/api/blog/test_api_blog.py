import json

class TestBlog:
    '''Test Blog API'''
    def test_blog_can_get_blog(self, app_client, session):
        response = app_client.get('/api/blog/')
        assert response.status_code == 200

    def test_blog_cant_get_blog_detail(self, app_client, session):
        response = app_client.get('/api/blog/1')
        assert response.status_code == 404

    def test_blog_can_get_blog_detail(self, app_client, session, create_entries):
        response = app_client.get('/api/blog/1')
        assert response.status_code == 200

    def test_blog_can_search_by_author(self, app_client, session):
        response = app_client.get('/api/blog/search/by_author/Mike')
        assert response.status_code == 200

    def test_blog_can_search_by_category(self, app_client, session):
        response = app_client.get('/api/blog/search/by_category/Python')
        assert response.status_code == 200