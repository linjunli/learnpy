# 正则表达式
# re模块
# \d匹配一个数字,\s匹配一个空格，\w匹配一个数字或者字符，()分组
s = r'ABC\-001' # 使用r前缀不用考虑转义
import re
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
m = re.match(r'^(\d{3})\-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.groups())

# base64
import base64
encode = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(encode)
# url中不能出现+/
# urlsafe_b64encode将+/替换为-_
urlbase = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(urlbase)

# struct
# >代表big-endian就是网络序,I代表4字节无符号整数
# H代表2字节无符号整数
import struct
value = struct.pack('>I', 10240099)
print(value)
fourAndTwo = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(fourAndTwo)

# hashlib
# 摘要算法，通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
# 用于hash密码
import hashlib
md5 = hashlib.md5()
md5.update('The best handsome man is lilinjun of the world!'.encode('utf-8'))
print(md5.hexdigest())
sha1 = hashlib.sha1()
sha1.update('The best handsome man is lilinjun of the world!'.encode('utf-8'))
print(sha1.hexdigest())

# itertools迭代对象处理
# 无限迭代虽然可以一直迭代，但takewhile可以截取有限序列
import itertools
# 无限迭代
naturals = itertools.count()
naturalsABC = itertools.cycle('ABC')
naturalsRepeat = itertools.repeat('A', 3)
# for n in naturals:
#     print(n)
ns = itertools.takewhile(lambda x: x <=10, naturals)
print(list(ns))
# chain()串联迭代
for c in itertools.chain('ABC', 'DEF'):
    print(c)
# groupby() 挑出相邻重复元素
for key,group in itertools.groupby('AABESDDDFFGGHVSEF'):
    print(key, list(group))
for key,group in itertools.groupby('AaaBbbCccdD', lambda x: x.upper()):
    print(key, list(group))

# contextlib
# 实现自动关闭(文件读写等)
# 相当于省略了类中的__enter__和__exit__函数
from contextlib import contextmanager

class Query(object):
    def __init__(self, name):
        self.name = name
    def query(self):
        print('Query info about %s...'% self.name)
    
@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')
with create_query('Bod') as q:
    q.query()

# closing
# 如果对象没有上下文就没法使用with,closing就是把对象变为上下文对象
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.xiaoying.com')) as page:
    for line in page:
        print(line)
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

# XML
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax: start_element: %s,attrs:%s'% (name,str(attrs)))
    def end_element(self, name):
        print('sax:end_element:%s'% name)
    def char_data(self, text):
        print('sax:char_data: %s'% text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

# HTMLParser
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)
    def handle_endtag(self, tag):
        print('</%s>' % tag)
    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)
    def handle_data(self, data):
        print(data.replace(u'\xa0', u' '))
    def handle_comment(self, data):
        print('<!--', data, '-->')
    def handle_entityref(self, name):
        print('&%s;' % name)
    def handle_charref(self, name):
        print('&#%s;' % name)
parserHTML = MyHTMLParser()
parserHTML.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

print('<==============urllib===============>')
# urllib
# 提供一系列用于操作url的功能
from urllib import request, parse
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Statud:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:',data.decode('utf-8'))
# 模拟请求
print('<==============模拟请求===============>')
req = request.Request('https://www.xiaoying.com')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    data = f.read()
    print('Statud:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:',data.decode('utf-8'))
print('<==============模拟微博登录===============>')
# email = input('Email:')
# passwd = input('Password:')
# login_data = parse.urlencode([
#     ('username', email),
#     ('password', passwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])

# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

print('<==============常用第三方模块===============>')
# PIL: Python Imaging Library
# virtualenv:独立的python环境
# 图形界面: Tk,wxWigets,Qt,GTK;python自带Tkinter
from tkinter import *
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello,world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
# app = Application()
# app.master.title('Hello World!')
# app,mainloop()

# 网络编程
# TCP/IP
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80))