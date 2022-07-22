"""
@author:maohui
@time:2022/7/21 15:38
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

#定义一个类描述每个页面都有的属性和方法

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver #调试
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage():

    def __init__(self,driver):
        self.driver=driver
        # self.driver=webdriver.Chrome() #调试

    #元素定位
    def locator(self,loc):
        return self.driver.find_element(*loc)

    # 输入
    def input(self, loc, value):
        self.wait_ele_presence(loc)
        self.locator(loc).clear()
        self.locator(loc).send_keys(value)

    # 点击
    def click(self, loc):
        self.wait_ele_presence(loc)
        self.locator(loc).click()

    #js点击
    def js_click(self,loc):
        self.driver.execute_script("arguments[0].click();",loc)
    # 等待
    def wait_ele_presence(self, loc):
        self.wait = WebDriverWait(self.driver, 30)
        self.wait.until(expected_conditions.presence_of_element_located(loc))

    # 获取文本
    def get_text(self, loc):
        self.wait_ele_presence(loc)
        return self.locator(loc).text

    # 获取机器屏幕大小x,y
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 屏幕向下滑动
    def swipe_down(self, t):
        """
        滑动时X轴不变，Y轴由小到大,t是滑动消耗的时间
        """
        screensize = self.get_size()
        x1 = int(screensize[0] * 0.5)  # x坐标
        y1 = int(screensize[1] * 0.25)  # 起始y坐标
        y2 = int(screensize[1] * 0.75)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # #切换所在窗口
    # def switch_window(self):
    #     expect_window_url=self.driver.current_url
    #     for handle in self.driver.window_handles:
    #         self.driver.switch_to.window(handle)
    #         if expect_window_url==self.driver.current_url:
    #             break


    #具体操作
    #下拉微信index页为找到小程序
    def swipe_down_weixin(self):
        self.swipe_down(1)

    #切换到首页
    def switch_to_index(self):
        self.click((By.XPATH,'//*[@id="home"]/wx-nav-bottom/wx-view/wx-view[1]/wx-view'))
    #切换到购物车
    def switch_to_car(self):
        self.click((By.XPATH,'//*[@id="home"]/wx-nav-bottom/wx-view/wx-view[2]/wx-view'))
    #切换到我的
    def switch_to_my(self):
        self.click((By.XPATH, '//*[@id="home"]/nav-bottom//view/view[3]'))