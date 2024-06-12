from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BaseSetup():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        

    def clear_textarea(self):  # For clearing the text areas for clean input
        self.driver.find_element(By.XPATH, "//input[@name='username']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='password']").clear()

    def add_waits(self, param):
        comp_status = self.wait.until(EC.visibility_of_element_located((By.XPATH, param)))
        comp_status.is_displayed()