"""
@author:maohui
@time:2022/7/21 18:11
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


from selenium.webdriver.common.by import By

from base.basepage import BasePage

class CarPage(BasePage):
    #元素定位
    all_select_loc=(By.XPATH,'//*[@id="shoppingCart"]/wx-view/wx-view/wx-van-checkbox/wx-view/wx-view[2]')
    delete_loc=(By.XPATH,'//*[@id="shoppingCart"]/wx-view/wx-view/wx-view[2]/wx-van-button[1]/wx-button/wx-view')
    count_loc=(By.XPATH,'//*[@id="shoppingCart"]/wx-view/wx-view/wx-view[2]/wx-van-button[2]/wx-button/wx-view')

    #全选操作
    def all_select(self):
        self.wait_ele_presence(self.all_select_loc)
        self.click(self.all_select_loc)

    #删除操作
    def delete(self):
        self.wait_ele_presence(self.delete_loc)
        self.click(self.delete_loc)

    #结算操作
    def count(self):
        self.wait_ele_presence(self.count_loc)
        self.click(self.count_loc)