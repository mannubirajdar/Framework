from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys as Key
from base.base_driver import BaseSetup
from configfiles.Locators import Locator


class Perform_load(BaseSetup):
    def __init__(self, driver, wait, action):
        super().__init__(driver, wait)
        self.driver = driver
        self.action = action

    tickit1 = "LOAD <file:/opt/anzograph/etc/tickit.ttl.gz> INTO GRAPH <tickit>"
    AUTO_CLEAR_RESULTS = Locator.AUTO_CLEAR_RESULTS
    QUERY_AREA = Locator.QUERY_AREA
    QUERY_TEXT_AREA = Locator.QUERY_TEXT_AREA
    RUN_FUNCTION = Locator.RUN_FUNCTION
    QUERY_RESPONSE_AREA = Locator.QUERY_RESPONSE_AREA

    def get_auto_clear_results(self):
        return self.driver.find_element(By.XPATH, self.AUTO_CLEAR_RESULTS)

    def get_query_area(self):
        return self.driver.find_element(By.XPATH, self.QUERY_AREA)

    def get_query_text_area(self):
        return self.driver.find_element(By.XPATH, self.QUERY_TEXT_AREA)

    def get_run_function(self):
        return self.driver.find_element(By.XPATH, self.RUN_FUNCTION)

    def get_query_response_area(self):
        return self.driver.find_element(By.XPATH, self.QUERY_RESPONSE_AREA)

    def validate_basic_load(self):

        act_update_text = " "
        self.add_waits(self.AUTO_CLEAR_RESULTS)
        self.get_auto_clear_results().click()

        # Select all lines from query console and delete it
        query_area = self.get_query_area()
        self.action.click(query_area).key_down(Key.CONTROL).send_keys("a").key_up(Key.CONTROL).key_down(Key.DELETE) \
            .perform()

        # Send the load query to the query console and load it
        self.action.move_to_element(to_element=self.get_query_text_area()).send_keys(self.tickit1).perform()
        self.get_run_function().click()
        self.add_waits(self.RUN_FUNCTION)

        # Validate the load or failure of query
        try:
            exp_update_text = "Update Successful"
            act_update_text = self.get_query_response_area().text
            assert act_update_text == exp_update_text, "Failed :: Update didn't captured"
        except:
            print("Error caught :: ", act_update_text)
