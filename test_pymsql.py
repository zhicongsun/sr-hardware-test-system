# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:55:33 2020

@author: SZC
"""
import pymysql
try:
    db = pymysql.connect("localhost","root","SR2020","sr_test")
    print("已连接数据库sr_test")
except:
    print("连接数据库sr_test失败，以下操作无效，请检查设置")
cursor = db.cursor()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print("version: %s" %data)

sql = """INSERT INTO `sr_test`.`pcb_data` 
        (`user_name`, `pcb_version`, `qualified_or_not`, `firmware_version`, `pcb_numb`) 
         VALUES (%s, %s, %s, %s, %s)"""
sr_user_name = "WXQ"
sr_pcb_version = "V0.1"
sr_qualified_or_not = "True"
sr_firmware_version = "V1.1.0"
sr_pcb_numb = "2020072201"
values = (sr_user_name,sr_pcb_version,sr_qualified_or_not,sr_firmware_version,sr_pcb_numb)
try:
    cursor.execute(sql,values)
    db.commit()
    print("成功向表pcb_data中插入数据")
except:
    db.rollback()
    print("向表pcb_data插入数据失败")
try:
    db.close()
    print("已断开与数据库sr_test的连接")
except:
    print("断开连接失败，请检查设置")
