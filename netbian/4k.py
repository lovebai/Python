import urllib.request
import os
import random


def url_open(url_num):
    req = urllib.request.Request(url_num)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36')
    response = urllib.request.urlopen(url_num)
    html = response.read()
    return html

def url_get(load,url_num):
    try:
        html = url_open(url_num).decode('gbk')
        img_addrs = []
        a = html.find('<a href=\"\" id=\"img\"><img src=')
        while a!=-1:
            b = html.find('.jpg\"',a,a+255)
            if b != -1:
                img_addrs.append(load+html[a+ 30:b+4])
            else:
                b = a + 9
            a = html.find('<a href=\"\" id=\"img\"><img src=',b)
            return img_addrs
    except urllib.error.URLError as e:
        print ('白总提示:\n出现'+e.code+'错误，请重启软件')          #异常状态


def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)
            print('正在下载【'+str(filename)+'】关闭窗口即可停止下载')
    #f.close()

def download_4k(folder='4K',page=24943):
    if os.path.exists('4K'):
        pass
    else:
        os.mkdir(folder)
    os.chdir(folder)

    url = 'http://pic.netbian.com/tupian/'
    load = 'http://pic.netbian.com/' 
    num = random.randint(1,page)
    for i in range(page):
        num -= i
        url_num = url + str(num) + '.html'
        img_addrs = url_get(load,url_num)
        save_imgs(folder,img_addrs)


if __name__== '__main__':
    download_4k()
    
