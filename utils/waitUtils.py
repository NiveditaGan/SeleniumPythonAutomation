from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWaitUtilities:

    def __init__(self, driver):
        self.driver = driver
    def explicit_wait(self, time, text):
        element = WebDriverWait(self.driver, time).until(
            expected_conditions.presence_of_element_located((By.XPATH, text))
        )