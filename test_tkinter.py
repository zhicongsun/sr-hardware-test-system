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
        alignstr = '%dx%d' % (screenwidth,screenheight) 
        self.top.geometry(alignstr)
        self.top.resizable(width=True,height=True)
        
        #加载label 1
        self.label1_var = tk.StringVar()
        self.label1_bg = tk.StringVar()
        self.label1_bg = 'blue'
        self.label1_var.set('等待扫描PCB')
        self.label1 = ttk.Label(self.top,textvariable=self.label1_var,background=self.label1_bg)
        self.label1.pack()

        #加载label 2
        self.label2_var = tk.StringVar()
        self.label2_bg = tk.StringVar()
        self.label2_bg = 'blue'
        self.label2_var.set('等待烧录固件')
        self.label2 = ttk.Label(self.top,textvariable=self.label2_var,background=self.label2_bg)
        self.label2.pack()
        
        #加载button 1
        button2 = tk.Button(self.top,text='启动测试',font=('Arial', 12), width=10, height=1)
        button2.pack()
        
        #加载button 1
        button1 = tk.Button(self.top,text='测试按钮',font=('Arial', 12), width=10, height=1, command=self.button1_func)
        button1.pack()
        
        #运行界面
        self.top.mainloop()

    def button1_func(self):
        #按下button1的响应函数
        # self.label1_var.set('测试成功')
        self.label1["text"] = 'PCB版本为V1.0'
        self.label1["background"] = 'red'

Sr=SrTestGUI()

