from flask import url_for

class TestBlog:
    '''Test Blog'''
    def test_blog_index_view(self, app_client, session):
        response = app_client.get(url_for('blog.index'))
        assert response.status_code == 200

    def test_blog_cant_get_detail_view_when_no_entry(self, app_client, session):
        response = app_client.get(url_for('blog.entry_detail', entry_id=1))
        assert response.status_code == 404

    def test_blog_can_get_detail_view_when_entry(self, app_client, session, create_entries):
        response = app_client.get(url_for('blog.entry_detail', entry_id=1))
        assert response.status_code == 200

    def test_blog_can_search_by_author(self, app_client, session):
        response = app_client.get(url_for('blog.search_by_author', name='Mike'))
        assert response.status_code == 200
