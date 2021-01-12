# -*- coding: utf-8 -*-
from po_weixin.page.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class AddressBookPage(BasePage):

    def add_department(self):
        self.find_element(By.XPATH, "//*[@id='js_contacts47']/div/div[1]/div/div[1]/a/i").click() # 点击页面的【+】
        self.find_element(By.XPATH, "//*[@id='js_contacts47']/div/div[1]/ul/li[1]/a").click() # 点击【添加部门】
        self.find_element(By.XPATH, "//*[@class='qui_inputText ww_inputText']").send_keys("质量管理部门一组") # 输入要添加的部门名称
        time.sleep(5)
        self.find_element(By.XPATH,"//*[@id='__dialog__MNDialog__']/div/div[2]/div/form/div[3]/a/span[2]").click() # 点击所属部门下拉按钮
        time.sleep(5)
        self.find_element(By.XPATH, "//*[@class='qui_dropdownMenu ww_dropdownMenu member_colLeft js_party_list_container']//*[@id='1688851069644523_anchor']").click() # 点击部门列表下的"质量管理部"
        time.sleep(3)
        self.find_element(By.XPATH, "//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]").click() # 点击【确定】
        time.sleep(3)
        departments = self.find_elements(By.XPATH, "//*[@class='jstree-anchor']")
        departments_text_list = []
        for element in departments:
            departments_text_list.append(element.text)
        return departments_text_list




