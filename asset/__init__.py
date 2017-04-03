#encoding: utf-8

from flask import Blueprint

asset = Blueprint('asset',
                  __name__,
                  #template_folder='../templates/',   #指定模板路径
                  #static_folder='../static/',#指定静态文件路径
                  )

import views