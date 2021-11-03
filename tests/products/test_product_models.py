import pytest


from django.test import Client
from products.models import Products,Category 

@pytest.mark.django_db
def test_product_table():
    client = Client()
    product = Products.objects.create(productName = 'biscuit',
                                     nutriScore = 'a',
                                     linkToIMG = 'alink',
                                     linkToURLOFF = 'anotherlink',
                                     linkToNutriForG = 'alink,once again')
    expected_value = 'biscuit'
    assert str(product.productName) == expected_value

@pytest.mark.django_db
def test_category_table():
    client = Client()
    category = Category.objects.create(categoryName = 'Snacks')
    expected_value = 'Snacks'
    assert str(category.categoryName) == expected_value
