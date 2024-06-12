from selenium.webdriver.common.by import By
from base.base_driver import BaseSetup
from configfiles.Locators import Locator


class AZG_LOGIN(BaseSetup):
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        super().__init__(driver, wait)

    user = "admin"
    pas1 = "Passw0rd1"
    SIGN_IN = Locator.SIGN_IN
    TEXT_USERNAME = Locator.TEXT_USERNAME
    TEXT_PASSWORD = Locator.TEXT_PASSWORD
    ERR_AREA = Locator.ERR_AREA
    QUERY_CONSOLE = Locator.QUERY_CONSOLE
    USER_DROPDOWN = Locator.USER_DROPDOWN
    USER_LOGGED_IN = Locator.USER_LOGGED_IN

    def get_sign_in_button(self):
        return self.driver.find_element(By.XPATH, self.SIGN_IN)

    def get_username_textarea(self):
        return self.driver.find_element(By.XPATH, self.TEXT_USERNAME)

    def get_password_textarea(self):
        return self.driver.find_element(By.XPATH, self.TEXT_PASSWORD)

    def get_error_response(self):
        return self.driver.find_element(By.XPATH, self.ERR_AREA)

    def get_invalid_response(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#error")

    def get_user_dropdown(self):
        return self.driver.find_element(By.XPATH, self.USER_DROPDOWN)

    def get_user(self):
        return self.driver.find_element(By.XPATH, self.USER_LOGGED_IN)

    def get_out_from_user_tray(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#menu-appbar")

    def login(self):
        self.add_waits(self.SIGN_IN)
        exp_visible = "Sign In"
        button_visible = self.get_sign_in_button().get_attribute('innerHTML')
        assert button_visible == exp_visible, "Failed :: Login Page is not loaded properly or may be changed"

    def validate_login_errors(self):
        # Scenario - 1 : Validate sign in error by only entering password -
        self.clear_textarea()
        self.get_password_textarea().send_keys(self.pas1)
        self.get_sign_in_button().click()

        exp_uname_err = "Username is required"
        act_uname_err = self.get_error_response().get_attribute('data-error')
        assert act_uname_err == exp_uname_err, "Failed :: error text for username has been changed or blank"

        # Scenario - 2 : Validate sign in error by only entering username -
        self.clear_textarea()
        self.get_username_textarea().send_keys(self.user)
        self.get_sign_in_button().click()

        exp_pass_err = "Password is required"
        act_pass_err = self.get_error_response().get_attribute('data-error')
        assert act_pass_err == exp_pass_err, "Failed :: error text for password has been changed or blank"

        # Scenario - 3 : Validate sign-in for wrong credentials
        self.clear_textarea()
        self.get_username_textarea().send_keys(self.user)
        self.get_password_textarea().send_keys("password")
        self.get_sign_in_button().click()

        exp_err = "Please enter a valid username and password"
        err_msg = self.get_invalid_response().get_attribute('innerHTML')
        list_1 = err_msg.split()  # Store the multiline output into list of strings
        act_cred_err = " "
        act_cred_err = act_cred_err.join(list_1)

        assert act_cred_err == exp_err, "Failed :: Unable to generate error for a valid username and password"

    def validate_login_success(self):
        """
            Validates successful login by reading logged username
            Accepts - None
            Returns - None
        """
        self.clear_textarea()

        # provide the valid username and password in cleared textareas
        self.get_username_textarea().send_keys(self.user)
        self.get_password_textarea().send_keys(self.pas1)
        self.get_sign_in_button().click()

        # Validate that user logged in by reading user name
        self.add_waits(self.QUERY_CONSOLE)
        self.get_user_dropdown().click()
        user_name = self.get_user().get_attribute('innerHTML')
        self.get_out_from_user_tray().click()

        assert user_name != " ", "Failed :: User failed to login"
