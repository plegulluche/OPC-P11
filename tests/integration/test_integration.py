import pytest
from account.forms import AccountAuthenticationForm, RegistrationForm
from account.models import Account
from account.views import (account_view, login_view, logout_view,
                           registration_view)
from django.contrib import auth
from django.http import response
from django.test import Client
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed

CLIENT = Client()

@pytest.mark.django_db
def test_login_route():

    client = Client()

 #Inscrire un utilisateur à l’aide de la vue `signup`afin de l’enregistrer dans la base de données
    credentials = {
            "email": "donald@gmail.com",
            "password1": "Xqjrpffh8", 
            "password2" : "Xqjrpffh8",
            "username": "Donaldduck"}
    
    temp_user = client.post(reverse('add_user'), credentials)

    #Connecter cet utilisateur avec la vue `login`
    response = client.post(reverse('login'), {'email': 'donald@gmail.com', 'password': 'Xqjrpffh8'})

    #Vérifier que la redirection vers la page d’accueil est effectuée
    assert response.status_code == 302
    assert response.url == reverse('mainpage')

    #Vérifier que l’utilisateur est bien authentifié 
    user = auth.get_user(client)
    assert user.is_authenticated
    
@pytest.mark.django_db
def test_signup_route():
    
    """
    Test approach starts with testing if the 'signup' route maps to 'SignUpView'. Then we test 
    if the SignUpView renders the correct template ( registration/signup.html ) with correct Form ( SignUpForm ).
    After that we create a temporary user, by using our 'signup' route and checking if redirects the user to 
    the 'login' route, if everything went fine.
    """

    # Testing if the 'signup' route maps to 'SignUpView'
    url = reverse('add_user')
    assert url == '/register/'

    # Testing if the SignUpView renders the correct template ( registration/signup.html ) with correct Form ( SignupForm )
    response = CLIENT.get(reverse('add_user'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'register.html')

    credentials = {
            "email": "donald@gmail.com",
            "password1": "Xqjrpffh8", 
            "password2" : "Xqjrpffh8",
            "username": "Donaldduck"}
    # creating a temporary user and testing if the user gets redirected to 'login' route if signup was successful
    response = CLIENT.post(reverse('add_user'), credentials)
    assert response.status_code == 302
    assert response.url == reverse('mainpage')
    
    
@pytest.mark.django_db
def test_signup_route_failed():

        """
        Testing 'signup' route with the wrong credentials and testing if user stays on the 'signup' 
        route if the signup process failed
        """

        credentials = {
            "email": "donald@gmail.com",
            "password1": "Xqjrpffh8", 
            "password2" : "",
            "username": "Donaldduck"}
        response = CLIENT.post(reverse('add_user'), credentials)
        assertTemplateUsed(response, 'register.html')


@pytest.mark.django_db
def test_profile_route():

    """
    First we test if 'profile' route  maps to 'account_page', then we login with a temporary user and 
    access the profile route and test if the correct template ( account_page.html ) was rendered
    """
    
    # Testing if the 'profile' route maps to 'account_view'
    url = reverse('account_page')
    assert resolve(url).func, account_view

    credentials = {
            "email": "donald@gmail.com",
            "password1": "Xqjrpffh8", 
            "password2" : "Xqjrpffh8",
            "username": "Donaldduck"}
    temp_user = CLIENT.post(reverse('add_user'), credentials)
    CLIENT.post(reverse('login'), {'username': 'Donaldduck', 'password': 'Xqjrpffh8'})

    # Testing if the ProfileView renders correct template ( profile.html )
    response = CLIENT.get(reverse('account_page'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'account_page.html')