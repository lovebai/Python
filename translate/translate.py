from tkinter import *
import urllib.request
import urllib.parse
import json


root = Tk()
root.title("在线翻译小程序")
root.geometry("550x300")
#root.iconbitmap('E:\\python\\fanyi\\test\\translate.ico')#窗口图标

frame=Frame(root)
frame.pack()
var=StringVar()

Label(frame, text='请在下面的输入要翻译的内容',font=('Arial', 16),pady=10).grid(row=1,column=0)
Entry(frame,width=75,textvariable=var).grid(row=2,column=0,padx=10)

def translate():
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    content=var.get()
    data={}
    data['i']=content
    data['from']= 'AUTO'
    data['to']='AUTO'
    data['smartresult']=' dict'
    data['client']= 'fanyideskweb'
    data['salt']='15703737120406'
    data['sign'] ='441d708b3695e3e9e55bf599f1768cf5'
    data['ts']= '1570373712040'
    data['bv'] ='b4cf244dcaabcc8b2ae8b3c5559d3dd6'
    data['doctype'] ='json'
    data['version'] ='2.1'
    data['keyfrom']= 'fanyi.web'
    data['action']= 'FY_BY_CLICKBUTTION'

    data=urllib.parse.urlencode(data).encode('utf-8')

    response=urllib.request.urlopen(url,data)
    html=response.read().decode('utf-8')

    target=json.loads(html)
    results=target['translateResult'][0][0]['tgt']
    t1.insert(INSERT,results)
    

def re_translation():
    t1.delete(0.0, END)
    var.set("")
    
frame1=Frame(root)
frame1.pack()

Label(frame1, text='翻译结果',font=('Arial', 16),pady=10).grid(row=1,column=0)
t1 = Text(frame1, height=5,width=75)
t1.grid(row=2,column=0,padx=10)
t1.config(state=NORMAL)

frame2=Frame(root)
frame2.pack()

Button(frame2,text="翻 译",font=(15),command=translate).grid(row=1,column=0,padx=15,pady=15)
Button(frame2,text="清 空",font=(15),command=re_translation).grid(row=1,column=1,padx=15,pady=15)

mainloop()
