import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.add_player_page import AddPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en/players/add')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

        # Create and assign class Login and Dashboard
        user_login = LoginPage(self.driver)
        dashboard_page = Dashboard(self.driver)

        # Log into the system and load the dashboard page
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_the_sign_in_button()

        dashboard_page.check_dashboard_page_title()  # Check dashboard page title
        dashboard_page.click_on_the_add_player_button()  # Go to Add player page

    def test_add_player(self):
        add_player = AddPlayer(self.driver)  # Check add player page title
        dashboard_page = Dashboard(self.driver)

        add_player.check_add_player_page_title()  # Check title
        add_player.fill_fields()  # Fill all fields on Add Player page
        add_player.click_on_the_submit_button()  # Add new player to database
        add_player.click_on_the_main_page_button()  # Go to dashboard page

        dashboard_page.check_dashboard_page_title()  # Check test dashboard page title
        dashboard_page.check_last_added_player()  # Check last added player on the dashboard page

    @classmethod
    def tearDown(self):
        self.driver.quit()
