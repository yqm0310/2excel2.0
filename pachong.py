import urllib.request
import urllib.parse

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

import socket

from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import tkinter.scrolledtext


root = tkinter.Tk()
root.title('爬虫')  # 标题
root.geometry('800x600')  # 窗体大小
root.resizable(False, False)  # 固定窗体
text=tkinter.scrolledtext.ScrolledText(root,font=('微软雅黑',10),fg='blue')

requestSrc = 'http://python.org/'

def showMsg(showInfo):
    try:
        text.insert(END, showInfo + '\n')
        text.see(END)
    except:
        print(showInfo)

#抓取方法1
def f1():

    response = urllib.request.urlopen(requestSrc)
    html = response.read()
    showMsg(html)

#使用 Request
def f2():
    req = urllib.request.Request(requestSrc)
    response = urllib.request.urlopen(req)
    the_page = response.read()
    showMsg(the_page)

#发送数据
def f3():
    url = 'http://localhost/login.php'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = {
        'act': 'login',
        'login[email]': 'yzhang@i9i8.com',
        'login[password]': '123456'
    }

    data = urllib.parse.urlencode(values)
    req = urllib.request.Request(url, data)
    req.add_header('Referer', 'http://www.python.org/')
    response = urllib.request.urlopen(req)
    the_page = response.read()

    showMsg(the_page.decode("utf8"))



#发送数据和header
def f4():

    url = 'http://localhost/login.php'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = {
        'act': 'login',
        'login[email]': 'yzhang@i9i8.com',
        'login[password]': '123456'
    }
    headers = {'User-Agent': user_agent}

    data = urllib.parse.urlencode(values)
    req = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(req)
    the_page = response.read()

    showMsg(the_page.decode("utf8"))



#http 错误
def f5():
    req = urllib.request.Request('http://www.python.org/fish.html')
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        showMsg(e.code)
        showMsg(e.read().decode("utf8"))


#异常处理1
def f6():
    req = Request("http://twitter.com/")
    try:
        response = urlopen(req)
    except HTTPError as e:
        showMsg('The server couldn\'t fulfill the request.')
        showMsg('Error code: '+e.code)
    except URLError as e:
        showMsg('We failed to reach a server.')
        showMsg('Reason: '+ e.reason)
    else:
        showMsg("good!")
        showMsg(response.read().decode("utf8"))



#异常处理2
def f7():
    req = Request("http://twitter.com/")
    try:
        response = urlopen(req)
    except URLError as e:
        if hasattr(e, 'reason'):
            showMsg('We failed to reach a server.')
            showMsg('Reason: '+ e.reason)
        elif hasattr(e, 'code'):
            showMsg('The server couldn\'t fulfill the request.')
            showMsg('Error code: '+ e.code)
    else:
        showMsg("good!")
        showMsg(response.read().decode("utf8"))


#HTTP认证
def f8():
    # create a password manager
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

    # Add the username and password.
    # If we knew the realm, we could use it instead of None.
    top_level_url = "https://cms.tetx.com/"
    password_mgr.add_password(None, top_level_url, 'yzhang', 'cccddd')

    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib.request.build_opener(handler)

    # use the opener to fetch a URL
    a_url = "https://cms.tetx.com/"
    x = opener.open(a_url)
    showMsg(x.read())

    # Install the opener.
    # Now all calls to urllib.request.urlopen use our opener.
    urllib.request.install_opener(opener)

    a = urllib.request.urlopen(a_url).read().decode('utf8')
    showMsg(a)


#使用代理
def f9():

    showMsg(text)

    proxy_support = urllib.request.ProxyHandler({'sock5': 'localhost:1080'})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)

    a = urllib.request.urlopen("http://g.cn").read().decode("utf8")
    showMsg(a)


#超时
def f10():
    # timeout in seconds
    timeout = 2
    socket.setdefaulttimeout(timeout)

    # this call to urllib.request.urlopen now uses the default timeout
    # we have set in the socket module
    req = urllib.request.Request('http://twitter.com/')
    a = urllib.request.urlopen(req).read()
    showMsg(a)

btn1 = tkinter.Button(root, text='最简单', command=f1).pack(ipadx=10,ipady=2,padx=0,pady=0,side=TOP)
btn2 = tkinter.Button(root, text='使用 Request', command=f2).pack(ipadx=10,ipady=2,padx=10,pady=0,side=TOP)
btn3 = tkinter.Button(root, text='发送数据', command=f3).pack(ipadx=10,ipady=2,padx=20,pady=0,side=TOP)
btn4 = tkinter.Button(root, text='发送数据和header', command=f4).pack(ipadx=10,ipady=2,padx=30,pady=0,side=TOP)
btn5 = tkinter.Button(root, text='http 错误', command=f5).pack(ipadx=10,ipady=2,padx=40,pady=0,side=TOP)
btn6 = tkinter.Button(root, text='异常处理1', command=f6).pack(ipadx=10,ipady=2,padx=50,pady=0,side=TOP)
btn7 = tkinter.Button(root, text='异常处理2', command=f7).pack(ipadx=10,ipady=2,padx=60,pady=0,side=TOP)
btn8 = tkinter.Button(root, text='HTTP 认证', command=f8).pack(ipadx=10,ipady=2,padx=70,pady=0,side=TOP)
btn9 = tkinter.Button(root, text='使用代理', command=f9).pack(ipadx=10,ipady=2,padx=80,pady=0,side=TOP)
btn10 = tkinter.Button(root, text='超时', command=f10).pack(ipadx=10,ipady=2,padx=90,pady=0,side=TOP)
text.pack(ipadx=200,ipady=100,padx=0,pady=10,side=TOP)


root.mainloop()