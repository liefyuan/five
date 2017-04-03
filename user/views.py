#encoding: utf-8
from user import user
from main import main
from flask import render_template, redirect,session,request
from werkzeug.security import generate_password_hash,check_password_hash
from functools import wraps
from models import *
import os
import hashlib

# 简单的错误处理
class loginError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


#登录、注册认证函数
def authorize(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        user = session.get('logged_in',None)#取得登录标志
        if user:
            return fn(*args, **kwargs)#登录了就返回请求
        else:
            return redirect('user/nolognin')#否则就转到注册的页面
    return wrapper


#哈希加盐的密码加密方法
def enPassWord(password):#将明密码转化为hash码
    return generate_password_hash(password)#返回转换的hash码

def checkPassWord(enpassword,password):#第一参数是从数据查询出来的hash值，第二参数是需要检验的密码
    return check_password_hash(enpassword,password)#如果匹配返回true



#注册新用户
@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("user/register.html")
    if request.method == 'POST':
        u = request.form['username']
        p = enPassWord(request.form['password'])
        email = request.form['email']
        addUser(u,p,email)
        return redirect('/signin')#注册完之后进入登录页面


#登录用户
@main.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template("user/login.html")
    if request.method == 'POST':
        u = request.form['username']
        p = request.form['password']
        if isNameExisted(u):
            t = checkPassword(u);#获得数据库存储的hash值
            if check_password_hash(t,p):#查询有没有这个用户
                session['logged_in'] = True
                return redirect('/user/blog')
        else:#没有用户就是新用户那么就转入注册页面
            return redirect('/register')


#注销用户
@main.route('/signout', methods=['GET', 'POST'])
@authorize
def signout():
    session['logged_in'] = False
    return redirect('/home')


@user.route('/')
@user.route('/blog')
@authorize
def blog():
    return render_template('user/blog.html')

@user.route('/nolognin')
def nolognin():
    return render_template('user/nolognin.html')
