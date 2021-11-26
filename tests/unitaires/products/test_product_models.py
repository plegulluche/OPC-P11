import pytest


from django.test import Client
from products.models import Nutrimage, Product,Category 

@pytest.mark.django_db
def test_product_table():
    client = Client()
    product = Product.objects.create(name = 'biscuit',
                                     nutriScore = 'a',
                                     linkToIMG = 'alink',
                                     linkToURLOFF = 'anotherlink',
                                     linkToNutriForG = 'alink,once again')
    expected_value = 'biscuit'
    assert str(product.name) == expected_value

@pytest.mark.django_db
def test_category_table():
    client = Client()
    category = Category.objects.create(name = 'Snacks')
    expected_value = 'Snacks'
    assert str(category.name) == expected_value


@pytest.mark.django_db
def test_Nutrimage_table():
    client = Client()
    nutrimage = Nutrimage.objects.create(name = 'a',link = 'alink')
    expected_value = 'a'
    assert str(nutrimage.name) == expected_value