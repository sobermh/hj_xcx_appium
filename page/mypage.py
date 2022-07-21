"""
@author:maohui
@time:2022/7/21 18:17
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

class MyPage(BasePage):
    #元素定位:采样点
    wait_payoffline_loc=(By.XPATH,'//*[@id="personal"]/wx-view/wx-view[2]/wx-van-grid/wx-view/wx-van-grid-item[1]/wx-view/wx-view')
    wait_confirm_loc=(By.XPATH,'//*[@id="personal"]/wx-view/wx-view[2]/wx-van-grid/wx-view/wx-van-grid-item[2]/wx-view/wx-view')
    offlineall_loc=(By.XPATH,'//*[@id="personal"]/wx-view/wx-view[2]/wx-van-grid/wx-view/wx-van-grid-item[3]/wx-view/wx-view')
    order_test_loc=(By.XPATH,'//*[@id="personal"]/wx-view/wx-view[2]/wx-van-grid/wx-view/wx-view')

    #居家
    wait_payonline_loc=(By.XPATH,'//*[@id="personal"]/wx-view/wx-view[3]/wx-van-grid/wx-view/wx-van-grid-item[1]/wx-view/wx-view')
    wait_send_loc=(By.XPATH,'//*[@id="personal"]/wx-view/wx-view[3]/wx-van-grid/wx-view/wx-van-grid-item[2]/wx-view/wx-view')
    wait_revice_loc=(By.XPATH,'//*[@id="personal"]/wx-view/wx-view[3]/wx-van-grid/wx-view/wx-van-grid-item[3]/wx-view/wx-view')
    onlineall_loc=(By.XPATH,'//*[@id="personal"]/wx-view/wx-view[3]/wx-van-grid/wx-view/wx-van-grid-item[4]/wx-view/wx-view')

    coupon_loc=(By.XPATH,'//*[@id="personal"]/wx-view/wx-view[4]/wx-van-cell[1]/wx-view/wx-view[1]/wx-view/wx-view')
    revice_address_loc=(By.XPATH,'//*[@id="personal"]/wx-view/wx-view[4]/wx-van-cell[2]/wx-view')
    kefu_loc=(By.XPATH,'//*[@id="personal"]/wx-view/wx-view[4]/wx-van-cell[3]/wx-view/wx-view[1]/wx-view/wx-view')
    loginout_loc=(By.XPATH,'//*[@id="personal"]/wx-view/wx-view[5]/wx-van-button/wx-button/wx-view')

    #点击采样点待支付
    def click_wait_payoffline(self):
        self.wait_ele_presence(self.wait_payoffline_loc)
        self.click(self.wait_payoffline_loc)

    #点击带核酸
    def click_wait_confirm(self):
        self.wait_ele_presence(self.wait_confirm_loc)
        self.click(self.wait_confirm_loc)

    #点击采样点全部
    def click_offlineall(self):
        self.wait_ele_presence(self.offlineall_loc)
        self.click(self.offlineall_loc)

    #点击预约检测
    def click_order_test(self):
        self.wait_ele_presence(self.order_test_loc)
        self.click(self.order_test_loc)

    #点击居家待支付
    def click_wait_payonline(self):
        self.wait_ele_presence(self.wait_payonline_loc)
        self.click(self.wait_payonline_loc)

    #点击代发货
    def click_wait_send(self):
        self.wait_ele_presence(self.wait_send_loc)
        self.click(self.wait_send_loc)

    #点击待收获
    def click_wait_revice(self):
        self.wait_ele_presence(self.wait_revice_loc)
        self.click(self.wait_revice_loc)

    #点击居家全部
    def click_onlineall_loc(self):
        self.wait_ele_presence(self.onlineall_loc)
        self.click(self.onlineall_loc)

    #点击我的优惠卷
    def click_coupon(self):
        self.wait_ele_presence(self.coupon_loc)
        self.click(self.coupon_loc)

    #点击收货地址
    def click_revice_address(self):
        self.wait_ele_presence(self.revice_address_loc)
        self.click(self.revice_address_loc)

    #点击联系客服
    def click_kefu(self):
        self.wait_ele_presence(self.kefu_loc)
        self.click(self.kefu_loc)

    #点击退出登录
    def click_loginout(self):
        self.wait_ele_presence(self.loginout_loc)
        self.click(self.loginout_loc)