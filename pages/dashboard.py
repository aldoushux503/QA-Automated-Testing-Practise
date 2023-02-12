import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class Dashboard(BasePage):
    # XPath to the menu bar and buttons
    menu_scouts_panel_label_box_xpath = '//h6[text()="Scouts Panel"]'
    menu_main_page_button_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]'
    menu_players_button_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]'
    menu_language_button_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]'
    menu_sign_out_button_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]'

    # XPath to 4 count boxes and their container
    four_count_container = '//*[@id="__next"]/div[1]/main/div[2]'
    players_count_xpath = '//*[@id="__next"]/div[1]/main/div[2]/div[1]/div'
    matches_count_xpath = '//*[@id="__next"]/div[1]/main/div[2]/div[2]/div'
    reports_count_xpath = '//*[@id="__next"]/div[1]/main/div[2]/div[3]/div'
    events_count_xpath = '//*[@id="__next"]/div[1]/main/div[2]/div[4]/div'

    # XPath to Scout panel container, logo, dev contact
    scouts_panel_container_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[1]/div'
    scouts_panel_logo_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[1]'
    scouts_panel_label_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[2]/p'
    scouts_panel_dev_contact_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[3]/a'

    # XPaths to Shortcuts container and add player
    shortcut_container_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[2]/div'
    shortcut_text_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/h2'
    shortcut_add_player_button_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/a/button'

    # XPath to Activity container
    activity_container_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[3]'
    activity_container_title_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/h2'

    # XPath last created player
    last_created_player_textbox_xpath = '//*[text()="Last created player"]'
    last_created_player_link_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[1]'

    # XPath last updated player
    last_updated_player_textbox_xpath = '//*[text()="Last updated player"]'
    last_updated_player_link_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[2]'

    # XPath last created match
    last_created_match_textbox_xpath = '//*[text()="Last created match"]'
    last_created_match_link_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[3]'

    # XPath last updated match
    last_updated_match_textbox_xpath = '//*[text()="Last updated match"]'
    last_updated_match_link_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[4]'

    # XPath last updated report
    last_updated_report_textbox_xpath = '//*[text()="Last updated report"]'
    last_updated_report_link_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[5]'

    # DashBoard URL and expected title for test
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/en"
    expected_title = "Scouts panel"
    expected_language_text_english = "English"

    wait = WebDriverWait(driver, 10)

    def check_dashboard_page_title(self):
        self.wait_for_element_to_be_clickable(self.menu_players_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def check_language_button_text(self):
        self.wait_for_element_to_be_clickable(self.menu_language_button_xpath)
        self.assert_element_text(self.driver, self.menu_language_button_xpath, self.expected_language_text_english)

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.shortcut_add_player_button_xpath)

    def click_on_sign_out_button(self):
        self.click_on_the_element(self.menu_sign_out_button_xpath)

    def click_on_language_button(self):
        self.click_on_the_element(self.menu_language_button_xpath)

    def create_screen_shoot_dashboard(self, save_name):
        self.screen_shoot(save_name)

