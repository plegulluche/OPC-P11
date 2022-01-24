from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

class TestAuthentification(StaticLiveServerTestCase):

        
    def setUp(self):
        s = Service('/home/ouranos/Documents/Projets python/OPC/Projet 11/OPC-p11/tests/functionnal_tests/chromedriver')
        self.browser = webdriver.Chrome(service=s)
        
    
        
    def signup(self):
        self.browser.get(self.live_server_url + reverse('add_user'))
        
        email = self.browser.find_element_by_name('email')
        email.send_keys('testuser2@gmail.com')
        username = self.browser.find_element_by_id('username')
        username.send_keys('testuser2')
        password = self.browser.find_element_by_id('password')
        password.send_keys('Pierre1234')
        register = self.browser.find_element_by_id('register')
        register.click()
        
    
        
        self.assertEqual(self.browser.current_url, self.live_server_url + reverse('activate_your_mail'))
        
        self.browser.close()