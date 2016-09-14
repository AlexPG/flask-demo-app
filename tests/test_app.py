from flask import current_app

def test_app_creation(app):
    assert not (current_app is None)

def test_current_app_is_testing(app):
    assert current_app.config['TESTING']
