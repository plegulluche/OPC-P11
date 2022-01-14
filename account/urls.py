from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.registration_view, name='add_user'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('account/', views.account_view, name='account_page'),
    # Activate account 
    path('activate-email/<slug:token>', views.activate_email_view, name='activate'),
    path('success', views.active_succes_view, name='success'),
    path('activate-message', views.activate_message_view, name="activate_your_mail")
]
