from flask import url_for

class TestAdmin:
    '''Test Admin'''
    def test_admin_index_view(self, app_client):
        response = app_client.get(url_for('admin.index'))
        assert response.status_code == 200
