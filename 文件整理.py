#coding=utf-8
import os
import shutil
'''
1.输入路径
2.找到路径下面所有的文件
3.创建整理后的文件夹
4.分类文件，按照后缀来分类并建立文件夹
5.移动文件
'''

def Clean(path,dirname):
    #获取所有文件
    names = os.listdir(path)
    path_list = [os.path.join(path,name) for name in names]
    #整理后文件
    clean_path = os.path.join(path,dirname)
    #判断文件是否存在，如果不存在，就创建
    if not os.path.exists(clean_path):
        os.makedirs(clean_path)
    for paths in path_list:
        #过滤文件夹
        if not os.path.isfile(paths):
            continue
        #后缀.doc
        postfix = os.path.splitext(paths)[1]
        #除点doc
        postfix = postfix[1:]
        #建立以后缀为名称的文件夹
        postfix_path = os.path.join(clean_path,postfix)
        if not os.path.exists(postfix_path):
            os.makedirs(postfix_path)
        #拷贝文件
        name = os.path.split(paths)[1]
        target_name = os.path.join(postfix_path,name)
        try:
            shutil.move(paths,target_name)
        except:
            pass
if __name__=='__main__':

    path = input("please input your directory path:")
    path = r'\\'.join(path.split("\\"))
    name = input("make youself directory path:")
    Clean(path,name)
