'''
@Descripttion: 下载4K壁纸小程序
@version: 1.0.0
@Author: Xiaobai
@Date: 2019-12-14 11:36:27
@LastEditors  : Xiaobai
@LastEditTime : 2019-12-18 23:05:33
'''
import urllib.request
import parsel
import os

## 分类选择操作
def link_url(site):
    print("请小主人选择一下分类\n")
    pictureclass = ['/4kfengjing/','/4kmeinv/','/4kyouxi/','/4kdongman/','/4kyingshi/','/4kmingxing/','/4kqiche/','/4kdongwu/','/4krenwu/','/4kmeishi/','/4kzongjiao/','/4kbeijing/']
    classname = ['0：风景','1：美女','2：游戏','3：动漫','4：影视','5：明星','6：汽车','7：动物','8：人物','9：美食','10：宗教','11：背景\n']
    for each in classname:#遍历显示分类内容
        print(each)
    t=int(input('请输入分类序号：'))#提示输入分类编号
    if(t==1):#一个小提示
        print("哦哟哟，小心营养跟不上哦！^T_T^\n\n")
    url=site+pictureclass[t]
    #print(url)
    print('你选择了',classname[t][-2]+classname[t][-1])
    return url#返回值
    
##请求操作
def open_url(url):#打开网页
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html#返回值

##获取当前分类的所有页面数
def page_num(html):#获取页数
    html=html.decode('GBK')#将页面设置为GBK编码
    sel = parsel.Selector(html)#使用paesel模块
    div = sel.css('.page a::text')[-2].extract()#查找特定内容
    return div#返回值

##获取当前所有页链接地址    
def find_img(site,urls):#获取图片页面链接
    arr_url=[]#创建一个数组将链接添加到这个数组里面
    html=open_url(urls).decode('GBK')#请求页面后返回并设置为GBK编码格式
    sels = parsel.Selector(html)#使用paesel模块
    divs = sels.css('.slist ul')#筛选内容
    a_href =divs.css('li a::attr(href)').getall()#详细筛选需要的内容
    for i in a_href:#遍历
        pages=site+i#拼接url
        arr_url.append(pages)#添加到数组
    return arr_url#返回数组

def search_img(site,num_url):#获取图片下载地址
    #print(num_url)
    html=open_url(num_url).decode('GBK')#请求页面后返回并设置为GBK编码格式
    selss = parsel.Selector(html)#使用paesel模块
    pic_url = selss.css('.photo .photo-pic img::attr(src)').getall()#获取图片下载链接地址
    picture=[]#创建数组
    for k in pic_url:#遍历
        url=site+k#拼接url
        picture.append(url)#添加到数组
    #print(picture)
    return picture#返回数组
    
def search_title(site,num_url):#获取图片名称
    html=open_url(num_url).decode('GBK')#请求页面后返回并设置为GBK编码格式
    selss = parsel.Selector(html)#使用paesel模块
    pic_title = selss.css('.photo .photo-pic img::attr(title)').extract_first()#查找图片名称
    pictitle=[]#创建数组
    pictitle.append(pic_title)#将标题添加到数组
    #print(pictitle)
    return pictitle#返回值


def save_img(folder,picurl,pictitle):#保存图片
    for each in picurl:#遍历所有图片链接
        suffix = each.split('.')[-1]#分割文件名
        for name in pictitle:#遍历所有图片名称
            if(os.path.exists(name+'.'+suffix)):#判断文件是否存在，如果存在则跳过
                pass
            else:
                with open(name+'.'+suffix,'wb') as f:
                    img=open_url(each)
                    f.write(img)#写入文件
            print('正在保存',name)


def download(folder='Wallpaper'):
    if os.path.exists(folder):#判断目录是否存在,如果不存在则创建，存在则跳过
        pass
    else:
        os.mkdir(folder)#创建成功目录
    os.chdir(folder)#切换工作目录
    print('图片保存目录为：',os.getcwd())#打印当前工作目录
    site = 'http://pic.netbian.com'#目标网站地址
    url=link_url(site)#分类页链接
    #1页21张图片
    html=open_url(url)#打开网页
    page=int(page_num(html))+1#获取页数
    
    for i in range(1,page):#遍历所有页面
        ++i
        if(i!=1):#由于网页结构问题所有加此判断
            urls=url+'index_'+str(i)+'.html'#拼接链接
        else:
            urls=url+'index.html'#拼接链接
        num_page=find_img(site,urls)#查找当前页内所有的链接
        for num_url in num_page:#遍历各个页面
            picurl=search_img(site,num_url)#查找图片链接
            pictitle=search_title(site,num_url)#获取图片标题
            save_img(folder,picurl,pictitle)#保存获取的图片
            #print(pictitle)
            
print("""使用方法：比如你想下载\'美食\'那么就在输入框内输入它的序号\'9\'然后按下回车即可\n如果要停止下载可以按\"CTRL+C\"或者直接关闭本窗口Linux系统也按\"CTRL+C\"""")#文本提示

if __name__ == "__main__":
    download()
