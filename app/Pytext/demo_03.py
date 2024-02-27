from appium import webdriver
import time
import pytest


class Test_01():

    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def teardown_class(self):
        self.driver.quit()

    def setup(self):
        self.driver.start_activity('com.android.settings', '.Settings')

    def teardown(self):
        time.sleep(2)
        self.driver.close_app()

    def test_01(self):
        self.driver.find_element_by_id('com.android.settings:id/search').click()
        el = self.driver.find_element_by_id('android:id/search_src_text')
        el.send_keys('abc')
        el.clear()
        el.send_keys('123')
        el.clear()
        el.send_keys('老王')
        el.clear()

    @pytest.mark.run(order=1)
    def test_02(self):
        self.driver.find_element_by_xpath('//*[contains(@text,"更多")]').click()
        text = self.driver.find_element_by_xpath('//*[contains(@text,"移动网络")]').text
        assert '移动网络' == text


if __name__ == '__main__':
    pytest.main(['-s', 'demo_03.py'])
