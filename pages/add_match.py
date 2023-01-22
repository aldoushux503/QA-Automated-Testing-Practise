from pages.base_page import BasePage


class AddMatch(BasePage):
    # XPath to the whole form on the page
    add_match_form_xpath = '//form'

    # XPath to the title adding match
    add_match_title_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[1]/div/span'

    # XPath to my team field
    my_team_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[1]/div/label'
    my_team_field_xpath = '//input[@name="myTeam"]'

    # XPath to enemy team field
    enemy_team_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[1]/div/label'
    enemy_team_field_xpath = '//input[@name="enemyTeam"]'

    # XPath to my team score field
    my_team_score_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[3]/div/label'
    my_team_score_field_xpath = '//input[@name="myTeamScore"]'

    # XPath to Enemy team score field
    score_enemy_team_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[4]/div/label'
    score_enemy_team_field_xpath = '//input[@name="enemyTeamScore"]'

    # XPath to date field
    date_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[5]/div/label'
    date_field_xpath = '//input[@name="date"]'

    # XPath to "Match at home" or "Match out home select field"
    match_at_or_out_home_select_field_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[6]'

    # XPath to T-shirt color field
    tshirt_color_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[7]/div/label'
    tshirt_color_field_xpath = '//input[@name="tshirt"]'

    # XPath to league field
    league_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[8]/div/label'
    league_field_xpath = '//input[@name="league"]'

    # XPath to time played field
    time_played_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[9]/div/label'
    time_played_field_xpath = '//input[@name="timePlayed"]'

    # XPath to number field
    number_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[10]/div/label'
    number_field_xpath = '//input[@name="number"]'

    # XPath to web match field
    web_match_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[11]/div/label'
    web_match_field_xpath = '//input[@name="webMatch"]'

    # XPath to general field
    general_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[12]/div/label'
    general_field_xpath = '//input[@name="general"]'

    # XPath to rating field
    rating_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[13]/div/label'
    rating_field_xpath = '//input[@name="rating"]'

    # XPath to submit and clear buttons
    submit_button_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[1]'
    clear_button_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[2]'

    pass
