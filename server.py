# WSGI
# 从wsgiref模块导入：
# from wsgiref.simple_server import make_server
# # 导入我们自己的application函数
# from web import application

# # 创建服务器
# httpd = make_server('', 8000, application)
# print('Server HTTP on port 8000...')
# # 开始监听HTTP请求
# httpd.serve_forever()

# WSGI进一步抽象得到web框架
# flask: 简单好用的web框架
# Django: 全能web框架 
# web.py: 一个小巧的web框架
# Bottle: 和Flask类似的web框架
# Tornado: Facebook的开源异步web框架
# pip3 install flask
from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()

# 使用模版