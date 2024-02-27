import base64

from appium import webdriver
import time


desired_caps = {}
# 平台名称
desired_caps['platformName'] = 'Android'
# 平台版本
desired_caps['platformVersion'] = '7.1.2'
# 设备号
desired_caps['deviceName'] = '127.0.0.1:62001'
# 应用的包名
desired_caps['appPackage'] = 'com.android.settings'
# 代表启动的界面
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(3)

# 发送文件到手机
# driver.push_file('/sdcard/Download', source_path=r'C:\Users\wsy\Desktop\1.txt')

# 从手机里面拉取文件
# data = driver.pull_file("/sdcard/hello.txt")
# print(data)
# 解码base64数据
# print(str(base64.b64decode(data), "utf-8"))

# 获取当前屏幕内的元素结构
page_data = driver.page_source
if "显示" in page_data:
    print("进入设置页面")
else:
    print("没进入设置页面")

driver.close_app()
driver.quit()












