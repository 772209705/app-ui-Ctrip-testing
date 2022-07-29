from TestCases import test_ctrip
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# 出发时间
setOut = '//*[@text="7月29日今天"]'
# 回来时间
comeBack = '//*[@text="7月31日后天"]'

class TestCtrip:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 明确是安卓系统还是IOS系统
        desired_caps['platformVersion'] = '7.1.2'  # 系统对应的版本号
        desired_caps['deviceName'] = 'Android Emulator'  # 连接的手机设备名称，通过adb devices 查看
        desired_caps['appPackage'] = 'ctrip.android.view'  # 包名
        desired_caps[
            'appActivity'] = 'ctrip.business.splash.CtripSplashActivity'  # APP首页 ctrip.business.planthome.CtripPlantHomeActivity
        desired_caps['resetKeyboard'] = True  # 将数字键盘给隐藏起来
        desired_caps['noReset'] = True  # 不重置APP
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def teardown(self):
        self.driver.quit()

    def test_01_Select_city(self):
        '''
            选择城市
        '''
        # 显示等待
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="机票"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="机票"]').click()
        # 选择城市 出发地
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[1]')))
        self.driver.find_element(MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[1]')\
            .click()
        # 断言 是否拉起出发地弹框
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="选择出发地"]')))
        assert '选择出发地' == self.driver.find_element(MobileBy.XPATH, '//*[@text="选择出发地"]').text
        self.driver.back()
        # 选择城市 目的地
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[2]')))
        self.driver.find_element(MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[2]').click()
        # 断言 是否拉起目的地弹框
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="选择目的地"]')))
        assert '选择目的地' == self.driver.find_element(MobileBy.XPATH, '//*[@text="选择目的地"]').text
        self.driver.back()

    def test_02_Select_time(self):
        '''
            选择日期
        '''
        # 显示等待
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="机票"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="机票"]').click()

        # 选择时间
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, setOut )))
        self.driver.find_element(MobileBy.XPATH,'//*[@text="单程"]').click()
        self.driver.find_element(MobileBy.XPATH,setOut).click()
        # 断言 //*[@text="选择出发日期"]
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="选择出发日期"]')))
        assert '选择出发日期' == self.driver.find_element(MobileBy.XPATH, '//*[@text="选择出发日期"]').text

    def test_03_Ticket_inquiry(self):
        '''
            查询机票
        '''
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="机票"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="机票"]').click()
        # 点击 出发地
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[1]')))
        self.driver.find_element(MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[1]').click()
        # 选择 出发城市
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="广州"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="广州"]').click()
        # 点击 目的地
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[2]')))
        self.driver.find_element(MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[2]').click()
        # 选择 目的地城市
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="杭州"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="杭州"]').click()
        # 查询机票
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="查 询"]')))
        self.driver.find_element(MobileBy.XPATH,'//*[@text="查 询"]').click()
        # 断言 是否跳转到查询结果页
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="广州"]')))
        assert '广州' == self.driver.find_element(MobileBy.XPATH, '//*[@text="广州"]').text
        assert '杭州' == self.driver.find_element(MobileBy.XPATH, '//*[@text="杭州"]').text

    def test_04_change_button(self):
        '''
            调换城市
        :return:
        '''
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="机票"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="机票"]').click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="单程"]')))
        self.driver.find_element(MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[2]')\
            .click()
        # 断言

    def test_05_retun_Select_city(self):
        '''
        往返模块 选择城市
        :return:
        '''
        # 显示等待
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="机票"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="机票"]').click()

        # 选择 往返
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="往返"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="往返"]').click()

        # 选择城市 出发地
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[1]')))
        self.driver.find_element(MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[1]').click()
        # 断言 是否拉起出发地弹框
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="选择出发地"]')))
        assert '选择出发地' == self.driver.find_element(MobileBy.XPATH, '//*[@text="选择出发地"]').text
        self.driver.back()

        # 选择城市 目的地
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[2]')))
        self.driver.find_element(MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[2]').click()
        # 断言 是否拉起 目的地弹框
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="选择目的地"]')))
        assert '选择目的地' == self.driver.find_element(MobileBy.XPATH, '//*[@text="选择目的地"]').text
        self.driver.back()

    def test_06_retun_Select_time(self):
        '''
         往返模块 选择日期
        :return:
        '''
        # 显示等待
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="机票"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="机票"]').click()
        # 选择 往返
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="往返"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="往返"]').click()
        # 选择开始时间
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, setOut)))
        self.driver.find_element(MobileBy.XPATH, setOut).click()
        # 断言 是否拉起 日历弹框
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="选择往返日期"]')))
        assert '选择往返日期' == self.driver.find_element(MobileBy.XPATH, '//*[@text="选择往返日期"]').text
        self.driver.back()
        # 选择回来时间
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, comeBack)))
        self.driver.find_element(MobileBy.XPATH, comeBack).click()
        # 断言 是否拉起 日历弹框
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="选择往返日期"]')))
        assert '选择往返日期' == self.driver.find_element(MobileBy.XPATH, '//*[@text="选择往返日期"]').text
        self.driver.back()

    def test_07_retun_Ticket_inquiry(self):
        '''
         往返模块 查询机票
        :return:
        '''
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="机票"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="机票"]').click()
        # 选择 往返
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="往返"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="往返"]').click()
        # 点击 出发地
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[1]')))
        self.driver.find_element(MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[1]').click()
        # 选择 出发城市
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="广州"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="广州"]').click()
        # 点击 目的地
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[2]')))
        self.driver.find_element(MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[2]').click()
        # 选择 目的地城市
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="杭州"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="杭州"]').click()
        # 查询机票
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="查 询"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="查 询"]').click()
        # 断言 是否跳转到查询结果页
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="广州"]')))
        assert '广州' == self.driver.find_element(MobileBy.XPATH, '//*[@text="广州"]').text
        assert '杭州' == self.driver.find_element(MobileBy.XPATH, '//*[@text="杭州"]').text

    def test_08_retun_change_button(self):
        '''
         往返模块 调换城市
        :return:
        '''
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="机票"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="机票"]').click()
        # 选择 往返
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="往返"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="往返"]').click()

        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="单程"]')))
        self.driver.find_element(MobileBy.XPATH,
                                 '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[2]') \
            .click()

    def test_09_OneWay_retun_switch(self):
        '''
        单程/往返 切换
        :return:
        '''
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="机票"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="机票"]').click()
        # 选择 往返
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="往返"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="往返"]').click()

        # 断言 是否出现往返选项卡才出现的 往返日期 comeBack
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, comeBack)))
        assert '7月31日后天' == self.driver.find_element(MobileBy.XPATH, comeBack).text
        # 选择 单程
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="单程"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="单程"]').click()

    def test_10_Tick_button(self):
        '''
        勾选所有按钮
        :return:
        '''
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="机票"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="机票"]').click()
        # 勾选所有按钮
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@text="往返"]')))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="往返"]').click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]')))
        self.driver.find_element(MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]')\
            .click()
        self.driver.find_element(MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.ImageView[1]')\
            .click()
        self.driver.find_element(MobileBy.XPATH, '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]')\
            .click()

