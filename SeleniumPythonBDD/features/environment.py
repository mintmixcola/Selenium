#coding=utf-8
#该文件主要用于初始化环境
from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Firefox()

def after_all(context):
    context.driver.close()#传参一定是context，可以理解为全局变量plus