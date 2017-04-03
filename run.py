#encoding: utf-8

from flask import Flask
from asset import asset
from user import user
from main import main
from study import study




app = Flask(__name__,
              template_folder='templates',  # 指定模板路径，可以是相对路径，也可以是绝对路径。
              static_folder='static',  # 指定静态文件前缀，默认静态文件路径同前缀
              # static_url_path='/opt/auras/static',     #指定静态文件存放路径。
              )
app.register_blueprint(asset, url_prefix='/asset')  # 注册asset蓝图，并指定前缀。
app.register_blueprint(user, url_prefix='/user')  # 注册user蓝图，并指定前缀。
app.register_blueprint(study, url_prefix='/study')  # 注册study蓝图，并指定前缀。
app.register_blueprint(main,)  # 注册main蓝图，没有指定前缀。


app.config['SECRET_KEY'] = 'you never guess'
app.config['UPLOAD_FOLDER'] = 'upload'


if __name__ == '__main__':
    app.run()
#     apple.run(host='0.0.0.0', port=8000, debug=True)
    # 运行flask http程序，host指定监听IP，port指定监听端口，调试时需要开启debug模式。
