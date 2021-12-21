# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年12月16日
"""
# UA伪装（反反爬策略）
'''
UA:User-Agent（请求载体的身份标识）
UA检测：门户网站的服务器会坚持对应请求的载体身份标识，如果是某一款浏览器
则说明是一个正常的请求，但是，如果检测到请求的载体身份标识不是基于某一款浏览器的
则表示该请求为不正常的请求（爬虫），则服务器端很有可能拒绝该次请求
'''
# UA伪装
'''
让爬虫对应的请求载体身份标识伪装成某一款浏览器
'''
import requests

if __name__ == '__main__':
    # UA伪装：将对应的Usre-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
    }
    url_example = 'https://www.baidu.com/s?wd=pdd'  # 百度搜索引擎的格式，需要wd就是检索的参数
    url = 'https://www.baidu.com/s?'
    # 处理url携带的参数:封装到字典中
    kw = input('输入搜索内容')
    param = {
        'wd': kw
    }
    # 对指定url发起的请求对应的url是携带参数的，并在请求过程中携带了参数,并加入UA伪装
    response = requests.get(url=url, params=param,headers=headers)
    page_text = response.text
    filename = kw + '.html'
    with open('../gotpages/' + filename, 'w', encoding='utf-8') as stream:
        stream.write(page_text)
    print(filename, '保存成功')
