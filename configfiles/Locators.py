

class Locator:

    # Login related locators
    SIGN_IN = "//button[text()='Sign In']"
    TEXT_USERNAME = "//input[@name='username']"
    TEXT_PASSWORD = "//input[@name='password']"
    ERR_AREA = "//input[@class='invalid']/following-sibling::span"
    QUERY_CONSOLE = "//span[text()='Query Console']"
    USER_DROPDOWN = "//div[@class='menu-section'][2]/descendant::button"
    USER_LOGGED_IN = "//div[@class='cf']/child::div/strong"

    # Load related locators
    AUTO_CLEAR_RESULTS = "//span[text()='Auto Clear Results']"
    QUERY_AREA = "//div[@class='CodeMirror-lines'][1]"
    QUERY_TEXT_AREA = "//span[@role='presentation']"
    RUN_FUNCTION = "//span[text()='Run']"
    QUERY_RESPONSE_AREA = "//div[@id='resultsId1']/descendant::span[@role]"

