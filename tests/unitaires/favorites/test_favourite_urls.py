from django.urls import reverse, resolve


def test_favorites():
    path = reverse("favoritepage")
    assert path == "/favorites"
    assert resolve(path).view_name == "favoritepage"


def test_makefavourite():
    path = reverse("makefav", kwargs={"productid": 1})
    assert path == "/makefavourite/1"
    assert resolve(path).view_name == "makefav"
