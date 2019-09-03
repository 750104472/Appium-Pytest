"""
------------------------------------
@Time : 2019/7/23 20:22
@Auth : linux超
@File : conftest.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import pytest
from datetime import datetime
from pages.loginPage import LoginPage
from pages.modelplatesPage import ModelplatesPage
from appium import webdriver
from py._xmlgen import html
from common.record_log import logger
from config.app_config import desired_caps

_driver = None

@pytest.fixture(scope='session')
def driver():
    global _driver
    logger.info('------------open APP------------')
    _driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    yield _driver
    logger.info('------------close APP------------')
    _driver.quit()

@pytest.fixture
def get_contents(driver):
    contents = driver.contexts
    logger.info(f'------------{contents}------------')
    yield contents

@pytest.fixture
def get_current_contents(driver):
    current_content = driver.current_context
    logger.info(f'------------{current_content}------------')
    yield current_content

@pytest.fixture(scope='class')
def ini_pages(driver):
    login_page = LoginPage(driver)
    yield driver, login_page
    driver.reset()



#
# # 测试失败时添加截图和测试用例描述(用例的注释信息)
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     当测试失败的时候，自动截图，展示到html报告中
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_")+".png"
#             screen_img = _capture_screenshot()
#             if file_name:
#                 html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % screen_img
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#         report.description = str(item.function.__doc__)
#         report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")
#
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.insert(1, html.th('Description'))
#     cells.insert(2, html.th('Test_nodeid'))
#     cells.insert(3, html.th('Time', class_='sortable time', col='time'))
#     cells.pop(2)
#
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(1, html.td(report.description))
#     cells.insert(2, html.td(report.nodeid))
#     cells.insert(3, html.td(datetime.utcnow(), class_='col-time'))
#     cells.pop(2)


def _capture_screenshot():
    """
    截图保存为base64
    :return:
    """
    return _driver.get_screenshot_as_base64()






