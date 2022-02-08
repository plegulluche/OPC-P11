from django.urls import reverse, resolve


def test_productpage():
    path = reverse("productpage", kwargs={"productid": 1})
    assert path == "/product/1"
    assert resolve(path).view_name == "productpage"


def test_searchresult():
    path = reverse("searchresult")
    assert path == "/searchresults"
    assert resolve(path).view_name == "searchresult"


def test_substitution_results():
    path = reverse("substitute_results", kwargs={"productid": 1})
    assert path == "/substitution_results/1"
    assert resolve(path).view_name == "substitute_results"
