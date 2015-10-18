# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import re
import os
import urllib2
import urllib
#打开URL
def url_open(url):
 req=urllib2.Request(url)
 req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36')
 resp=urllib2.urlopen(req)
 html=resp.read()
 return html
#找到有图片的链接
def get_page(url):
 html=url_open(url)
 find_html=r'<a target="_blank" href="(http://www.mm131.com/xinggan/\d{3}\d?\.html)">'
 htmllist=re.findall(find_html,html)
 return htmllist
#在链接中找图片
def get_img(url):
 html=url_open(url)
 #获得图片数量
 find_img_num=r"<a href='\d{3}\d?_\d\d?\.html' "
 img_num=len(re.findall(find_img_num,html))
 #获得图片编号
 find_img_id=r"<a href='(\d{3}\d?)_\d\d?\.html' "
 img_id=(re.findall(find_img_id,html))[0]
 #图片链接的规律是http://img1.mm131.com/pic/\d{3}\d/\d\d?\.jpg,其中第二个数字是从1到图片总量的数字
 #根据这个规律，以下是寻找图片的链接保存在一个列表
 num=1
 imglist=[]
 for eachimg in range(0,img_num,1):
  eachimg='http://img1.mm131.com/pic/%s/%s.jpg' %(img_id,str(num))
  imglist.append(eachimg)
  num+=1
 return img_id,img_num,imglist
#下载图片
def download():
 url='http://www.mm131.com/xinggan/'#这个是性感美女板块的第一页，可以模仿上面找规律方法，并通过循环来下载所有页或其他板块
 h=get_page(url)
 if not os.path.exists('Beauty'):
        os.mkdir('Beauty')
 os.chdir('Beauty')
 for eachhtml in h:
  (pid,num,piclist)=get_img(eachhtml)
  if not os.path.exists(pid):
    os.mkdir(pid)
  os.chdir(pid)
  for eachpic in piclist:
   eachpic_name=(eachpic).split('/')[-1]
   if not os.path.exists(eachpic_name):    #同个美女保存在一个以美女编号为名的文件夹
     urllib.urlretrieve(eachpic,eachpic_name,None)
  print u'已成功获取',num,u'张图片保存于',pid,u'中,正在获取下一批,请耐心等待...'
  os.chdir('E:\mm')#这个相当于返回上一个文件夹
 print u'获取完毕!'
download()
