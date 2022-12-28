#此脚本为渡口机场签到脚本如果你没有注册请到这个链接注册https://dukou.dev/user/register?code=rRNI
#-------------------------------------------
#打开chrome，按f12打开开发者工具，选择”网络“（Network）模块
#然后点击签到按钮，下方会抓取到名为”checkin“的响应
#在”标头“页面往下翻到请求标头，复制自己的”access-token“以及”cookie“
#填入下方：
accesstoken = '填写你的access-token'
cookie = '_ga=xxxxxxxxxx; _gid=xxxxxxxxx'
#-------------------------------------------




import requests
import re
import json
import time
import os
import sys
from bs4 import BeautifulSoup
import html
import json


url = 'https://dukou.dev/api/user/checkin'
headers = {
    'authority': 'dukou.dev',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'access-token': accesstoken,
    'cookie': cookie,
    'referer': 'https://dukou.dev/user/index',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
response_dict = json.loads(response.text)

result = response_dict['result']
print(result)
