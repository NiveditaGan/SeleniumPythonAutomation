import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage
from utils.ExcelUtils import TestGetData
from utils.TestBase import TestBaseclass
from utils.driverHelper import TestDriverHelper
from utils.waitUtils import TestWaitUtilities


class TestEnd2EndValidation(TestBaseclass):

    def test_registration(self, getData):
        self.driver.maximize_window()
        log = self.getLogger()
        log.info("Performing Registration")
        print("Performing Registration")
        homePage = HomePage(self.driver)
        self.driver.refresh()
        homePage.shopName().send_keys(getData[0]["Name"])
        log.info("Name entered is "+getData[0]["Name"])
        homePage.enterEmail().send_keys(getData[0]["Email"])
        homePage.enterPassword().send_keys(getData[0]["Password"])
        homePage.selectSubmit().click()
        assertPage = TestDriverHelper(self.driver)
        assertPage.setPageDriver(self.driver)

    def test_submit_msg(self):
        log = self.getLogger()
        log.info("validate submit message")
        print("validate submit message")
        homePage = HomePage(self.driver)
        waitUtilities = TestWaitUtilities(self.driver)
        waitUtilities.explicit_wait(10, "//*[contains(text(),'Success')]")
        msg = homePage.validateMsg().is_displayed()
        assert msg, "Message is not displayed"


    @pytest.fixture(params=[TestGetData.getCellData("TestCase1"), TestGetData.getCellData("TestCase2"), TestGetData.getCellData("TestCase3")])
    def getData(self, request):
        return request.param



