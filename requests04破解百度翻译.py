# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年12月16日
"""
# ajax
import json

'''
ajax:在网页源码XHR中，有ajax的包，ajax就是实现动态交互的手段
在百度翻译输入英语时，每输入一个字母，ajax都会有sug包（post请求带有参数），因为每输入一个字符ajax都会处理
最后一个sug包就是带有完整的单词参数的包
响应数据是一组json数据
'''
import requests

if __name__ == '__main__':
    url = 'https://fanyi.baidu.com/sug'
    #  UA伪装
    header = {
        'User - Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
    }
    # 参数传递
    word = input('翻译：')
    params = {
        'kw': word
    }
    # 发送请求
    response = requests.post(url=url, params=params, headers=header)  # 用哪个request方法是由抓包工具general中Request Method决定的
    # 获取响应数据----可以在content-type获取响应数据类型
    dic_obj = response.json()  # json方法返回的是obj，这个是个字典对象
    # 持久化存储
    with open(r'../gotpages/translation.json', 'w', encoding='utf-8') as stream:
        json.dump(dic_obj, fp=stream, ensure_ascii=True)  # 中文不可以用ascii码编码
    print('over')
