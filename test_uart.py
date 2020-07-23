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
 
# def waitForPcbData(self): 
#     #非循环模式，只读取一行数据，需要在循环中调用该函数
#     flag=[0,0]
#     self.line = self.ser.readline()#读取一行数据
#     if len(self.line) !=0:#有数据则输出
#         print("Rsponse : %s" % self.line.decode('utf-8'))  #串口接收到数据，然后显示
#         flag[0] = True
#     else:
#         flag[0] = False
#         pass
#     flag[1]=self.line
#     return flag
def waitForPcbData(): 
    #调用函数即可，循环接收一行数据
    while True:
        line = ser.readline()                              #读取一行数据
        if len(line) !=0:
            print("Rsponse : %s" % line.decode('utf-8'))  #串口接收到数据，然后显示
        else:
            pass
 
# def sendAT_Cmd(serInstance, atCmdStr, waitforOk):
#    # print("Command: %s" % atCmdStr)
#     serInstance.write(atCmdStr.encode('utf-8'))   # atCmdStr 波特率
#     # or define b'string',bytes should be used not str
 
#     if (waitforOk == 1):
#         waitForCmdOKRsp()
#     else:
#         waitForCmdRsp()

"""主函数"""
if __name__ == "__main__":
    plist = list(serial.tools.list_ports.comports())
    
    if len(plist) <= 0:
        print("没有发现端口!")
    else:
        plist_0 = list(plist[0])
        serialName = plist_0[0]       #先自动检测串口， 检测到可用串口，取出串口名
        print("可用端口>>>",serialName)
     
    try:
        ser = serial.Serial(serialName, 115200, timeout=1)  # timeout=1s
        print("已连接端口>>>", ser.name,"波特率115200")
    except:
        print("串口连接失败，请拔下串口重试，并且检查设置！")
    waitForPcbData()
    ser.close()
    print("串口已断开连接")
