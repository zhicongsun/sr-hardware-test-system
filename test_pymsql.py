# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:55:33 2020

@author: SZC
"""
import pymysql
def write_database(pcb_data):
    try:
        db = pymysql.connect("localhost","root","SR2020","sr_test")
        print("已连接数据库sr_test")
    except:
        print("连接数据库sr_test失败，以下操作无效，请检查设置")
    cursor = db.cursor()
    
    sql = """INSERT INTO `sr_test`.`pcb_data` 
            (`user_name`, `pcb_version`, `qualified_or_not`, `firmware_version`, `pcb_numb`) 
             VALUES (%s, %s, %s, %s, %s)"""
    sr_user_name = pcb_data[1][1]
    sr_pcb_version = pcb_data[2][1]
    sr_qualified_or_not = pcb_data[3][1]
    sr_firmware_version = pcb_data[4][1]
    sr_pcb_numb = pcb_data[5][1]
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
"""主程序"""
if __name__ == "__main__":
    pcb_data = [ #初始化数据
        {'report_code': 'none', 
          'task_name':'第四代电气PCB测试',
          'report_date':'none',
          'report_creator':'SRUser'},
            ['user_name','SRUser'],
            ['pcb_version','none'],
            ['qualified_or_not','none'],
            ['firmwave_version','none'],
            ['pcb_numb','none']
        ]
    write_database(pcb_data)
