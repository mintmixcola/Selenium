#coding=utf-8
import logging
import os
import datetime

class UserLog(object):
    def __init__(self):      
        self.logger = logging.getLogger()#得到一个对象
        self.logger.setLevel(logging.DEBUG)#设置一个等级

        #文件名字
        base_dir = os.path.dirname(os.path.abspath(__file__))#abspath获取当前文件路径。dirname获取目录路径，不包含文件名
        log_dir = os.path.join(base_dir,"logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log"#获取当前时间，并要求格式为年月日 拼接
        log_name = log_dir+"/"+log_file

        #文件输出日志
        self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')#("D:\\SeleniumPython\\Mooc\\log\\logs\\test.log")
        self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(levelno)s :%(levelname)s---> %(message)s ')
        self.file_handle.setFormatter(formatter)#file_handle设置格式，格式为formatter格式
        self.logger.addHandler(self.file_handle)
        '''
        consle = logging.StreamHandler()#得到一个流对象
        logger.addHandler(consle)
        logger.debug("teste")#将这个流对象添加进一个 ，使其能在控制台输出
        consle.close()
        logger.removeHandler(consle)#两个对象都记得清空！！！
        '''
        #self.logger.debug("teste")


    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()