import pytest
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from account.models import Account
from products.models import Product
from favorites.models import FavouriteProduct
from favorites.views import favorites_page,save_favorite

CLIENT = Client()

@pytest.mark.django_db
def test_favorites_page():
    
    credentials = {
            "email": "donald@gmail.com",
            "password1": "Xqjrpffh8", 
            "password2" : "Xqjrpffh8",
            "username": "Donaldduck"}
    
    temp_user = CLIENT.post('/register/',credentials)
    CLIENT.post('/login/', {'email': 'donald@gmail.com', 'password': 'Xqjrpffh8'})
    
    response = CLIENT.get(reverse('favoritepage'))
    
    assert response.status_code == 200
    assertTemplateUsed(response, 'favorites.html')



@pytest.mark.django_db
def test_save_fav_view():
    temp_user = Account.objects.create(email ='anemail@email.com',
                                         username = 'Testuser',
                                         password = 'Xqjrpffh8')
    product1 = Product.objects.create(name = 'product1',
                                        nutriScore = 'a')
    product2 = Product.objects.create(name = 'product2',
                                        nutriScore = 'b')
    CLIENT.login(email = 'anemail@email.com', password = 'Xqjrpffh8')
    
    response = CLIENT.get(reverse('makefav', kwargs= {'productid' : 1}))
    
    assert response.status_code == 302
    

