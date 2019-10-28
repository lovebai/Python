import urllib.request
import json
import os

print("我已经开始下载咯^_^请稍等一下下，么么哒")
if os.path.exists("mz"):
    pass
else:
    os.mkdir("mz")
os.chdir("mz")

def img_open(url):
    url = url
    response = urllib.request.urlopen(url)
    html = response.read().decode("utf-8")
    target = json.loads(html)
    for i in range(20):
        try:
            try:
                result =target["data"][i]['title']
                results =target["data"][i]['pic']
                with open(result+".jpg",'wb')as f:
                    response = urllib.request.urlopen(results)
                    img = response.read()
                    f.write(img)
            except:
                print("已经下载完成了")
        except IndexError:
            print('没有了')

for temp in range(1,17):
    url = "http://cos.top15.cn/api/listApi.php?page="+str(temp)
    if temp ==1:
        img_open(url)
    elif temp ==2:
        img_open(url)
    elif temp ==3:
        img_open(url)
    elif temp ==4:
        img_open(url)
    elif temp ==5:
        img_open(url)
    elif temp ==6:
        img_open(url)
    elif temp ==7:
        img_open(url)
    elif temp ==8:
        img_open(url)
    elif temp ==9:
        img_open(url)
    elif temp ==10:
        img_open(url)
    elif temp ==11:
        img_open(url)
    elif temp ==12:
        img_open(url)
    elif temp ==13:
        img_open(url)
    elif temp ==14:
        img_open(url)
    elif temp ==15:
        img_open(url)
    elif temp ==16:
        img_open(url)
    else:
        print("已经没有了")

