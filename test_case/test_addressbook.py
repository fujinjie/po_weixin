# -*- coding: utf-8 -*-
import pytest

from page.main import Main


class TestAddressBook:

    def test_add_department(self):
        deparements = Main().go_to_addressbook_page().add_department()
        exc = "质量管理部门一组"
        print(deparements)
        assert exc in deparements




if __name__ == "__main__":

    pytest.main(['-v', '-s', 'test_addressbook.py'])