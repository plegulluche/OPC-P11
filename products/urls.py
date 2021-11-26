from django.urls import path

from . import views

urlpatterns = [
    path('product/<int:productid>', views.product_view, name='productpage'),
    path('searchresults', views.search_results, name='searchresult'),
    path('substitution_results/<int:productid>', views.substitution_results, name='substitute_results'),
]