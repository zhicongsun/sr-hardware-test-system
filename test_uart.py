# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:44:41 2020

@author: SZC
"""

import serial
import sys
import os
import time
import re
 
import serial.tools.list_ports
 

def waitForPcbData(): 
    while True:

        line = ser.readline()                              #读取一行数据
        if len(line) !=0:
            print("Rsponse : %s" % line.decode('utf-8'))  #串口接收到数据，然后显示
        else:
            pass
 
def sendAT_Cmd(serInstance, atCmdStr, waitforOk):
   # print("Command: %s" % atCmdStr)
    serInstance.write(atCmdStr.encode('utf-8'))   # atCmdStr 波特率
    # or define b'string',bytes should be used not str
 
    if (waitforOk == 1):
        waitForCmdOKRsp()
    else:
        waitForCmdRsp()
 

plist = list(serial.tools.list_ports.comports())
 
if len(plist) <= 0:
    print("没有发现端口!")
else:
    plist_0 = list(plist[0])
    serialName = plist_0[0]       #先自动检测串口， 检测到可用串口，取出串口名
    print("可用端口>>>",serialName)
 
ser = serial.Serial(serialName, 115200, timeout=1)  # timeout=1s
print("已连接端口>>>", ser.name,"波特率115200")
waitForPcbData()
ser.close()
