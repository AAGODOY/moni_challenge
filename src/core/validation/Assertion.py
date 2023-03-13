from src.core.driver.WebDriver import WebDriver
import allure, pytest, datetime

class Assertion():

    def assertTrue(self,failedMessage,value):
        try:
            assert True == value
            self.__save_screenshot_in_allure()
        except:
            self.__save_screenshot_in_allure()
            pytest.fail(failedMessage,False)

    def assertFalse(self,failedMessage,value):
        try:
            assert False == value
            self.__save_screenshot_in_allure()
        except:
            self.__save_screenshot_in_allure()
            pytest.fail(failedMessage,False)

    def assertEquals(self,failedMessage='', expectedValue=None, actualValue=None):
        try:
            assert expectedValue == actualValue
            self.__save_screenshot_in_allure()
        except:
            self.__save_screenshot_in_allure()
            pytest.fail("{}. Expected: '{}' but Actual is: '{}'".format(failedMessage,expectedValue,actualValue),False)

    def assertNotEquals(self,failedMessage='', expectedValue=None, actualValue=None):
        try:
            assert expectedValue != actualValue
            self.__save_screenshot_in_allure()
        except:
            self.__save_screenshot_in_allure()
            pytest.fail("Equals. Expected: '{}' but Actual is: '{}'. {}".format(expectedValue,actualValue,failedMessage),False)

    def __save_screenshot_in_allure(self):
        allure.attach(WebDriver().get_driver().get_screenshot_as_png(),str(datetime.datetime.now()),attachment_type=allure.attachment_type.PNG)