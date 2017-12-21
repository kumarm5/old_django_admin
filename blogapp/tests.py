# from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# Create your tests here.

class AccountTestCase(LiveServerTestCase):
    
    def setUp(self):
        self.selenium = webdriver.Chrome('C:/Users/Mukul Kumar/Downloads/chromedriver_win32/chromedriver.exe')
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_login(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin/login/')

        #find the form element
        first_name = selenium.find_element_by_id('id_username')
        last_name = selenium.find_element_by_id('id_password')

        submit = selenium.find_element_by_name('login')

        #Fill the form with data
        first_name.send_keys('admin')
        time.sleep(1)
        last_name.send_keys('admin@123')
        time.sleep(1)
        #submitting the form
        submit.send_keys(Keys.RETURN)
        time.sleep(1)
        #check the returned result
        assert 'Site administration' in selenium.page_source

    # def test_logout(self):
    #     selenium = self.selenium
    #     #Opening the link we want to test
    #     selenium.get('http://127.0.0.1:8000/admin/')

    #     id_logout = selenium.find_element_by_id('id_logout')

    #     assert 'Logged out' in selenium.page_source
