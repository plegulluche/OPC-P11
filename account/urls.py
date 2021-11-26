from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.registration_view, name='add_user'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('account/', views.account_view, name='account_page'),
]
