import pytest

from django.urls import reverse, resolve


def test_register():
    path = reverse('add_user')
    assert path == '/register/'
    assert resolve(path).view_name == 'add_user'

def test_login():
    path = reverse('login')
    assert path == '/login/'
    assert resolve(path).view_name == 'login'
    
def test_logout():
    path = reverse('logout')
    assert path == '/logout/'
    assert resolve(path).view_name == 'logout'
    
def test_account():
    path = reverse('account_page')
    assert path == '/account/'
    assert resolve(path).view_name == 'account_page'