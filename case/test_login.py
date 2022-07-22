"""
@author:maohui
@time:2022/7/22 8:57
  　　　　　　　 ┏┓    ┏┓+ +
  　　　　　　　┏┛┻━━━━┛┻┓ + +
  　　　　　　　┃        ┃ 　 
  　　　　　　　┃     ━  ┃ ++ + + +
  　　　　　 　████━████ ┃+
  　　　　　　　┃        ┃ +
  　　　　　　　┃   ┻    ┃
  　　　　　　　┃        ┃ + +
  　　　　　　　┗━┓   ┏━━┛
  　　　　　　　  ┃   ┃
  　　　　　　　  ┃   ┃ + + + +
  　　　　　　　  ┃   ┃　　　Code is far away from bug with the animal protecting
  　　　　　　　  ┃   ┃+ 　　　　神兽保佑,代码无bug
  　　　　　　　  ┃   ┃
  　　　　　　　  ┃   ┃　　+
  　　　　　　　  ┃   ┗━━━━━━━┓ + +     
  　　　　　　　  ┃           ┣┓
  　　　　　　　  ┃           ┏┛
  　　　　　　　  ┗┓┓┏━━━━━┳┓┏┛ + + + +
  　　　　　　　   ┃┫┫     ┃┫┫
  　　　　　　　   ┗┻┛     ┗┻┛+ + + +
"""
import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

from base.basepage import BasePage
from page.mypage import MyPage
class TestLogin():
    @classmethod
    def setup_class(cls):
        """初始化打开微信界面"""
        desired_caps = {}  # 包装
        desired_caps['platformName'] = 'Android'  # 系统名称
        desired_caps['platformVersion'] = '7'  # 系统的版本号
        desired_caps['deviceName'] = 'Redmi_7A'  # 设备名称,这个没有严格的规定,但是一定要有
        desired_caps['appPackage'] = 'com.tencent.mm'  # APP包名
        desired_caps['appActivity'] = '.ui.LauncherUI'  # APP入口的activity
        desired_caps['noReset'] = True  # 不重置app的缓存文件
        # desired_caps['fullReset'] = False  # 不重置app的缓存文件
        desired_caps['unicodeKeyboard'] = True  # 设置键盘支持中文输入
        desired_caps['resetKeyboard'] = True  # 重置键盘
        desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:appbrand0'}

        # 连接appium server，告诉appium，代码要操作哪个设备上的哪个APP
        # 启动手机上App
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        #进入小程序
        hjkj_loc = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("微信团队")')  # 汇健科技
        xcx_loc=(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("杭州")')
        BasePage(cls.driver).wait_ele_presence(hjkj_loc)
        BasePage(cls.driver).swipe_down_weixin()
        BasePage(cls.driver).click(xcx_loc)
        time.sleep(5)
        # print(cls.driver.contexts)
        # print(cls.driver.current_url)
        # cls.driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
        # cls.driver.switch_to.window(cls.driver.window_handles[-1])
    @classmethod
    def teardown_class(cls):
        """关闭微信界面"""
        cls.driver.quit()

    def test_02(self):
        """授权登录功能"""
        BasePage(self.driver).switch_to_my()
        print(self.driver.current_url)
        # BasePage(self.driver).switch_window()
        # BasePage(self.driver).swipe_down(1)
        time.sleep(5)
        print(self.driver.current_url)
        print(self.driver.window_handles)
        MyPage(self.driver).click_loginout()
        BasePage(self.driver).click((By.XPATH,'//*[@id="personal"]/wx-van-popup/wx-view/wx-view/wx-view[3]/wx-button[2]'))
        BasePage(self.driver).click((By.XPATH,'/html/body/wx-view/wx-view[3]/wx-view/wx-button'))
        BasePage(self.driver).click((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("允许")'))
        BasePage(self.driver).switch_to_my()
        actual_text=BasePage(self.driver).get_text((By.XPATH,'//*[@id="personal"]/wx-view/wx-view[1]/wx-view/wx-view/wx-view'))
        assert "毛万森"==actual_text
if __name__ == '__main__':
    pytest.main(['-vs', "--alluredir", "./report/", "--clean-alluredir"])