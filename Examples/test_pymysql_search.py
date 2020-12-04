# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:55:33 2020

@author: SZC
"""
import pymysql
def is_admin(admin_name,password):#通过数据库判断是否未管理员，是则返回True,否则返回False
    try:
        db = pymysql.connect("localhost","root","SR2020","sr_test")
        print("已连接数据库sr_test")
    except:
        print("连接数据库sr_test失败，以下操作无效，请检查设置")
    cursor = db.cursor()
    search_cmd = """select * from sr_test.administrators_data"""
    cursor.execute(search_cmd)
    admin_data = cursor.fetchall()
    each_result = []*len(admin_data)
    for i in range(len(admin_data)):
    allow_open = []*2    
        each_result.append((admin_name in admin_data[i]))
    result = True in each_result
    print(each_result)
    
    if result == True:
        id_admin = each_result.index(True)#记录是哪个用户
        print("用户 %s 存在" %admin_name)
        if password == admin_data[id_admin][1]:#判断密码是否正确
            allow_open[0] = True
            print("用户 %s 密码正确" % admin_name)
            allow_open[1] = "你好管理员"
        else:
            allow_open[0] = False
            print("用户 %s 密码错误" % admin_name)
            allow_open[1]="用户存在，密码错误"
    else:
        print("用户不存在")
        allow_open[1] = "用户不存在"
    
    try:
        db.close()
        print("已断开与数据库sr_test的连接")
    except:
        print("断开连接失败，请检查设置")
    return allow_open
        
"""主程序"""
if __name__ == "__main__":
    
    admin_name = "SZC"
    password = "SZC2020"
    a = is_admin(admin_name,password)
    print(a)