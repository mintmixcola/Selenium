#coding=utf-8
import sys
sys.path.append('D:\\SeleniumPython\\Mooc')
from page.register_page import RegisterPage
from util.get_code import Getcode
class RegisterHandle(object):
    def __init__(self,driver):
        self.driver = driver
        self.register_p = RegisterPage(self.driver)

    #输入邮箱
    def send_user_eamil(self,email):
        self.register_p.get_email_element().send_keys(email)

    #输入用户名
    def send_user_name(self,user_name):
        self.register_p.get_username_element().send_keys(user_name)

    #输入密码
    def send_user_password(self,password):
        self.register_p.get_passsword_element().send_keys(password)

    #输入验证码
    def send_user_code(self,file_name):
        get_code_text = Getcode(self.driver)
        code = get_code_text.code_online(file_name)
        self.register_p.get_code_element().send_keys(code)
    
    #获取文字信息
    def get_user_text(self,info,user_info):
        try:#first_case版没有user,first_ddt_case版有user
            if  info == 'user_email_error':
                text = self.register_p.get_email_error_element().text
            elif info == 'user_name_error':
                text = self.register_p.get_name_error_element().text
            elif info  == 'password_error':
                text = self.register_p.get_password_error_element().text
            else:
                text = self.register_p.get_code_error_element().text
                #.get_attribute('value')可获取value值
        except:
            text = None
        return text

    #点击注册按钮
    def click_register_button(self,register_button):
        self.register_p.get_button_element().send_keys(register_button)

    #获取注册按钮文字
    def get_register_text(self):
        return self.register_p.get_button_element().text