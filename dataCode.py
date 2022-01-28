# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 13:41:09 2022

@author: ANU
"""
import os
import json
import requests
import urllib.request
import ddddocr

def save_pic(file,data,filename):
    with open(file,'wb') as p:
       p.write(data.read())
       print(f"成功保存文件: {filename}")
    with open(file,'rb') as d:
       ocr = ddddocr.DdddOcr()
       res = ocr.classification(d.read())
       print("识别验证码为: {}".format(res))

# def dataCode(file,data):
#     with open(file,'rb') as p:
#         p.write(data.read())
#     print(f"成功保存文件: {file}")
      
if __name__ == '__main__':   
    
    ''' 
    
    爬取验证码 
    识别验证码，将图片上的验证码转换为数据dataCode
    '''
    
    cookies = {
        'acw_tc': '3ccdc16516432491137935169e76af733a9961262dc21826aa816dcf9337c5',
    }
    
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://hzpba.nmpa.gov.cn/gccx/',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    
    
    root  = os.path.join(os.getcwd(),'pic')
    # 定义下载验证码图片的数量
    num = 21
    for i in range(1,num+1):
        
        filename = '第{}张验证码.jpg'.format(i)
        file = os.path.join(root,filename)
        if os.path.isfile(file):
            print('{}文件存在'.format(filename))
            i += 1
            continue
        try:
            response = requests.get('https://hzpba.nmpa.gov.cn/HZPBZCX/PTHZPBA-SERVER/gsxxcx/kaptcha', headers=headers, cookies=cookies)
            dic = json.loads(response.content)
            # pic_url = dic['base64Img']
            conn = urllib.request.urlopen(dic['base64Img'])
        except Exception as e:
            print('Error:',e)

        save_pic(file,conn,filename)
       
        
    
    
    