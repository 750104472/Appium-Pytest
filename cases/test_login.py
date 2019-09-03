"""
------------------------------------
@Time : 2019/7/13 20:01
@Auth : linux超
@File : test_login.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import pytest

from datas.login_datas import LoginData
from common.record_log import logger
import pdb


class TestLogin(object):
    """登录测试用例"""
    logger = logger
    t_data = LoginData

    @pytest.mark.login
    @pytest.mark.parametrize('user, pwd', t_data.login_success_data)
    def test_login_success(self, ini_pages,get_contents,get_current_contents, user, pwd):
        """登录:登录成功"""
        login_page = ini_pages[1]
        login_page.login(user, pwd)






if __name__ == '__main__':
    pytest.main()
