from django.urls import reverse
from django.test import Client
from account.models import Account
import pytest
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db   
def test_registration_view():
    client = Client()
    payload = {
            "email": "foo@gmail.com",
            "password": "oAy&mX57qeo&C3cE", 
            "username": "Donaldduck",
            }
    response = client.post('/register/', payload)
    
    user = Account.objects.filter(email="foo@gmail.com").first()
    
    assert user.email == 'foo@gmail.com'
    assert response.status_code == 302

@pytest.mark.django_db
def test_login_with_valid_user():
    client = Client()
    email = "foo@gmail.com"
    password = "oAy&mX57qeo&C3cE" 
    username = "Donaldduck"
    email_is_active = True
            
    new_user = Account()
    new_user.username = username
    new_user.password = password
    new_user.email_is_active = email_is_active
    new_user.email = email
    new_user.save()
    new_user.set_password(password)
    new_user.save()
    payload = {"email":"foo@gmail.com", "password" :'oAy&mX57qeo&C3cE'}
    response = client.post('/login/', payload)
    assert response.status_code == 302
    assertTemplateUsed('mainpage.html')
    
@pytest.mark.django_db
def test_login_unregistered_user():
    client = Client()
    email = "foo@gmail.com"
    password = "oAy&mX57qeo&C3cE" 
    username = "Donaldduck"
    email_is_active = False
            
    new_user = Account()
    new_user.username = username
    new_user.password = password
    new_user.email_is_active = email_is_active
    new_user.email = email
    new_user.save()
    new_user.set_password(password)
    new_user.save()
    payload = {"email":"foo@gmail.com", "password" :'oAy&mX57qeo&C3cE'}
    response = client.post('/login/', payload)
    message = response.context['message']
    assertTemplateUsed(response, 'login.html')
    assert message == "merci d'activer votre compte"
    assert response.status_code == 200
    
@pytest.mark.django_db
def test_login_wrong_credentials():
    client = Client()
    email = "foo@gmail.com"
    password = "oAy&mX57qeo&C3cE" 
    username = "Donaldduck"
    email_is_active = False
            
    new_user = Account()
    new_user.username = username
    new_user.password = password
    new_user.email_is_active = email_is_active
    new_user.email = email
    new_user.save()
    new_user.set_password(password)
    new_user.save()
    payload = {"email":"foo@gmail.com", "password" :'oA&C3cE'}
    response = client.post('/login/', payload)
    message = response.context['message']
    assertTemplateUsed(response, 'login.html')
    assert message == "vos identifiants ne sont pas corrects"
    assert response.status_code == 200
    
@pytest.mark.django_db
def test_login_invalid_user():
    client = Client()
   
    payload = {"email":"fake@gmail.com", "password" :'57qeo&C3cE'}
    response = client.post('/login/', payload)
    message = response.context['message']
    assertTemplateUsed(response, 'login.html')
    assert message == "aucun utilisateur ne correspond a vos informations saisies"
    assert response.status_code == 200
    

def test_logout_view():
    client = Client()
    response = client.get(reverse('logout'))
    assert response.status_code == 302
    assertTemplateUsed('logout.html')
    
def test_activate_message_view():
    client = Client()
    response = client.get(reverse('activate_your_mail'))
    assert response.status_code == 200
    assertTemplateUsed('activate_email.html')
    
def test_active_succes_view():
    client = Client()
    response = client.get(reverse('success'))
    assert response.status_code == 200
    assertTemplateUsed('active_success.html')

@pytest.mark.django_db
def test_activate_mail_worked_view():
    client = Client()
    email = "foo@gmail.com"
    password = "oAy&mX57qeo&C3cE" 
    username = "Donaldduck"
    token = 1
    email_is_active = False
            
    new_user = Account()
    new_user.username = username
    new_user.token = token
    new_user.password = password
    new_user.email_is_active = email_is_active
    new_user.email = email
    new_user.save()
    new_user.set_password(password)
    new_user.save()
    response = client.get(reverse('activate',kwargs= {'token':1}))
    
    assert response.status_code == 302
    assertTemplateUsed('success.html')
    
@pytest.mark.django_db
def test_activate_mail_failed_view():
    client = Client()
    email = "foo@gmail.com"
    password = "oAy&mX57qeo&C3cE" 
    username = "Donaldduck"
    token = 1
    email_is_active = False
            
    new_user = Account()
    new_user.username = username
    new_user.token = token
    new_user.password = password
    new_user.email_is_active = email_is_active
    new_user.email = email
    new_user.save()
    new_user.set_password(password)
    new_user.save()
    response = client.get(reverse('activate',kwargs= {'token':12}))
    
    assert response.status_code == 302
    assertTemplateUsed('login.html')
    
def test_account_view():
    client = Client()
    response = client.get(reverse('account_page'))
    
    assert response.status_code == 200
    assertTemplateUsed('account_page.html')