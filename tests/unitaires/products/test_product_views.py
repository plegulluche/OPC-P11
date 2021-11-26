from django.test import Client
from django.urls import reverse, resolve
from products.models import Product
import pytest
from pytest_django.asserts import assertTemplateUsed

@pytest.mark.django_db
def test_product_page():
    product = Product.objects.create(name='fsefesg',
                           nutriScore='a',
                           linkToIMG = 'drgdhrdaaarrhdrh',
                            linkToURLOFF = 'drggdrgdrdhrdrhdrh',
                            linkToNutriForG = 'drgdhrzeerdrhdrh'
                            )
    client = Client()
    response = client.get(reverse('productpage',kwargs={'productid':1}))
    
    assert response.status_code == 200
    assertTemplateUsed(response, 'product.html')