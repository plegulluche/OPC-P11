from django.urls import path

from main import views

urlpatterns = [
    path("", views.mainpage, name="mainpage"),
    path("legal", views.legalpage, name="legalpage"),
]
