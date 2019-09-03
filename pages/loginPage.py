"""
------------------------------------
@Time : 2019/7/13 19:55
@Auth : linux超
@File : loginPage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from pages.base.base import Base
from common.parse_config import ParseConfig
from config.config import LOCATOR_PATH
from appium import webdriver
import time
class LoginPage(Base):

    locator = ParseConfig(LOCATOR_PATH)
    # username_input = locator('LoginPage', 'username_input')  # 用户名输入框 实际：username_input = ('id', 'user_login')
    password_input = locator('LoginPage', 'password_input')  # 密码输入框
    login_button = locator('LoginPage', 'login_button')  # 登录按钮
    midbutton = locator('LoginPage', 'midbutton')  # 登出按钮
    switchpassword = locator('LoginPage', 'switchpassword')
    settingbutton = locator('LoginPage', 'settingbutton')

    def login(self, phone: str, password: str):
        self.logger.info(f"开始登录")
        self.click_midbutton()
        self.click_switchpassword()
        self.input_user(phone)
        self.input_password(password)
        self.click_login()

    def click_midbutton(self):
        self.click(*self.midbutton)

    def click_switchpassword(self):
        self.click(*self.switchpassword)

    def input_user(self, phone: str):
        self.logger.info("输入用户名:{}".format(phone))
        self.find_element_by_android_uiautomator('resourceId','io.manong.developerdaily:id/edt_phone').send_keys(phone)

    def input_password(self, password: str):
        self.logger.info("输入密码:{}".format(password))
        self.send_keys(*self.password_input, value=password)

    def click_login(self):
        self.logger.info("点击登录按钮")
        self.click(*self.login_button)

    def logout(self):
        self.logger.info("点击我的按钮")
        self.find_element_by_android_uiautomator('text', '我的').click()
        time.sleep(4)
        target = self.find_element_by_android_uiautomator('text', '礼物兑换')
        targetx = target.location['x']
        targety = target.location['y']
        self.driver.swipe(targetx, targety, targetx, targety - 800, 500)
        self.find_element_by_android_uiautomator('text','设置').click()
        self.find_element_by_android_uiautomator('text','退出当前账户').click()
        self.find_element_by_android_uiautomator('text','退出').click()

    def get_contents(self):
        eles = self.get_contents()
        self.logger.info(f"上下文是：{eles}")
        return eles

    def get_currentcontent(self):
        ele = self.get_currentcontent()
        self.logger.info(f"当前的上下文是：{ele}")
        return ele







if __name__ == '__main__':
    pass
