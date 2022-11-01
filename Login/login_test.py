import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Version1.settings') #导入django环境，方便测试
import django
from django.shortcuts import render
django.setup()

from django.db.models.aggregates import Count



def login_try(name,password):
    if name == 'lsy'and password == '123':
        print('登录成功！')
        return '登录成功！'
    elif name == ''and password == '':
        print('请输入用户名和密码：')
        return '请输入用户名和密码：'
    else:
        print('用户名或密码错误！')
        return '用户名或密码错误!'

if __name__ == '__main__':
    login_try('','')



