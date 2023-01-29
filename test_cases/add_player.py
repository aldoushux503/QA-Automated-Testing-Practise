import os
import time
import unittest
from selenium import webdriver

from pages.add_player_page import AddPlayer
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en/players/add')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

        # Log in to the webpage
        user_login = LoginPage(self.driver)
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_the_sign_in_button()

    def test_add_player(self):
        # Check add player page title
        add_player = AddPlayer(self.driver)
        add_player.check_add_player_page_title()

        # Click submit button
        add_player.click_on_the_submit_button()

    @classmethod
    def tearDown(self):
        self.driver.quit()
