# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:55:33 2020

@author: SZC
"""
import pymysql
def write_database(pcb_data):
    # 要写入的参数赋值
    sr_admin_name = pcb_data[1][1]
    sr_date_time = pcb_data[2][1]
    sr_pcb_version = pcb_data[3][1]
    sr_test_firmwave_version = pcb_data[4][1]
    sr_qualified_or_not = pcb_data[5][1]
    sr_func_firmware_version = pcb_data[6][1]
    sr_pcb_numb = pcb_data[7][1]
    sr_io_din = pcb_data[8][1]
    sr_io_dout = pcb_data[9][1]
    sr_uart115200_packet_loss_rate = pcb_data[10][1]
    sr_uart115200_error_rate = pcb_data[11][1]
    sr_uart115200_delay_time = pcb_data[12][1]
    sr_can50k_packet_loss_rate = pcb_data[13][1]
    sr_can50k_error_rate = pcb_data[14][1]
    sr_uart9600_packet_loss_rate = pcb_data[15][1]
    sr_uart9600_error_rate = pcb_data[16][1]
    sr_uart9600_delay_time = pcb_data[17][1]
    sr_can100k_packet_loss_rate = pcb_data[18][1]
    sr_can100k_error_rate = pcb_data[19][1]

    # 连接数据库并获取光标
    try:
        db = pymysql.connect("localhost","root","SR2020","sr_test")
        print("已连接数据库sr_test")
    except:
        print("连接数据库sr_test失败，以下操作无效，请检查设置")
    cursor = db.cursor()

    # 向数据库的pcb_data表中写入数据
    sql = """INSERT INTO `sr_test`.`pcb_data` 
            (`admin_name`, `date_time`,`pcb_version`, `test_firmwave_version`,`qualified_or_not`, `func_firmwave_version`, 
            `pcb_numb`,`io_din`,`io_dout`,`uart115200_packet_loss_rate`,`uart115200_error_rate`,
            `uart115200_delay_time`,`can50k_packet_loss_rate`,`can50k_error_rate`) 
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    values = (sr_admin_name,sr_date_time,sr_pcb_version,sr_test_firmwave_version,sr_qualified_or_not,sr_func_firmware_version,
    sr_pcb_numb,sr_io_din,sr_io_dout,sr_uart115200_packet_loss_rate,sr_uart115200_error_rate,sr_uart115200_delay_time,
    sr_can50k_packet_loss_rate,sr_can50k_error_rate)
    try:
        cursor.execute(sql,values)
        db.commit()
        print("成功向表pcb_data中插入数据")
    except:
        db.rollback()
        print("向表pcb_data插入数据失败")
    
    # 向数据库的peripheral_data表中写入数据
    sql = """INSERT INTO `sr_test`.`peripheral_data` 
        (`pcb_numb`,`io_din`,`io_dout`,
        `uart115200_packet_loss_rate`,`uart115200_error_rate`,`uart115200_delay_time`,
        `can50k_packet_loss_rate`,`can50k_error_rate`,
        `uart9600_packet_loss_rate`,`uart9600_error_rate`,`uart9600_delay_time`,
        `can100k_packet_loss_rate`,`can100k_error_rate`) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" 
   
    values = (sr_pcb_numb,sr_io_din,sr_io_dout,
            sr_uart115200_packet_loss_rate,sr_uart115200_error_rate,sr_uart115200_delay_time,
            sr_can50k_packet_loss_rate,sr_can50k_error_rate,
            sr_uart9600_packet_loss_rate,sr_uart9600_error_rate,sr_uart9600_delay_time,
            sr_can100k_packet_loss_rate,sr_can100k_error_rate)
    try:
        cursor.execute(sql,values)
        db.commit()
        print("成功向表peripheral_data中插入数据")
    except:
        db.rollback()
        print("向表peripheral_data插入数据失败")
    
    # 断开与数据库的连接
    try:
        db.close()
        print("已断开与数据库sr_test的连接")
    except:
        print("断开连接失败，请检查设置")

"""主程序"""
if __name__ == "__main__":
    pcb_data = [ #测试的数据
        {'report_code': 'None', 
         'task_name':'None',
         'report_date':'None',
         'report_creator':'None'},
        ['admin_name','None'],#在is_admin中赋值，登录时
        ['date_time','None'],#在generate_pcb_nub中赋值，最后按下生成PDF按钮时
        ['pcb_version','None'],#在runuart中赋值，扫码时
        ['test_firmwave_version','None'],
        ['qualified_or_not','True'],
        ['func_firmwave_version','None'],
        ['pcb_numb','20200806T0001'],#在generate_pcb_nub中赋值，最后按下生成PDF按钮时
        ['io_din','None'],
        ['io_dout','None'],
        ['uart115200_packet_loss_rate',0],
        ['uart115200_error_rate',0],
        ['uart115200_delay_time',0],
        ['can50k_packet_loss_rate',0],
        ['can50k_error_rate',0],
        ['uart9600_packet_loss_rate',0],
        ['uart9600_error_rate',0],
        ['uart9600_delay_time',0],
        ['can100k_packet_loss_rate',0],
        ['can100k_error_rate',0]
    ]
    write_database(pcb_data)
