import inspect
import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utils.TestBase import TestBaseclass
driver=None

@pytest.fixture(scope="class")
def setup(request):   #request--> instance of the fixture that comes by default for a fixture
    # browser_name=request.config.
    #if(browser_name in "chrome"):
    log=TestBaseclass.getLogger()
    log.info("launching browser")
    print("launching browser")
    global driver
    service_obj = Service("/Users/niveditagan/PycharmProjects/pythonProject1/chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    log.info("navigating to the url")
    print("navigating to the url")
    driver.get("https://www.rahulshettyacademy.com/angularpractice")
    request.cls.driver = driver
    yield
    log.info("close the browser")
    print("close the browser")
    driver.close()
    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
    )

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
       # if (report.skipped and xfail) or (report.failed and not xfail):
        file_name = report.nodeid.replace("::", "_") + ".png"
        _capture_screenshot(file_name)
        if file_name:
            html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
            extra.append(pytest_html.extras.html(html))
    report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

