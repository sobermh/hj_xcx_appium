"""
@author:maohui
@time:2022/7/21 15:54
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

class IndexPage(BasePage):
    #元素定位
    search_loc=(By.XPATH,'//*[@id="home"]/wx-view/wx-van-field/wx-van-cell/wx-view/wx-view[2]/wx-view/wx-input/div[1]')
    colonscr_loc=(By.XPATH,'//*[@id="home"]/wx-view/wx-view[2]/wx-image[1]/div')
    lungscr_loc=(By.XPATH,'//*[@id="home"]/wx-view/wx-view[2]/wx-image[2]/div')

    #搜索功能
    def search(self):
        self.wait_ele_presence(self.search_loc)
        self.input(self.search_loc,'lungscr')

    #点击血清肽谱检测
    def click_colonscr(self):
        self.wait_ele_presence(self.colonscr_loc)
        self.click(self.colonscr_loc)

    #点击唾液代谢检测
    def click_lungscr(self):
        self.wait_ele_presence(self.lungscr_loc)
        self.click(self.lungscr_loc)