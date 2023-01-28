#coding=utf-8
#要运行BDD类的文件需进入cmd中，进入SeleniumPythonBDD目录下，输入behave即可运行
#2.0就已经是操作层了

from behave import *
from features.lib.pages.register_page import RegisterPage

use_step_matcher('re')


@when('I open the register website "([^"]*)"')
def step_register(context,url):
    RegisterPage(context).get_url(url)
    #context.driver.get(url)

@then('I expect that the title is "([^"]*)"')
def step_register1(context,title_name):
    title = RegisterPage(context).get_title(title_name)
    #title = context.driver.title
    assert title_name in title

@when('I set with useremail "([^"]*)"')
def step_register(context,useremail):
    RegisterPage(context).send_useremail(useremail)
    #context.driver.find_element_by_id("register_email").send_keys(useremail)

@when('I set with username "([^"]*)"')
def step_register(context,username):
    RegisterPage(context).send_username(username)
    #context.driver.find_element_by_id("register_nickname").send_keys(username)

@when('I set with password "([^"]*)"')
def step_register(context,password):
    RegisterPage(context).send_password(password)
    #context.driver.find_element_by_id("register_password").send_keys(password)

@when('I set with code "([^"]*)"')
def step_register(context,code):
    RegisterPage(context).send_code(code)
    #context.driver.find_element_by_id("captcha_code").send_keys(code)

@when('I clcik with registerbutton')
def step_register(context):
    RegisterPage(context).click_register_button
    #context.driver.find_element_by_id("register-btn").click()

@then('I expect that text "([^"]*)"')
def step_register(context,code_text):
    text= RegisterPage(context).get_code_text
    #text = context.driver.find_element_by_id("captcha_code-error").text
    assert code_text in text