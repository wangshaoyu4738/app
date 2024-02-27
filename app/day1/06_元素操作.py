# 从appium库里面导入driver对象
from appium import webdriver
# server 启动参数
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# 注: 如果插入中文,需要在desired_caps里面增加2个参数:
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# 声明driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 点击搜索按钮
driver.find_element_by_id("com.android.settings:id/search").click()
# 定位到输入框并输入abc
a = driver.find_element_by_id("android:id/search_src_text")
a.send_keys("abc")
# 清空输入框内容
a.clear()
driver.find_element_by_id("android:id/search_src_text").send_keys("传智播客")
# 获取元素的文本内容
text_vlaue = driver.find_elements_by_class_name("android.widget.TextView")
for i in text_vlaue:
    print(i.text)
# 获取元素的属性值
data = driver.find_element_by_id("com.android.settings:id/title")
print(data.get_attribute('resourceId'))
# 定位搜索按钮
get_value = driver.find_element_by_id("com.android.settings:id/search")
# 输出按钮坐标
print(get_value.location)
# 获取app包名和启动名
print(driver.current_package)
print(driver.current_activity)

