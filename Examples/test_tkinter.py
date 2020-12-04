# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:02:22 2020

@author: SZC
"""
import tkinter as tk
from tkinter import ttk

class SrTestGUI:
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
        self.label1.grid(row=0,column=0)

        #加载label 2
        self.label2_var = tk.StringVar()
        self.label2_bg = tk.StringVar()
        self.label2_bg = 'grey'
        self.label2_var.set('已连接')
        self.label2 = ttk.Label(self.top,textvariable=self.label2_var,background=self.label2_bg)
        self.label2.grid(row=0,column=1)
        
        #加载label 3
        self.label3_var = tk.StringVar()
        self.label3_bg = tk.StringVar()
        self.label3_bg = 'blue'
        self.label3_var.set("PCB版本")
        self.label3 = ttk.Label(self.top,textvariable=self.label3_var,background=self.label3_bg)
        self.label3.grid(row=1,column=0)
        
        #加载label 4
        self.label4_var = tk.StringVar()
        self.label4_bg = tk.StringVar()
        self.label4_bg = 'grey'
        self.label4_var.set("V0.1")
        self.label4 = ttk.Label(self.top,textvariable=self.label4_var,background=self.label4_bg)
        self.label4.grid(row=1,column=1)
        
        #加载label 5
        self.label5_var = tk.StringVar()
        self.label5_bg = tk.StringVar()
        self.label5_bg = 'blue'
        self.label5_var.set("是否合格")
        self.label5 = ttk.Label(self.top,textvariable=self.label5_var,background=self.label5_bg)
        self.label5.grid(row=2,column=0)
        
        #加载label 6
        self.label6_var = tk.StringVar()
        self.label6_bg = tk.StringVar()
        self.label6_bg = 'grey'
        self.label6_var.set("是")
        self.label6 = ttk.Label(self.top,textvariable=self.label6_var,background=self.label6_bg)
        self.label6.grid(row=2,column=1)
        
        #加载label 7
        self.label7_var = tk.StringVar()
        self.label7_bg = tk.StringVar()
        self.label7_bg = 'blue'
        self.label7_var.set("固件版本")
        self.label7 = ttk.Label(self.top,textvariable=self.label7_var,background=self.label7_bg)
        self.label7.grid(row=3,column=0)
        
        #加载label 8
        self.label8_var = tk.StringVar()
        self.label8_bg = tk.StringVar()
        self.label8_bg = 'grey'
        self.label8_var.set("V1.1.0")
        self.label8 = ttk.Label(self.top,textvariable=self.label8_var,background=self.label8_bg)
        self.label8.grid(row=3,column=1)
        
        #加载label 9
        self.label9_var = tk.StringVar()
        self.label9_bg = tk.StringVar()
        self.label9_bg = 'blue'
        self.label9_var.set("检测人员")
        self.label9 = ttk.Label(self.top,textvariable=self.label9_var,background=self.label9_bg)
        self.label9.grid(row=4,column=0)
        
        #加载label 10
        self.label10_var = tk.StringVar()
        self.label10_bg = tk.StringVar()
        self.label10_bg = 'grey'
        self.label10_var.set("SRUser")
        self.label10 = ttk.Label(self.top,textvariable=self.label10_var,background=self.label10_bg)
        self.label10.grid(row=4,column=1)
        
        #加载label 11
        self.label11_var = tk.StringVar()
        self.label11_bg = tk.StringVar()
        self.label11_bg = 'grey'
        self.label11_var.set("请连接扫码枪！")
        self.label11 = ttk.Label(self.top,textvariable=self.label11_var,background=self.label11_bg)
        self.label11.grid(row=1,column=2)
        
        #加载button 1
        button1 = tk.Button(self.top,text='测试按钮',font=('Arial', 12), width=10, height=1, command=self.button1_func)
        button1.grid(row=2,column=2)
        self.refresh_data()
        #运行界面
        self.top.mainloop()

    def button1_func(self):
        #按下button1的响应函数
        # self.label1_var.set('测试成功')
        self.label10["text"] = 'hhhhhhh'
        self.label10["background"] = 'red'
    def refresh_data(self):
        print("测试刷新中")
        self.label2_var.set("测试刷新")
        self.label2["background"] = 'red'
        self.top.after(1000,self.refresh_data)

Sr=SrTestGUI()

