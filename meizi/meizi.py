import requests
import os
import parsel

print("本实例只下载几张图")
def url_open():
    response = requests.get("http://cos.top15.cn/")
    html = response.text
    sel = parsel.Selector(html)
    div =sel.css(".item")
    url = []
    for divs in div:
        img_url = divs.css(".a-img .pic::attr(src)").extract()
        img_title = divs.css(".a-img .pic::attr(alt)").extract()
        url.append((img_url,img_title))
    return url

def save_img():
    urls =url_open()
    for url in urls:
        response = requests.get(url[0][0])
        print(response)
        suffix = url[0][0].split(".")[-1]
        with open(url[1][0]+"."+suffix,mode="wb")as f:
            f.write(response.content)




def download_meizi():
    if os.path.exists("meizi"):
        pass
    else:
        os.mkdir("meizi")
    os.chdir("meizi")
    save_img()

if __name__=="__main__":
    download_meizi()

