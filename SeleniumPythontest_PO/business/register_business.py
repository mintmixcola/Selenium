#coding=utf-8
import sys
sys.path.append('D:\\SeleniumPython')
from Mooc.handle.register_handle import RegisterHandle
class RegisterBusiness(object):
    def __init__(self,driver):
        self.regiser_h = RegisterHandle(driver)

    def user_base(self,email,name,password,file_name):
        self.regiser_h.send_user_eamil(email)
        self.regiser_h.send_user_name(name)
        self.regiser_h.send_user_password(password)
        self.regiser_h.send_user_code(file_name) 
        self.regiser_h.click_register_button()
        self.regiser_h.get_register_text()

    def register_function(self,email,username,password,code,assertCode,assertText):
        self.user_base(email,username,password,code)
        if self.regiser_h.get_user_text(assertCode,assertText)==None:
            print("邮箱检验不成功")
            return True
        else:
            return False
    #执行操作
    #判断button按钮是否存在进而判断是否注册成功
    def register_success(self):
        if self.regiser_h.get_register_text()  == None:
            return True
        else:
            return False

    #email错误
    def login_email_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.regiser_h.get_user_text('email_error',"请输入有效的电子邮件地址")==None:
            print("邮箱检验不成功")
            return True
        else:
            return False

    #name错误
    def login_name_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.regiser_h.get_user_text('name_error',"字符长度必须大于等于4，一个中文算两个字符")==None:
            print("用户名检验不成功")
            return True
        else:
            return False

    #password错误
    def login_password_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)  
        if self.regiser_h.get_user_text('password_error',"最少需要输入5个字符")==None:
            print("密码检验不成功")
            return True
        else:
            return False

    #code错误
    def login_code_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.regiser_h.get_user_text('code_error',"验证码错误")==None:
            print("密码检验不成功")
            return True
        else:
            return False
       


