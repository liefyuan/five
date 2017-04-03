# excute database operation
# -*- coding:UTF-8 -*-

#该文件是作为数据库操作的“驱动”程序

import MySQLdb

conn = MySQLdb.connect("localhost", "root","" , "test")
cur = conn.cursor()

def addUser(username, password, email):#注册新用户
    sql = "insert into user (username,password,email) values ('%s','%s','%s')" % (username, password, email)
    cur.execute(sql)
    conn.commit()
    conn.close()


def isExisted(username, password):#检查用户是否存在
    sql = "select * from user where username ='%s' and password ='%s'" % (username, password)
    cur.execute(sql)
    result = cur.fetchall()
    if (len(result) == 0):
        return False
    else:
        return True

def isNameExisted(username):#检查名字是否存在
    sql = "select * from user where username ='%s'" % (username)
    cur.execute(sql)
    result = cur.fetchall()
    if (len(result) == 0):
        return False
    else:
        return True


def checkPassword(username):#检查密码是否正确
    sql = "select password from user where username ='%s'" % (username)
    cur.execute(sql)
    result = cur.fetchall()
    return str(result)[3:69]#返回hash码


def addValue(value,id):
    sql = " update monitor set revalue= '%s' where id='%s'" % (value, id)
    cur.execute(sql)
    conn.commit()
   # conn.close()


def retValue(id):
    sql = "select * from monitor where id ='%s'" % (id)
    cur.execute(sql)
    result = cur.fetchall()
    if (len(result) == 0):
        return False
    else:
        tem = str(result)
        tem1 = tem[7:15]
        return tem1