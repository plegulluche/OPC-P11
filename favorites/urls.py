from django.urls import path

from . import views

urlpatterns = [
    path('favorites', views.favorites_page, name='favoritepage'),
    path('makefavourite/<int:productid>', views.save_favorite, name='makefav'),
    
]