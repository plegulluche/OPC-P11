import pytest

from products.models import Nutrimage, Product, Category


@pytest.mark.django_db
def test_product_table():
    product = Product.objects.create(
        name="biscuit",
        nutriScore="a",
        linkToIMG="alink",
        linkToURLOFF="anotherlink",
        linkToNutriForG="alink,once again",
    )
    expected_value = "biscuit"
    assert str(product.name) == expected_value
    assert product.__str__() == expected_value


@pytest.mark.django_db
def test_category_table():
    category = Category.objects.create(name="Snacks")
    expected_value = "Snacks"
    assert str(category.name) == expected_value
    assert category.__str__() == expected_value


@pytest.mark.django_db
def test_Nutrimage_table():
    nutrimage = Nutrimage.objects.create(name="a", link="alink")
    expected_value = "a"
    assert str(nutrimage.name) == expected_value
    assert nutrimage.__str__() == expected_value
