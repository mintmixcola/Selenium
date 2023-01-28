#coding=utf-8
#BDD Behavior-driven development 行为驱动开发
#pip install Behave pip install Pyhamcrest
Feature:Register User

    As a developer
    This is my first bdd project#描述
    Sceenario: open register website#Sceenario 场景
        When I open the register website "http://www.5itest.cn/register"
        Then I expect that the title is "注册"

    Sceenario: input username
        When I set with useremail "2292442905@qq.com"
        And I set with username "user111"
        And I set with password "111111"
        And I set with code "tets"
        And I click with registerbutton
        Then I expect that text "验证码错误"
