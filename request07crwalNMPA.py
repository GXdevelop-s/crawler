# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年12月23日
"""
import json

import requests

if __name__ == '__main__':
    # url1
    url1 = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    list_id = []
    list_result = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
    }
    page_nums = int(input('想要获取的页数：'))
    for i in range(page_nums):
        n = i + 1
        paras1 = {
            'on': ' true',
            'page': str(n),
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        response = requests.post(url=url1, headers=head, params=paras1).json()
        # 依据json串获取到了本次页上的id信息
        for dicts in response['list']:
            list_id.append(dicts['ID'])
    # url2 详情页
    url2 = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in list_id:
        paras2 = {
            'id': id
        }
        response2 = requests.post(url=url2, headers=head, params=paras2).json()
        list_result.append(response2)
    # 持久化储存
    with open(r'../gotpages/nmpadatas.json', 'w', encoding='utf-8') as stream:
        json.dump(list_result, stream, ensure_ascii=False)
    # for dicts in list_result:
    #     print(dicts)
    print('over')
