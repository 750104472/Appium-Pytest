

desired_caps = {
    'platformName' : 'Android',              # 测试平台
    'platformVersion' : '7',                 # 平台版本,不能写错
    'deviceName' : 'test',                   # 设备名称，多设备时需区分
    # desired_caps['app'] : r'e:\apk\wv.apk'  # app package名
    'appPackage' : 'io.manong.developerdaily',  # app package名
    'appActivity' : 'io.toutiao.android.ui.activity.LaunchActivity',         # app默认Activity
    'unicodeKeyboard' : True,                # 一定要有该参数，否则unicode
    'resetKeyboard' : True,                  # 一定要有该参数，否则unicode 输入的中文无效
    'noReset' : True,
    'newCommandTimeout' : 6000
}
