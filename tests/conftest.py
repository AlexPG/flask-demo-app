import pytest

from demo_app import create_app

@pytest.fixture(scope='session')
def app(request):
    app = create_app('testing')
    app_context = app.app_context()
    app_context.push()

    def teardown():
        app_context.pop()

    request.addfinalizer(teardown)

    return app

@pytest.fixture(scope='session')
def app_client(app, request):
    client = app.test_client()

    return client