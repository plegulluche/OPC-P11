import pytest

from django.urls import reverse, resolve


def test_main_page_url():
    path = reverse('mainpage')
    assert path == "/home/"
    assert resolve(path).view_name == "mainpage"
