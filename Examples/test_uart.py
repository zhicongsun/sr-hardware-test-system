# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:44:41 2020

@author: SZC
"""

import serial 
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
class ReadPcbData:
    def __init__(self):
        self.connect_flag = True
        print("init the ReadPcbData")
        
    def waitForPcbData(self): 
        #调用函数即可，循环接收一行数据
        flag = [0,0]#硬件连接标志位
        while True:
            if (self.is_connected()):#判断端口是否硬件连接
                flag[1] = 1
                try:#硬件连接时，接受数据
                    
                    line = self.ser.readline()                              #读取一行数据
                    if len(line) !=0:
                        print("Rsponse : %s" % line.decode('utf-8'))  #串口接收到数据，然后显示
                    else:
                         pass
                except: #情况一：读取数据时被硬件拔掉
                        #情况二：拔掉，重新硬件连接上后，还未软件连接
                    if self.connect_uart()==False:
                        print("接受数据时串口被拔下！")
                    else:
                        print("端口重连成功！")

            else:#无硬件连接，原有的软件连接关闭
                flag[1]=0
                try:#尝试关闭软件连接
                    self.ser.close()
                except:#第一次端口就未连接，则没有串口实例,会出现异常
                    pass
                if (flag[0]==1 and flag[1]==0):#检测第一次硬件拔掉的下降沿，该字符只显示一次
                    print("端口硬件未连接！软件连接已关闭！")
            flag[0] = flag[1]
            print(self.connect_flag)

    
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
    
    test_uart = ReadPcbData()
    test_uart.connect_uart()
    test_uart.waitForPcbData()

