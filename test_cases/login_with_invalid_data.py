import os
import unittest
from selenium import webdriver

from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestInvalidLogin(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_invalid_login_in(self):
        user_login = LoginPage(self.driver)  # Create and assign variable class LoginPage

        user_login.check_login_page_title()  # Check login page title
        user_login.type_in_email("usergetnada.com")  # Enter invalid login data
        user_login.type_in_password("Test1234")  # Enter invalid password data
        user_login.click_on_the_sign_in_button()  # Try to log into the webpage
        user_login.check_invalid_password_message()  # Check invalid password pop-up message

    @classmethod
    def tearDown(self):
        self.driver.quit()
