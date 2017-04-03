# -*- coding:UTF-8 -*-
from werkzeug.utils import secure_filename
from flask import request,jsonify,send_from_directory,abort,Flask
import time
import os
import sys
import base64
from flask import render_template
from study import study
from main import main



# UPLOAD_FOLDER = 'upload'
# main.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'xls', 'JPG', 'PNG', 'xlsx', 'gif', 'GIF'])


# 用于判断文件后缀
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@study.route('/')
@study.route('/upload')
def upload():
    return render_template('study/study_upload.html')


# 上传文件
@study.route('/api/upload', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = os.path.join(basedir, 'upload')
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['myfile']  # 从表单的file字段获取文件，myfile为该表单的name值
    if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
        fname = secure_filename(f.filename)
        print fname
        ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
        unix_time = int(time.time())
        new_filename = str(unix_time) + '.' + ext  # 修改了上传的文件名
        f.save(os.path.join(file_dir, new_filename))  # 保存文件到upload目录
        token = base64.b64encode(new_filename)
        print token

        return jsonify({"errno": 0, "errmsg": "上传成功", "token": token})
    else:
        return jsonify({"errno": 1001, "errmsg": "上传失败"})


@study.route('/download/<filename>', methods=['GET'])
def download(filename):
    if request.method=="GET":
        if os.path.isfile(os.path.join(basedir,'upload', filename)):
            return send_from_directory('upload',filename,as_attachment=True)
        abort(404)

#############################################################################
#多文件上传方法
#############################################################################


@study.route('/muilti-upload', methods=['GET','POST'])
def muiltiUpload():
	if request.method == 'POST':
		#"""Handle the upload of a file."""
		form = request.form
		# 这里获取绝对路径
		abpath = os.path.abspath('./upload/')
		for upload in request.files.getlist("file"):
			filename = upload.filename.rsplit("/")[0]
			destination = "/".join([abpath, filename])
			print "Accept incoming file:", filename
			print "Save it to:", destination
			upload.save(destination)

		return jsonify(status='ok' ,msg='OVER')
	else:
		return render_template('study/study_muilti-upload.html')