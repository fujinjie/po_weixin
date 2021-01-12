# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
import time

from page.home_page import HomePage
from page.addressbook_page import AddressBookPage
from page.login_page import LoginPage


class Main:

    driver = LoginPage().login_with_adjective()


    def go_to_home_page(self):
        self.driver.find_element(By.XPATH, "//*[@id='menu_index']/span").click()
        return HomePage(self.driver)

    def go_to_addressbook_page(self):
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        return AddressBookPage(self.driver)