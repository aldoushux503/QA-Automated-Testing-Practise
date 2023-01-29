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

    # XPath to District label and component
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
    web_90_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[17]/div/label'
    web_90_field_xpath = '//input[@name="web90"]'

    # XPath to webFB label and field
    webFB_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[18]/div/label'
    webFB_field_xpath = '//input[@name="webFB"]'

    # XPath to add link to YouTube button
    add_link_to_youtube_button_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[19]/button'

    # XPath to submit button
    submit_button_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[1]'

    # XPath to clear button
    clear_button_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[2]'

    def check_add_player_page_title(self):
        time.sleep(5)
        assert self.get_page_title(self.add_player_url) == self.expected_title

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)




