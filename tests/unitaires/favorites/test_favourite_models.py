import pytest

from favorites.models import FavouriteProduct
from account.models import Account
from products.models import Product


@pytest.mark.django_db
def test_favorites_model():
    user = Account.objects.create(
        username="blob", email="blob@blobmail.com", password="SuperPass1234"
    )
    product = Product.objects.create(name="jambon", nutriScore="a")
    favorite = FavouriteProduct.objects.create(user=user, product=product)

    expected_value = "product jambon marked favourite by blob"
    assert str(favorite) == expected_value
