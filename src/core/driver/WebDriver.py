from selenium import webdriver

class WebDriver():
    __DRIVER = None
    __BROWSER = "chrome"
    __INCOGNITO_MODE = True
    __HEADLESS_MODE = False
    __LANG = "es-AR"
    __DRIVER_PATH = "./drivers/chromedriver"
    __URL_APP = "https://demo.opencart.com/admin/"

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(WebDriver, cls).__new__(cls)
        return cls.instance

    def create_driver(self):
        if self.__BROWSER == "chrome":
            chromeoptions = webdriver.ChromeOptions()
            if self.__INCOGNITO_MODE:
                chromeoptions.add_argument("--incognito")
            if self.__HEADLESS_MODE:
                chromeoptions.add_argument("--headless")
                chromeoptions.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")
            if self.__LANG:
                chromeoptions.add_argument("--lang={}".format(self.__LANG))
            self.__DRIVER = webdriver.Chrome(executable_path=self.__DRIVER_PATH, options=chromeoptions)
        self.__DRIVER.maximize_window()
        self.__DRIVER.get(self.__URL_APP)

    def get_driver(self):
        return self.__DRIVER