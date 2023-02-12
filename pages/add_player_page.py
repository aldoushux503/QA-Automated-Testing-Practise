import time

from pages.base_page import BasePage


class AddPlayer(BasePage):
    # Add Player page title and URL
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"

    # XPath to the label add player
    add_match_title_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[1]/div/span'

    # XPath to email label and field
    email_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[1]/div/label'
    email_field_xpath = '//input[@name="email"]'

    # XPath to phone label and field
    phone_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[4]/div/label'
    phone_field_xpath = '//input[@name="phone"]'

    # XPath to age label and field
    age_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[7]/div/label'
    age_field_xpath = '//input[@name="age"]'

    # XPath to age label and field
    level_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[10]/div/label'
    level_field_xpath = '//input[@name="level"]'

    # XPath to District label and components
    district_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[13]/div/label'
    district_field_xpath = '//*[@id="mui-component-select-district"]'

    # XPath to add language button
    add_language_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[15]/button'

    # XPath to name label and field
    name_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[2]/div/label'
    name_field_xpath = '//input[@name="name"]'

    # XPath to weight label and field
    weight_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[5]/div/label'
    weight_field_xpath = '//input[@name="weight"]'

    # XPath to leg select label and component
    leg_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[8]/div/label'
    leg_field_xpath = '//*[@id="mui-component-select-leg"]'

    # XPath to main position label and field
    main_position_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[11]/div/label'
    main_position_field_xpath = '//input[@name="mainPosition"]'

    # XPath to achievements label and field
    achievements_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[14]/div/label'
    achievements_field_xpath = '//input[@name="achievements"]'

    # XPath to Surname label and field
    surname_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[3]/div/label'
    surname_field_xpath = '//input[@name="surname"]'

    # XPath to Height label and field
    height_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[6]/div/label'
    height_field_xpath = '//input[@name="height"]'

    # XPath to Club label and field
    club_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[9]/div/label'
    club_field_xpath = '//input[@name="club"]'

    # XPath to Second position label and field
    second_position_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[12]/div/label'
    second_position_field_xpath = '//input[@name="secondPosition"]'

    # XPath to web Laczy label and field
    web_laczy_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[16]/div/label'
    web_laczy_field_xpath = '//input[@name="webLaczy"]'

    # XPath to web90 label and field
    web_ninety_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[17]/div/label'
    web_ninety_field_xpath = '//input[@name="web90"]'

    # XPath to webFB label and field
    facebook_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[18]/div/label'
    facebook_field_xpath = '//input[@name="webFB"]'

    # XPath to add link to YouTube button
    add_link_to_youtube_button_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[19]/button'

    # XPath to submit button
    submit_button_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[1]'

    # XPath to clear button
    clear_button_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[2]'

    # XPath to main page button
    main_page_button_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]'

    # Data for filling fields
    email = "cat_lover@gmail.com"
    phone = "+48884404404"
    age = "05.02.2023"
    level = "Professional"
    district = "Masovia"
    name = "Catt"
    weight = "70"
    leg = "Left leg"
    main_position = "Quarterback"
    achievements = "Grammy"
    surname = "Paw"
    height = "170"
    club = "Real Madrid"
    second_position = "Goalkeeper"
    laczy_pilka = "text"
    ninety = "text"
    facebook = "cat_love.facebook.com"

    # Sample empty field
    cleared_field = ""

    array_XPath = [email_field_xpath, phone_field_xpath, age_field_xpath, level_field_xpath, district_field_xpath,
                   name_field_xpath, weight_field_xpath, leg_field_xpath, main_position_field_xpath,
                   achievements_field_xpath,
                   surname_field_xpath, height_field_xpath, club_field_xpath, second_position_field_xpath,
                   web_laczy_field_xpath,
                   web_ninety_field_xpath, facebook_field_xpath]

    def fill_fields(self):
        self.type_in_email(self.email)
        self.type_in_phone(self.phone)
        self.type_in_age(self.age)
        self.type_in_level(self.level)
        self.type_in_district(self.district)
        self.type_in_name(self.name)
        self.type_in_weight(self.weight)
        self.type_in_leg(self.leg)
        self.type_in_main_position(self.main_position)
        self.type_in_achievement(self.achievements)
        self.type_in_surname(self.surname)
        self.type_in_height(self.height)
        self.type_in_club(self.club)
        self.type_in_second_position(self.second_position)
        self.type_in_laczy_pilka(self.laczy_pilka)
        self.type_in_ninety(self.ninety)
        self.type_in_facebook(self.facebook)

    def check_cleared_player_fields(self):
        # Loop goes through the array_XPath and check that the field is empty
        for path in self.array_XPath:
            self.assert_element_text(self.driver, path, self.cleared_field)
            self.assert_element_text(self.driver, self.email_field_xpath, self.cleared_field)

    def check_add_player_page_title(self):
        self.wait_for_element_to_be_clickable(self.clear_button_xpath)
        assert self.get_page_title(self.add_player_url) == self.expected_title

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def click_on_the_clear_button(self):
        self.click_on_the_element(self.clear_button_xpath)

    def click_on_the_main_page_button(self):
        self.click_on_the_element(self.main_page_button_xpath)

    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_field_xpath, phone)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_level(self, level):
        self.field_send_keys(self.level_field_xpath, level)

    def type_in_district(self, district):
        self.select_in_drop_down_field(self.district_field_xpath, district)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_field_xpath, weight)

    def type_in_leg(self, leg):
        self.select_in_drop_down_field(self.leg_field_xpath, leg)

    def type_in_main_position(self, position):
        self.field_send_keys(self.main_position_field_xpath, position)

    def type_in_achievement(self, achievement):
        self.field_send_keys(self.achievements_field_xpath, achievement)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_height(self, height):
        self.field_send_keys(self.height_field_xpath, height)

    def type_in_club(self, club):
        self.field_send_keys(self.club_field_xpath, club)

    def type_in_second_position(self, second_position):
        self.field_send_keys(self.second_position_field_xpath, second_position)

    def type_in_laczy_pilka(self, laczy_pilka):
        self.field_send_keys(self.web_laczy_field_xpath, laczy_pilka)

    def type_in_ninety(self, ninety):
        self.field_send_keys(self.web_ninety_field_xpath, ninety)

    def type_in_facebook(self, facebook):
        self.field_send_keys(self.facebook_field_xpath, facebook)

    def create_screen_shoot_add_player(self, save_name):
        self.screen_shoot(save_name)
