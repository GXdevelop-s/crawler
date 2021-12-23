# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年12月20日
"""
import json
import requests

if __name__ == '__main__':
    # url
    url = 'https://movie.douban.com/j/chart/top_list?'
    # UA伪装
    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
    }
    # 参数传递
    params = {
        'type': '24',
        'interval_id': '40:30',
        'start': '0',  # 从第几部电影开始取
        'limit': '20'  # 一次取出取出的个数
    }
    # 请求
    response = requests.get(url=url, headers=header, params=params)
    list_r = response.json()
    list_rr = []
    for item in list_r:
        list_rr.append(item.get('regions'))
    # 持久化存储
    with open('../gotpages/doubancom.json', 'w', encoding='utf-8') as stream:
        json.dump(list_rr, stream, ensure_ascii=False)
    print('done!')
