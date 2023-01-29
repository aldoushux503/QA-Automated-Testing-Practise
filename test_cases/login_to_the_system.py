import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_in_to_the_system(self):
        # Check page title
        user_login = LoginPage(self.driver)
        user_login.check_login_page_title()

        # Check text above login field
        user_login.check_scout_panel_text_label()

        # Log in to the webpage
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_the_sign_in_button()

        # Check test dashboard page title
        dashboard_page = Dashboard(self.driver)
        dashboard_page.check_dashboard_page_title()

    @classmethod
    def tearDown(self):
        self.driver.quit()
