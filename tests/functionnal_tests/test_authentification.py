from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

class TestAuthentification(StaticLiveServerTestCase):
    def test_open_chrome_window(self):
        self.browser = webdriver.Firefox("tests/functionnal_tests/geckodriver")
        self.browser.get(self.live_server_url)
        time.sleep(30)
        self.browser.close()