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
        self.driver=webdriver.Chrome() #调试

    #元素定位
    def locator(self,loc):
        return self.driver.find_element(*loc)

    # 输入
    def input(self, loc, value):
        self.locator(loc).clear()
        self.locator(loc).send_keys(value)

    # 点击
    def click(self, loc):
        self.locator(loc).click()

    # 等待
    def wait_ele_presence(self, loc):
        self.wait = WebDriverWait(self.driver, 30)
        self.wait.until(expected_conditions.presence_of_element_located(loc))

    # 获取文本
    def get_text(self, loc):
        return self.locator(loc).text

    #具体操作
    #切换到首页
    def switch_to_index(self):
        self.click((By.XPATH,'//*[@id="home"]/wx-nav-bottom/wx-view/wx-view[1]/wx-view'))
    #切换到购物车
    def switch_to_car(self):
        self.click((By.XPATH,'//*[@id="home"]/wx-nav-bottom/wx-view/wx-view[2]/wx-view'))
    #切换到我的
    def switch_to_my(self):
        self.click((By.XPATH, '//*[@id="home"]/wx-nav-bottom/wx-view/wx-view[3]/wx-view'))