from django.test import Client
from django.urls import reverse, resolve
from products.models import Product,Nutrimage,Category
from django.db.models import Q
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
    nutrimage = Nutrimage.objects.create(name='a', link="fsefseg")
    client = Client()
    response = client.get(reverse('productpage',kwargs={'productid':product.id}))
    
    assert response.status_code == 200
    assertTemplateUsed(response, 'product.html')

@pytest.mark.django_db
def test_search_result_page_redirect():
    
    product1 = Product.objects.create(name='poulet',
                           nutriScore='a',
                           linkToIMG = 'drgdhrdaaarrhdrh',
                            linkToURLOFF = 'drggdrgdrdhrdrhdrh',
                            linkToNutriForG = 'drgdhrzeerdrhdrh'
                            )
    
    client = Client()
    response = client.get(reverse('searchresult'), None)
    assert response.status_code == 302

@pytest.mark.django_db
def test_search_result_page():
    q = "poulet"
    product1 = Product.objects.create(name='poulet',
                           nutriScore='a',
                           linkToIMG = 'drgdhrdaaarrhdrh',
                            linkToURLOFF = 'drggdrgdrdhrdrhdrh',
                            linkToNutriForG = 'drgdhrzeerdrhdrh'
                            )
    product2 = Product.objects.create(name='poisson',
                                      nutriScore='a',
                            linkToIMG = 'drgdhrdaaarrhdrh',
                            linkToURLOFF = 'drggdrgdrdhrdrhdrh',
                            linkToNutriForG = 'drgdhrzeerdrhdrh'
                            )
    nutrimage = Nutrimage.objects.create(name='a', link="fsefseg")
    client = Client()
    response = client.get(reverse('searchresult'), {"q":q})

    assert len(response.context[0]['products']) == Product.objects.filter(Q(name__icontains=q)).order_by('name')[:10].count()
    
    assert response.status_code == 200
    assertTemplateUsed(response, 'research_result.html')
    
    for product in response.context[0]['products']:
        assert q in product.name
        


@pytest.mark.django_db
def test_substitution_results_view():
    category1 = Category.objects.create(name='poulet')
    category2 = Category.objects.create(name='arbre')
    product1 = Product.objects.create(name='pané de poulet',
                           nutriScore='c',
                           linkToIMG = 'drgdhrdaaarrhdrh',
                            linkToURLOFF = 'drggdrgdrdhrdrhdrh',
                            linkToNutriForG = 'drgdhrzeerdrhdrh'
                            )
    product1.category.add(category1)
    product2 = Product.objects.create(name='poulet',
                           nutriScore='a',
                           linkToIMG = 'drgdhrdaaarrhdrh',
                            linkToURLOFF = 'drggdrgdrdhrdrhdrh',
                            linkToNutriForG = 'drgdhrzeerdrhdrh'
                            )
    product2.category.add(category1)
    product3 = Product.objects.create(name='poisson',
                           nutriScore='a',
                           linkToIMG = 'drgdhrdaaarrhdrh',
                            linkToURLOFF = 'drggdrgdrdhrdrhdrh',
                            linkToNutriForG = 'drgdhrzeerdrhdrh'
                            )
    product3.category.add(category2)

    client = Client()
    response = client.get(reverse('substitute_results',kwargs={'productid':product1.id}))
    assert response.status_code == 200
    assertTemplateUsed(response, 'result.html')
    if response.context[0]['substitutes']:
        for product in response.context[0]['substitutes']:
            assert product.name == 'poulet'
        

