# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:24:05 2022

@author: ANU
"""

import pandas as pd
import requests
import os
import json


def make_path(*dirs):
    root = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(root, *dirs)

def req_get(url, headers={}, params={}, cookies={}):
    r = requests.Request('GET', url, headers=headers, params=params, cookies=cookies)
    req = r.prepare()
    
    print('{}\n{}\r\n{}\r\n'.format(
        '-----------START-----------', 
        req.method + ' ' + req.url, 
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items())
        ))
    
    s = requests.Session()
    return s.send(req, timeout=10)

def is_file(file):
    if os.path.isfile(file):
        print('File is already existed: %s' % file)
        return True
    return False

def save_file(data, file):             
    with open(file, 'w') as f:
        f.write(data)
    print(f"保存文件: {file}")
    print(f"文件大小: {round(os.path.getsize(file) / float(1024), 2)} KB")


cookies = {
    'acw_tc': '3ccdc15816431655477906773e5e5909e6f006d12df43a2c61857f24087ee5',
    
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/json;charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://hzpba.nmpa.gov.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://hzpba.nmpa.gov.cn/gccx/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

dict = {
        "on":'true',
        "currentPage":3,
        "pageSize":10,
        "prodName":"",
        "recordNo":"",
        "entName":"南京阿奴生物科技有限公司",
        "gb":"G"
        
        }

# 修改参数




data = json.dumps(dict).encode('utf-8')

response = requests.post('https://hzpba.nmpa.gov.cn/HZPBZCX/PTHZPBA-SERVER/gsxxcx/query', headers=headers, cookies=cookies, data=data)
