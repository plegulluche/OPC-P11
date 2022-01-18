from django.test import Client
from django.test.client import Client as NewClient,RequestFactory
from django.urls import reverse, resolve
from pytest_django.asserts import assertTemplateUsed

from main.views import mainpage

import pytest


def test_main_page_view():
    client = Client()
    path = reverse('mainpage')
    response = client.get(path)
    
    assert response.status_code == 200    
    
def test_main_renders_html():
    url = reverse('mainpage')
    client = Client()
    response = client.get(url)
    
    assert resolve(url).view_name == 'mainpage'
    
def test_legal_page_view():
    client = Client()
    path = reverse('legalpage')
    response = client.get(path)
    
    assert response.status_code == 200
    assert resolve(path).view_name == 'legalpage'

def test_404():
    client = NewClient()
    path = '/account/123'
    request = client.get(path)
    
    assertTemplateUsed(request, 'not-found.html')