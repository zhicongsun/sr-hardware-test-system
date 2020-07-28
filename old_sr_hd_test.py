# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:07:58 2020

@author: SZC
"""

"""生成PDF的类"""
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('pingbold', 'msyh.ttf'))

# 生成PDF文件
class PDFGenerator:
    def __init__(self):
        #规定格式规范
        self.file_path = ''#当前文件夹
        self.title_style = ParagraphStyle(name="TitleStyle", fontName="pingbold", fontSize=48, alignment=TA_LEFT,)
        self.sub_title_style = ParagraphStyle(name="SubTitleStyle", fontName="pingbold", fontSize=32,
                                              textColor=colors.HexColor(0x666666), alignment=TA_LEFT, )
        self.content_style = ParagraphStyle(name="ContentStyle", fontName="pingbold", fontSize=18, leading=25, spaceAfter=20,
                                            underlineWidth=1, alignment=TA_LEFT, )
        self.foot_style = ParagraphStyle(name="FootStyle", fontName="pingbold", fontSize=14, textColor=colors.HexColor(0xB4B4B4),
                                         leading=25, spaceAfter=20, alignment=TA_CENTER, )
        self.table_title_style = ParagraphStyle(name="TableTitleStyle", fontName="pingbold", fontSize=20, leading=25,
                                                spaceAfter=10, alignment=TA_LEFT, )
        self.sub_table_style = ParagraphStyle(name="SubTableTitleStyle", fontName="pingbold", fontSize=16, leading=25,
                                                spaceAfter=10, alignment=TA_LEFT, )
        self.basic_style = TableStyle([('FONTNAME', (0, 0), (-1, -1), 'pingbold'),
                                       ('FONTSIZE', (0, 0), (-1, -1), 12),
                                       ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                       ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                       ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                                       # 'SPAN' (列,行)坐标
                                       ('SPAN', (1, 0), (3, 0)),
                                       ('SPAN', (1, 1), (3, 1)),
                                       ('SPAN', (1, 2), (3, 2)),
                                       ('SPAN', (1, 5), (3, 5)),
                                       ('SPAN', (1, 6), (3, 6)),
                                       ('SPAN', (1, 7), (3, 7)),
                                       ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                       ])
        self.common_style = TableStyle([('FONTNAME', (0, 0), (-1, -1), 'pingbold'),
                                      ('FONTSIZE', (0, 0), (-1, -1), 12),
                                      ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                      ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                      ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                                      ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                     ])
        
    def genTaskPDF(self,pcb_data):
        self.pcb_data=pcb_data
        # self.filename = self.pcb_data[0]['report_code']#编号
        self.filename = str(self.pcb_data[2][1])#二维码数据
        
        story = []
        # 首页内容
        story.append(Spacer(1, 20 * mm))
        img = Image('sr.png')
        # img.drawHeight = 20 * mm
        # img.drawWidth = 40 * mm
        img.hAlign = TA_LEFT
        story.append(img)
        story.append(Spacer(1, 10 * mm))
        story.append(Paragraph("测试报告", self.title_style))
        story.append(Spacer(1, 20 * mm))
        story.append(Paragraph("Test Report of PCB", self.sub_title_style))
        story.append(Spacer(1, 45 * mm))
        story.append(Paragraph("报告编号：" + self.pcb_data[0]['report_code'], self.content_style))
        story.append(Paragraph("测试名称：" + self.pcb_data[0]['task_name'], self.content_style))
        story.append(Paragraph("报告日期：" + self.pcb_data[0]['report_date'], self.content_style))
        story.append(Paragraph(" 测试人：" + self.pcb_data[0]['report_creator'], self.content_style))
        story.append(Spacer(1, 55 * mm))
        story.append(Paragraph("内部文档，请勿外传", self.foot_style))
        story.append(PageBreak())

        # 表格允许单元格内容自动换行格式设置
        stylesheet = getSampleStyleSheet()
        body_style = stylesheet["BodyText"]
        body_style.wordWrap = 'CJK'
        body_style.fontName = 'pingbold'
        body_style.fontSize = 12

        # PCB测试数据
        story.append(Paragraph("PCB测试数据", self.table_title_style))
        story.append(Spacer(1, 3 * mm))
        task_table = Table(self.pcb_data[1:], colWidths=[40 * mm, 141 * mm], rowHeights=12 * mm, style=self.common_style)
        story.append(task_table)

        story.append(Spacer(1, 10 * mm))
        doc = SimpleDocTemplate(self.file_path + self.filename + ".pdf",
                                leftMargin=20 * mm, rightMargin=20 * mm, topMargin=20 * mm, bottomMargin=20 * mm)
        doc.build(story)
        print('已经生成PDF，文件名为 %s.pdf，请查看！' % self.pcb_data[0]['report_code'])
        
"""GUI界面的类"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class SrTestGUI:
    #调用了pcb_data全局变量
    #调用了串口实例获得状态信息
    #调用了PDF实例执行生成PDF的操作
    def __init__(self):
        #加载窗口
        self.top = tk.Tk()
        self.top.title('SR测试工具')
        screenwidth = self.top.winfo_screenwidth()
        screenheight = self.top.winfo_screenheight()
        alignstr = '%dx%d' % (screenwidth/4,screenheight/4) 
        self.top.geometry(alignstr)
        self.top.resizable(width=True,height=True)
        
        #加载label 1
        self.label1_var = tk.StringVar()
        self.label1_bg = tk.StringVar()
        self.label1_bg = 'blue'
        self.label1_var.set('扫描枪状态')
        self.label1 = ttk.Label(self.top,textvariable=self.label1_var,background=self.label1_bg)
        self.label1.grid(row=0,column=0,sticky = tk.W+tk.E)

        #加载label 2
        self.label2_var = tk.StringVar()
        self.label2_bg = tk.StringVar()
        self.label2_bg = 'grey'
        self.label2_var.set('未连接')
        self.label2 = ttk.Label(self.top,textvariable=self.label2_var,background=self.label2_bg)
        self.label2.grid(row=0,column=1,sticky = tk.W+tk.E)
        
        #加载label 3
        self.label3_var = tk.StringVar()
        self.label3_bg = tk.StringVar()
        self.label3_bg = 'blue'
        self.label3_var.set("PCB版本")
        self.label3 = ttk.Label(self.top,textvariable=self.label3_var,background=self.label3_bg)
        self.label3.grid(row=1,column=0,sticky = tk.W+tk.E)
        
        #加载label 4
        self.label4_var = tk.StringVar()
        self.label4_bg = tk.StringVar()
        self.label4_bg = 'grey'
        self.label4_var.set("none")
        self.label4 = ttk.Label(self.top,textvariable=self.label4_var,background=self.label4_bg)
        self.label4.grid(row=1,column=1,sticky = tk.W+tk.E)
        
        #加载label 5
        self.label5_var = tk.StringVar()
        self.label5_bg = tk.StringVar()
        self.label5_bg = 'blue'
        self.label5_var.set("是否合格")
        self.label5 = ttk.Label(self.top,textvariable=self.label5_var,background=self.label5_bg)
        self.label5.grid(row=2,column=0,sticky = tk.W+tk.E)
        
        #加载label 6
        self.label6_var = tk.StringVar()
        self.label6_bg = tk.StringVar()
        self.label6_bg = 'grey'
        self.label6_var.set("未知")
        self.label6 = ttk.Label(self.top,textvariable=self.label6_var,background=self.label6_bg)
        self.label6.grid(row=2,column=1,sticky = tk.W+tk.E)
        
        #加载label 7
        self.label7_var = tk.StringVar()
        self.label7_bg = tk.StringVar()
        self.label7_bg = 'blue'
        self.label7_var.set("固件版本")
        self.label7 = ttk.Label(self.top,textvariable=self.label7_var,background=self.label7_bg)
        self.label7.grid(row=3,column=0,sticky = tk.W+tk.E)
        
        #加载label 8
        self.label8_var = tk.StringVar()
        self.label8_bg = tk.StringVar()
        self.label8_bg = 'grey'
        self.label8_var.set("none")
        self.label8 = ttk.Label(self.top,textvariable=self.label8_var,background=self.label8_bg)
        self.label8.grid(row=3,column=1,sticky = tk.W+tk.E)
        
        #加载label 9
        self.label9_var = tk.StringVar()
        self.label9_bg = tk.StringVar()
        self.label9_bg = 'blue'
        self.label9_var.set("检测人员")
        self.label9 = ttk.Label(self.top,textvariable=self.label9_var,background=self.label9_bg)
        self.label9.grid(row=4,column=0,sticky = tk.W+tk.E)
        
        #加载label 10
        self.label10_var = tk.StringVar()
        self.label10_bg = tk.StringVar()
        self.label10_bg = 'grey'
        self.label10_var.set("SRUser")
        self.label10 = ttk.Label(self.top,textvariable=self.label10_var,background=self.label10_bg)
        self.label10.grid(row=4,column=1,sticky = tk.W+tk.E)
        
        #加载label 11
        self.label11_var = tk.StringVar()
        self.label11_bg = tk.StringVar()
        self.label11_bg = 'yellow'
        self.label11_var.set("请连接扫码枪！")
        self.label11 = ttk.Label(self.top,textvariable=self.label11_var,background=self.label11_bg)
        self.label11.grid(row=5,column=0,columnspan=100,sticky = tk.W+tk.E)
        
        #加载button 1
        button1 = tk.Button(self.top,text='生成PDF并写入数据库', command = self.button1_func)
        button1.grid(row=6,column=0,columnspan=100,sticky = tk.W+tk.E)        
        self.refresh_data()

    def button1_func(self):
        #按下button1的响应函数
        # self.label11["text"] = '已生成PDF，请查看！'#直接赋值方式不推荐
        global pcb_data #使用全局变量，按下按钮时获取的pcb_data是最新的数据
        global test_pdf
        self.label11_var.set('已生成PDF，请查看！')
        self.label11["background"] = 'red'
        test_pdf.genTaskPDF(pcb_data)
        write_database(pcb_data)
        
    def refresh_data(self):
        global pcb_data
        global readpcbdata #使用全局变量调用串口实例
        #扫描枪状态
        if readpcbdata.connect_flag == True:
            self.label2_var.set("已连接")
            self.label11_var.set("请扫描PCB二维码")
            self.label2["background"] = 'red'
        else:
            self.label2_var.set("未连接")
            self.label2["background"] = 'grey'
        #PCB版本
        if pcb_data[2][1] != 'none':
            self.label11_var.set("收到PCB二维码数据！")
            self.label4_var.set(pcb_data[2][1])
            self.label4["background"] = 'red'
        else:
            self.label4_var.set("none")
            self.label4["background"] = 'grey'
        self.top.after(500,self.refresh_data)

    
"""串口的类"""
import serial 
import serial.tools.list_ports
 
class ReadPcbData:
    def __init__(self):
        self.connect_flag = True
        self.hd_flag = [0,0]#硬件连接标志位
        print("init the ReadPcbData")
        
    def waitForPcbData(self): 
        #调用函数即可，循环接收一行数据
        # while True:
        data=[0,0]
        if (self.is_connected()):#判断端口是否硬件连接
            self.hd_flag[1] = 1
            try:#硬件连接时，接受数据
                
                self.line = self.ser.readline()                              #读取一行数据
                if len(self.line) !=0:
                    print("Rsponse : %s" % self.line.decode('utf-8'))  #串口接收到数据，然后显示
                    data[0] = True
                else:
                    data[0] = False
                    pass
                data[1] = self.line
            except: #情况一：读取数据时被硬件拔掉
                    #情况二：拔掉，重新硬件连接上后，还未软件连接
                if self.connect_uart()==False:
                    print("接受数据时串口被拔下！")
                else:
                    print("端口重连成功！")

        else:#无硬件连接，原有的软件连接关闭
            self.hd_flag[1]=0
            try:#尝试关闭软件连接
                self.ser.close()
            except:#第一次端口就未连接，则没有串口实例,会出现异常
                pass
            if (self.hd_flag[0]==1 and self.hd_flag[1]==0):#检测第一次硬件拔掉的下降沿，该字符只显示一次
                print("端口硬件未连接！软件连接已关闭！")
        self.hd_flag[0] = self.hd_flag[1]
        return data

    
    def connect_uart(self):
        plist = list(serial.tools.list_ports.comports())
        if len(plist) <= 0:#判断端口是否硬件连接
            print("没有发现端口!")
            self.connect_flag = False
        else:#已硬件连接，尝试软件连接
            plist_0 = list(plist[0])
            serialName = plist_0[0]       #先自动检测串口， 检测到可用串口，取出串口名
            print("可用端口>>>",serialName)
            try:#尝试软件连接
                self.ser = serial.Serial(serialName, 115200, timeout=1)  # timeout=1s
                print("已连接端口>>>", self.ser.name,"波特率115200")
                self.connect_flag = True
            except:#软件连接失败，原因未知，插拔重试
                print("尝试连接端口失败，请拔下重试，并且检查设置！")
                self.connect_flag = False
        return self.connect_flag
    
    def is_connected(self):#判断端口是否硬件连接
        return len(list(serial.tools.list_ports.comports()))

"""数据库写入函数"""
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
        
def runuart():
    global pcb_data
    global readpcbdata
    global thread_destroy_flag
    while thread_destroy_flag:
        recevied_data = readpcbdata.waitForPcbData()
        if recevied_data[0] is True:
            pcb_data[2][1] = recevied_data[1]
"""主函数"""
if __name__ == "__main__":
    import threading
    thread_destroy_flag = True
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
    test_pdf = PDFGenerator()#生成PDF实例，规定PDF格式
    readpcbdata = ReadPcbData()#生成串口实例
    readpcbdata.connect_uart()
    srgui = SrTestGUI()#生成GUI实例，规定样式
    
    t2 = threading.Thread(target=runuart)
    t2.start()
    def on_closing():
        global thread_destroy_flag
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            thread_destroy_flag = False
            srgui.top.destroy()

    srgui.top.protocol("WM_DELETE_WINDOW", on_closing)
    srgui.top.mainloop()
    
        
