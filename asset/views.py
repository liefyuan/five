#encoding: utf-8

from flask import render_template,session, redirect,request
from asset import asset
from main import main
from functools import wraps

#登录、注册认证函数
def liefyuan(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        user = session.get('comming', None)  # 取得登录标志
        if user:
            return fn(*args, **kwargs)  # 登录了就返回请求
        else:
            return redirect('/comming')
    return wrapper

#登录用户
@main.route('/comming', methods=['GET', 'POST'])
def comming():
    if request.method == 'GET':
        return render_template("user/login.html")
    if request.method == 'POST':
        u = request.form['username']
        p = request.form['password']
        if (u == "xiaohua") & (p == "987789"):
            session['comming'] = True
            return redirect('/asset')
        else:#没有用户就是新用户那么就转入注册页面
            return redirect('user/nolognin')

@asset.route('/')  # 指定路由为/，因为run.py中指定了前缀，浏览器访问时，路径为http://IP/asset/
@liefyuan
def index():
    print'__name__', __name__
    session['comming'] = False
    return render_template('asset/admin.html')  # 返回index.html模板，路径默认在templates下