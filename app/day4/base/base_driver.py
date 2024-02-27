from appium import webdriver


def init_driver(appPackage, appActivity):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.2'
    desired_caps['deviceName'] = '127.0.0.1:62001'
    # desired_caps['appPackage'] = 'com.android.contacts'
    # desired_caps['appActivity'] = '.activities.PeopleActivity'
    desired_caps['appPackage'] = appPackage
    desired_caps['appActivity'] = appActivity

    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
