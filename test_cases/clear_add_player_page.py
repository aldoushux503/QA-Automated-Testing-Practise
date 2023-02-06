import os
import time
import unittest
from selenium import webdriver

from pages.add_player_page import AddPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestClearPlayer(unittest.TestCase):

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

    def test_clear_player_page(self):
        add_player = AddPlayer(self.driver)  # Check add player page title

        add_player.check_add_player_page_title()  # Check title

        add_player.type_in_email("cat_lover@gmail.com")
        add_player.type_in_phone("+48884404404")
        add_player.type_in_age("05.02.2023")
        add_player.type_in_level("Professional")
        add_player.type_in_district("Masovia")
        add_player.type_in_name("Cat")
        add_player.type_in_weight("70")
        add_player.type_in_leg("Left leg")
        add_player.type_in_main_position("Quarterback")
        add_player.type_in_achievement("Grammy")
        add_player.type_in_surname("Paw")
        add_player.type_in_height("170")
        add_player.type_in_club("Real Madrid")
        add_player.type_in_second_position("Goalkeeper")
        add_player.type_in_laczy_pilka("text ")
        add_player.type_in_ninety("text")
        add_player.type_in_facebook("cat_love.facebook.com")

        add_player.click_on_the_clear_button()

    @classmethod
    def tearDown(self):
        self.driver.quit()
