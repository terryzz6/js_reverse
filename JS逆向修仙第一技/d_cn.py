#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   d_cn.py
@Time    :   2022/07/26 09:53:14
@Author  :   terryz 
@Version :   1.0
@Contact :   lvdouzhou0712@qq.com
@Desc    :   
    目标 d.cn
    登录接口 https://oauth.d.cn/auth/goLogin.html

'''


import requests
import execjs
import os
cur_dir  = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(cur_dir,'encrypt.js'), encoding='utf-8',mode='r') as f:
         js = f.read()


headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://oauth.d.cn/auth/goLogin.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

enc_pwd =execjs.compile(js).call('rsa','123456')

print('[*] ',enc_pwd);
params = (
    ('display', 'web'),
    ('name', 'lvdouzhou0712@qq.com'),
    ('pwd', str(enc_pwd)),
    ('to', 'https://www.d.cn/'),
)

response = requests.get('https://oauth.d.cn/auth/login', headers=headers, params=params)
print('[*] ',response.json());




