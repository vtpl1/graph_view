# test_my_application.py
import pytest

pytestmark = pytest.mark.skip("all tests still WIP")
from playwright.sync_api import Page


def test_visit_hello(page: Page):
    page.goto("/hello")
    assert page.inner_text("body") == 'Hello, World!'
    # page.click("text=More information")