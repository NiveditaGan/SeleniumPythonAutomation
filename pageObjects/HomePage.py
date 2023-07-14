from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    name = (By.XPATH, "//input[@name='name' and contains(@class,'form-control')]")
    email = (By.XPATH, "//input[@name='email']")
    passWord = (By.ID, "exampleInputPassword1")
    employment_status = (By.XPATH, "//input[@id='inlineRadio2' and @value='option2']")
    calender = (By.XPATH, "//input[@name='bday']")
    btn_submit = (By.XPATH, "//input[@value='Submit']")
    msg = (By.XPATH, "//*[contains(text(),'Success')]")
    def shopName(self):
        return self.driver.find_element(*HomePage.name)
        # this deserelizes above statement and makes --->
        # driver.find_element_by_xpath("//input[@name='name' and contains(@class,'form-control')]")

    def validateMsg(self):
        return self.driver.find_element(*HomePage.msg)
    def enterEmail(self):
        return self.driver.find_element(*HomePage.email)

    def enterPassword(self):
        return self.driver.find_element(*HomePage.passWord)

    def selectCalender(self):
        return self.driver.find_element(*HomePage.calender)

    def selectSubmit(self):
        return self.driver.find_element(*HomePage.btn_submit)
