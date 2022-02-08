import pytest
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from account.models import Account
from products.models import Product


CLIENT = Client()


@pytest.mark.django_db
def test_favorites_page():

    email = "donald@gmail.com"
    password = "Xqjrpffh8"
    username = "Donaldduck"
    email_is_active = True

    new_user = Account()
    new_user.username = username
    new_user.password = password
    new_user.email_is_active = email_is_active
    new_user.email = email
    new_user.save()
    new_user.set_password(password)
    new_user.save()

    CLIENT.post("/login/", {"email": "donald@gmail.com", "password": "Xqjrpffh8"})

    response = CLIENT.get(reverse("favoritepage"))

    assert response.status_code == 200
    assertTemplateUsed(response, "favorites.html")


@pytest.mark.django_db
def test_save_fav_view():
    Account.objects.create(
        email="anemail@email.com", username="Testuser", password="Xqjrpffh8"
    )
    Product.objects.create(name="product1", nutriScore="a")
    Product.objects.create(name="product2", nutriScore="b")
    CLIENT.login(email="anemail@email.com", password="Xqjrpffh8")

    response = CLIENT.get(reverse("makefav", kwargs={"productid": 1}))

    assert response.status_code == 302
