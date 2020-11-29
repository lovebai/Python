'''
@Descripttion: 学习项目
@version: 1.0.0
@Author: Xiaobai
@Date: 2019-12-23 18:30:11
@LastEditors  : Xiaobai
@LastEditTime : 2019-12-25 14:15:23
@BlogSite: https://www.xiaobaibk.com
'''

import urllib.request
import os,parsel,re
from bs4 import BeautifulSoup

def save_dir():#保存目录
    folder=str(input("[默认为当前目录下的GIF]请输入要保存的文件夹名字："))
    if(folder==''):
        folder='GIF'
    if(os.path.exists(folder)):
        pass
    else:
        os.mkdir(folder)
    os.chdir(folder)
    #print('您的保存目录是：',os.getcwd())

def open_url(url):#打开网页
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def get_page(url):#查找页码
    url=url+"forum-38-1.html"
    html=open_url(url)
    soup=BeautifulSoup(html,'lxml').find('div',class_='pg')
    page=soup.find_all('a')[-2].get_text()
    return page

def find_url(url,link):#查找图片页链接
    html=open_url(link)
    hr=parsel.Selector(html.decode('GBK'))
    th=hr.xpath("//h3/a/@href").extract()
    #banner=hr.xpath("//h3/a/@title").extract()
    urlnum=[]
    for k in th:
        urlnum.append(url+k)
    return urlnum
             
def open_page(j):#打开页面并查找图片地址
    html=open_url(j)
    div=parsel.Selector(html.decode('GBK'))
    img=div.xpath("//div[@align='center']/img/@src").extract()
    return img

def save_img(picurl):#保存图片
    for each in picurl:
        filename = each.split('/')[-1]
        if(os.path.exists(filename)):
            pass
        else:
            with open(filename,'wb')as file:
                picture=open_url(each)
                file.write(picture)
    #print('正在保存',filename)


def main():
    url="http://www.gifcc.com/"
    save_dir()
    page=int(get_page(url))+1
    print("正在保存文件中,请到",os.getcwd(),'目录下查看')
    print("停止保存请按“ctrl+c”或者直接关闭窗口")
    for i in range(1,page):
        ++i
        link=url+'forum-38-'+str(i)+'.html'
        img_url=find_url(url,link)
        for j in img_url:
            picurl=open_page(j)
            save_img(picurl)
        

if __name__ == "__main__":
    main()