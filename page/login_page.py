# -*- coding: utf-8 -*-
import json
from page.base_page import BasePage
import time



class LoginPage(BasePage):

    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def login_with_adjective(self):
        try:
            with open("/Users/fujinjie/PythonProjects/po_weixin/datas/cookies.txt", "r") as f:
                cookies = json.load(f)
                for cookie in cookies:
                    if "expiry" in cookie.keys():
                        cookie.pop("expiry")
                    self.driver.add_cookie(cookie)
            self.driver.get(self._base_url)
            time.sleep(2)
            self.driver.refresh()
        except:
            time.sleep(20)
            cookies = self.driver.get_cookies()
            with open("/Users/fujinjie/PythonProjects/po_weixin/datas/cookies.txt", "w") as f:
                json.dump(cookies, f)
        finally:
            return self.driver



