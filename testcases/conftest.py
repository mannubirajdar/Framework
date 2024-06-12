import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture(scope="class")
def pre_req(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    action = ActionChains(driver)
    wait = WebDriverWait(driver, 15)
    url = "https://10.115.254.24:8443/"
    driver.get(url)
    # return the required things to class so that testcase class and conftest should have the linkage
    request.cls.driver = driver
    request.cls.wait = wait
    request.cls.action = action
    yield
    driver.close()

