# conftest.py
import os
import tempfile
from typing import Dict

import pytest
from graph_view import create_app
from graph_view.db import get_db, init_db
from playwright.sync_api import BrowserType

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


class AuthActions(object):

    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post('/auth/login',
                                 data={
                                     'username': username,
                                     'password': password
                                 })

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)


@pytest.fixture(scope="session")
def context(browser_type: BrowserType, browser_type_launch_args: Dict,
            browser_context_args: Dict):
    context = browser_type.launch_persistent_context(
        "./foobar", **{
            **browser_type_launch_args,
            **browser_context_args, "locale": "en-GB",
            "ignore_https_errors": True
        })
    yield context
    context.close()