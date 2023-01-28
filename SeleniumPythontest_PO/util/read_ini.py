#conding=utf-8
import configparser
#类，封装
class ReadIni(object):
    #构造函数
    #传参self（自己）,file_name（文件名）,node（配置文件开头的东西）,并且file_name允许不输入为空，这种情况下默认赋值。。。否则调用load_ini方法加载文件得到需要的元
    #素对象；node也可不输入，为空，默认为。。。否则把node赋值给self.node这样就可以全局调用
    def __init__(self,file_name=None,node=None):
        if file_name == None:
            file_name = "D:\SeleniumPython\Mooc\config\LocalElement.ini"
        if node == None:
            self.node = "RegisterElement"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)
   
   #加载文件
   #传参self,file_name,初始化configparser对象赋值给cf，调用方法read获取到需要的那元素对象
    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf
    
    #获取value的值
    #传参self,key，通过构造函数调用load_ini方法得到cf对象,再进一步通过cf.get得到value
    # 值赋值给data，最后返回参数data
    def get_value(self,key):
       data = self.cf.get(self.node,key)
       return data

if __name__ =='__main__':
    read_init = ReadIni()
    #初始化ReadIni类，后面才能使用
    print(read_init.get_value('user_name'))
    #调用read_init文件下的get_value方法并将结果打印


    

#cf = configparser.ConfigParser()
#cf.read(r"D:\SeleniumPython\Mooc\config\LocalElement.ini")
#print(cf.get('RegisterElement','user_email'))
#configparser需要pip install Configparser