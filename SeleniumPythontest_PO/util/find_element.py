#conding=utf-8
from os import read
from util.read_ini import ReadIni
#元素定位方法的封装
class FindElement(object):
    #构造函数，使driver在该类下的全局都能调用
    def __init__(self,driver):
        self.driver = driver

    #具体的元素定位方法
    ##实例化ReadIni对象，调用其get——value方法，再将结果根据>号拆分，>左边的是元素类型，>右边的是元素名称，通过if语句分别对应各自定位方法。并加入
    ##了容错处理，如果出错则返回一个空值。
    def get_element(self,key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element_by_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            self.driver.save_screenshot('D:/Python code/Image/%s.png' %value)
            #注意格式
            return None
        
    
