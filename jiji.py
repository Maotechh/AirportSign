#此脚本为几鸡机场签到脚本如果你没有注册请到这个链接注册https://b.luxury/waf/PgAB7k3DmpXU1bNf2
import requests
import re
import json
import time
import os
import sys
def iIiii1i111i1I ( ) :
 if os . environ . get ( "jcid" ) :
  iii = os . environ [ "jcid" ]
  print ( "已获取用户名" + " " + iii )
  return iii
 else :
  print ( "获取账号失败，请export jcid='你的账号'" )
i111IiI1Iii1I = iIiii1i111i1I ( )
def OoOo ( ) :
 if os . environ . get ( "jcpw" ) :
  III = os . environ [ "jcpw" ]
  oO0oOo0O00O0o = len ( III )
  iiIiiiIII1Ii = list ( III )
  O0O00 = oO0oOo0O00O0o - 1
  i1iiIII111 = iiIiiiIII1Ii [ 0 ] + "****" + iiIiiiIII1Ii [ O0O00 ]
  print ( "已获取密码" + " " + i1iiIII111 )
  return III
 else :
  print ( "获取密码失败，请export jcpw='你的密码'" )
Ii = OoOo ( )
IIii11Ii = requests . session ( )
OOoOoo000O00 = {
 "email" : i111IiI1Iii1I ,
 "passwd" : Ii
 }
Ooo0Ooo = "https://a.luxury/signin?c=0.7831298079748228"
IIii11Ii . post ( Ooo0Ooo , data = OOoOoo000O00 )
ii1I1iII1I1I = IIii11Ii . post ( 'https://a.luxury/user/checkin?c=0.3588015978783363' )
i1I1IiIIiIi1 = ii1I1iII1I1I . content . decode ( 'unicode_escape' )
oo0O000ooO = re . compile ( r'"msg":"(?P<name>.*?)"' , re . S )
iIIiiIIiii1 = oo0O000ooO . finditer ( i1I1IiIIiIi1 )
i111IiI1Iii1I = [ ]
for iIi1ii1I1iI11 in iIIiiIIiii1 :
 print ( iIi1ii1I1iI11 . group ( "name" ) )
 i111IiI1Iii1I . append ( iIi1ii1I1iI11 . group ( "name" ) )
if i111IiI1Iii1I == [ ] :
 print ( "账号或密码错误，请检查" )
 if 55 - 55: I11II1Ii % iIi
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3