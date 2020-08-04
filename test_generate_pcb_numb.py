import pymysql
import re
import datetime

def generate_pcb_numb():
    global pcb_data
    
    #从数据库获取数据
    try:
        db = pymysql.connect("localhost","root","SR2020","sr_test")
        print("已连接数据库sr_test")
    except:
        print("连接数据库sr_test失败，以下操作无效，请检查设置")
    cursor = db.cursor()
    search_cmd = """select * from sr_test.pcb_data"""
    cursor.execute(search_cmd)
    pcb_database_info = cursor.fetchall()
    try:
        db.close()
        print("已断开与数据库sr_test的连接")
    except:
        print("断开连接失败，请检查设置")
    
    #产生pcb_numb
    now = datetime.datetime.now()
    now_ymd = now.strftime("%Y%m%d")#获取当时的年月日
    each_result = []*len(pcb_database_info)
    for i in range(len(pcb_database_info)):#遍历数据库中的每个pcb_numb，将合格与否记录在each_result中
        comp = re.match(now_ymd, pcb_database_info[i][6])#利用正则表达式比较数据库中的编码日期是否为当天
        if pcb_database_info[i][6] == "None" or comp == None:
            each_result.append('None')
        elif (comp.span() == (0,8)) and (pcb_database_info[i][4] == 'True'):
            each_result.append('True')
        elif (comp.span() == (0,8)) and (pcb_database_info[i][4] == 'False'):
            each_result.append('False')
        else:
            print("检测pcb_numb时发现数据库内容异常，请检查")

    pcb_data[2][1] = now.strftime("%Y-%m-%d %H:%M:%S")#为数据库的pcb_data的date_time赋值
    if pcb_data[5][1] == "True":#当前待加入的pcb是合格的，产生合格编号否则产生不合格编号，编号格式：日期+T/F+合格/不合格编号
        numb = each_result.count('True')+1  #如2020年8月4号第三个合格pcb的编号pcb_numb为20200804T0003
        if len(str(numb)) == 1:
            pcb_data[7][1] = now_ymd + "T" + "000" + str(numb)
        elif len(str(numb)) == 2:
            pcb_data[7][1] = now_ymd + "T" + "00" + str(numb)
        elif len(str(numb)) == 3:
            pcb_data[7][1] = now_ymd + "T" + "0" + str(numb)        
        elif len(str(numb)) == 4:
            pcb_data[7][1] = now_ymd + "T" + str(numb)        
        else:
            print("生产超过9999个合格产品，编号不足，请修改程序")
        print("生成合格编码：%s " % pcb_data[7][1])
    elif pcb_data[5][1] == "False":
        numb = each_result.count('False')+1
        if len(str(numb)) == 1:
            pcb_data[7][1] = now_ymd + "F" + "000" + str(numb)
        elif len(str(numb)) == 2:
            pcb_data[7][1] = now_ymd + "F" + "00" + str(numb)
        elif len(str(numb)) == 3:
            pcb_data[7][1] = now_ymd + "F" + "0" + str(numb)  
        elif len(str(numb)) == 4:
            pcb_data[7][1] = now_ymd + "F" + str(numb)        
        else:
            print("生产超过9999个不合格产品，编号不足，请修改程序")
        print("生成不合格编码：%s " % pcb_data[7][1])
    else:#
        print("未进行外设检测，无法正常生成pcb_numb")
        
    

if __name__ == "__main__":
    pcb_data = [ #初始化数据
        {'report_code': 'None', 
         'task_name':'None',
         'report_date':'None',
         'report_creator':'None'},
        ['admin_name','None'],
        ['date_time','None'],
        ['pcb_version','None'],
        ['test_firmwave_version','None'],
        ['qualified_or_not','True'],
        ['func_firmwave_version','None'],
        ['pcb_numb','None'],
        ['io_din','None'],
        ['io_dout','None'],
        ['uart115200_packet_loss_rate','None'],
        ['uart115200_error_rate','None'],
        ['uart115200_delay_time','None'],
        ['can50k_packet_loss_rate','None'],
        ['can50k_error_rate','None']
    ]

    generate_pcb_numb()