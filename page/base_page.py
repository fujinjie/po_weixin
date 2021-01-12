# -*- coding: utf-8 -*-
from selenium import webdriver


class BasePage:
    _base_url = ""

    def __init__(self, driver:webdriver = None):
        if driver is None:
            self.driver = webdriver.Safari()
        else:
            self.driver = driver
        if self._base_url != "":
            self.driver.get(self._base_url)

        self.driver.maximize_window()
        self.driver.implicitly_wait(30)


    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_elements(self, by, locator):
        return self.driver.find_elements(by, locator)

