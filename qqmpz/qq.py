import urllib.request
import tkinter as tk
import tkinter.messagebox


def open_url():
    url = ['http://api.klksq.vip/mpz/api.php?url=http://qiyansq.cn&tid=1&qq=',
           'http://api.klksq.vip/mpz/api.php?url=http://www.w6ds.cn&tid=1&qq=',
           'http://api.2019fafa.cn/mpz.php?id=null&url=http://lo.01si.cn&tid=425&mm=123456&qq=',
           'http://api.2019fafa.cn/mpz.php?id=null&url=http://www.371qq.cn&tid=16&mm=123456&qq=',
           'http://api.2019fafa.cn/api.php?id=null&url=http://www.qqguizu.com&tid=754&mm=123456&qq=',
           'http://api.2019fafa.cn/api.php?id=null&url=http://www.432ds.top&tid=2&mm=123456&qq=']
    txt = var.get()
    if len(str(txt)) <=10 and len(str(txt)) >4:
        tkinter.messagebox.showinfo('小白提示','正在领取中请稍等哦....名片赞会在12小时内到账！')
        for each in url:
            url = each + str(txt)
            req = urllib.request.Request(url)
            req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36')
            response = urllib.request.urlopen(url)
            print(response.url)
        tkinter.messagebox.showinfo('小白提示','恭喜你，领取成功啦！')
    else:
        tkinter.messagebox.showinfo('小白提示','请输入正确的QQ号!')
    

root = tk.Tk()
root.title('QQ名片赞领取小助手')
var=tk.StringVar()
root.geometry("450x200")
tk.Label(root, text='在文本框中输入QQ然后点领取按钮即可获得1000个QQ名片赞',font=('宋体', 12),pady=7,padx=5).grid(row=1,column=0)
tk.Entry(root,width=40,textvariable=var).grid(row=2,column=0,pady=15)
tk.Button(root,text="免 费 领 取",font=(10),command=open_url).grid(row=3,column=0,pady=10)
tk.Label(root, text='公告:输入要刷的QQ即可！每天每个账号只能领取一次哦！',font=('楷体', 12),padx=5,pady=15).grid(row=5,column=0,pady=15)
root.mainloop()


