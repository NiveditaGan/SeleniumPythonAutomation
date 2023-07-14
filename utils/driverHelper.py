import threading


class TestDriverHelper():
    threadToDriver = {None, None}

    def __init__(self, driver):
        self.driver = driver

    def get_pageDriver(self):
       return TestDriverHelper.pageDriver
    def get_threadToDriver(self):
        return TestDriverHelper.threadToDriver
    def setWebDriver(self, driver):
        threadID = threading.get_native_id()
        threadToDriver = {threadID, driver}
        print("{} {}".format("$$$$WEBDRIVER$$$$", threadToDriver))

    def getWebDriver(self):
        threadID = threading.get_native_id()
        threadToDriver = TestDriverHelper.get_threadToDriver()
        return threadToDriver[threadID]

    def setPageDriver(self, driver):
        self.driver = driver

    def getPageDriver(self):
        return self.driver