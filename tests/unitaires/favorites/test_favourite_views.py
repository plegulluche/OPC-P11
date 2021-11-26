import pytest
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

client = Client()

@pytest.mark.django_db
def test_favorites_page():
    
    credentials = {
            "email": "donald@gmail.com",
            "password1": "Xqjrpffh8", 
            "password2" : "Xqjrpffh8",
            "username": "Donaldduck"}
    
    temp_user = client.post('/register/',credentials)
    client.post('/login/', {'email': 'donald@gmail.com', 'password': 'Xqjrpffh8'})
    
    response = client.get(reverse('favoritepage'))
    
    assert response.status_code == 200
    assertTemplateUsed(response, 'favorites.html')



    
