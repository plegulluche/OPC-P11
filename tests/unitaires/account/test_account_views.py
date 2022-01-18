from http import HTTPStatus
from django.contrib.auth import authenticate
from django.test import TestCase
from django.urls import reverse
from django.test import Client
from account.models import Account

class TestView(TestCase):
    
    fixtures = ['account.json']
    def test_registration_view(self):
        #test get method
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200)
        
        #test invalid post data
        response = self.client.post("/register/", data={})
        self.assertEqual(response.status_code, 200)
        
        #test valid post data
        response = self.client.post("/register/", data={
            "email": "donald@gmail.com",
            "password1": "Xqjrpffh8", 
            "password2" : "Xqjrpffh8",
            "username": "Donaldduck"}
        )
        
        self.assertEqual(response.status_code, 302)
        
        user = Account.objects.get(email="donald@gmail.com")
        self.assertEqual(user.email,"donald@gmail.com")

    
    def test_logout_view(self):
        #test get method
        response = self.client.get("/logout/")
        self.assertEqual(response.status_code, 302)
        #test logout
        user = authenticate(email='testuser@gmail.com',password='oAy&mX57qeo&C3cE')
        self.assertTrue(user.is_authenticated)
        self.client.login(email='testuser@gmail.com',password='oAy&mX57qeo&C3cE')
        self.assertIn('_auth_user_id', self.client.session)
        
        self.client.logout()
        self.assertNotIn('_auth_user_id', self.client.session)
    
    def test_valid_login_view(self):
        #test get method
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)
        
        #test redirection
        self.client.login(email='testuser@gmail.com',password='oAy&mX57qeo&C3cE')
        self.assertIn('_auth_user_id', self.client.session)
        
    def test_invalid_login_view(self):    
        #test invalid form data
        self.client.logout()
        self.client.login(email='wrongamail@not.com',password='fejlskfj')
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_account_view(self):
        #test get method
        response = self.client.get("/account/")
        self.assertEqual(response.status_code, 200)
        
        
