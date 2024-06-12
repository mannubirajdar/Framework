import pytest
from pages.login_AZG import AZG_LOGIN
from pages.perform_load import Perform_load


@pytest.mark.usefixtures("pre_req")
class TestAZG_Basic:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login = AZG_LOGIN(self.driver, self.wait)
        self.load = Perform_load(self.driver, self.wait, self.action)

    # TestCase1 : Validate login page error messages and perform successful login
    def test_validate_login_page(self):
        self.login.login()
        self.login.validate_login_errors()
        self.login.validate_login_success()

    def test_validate_basic_load(self):
        self.load.validate_basic_load()