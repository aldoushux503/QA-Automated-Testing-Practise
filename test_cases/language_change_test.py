import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLanguageChange(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_change_language(self):
        user_login = LoginPage(self.driver)  # Create and assign variable class LoginPage and Dashboard
        dashboard_page = Dashboard(self.driver)

        user_login.check_login_page_title()  # Check login page title
        user_login.check_scout_panel_text_label()  # Check text above login field
        user_login.type_in_email("user01@getnada.com")  # Enter correct Login data
        user_login.type_in_password("Test-1234")  # Enter correct Password data
        user_login.click_on_the_sign_in_button()  # Log into the webpage

        dashboard_page.check_dashboard_page_title()  # Check dashboard page title
        dashboard_page.click_on_language_button()  # Check test dashboard page title
        dashboard_page.check_language_button_text()  # Check language changed to Polish

    @classmethod
    def tearDown(self):
        self.driver.quit()
