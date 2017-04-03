#encoding: utf-8

from flask import render_template,request,session
from main import main
from models import *



@main.route('/')
@main.route('/home')
def index():
    print'__name__', __name__
    return render_template('main/home.html')


@main.route('/doc')
def document():
    return render_template('main/doc.html')

