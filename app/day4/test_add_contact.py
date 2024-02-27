from appium import webdriver
import time
import pytest

from day4 import base
from day4.base.base_driver import init_driver
from day4.page.add_contact import Add_contact


class Test_01():
    def setup_class(self):
        # desired_caps = {}
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '7.1.2'
        # desired_caps['deviceName'] = '127.0.0.1:62001'
        # desired_caps['appPackage'] = 'com.android.contacts'
        # desired_caps['appActivity'] = '.activities.PeopleActivity'
        # desired_caps['unicodeKeyboard'] = True
        # desired_caps['resetKeyboard'] = True
        #
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver = init_driver(base.appPackage, base.appActivity)

    def teardown_class(self):
        self.driver.quit()

    def setup(self):
        self.driver.start_activity('com.android.contacts', '.activities.PeopleActivity')

    def teardown(self):
        time.sleep(2)
        self.driver.close_app()

    def test_01(self):
        # self.driver.find_element_by_id('com.android.contacts:id/floating_action_button').click()
        # # 解决第一次存在, 第二次不存在的问题
        # lefts = self.driver.find_elements_by_id('com.android.contacts:id/left_button')
        # if len(lefts) > 0:
        #     lefts[0].click()
        #
        # # name = self.driver.find_element_by_xpath('//*[contains(@text,"姓名")]')
        # # name.click()
        # # name.send_keys('wsy')
        # # mobile = self.driver.find_element_by_xpath('//*[contains(@text,"电话")]')
        # # mobile.click()
        # # mobile.send_keys('13111111111')
        #
        # els = self.driver.find_elements_by_class_name('android.widget.EditText')
        #
        # els[0].send_keys('wsy')
        # els[5].send_keys('13111111111')
        # self.driver.find_elements_by_class_name('android.widget.ImageButton').click()

        ac = Add_contact(self.driver)
        # 点击添加按钮
        ac.click_add()
        # 点击本地存储按钮
        ac.click_local()
        # 添加联系人
        ac.add_contact()
        # 点击返回退出
        ac.click_return()


if __name__ == '__main__':
    pytest.main(['-s', 'test_add_contact.py'])











