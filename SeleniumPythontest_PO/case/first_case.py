#conding=utf-8
import sys
sys.path.append('D:\\SeleniumPython\\Mooc')
from log.user_log import UserLog
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
from util.HTMLTestRunner_PY3 import HTMLTestRunner
import os
import time
class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        #cls.log = UserLog()
        #日志文件的使用
        #cls.logger = cls.log.get_log()
        cls.file_name = "D:/python code/Image/test001.png"

    def setUp(self,cls):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.5itest.cn/register")
        cls.logger.info("this is Firefox")
        self.login = RegisterBusiness(self.driver)
        

    def tearDown(self):
        time.sleep(2)
        '''
            python2.0
                if sys.exc_info()[0] 
                    self.driver.save_screenshot()
                会捕获当前程序是否异常,是则执行if语句内操作
            python3.0
                if sys.exc_info()[0]:
                    self._outcome.errors

        '''
        for method_name,error in self._outcom.errors:
            if error:
                case_name = self._testMethodName
                #拿到当前case的名字
                file_path = os.path.join(os.getcwd()+"\\Mooc"+"\\report\\"+case_name+".png")
                self.driver.save_screenshot(file_path)
        #self.driver.save_screenshot()
        #截图
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    #邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
    #case1:email错误
    def test_login_email_error(self,cls):
        email_error = self.login.login_email_error('34','user111','111111',cls.file_name)
        self.assertFalse(email_error,"case执行了")
        #通过assert判断是否为False，如果不是False，则返回预先定义好的msg和is not false
        
        '''
        if email_error == True:
            print("注册成功了，此条case执行失败")
        '''
     

    #case2:username错误
    def test_login_username_error(self,cls):
        username_error = self.login.login_name_error('2292442905@qq.com','@user111','111111',cls.file_name)
        self.assertFalse(username_error)
        '''
        if username_error == True:
            print("注册成功了，此条case执行失败")
        '''

    #case3:password错误
    def test_login_password_error(self,cls):
        password_error = self.login.login_password_error('2292442905@qq.com','user111','1111',cls.file_name)
        self.assertFalse(password_error)

        '''
        if password_error == True:
            print("注册成功了，此条case执行失败")
        '''

    #case4:code错误
    def test_login_code_error(self,cls):
        code_error = self.login.login_code_error('2292442905@qq.com','user111','111111',cls.file_name)
        self.assertFalse(code_error)

        '''
        if code_error == True:
            print("注册成功了，此条case执行失败")
        '''

    #case5:全部正确
    def test_login_success(self,cls):
        success = self.login.user_base('2292442905@qq.com','user111','111111',cls.file_name)
        self.assertFalse(success)

        '''
        if self.login.register_success() == True:
            print("注册成功")  
        '''

'''
def main():
    first = FirstCase()
    first.test_login_email_error
    first.test_login_username_error
    first.test_login_password_error
    first.test_login_code_error
    first.test_login_success
'''
#'''是多行注释

if __name__ == '__main__':
    #unittest.mian()
    file_path = os.path.join(os.getcwd()+"\\Mooc"+"\\report\\"+"first_case.html")
    f = open(file_path,'wb')
    #获取字符串并拼接形成路径名，打开
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_email_error'))
    suite.addTest(FirstCase('test_login_username_error'))
    suite.addTest(FirstCase('test_login_password_error'))
    suite.addTest(FirstCase('test_login_code_error'))
    suite.addTest(FirstCase('test_login_success'))
    #unittest.TextTestRunner.run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is first report",description=u"这个是我们第一次测试报告")
    runner.run(suite)