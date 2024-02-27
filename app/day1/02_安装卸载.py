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

driver.close_app()
time.sleep(3)

# 判断app是否安装
if driver.is_app_installed('io.manong.developerdaily'):
    # 卸载app
    driver.remove_app('io.manong.developerdaily')
else:
    # 安装app
    driver.install_app(r'D:\BaiduNetdiskDownload\python高级\代码\测试视频\5移动测试\2-其他资料\toutiao.apk')

driver.quit()

