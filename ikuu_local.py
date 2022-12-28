#此脚本为ikuu机场签到脚本如果你没有注册请到这个链接注册https://ikuuu.one/auth/register?code=c2zw
import requests
import re
import json
import time
import os
import sys
a=input("enter email")
ab=input("enter password")
# def fuck():
#     if os.environ.get("ikid"):
#         dr = os.environ["ikid"]
#         print("已获取用户名"+" "+dr)
#         return dr
#     else:
#         print("获取账号失败，请export ikid='你的账号'")
# a=fuck()       
# def shit():
#     if os.environ.get("ikpw"):
#         ikpw = os.environ["ikpw"]
#         pw1w = len(ikpw)
#         l = list(ikpw)
#         s=pw1w-1
#         sw=l[0]+"****"+l[s]
#         print("已获取密码"+" "+sw)
#         return ikpw
#     else:
#         print("获取密码失败，请export ikpw='你的密码'")     
# ab=shit()
session = requests.session()
p = {
  "email": a,
  "passwd": ab
}
b = "https://ikuuu.ltd/auth/login"
session.post(b,data=p)
resp = session.post('https://ikuuu.ltd/user/checkin')
page_content = resp.content.decode('unicode_escape')
obj = re.compile(r'"msg":"(?P<name>.*?)"', re.S)
result = obj.finditer(page_content)
a=[]
for it in result:
 print(it.group("name"))
 a.append(it.group("name"))
if a == [] :
    print("账号或密码错误，请检查")
#6

