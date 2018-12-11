import os
import time

'''
1.注意类型转换，input输入后是字符类型，要转换成整型
2.if elif  elif
int函数能够
（1）把符合数学格式的数字型字符串转换成整数
（2）把浮点数转换成整数，但是只是简单的取整，而非四舍五入。
'''

def Shutdowm(times):
    print(u"%d s后换机"%times)
    time.sleep(times)
    os.system("shutdown -s -t 0")

def Reboot(times):
    print(u"%d s后重启" % times)
    os.system("shutdown -r -t 0")

def ShutdownNow():
    print(u"正在关机")
    os.system("shutdown -r -t 0")
if __name__=='__main__':
    print(u"请选择：\n1.重启\n2.关机\n3.定时关机")
    select = input(u"请输入数字：")
    select = int(select)
    if select == 1:
        ti = input(u"重启：请输入重启时间（s）:")
        ti = int(ti)
        Reboot(ti)
    elif select == 2:
        ShutdownNow()
    elif select == 3:
        ti = input(u"定时关机：请输入定时关机时间（s）:")
        ti = int(ti)
        Shutdowm(ti)