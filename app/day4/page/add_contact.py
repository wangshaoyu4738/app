

class Add_contact():

    def __init__(self, driver):
        self.driver = driver

    def click_add(self):
        self.driver.find_element_by_id('com.android.contacts:id/floating_action_button').click()

    def click_local(self):
        # 解决第一次存在, 第二次不存在的问题
        lefts = self.driver.find_elements_by_id('com.android.contacts:id/left_button')
        if len(lefts) > 0:
            lefts[0].click()

    def click_return(self):
        self.driver.find_elements_by_class_name('android.widget.ImageButton').click()

    def add_contact(self):
        # self.driver.find_element_by_id('com.android.contacts:id/floating_action_button').click()
        # # 解决第一次存在, 第二次不存在的问题
        # lefts = self.driver.find_elements_by_id('com.android.contacts:id/left_button')
        # if len(lefts) > 0:
        #     lefts[0].click()

        # name = self.driver.find_element_by_xpath('//*[contains(@text,"姓名")]')
        # name.click()
        # name.send_keys('wsy')
        # mobile = self.driver.find_element_by_xpath('//*[contains(@text,"电话")]')
        # mobile.click()
        # mobile.send_keys('13111111111')

        els = self.driver.find_elements_by_class_name('android.widget.EditText')

        els[0].send_keys('wsy')
        els[5].send_keys('13111111111')
        # self.driver.find_elements_by_class_name('android.widget.ImageButton').click()

