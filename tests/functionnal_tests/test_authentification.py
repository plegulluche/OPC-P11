from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

class TestAuthentification(StaticLiveServerTestCase):
    def test_open_chrome_window(self):
        s = Service('/home/ouranos/Documents/Projets python/OPC/Projet 8/tests/functionnal_tests/chromedriver')
        self.browser = webdriver.Chrome(service=s)
        self.browser.get(self.live_server_url)
        time.sleep(30)
        self.browser.close()