# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:07:58 2020

@author: SZC
"""
"""GUI界面的类"""
import tkinter as tk
from tkinter import ttk

class SrTestGUI:
    def __init__(self,type):
        #加载窗口
        self.top = tk.Tk()
        self.top.title('SR测试工具')
        screenwidth = self.top.winfo_screenwidth()
        screenheight = self.top.winfo_screenheight()
        alignstr = '%dx%d' % (screenwidth,screenheight) 
        self.top.geometry(alignstr)
        self.top.resizable(width=True,height=True)
        
        #加载label 1
        self.label1_var = tk.StringVar()
        self.label1_bg = tk.StringVar()
        self.label1_bg = 'blue'
        self.label1_var.set('等待测试')
        self.label1 = ttk.Label(self.top,textvariable=self.label1_var,background=self.label1_bg)
        self.label1.pack()

        #加载button 1
        button1 = tk.Button(self.top,text='测试按钮',font=('Arial', 12), width=10, height=1, command=self.button1_func)
        button1.pack()
        
        #运行界面
        # readpcbdata = ReadPcbData()#开始读PCB信息
        # readpcbdata.waitForPcbData()
        # self.top.mainloop()
        

    def button1_func(self,type):
        #按下button1的响应函数
        # self.label1_var.set('测试成功')
        self.label1["text"] = '测试成功'
        self.label1["background"] = 'red'
        type.genTaskPDF()


"""生成PDF的类"""
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('pingbold', 'msyh.ttf'))
#pdfmetrics.registerFont(TTFont('ping', 'ping.ttf'))
#pdfmetrics.registerFont(TTFont('hv', 'Helvetica.ttf'))

# 生成PDF文件
class PDFGenerator:
    def __init__(self, filename):
        self.filename = filename
        # self.file_path = '/xxx/xxx/xxx/xxx/'
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

#    def genTaskPDF(self, home_data, task_data, basic_data, case_set_data, fail_case_data, p0_case_data):
#        story = []
    def genTaskPDF(self, home_data,task_data,basic_data):
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
        story.append(Paragraph("Test Report of XXX", self.sub_title_style))
        story.append(Spacer(1, 45 * mm))
        story.append(Paragraph("报告编号：" + home_data['report_code'], self.content_style))
        story.append(Paragraph("计划名称：" + home_data['task_name'], self.content_style))
        story.append(Paragraph("报告日期：" + home_data['report_date'], self.content_style))
        story.append(Paragraph(" 负责人：" + home_data['report_creator'], self.content_style))
        story.append(Spacer(1, 55 * mm))
        story.append(Paragraph("内部文档，请勿外传", self.foot_style))
        story.append(PageBreak())

        # 表格允许单元格内容自动换行格式设置
        stylesheet = getSampleStyleSheet()
        body_style = stylesheet["BodyText"]
        body_style.wordWrap = 'CJK'
        body_style.fontName = 'pingbold'
        body_style.fontSize = 12

        # 测试计划
        story.append(Paragraph("测试计划", self.table_title_style))
        story.append(Spacer(1, 3 * mm))
        task_table = Table(task_data, colWidths=[25 * mm, 141 * mm], rowHeights=12 * mm, style=self.common_style)
        story.append(task_table)

        story.append(Spacer(1, 10 * mm))

        # 基础参数
        story.append(Paragraph("基础参数", self.sub_table_style))
        basic_table = Table(basic_data, colWidths=[25*mm, 61*mm, 25*mm, 55*mm], rowHeights=12 * mm, style=self.basic_style)
        story.append(basic_table)

        story.append(Spacer(1, 10 * mm))
#
#        # 测试用例集
#        story.append(Paragraph("用例集参数", self.sub_table_style))
#        case_set_table = Table(case_set_data, colWidths=[25 * mm, 141 * mm], rowHeights=12 * mm, style=self.common_style)
#        story.append(case_set_table)
#
#        # story.append(PageBreak())
#        story.append(Spacer(1, 15 * mm))
#
#        # 失败用例--使用可以自动换行的方式需要data里都是str类型的才OK
#        story.append(Paragraph("失败用例", self.table_title_style))
#        story.append(Spacer(1, 3 * mm))
#        para_fail_case_data = [[Paragraph(cell, body_style) for cell in row] for row in fail_case_data]
#        fail_case_table = Table(para_fail_case_data, colWidths=[20 * mm, 35 * mm, 91 * mm, 20 * mm])
#        fail_case_table.setStyle(self.common_style)
#        story.append(fail_case_table)
#
#        story.append(Spacer(1, 15 * mm))
#
#        # 基础用例（P0）
#        story.append(Paragraph("基础用例（P0）", self.table_title_style))
#        story.append(Spacer(1, 3 * mm))
#        para_p0_case_data = [[Paragraph(cell, body_style) for cell in row] for row in p0_case_data]
#        p0_case_table = Table(para_p0_case_data, colWidths=[20 * mm, 35 * mm, 91 * mm, 20 * mm])
#        p0_case_table.setStyle(self.common_style)
#        story.append(p0_case_table)

        doc = SimpleDocTemplate(self.file_path + self.filename + ".pdf",
                                leftMargin=20 * mm, rightMargin=20 * mm, topMargin=20 * mm, bottomMargin=20 * mm)
        doc.build(story)
        
"""串口读取的类"""
import serial
import sys
import os
import time
import re
import serial.tools.list_ports
 
class ReadPcbData:
    def __init__(self):#生成类的时候就自动连接串口
        plist = list(serial.tools.list_ports.comports())
        if len(plist) <= 0:
            print("没有发现端口!")
        else:
            plist_0 = list(plist[0])
            serialName = plist_0[0]       #先自动检测串口， 检测到可用串口，取出串口名
            print("可用端口>>>",serialName)
            self.ser = serial.Serial(serialName, 115200, timeout=1)#1s
            print("已连接端口>>>", self.ser.name,"波特率115200")
    def waitForPcbData(self): 
        while True:
            self.line = self.ser.readline()#读取一行数据
            if len(self.line) !=0:#有数据则输出
                print("Rsponse : %s" % self.line.decode('utf-8'))  #串口接收到数据，然后显示
            else:
                pass

    # def sendAT_Cmd(self,serInstance, atCmdStr, waitforOk):
    #    # print("Command: %s" % atCmdStr)
    #     serInstance.write(atCmdStr.encode('utf-8'))   # atCmdStr 波特率
    #     # or define b'string',bytes should be used not str
     
    #     if (waitforOk == 1):
    #         waitForCmdOKRsp()
    #     else:
    #         waitForCmdRsp()
    

       
"""主函数"""
if __name__ == "__main__":
    import threading
    
    home_data = {'report_code': '1', 
           'task_name':'扫描器测试',
           'report_date':'2020.7.17',
           'report_creator':'SZC'
          }
    task_data = [
                    ['计划ID','1']
                ]
    basic_data = [
                    ['测试ID','1'],
                    ['测试ID','2','测试','3']
                ]
    
    test = PDFGenerator("Szc_Work2")
    test.genTaskPDF(home_data,task_data,basic_data)
    srgui = SrTestGUI(test)#GUI初始配置
    readpcbdata = ReadPcbData()#开启串口并连接
    # def rungui():
    #     srgui.top.mainloop()
    #     while True:
    #         pass
    def runuart():
        readpcbdata.waitForPcbData()
        if len(readpcbdata.line) != 0:
            print('666')
            srgui.label1["text"] = "666"
    # t1 = threading.Thread(target=rungui)
    t2 = threading.Thread(target=runuart)
    # t1.start()
    t2.start()
    srgui.top.mainloop()
    
        
