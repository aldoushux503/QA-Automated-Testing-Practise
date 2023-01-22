from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[contains(@class, 'MuiButtonBase-root MuiButton-root')]"
    scouts_panel_xpath = "//*[contains(@class, 'MuiTypography-root MuiTypography-h5')]"
    remind_password_xpath = "//*[contains(@class, 'MuiTypography-root MuiLink')]"
    select_language_xpath = "//*[contains(@class, 'MuiSelect-root MuiSelect')]"
    sing_in_xpath = "///*[contains(@class, 'MuiButtonBase-root MuiButton-root')]"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
