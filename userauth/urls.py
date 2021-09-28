from django.urls import path

from . import views

urlpatterns = [
    path('', views.authpage, name='authpage'),
    path('adduser/', views.create_user, name='add_user'),
]
