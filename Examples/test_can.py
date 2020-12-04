# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:51:24 2020

@author: SZC
"""  
import PCANBasic
from PCANBasic import *

class DriveCAN(PCANBasic):
    def can_init(self,chanel=PCAN_USBBUS1,bautrate=PCAN_BAUD_500K): #默认参数：通道、波特率
        # The Plug & Play Channel (PCAN-PCI) is initialized
        result = self.Initialize(chanel, bautrate)
        if result != PCAN_ERROR_OK:
            # An error occurred, get a text describing the error and show it
            result = self.GetErrorText(result)
            print(result[1])
        else:
            print ("PCAN-USB (Ch-1) was initialized")

    def can_filter(self,chanel=PCAN_USBBUS1,from_id=0,to_id=0x7FF,fileter_mode=PCAN_MODE_STANDARD): #默认参数：通道，起始id，结束id，滤波器模式（标准）
        #  The message filter is closed first to ensure the reception of the new range of IDs.
        result = self.SetValue(PCAN_USBBUS1,PCAN_MESSAGE_FILTER,PCAN_FILTER_CLOSE)
        if result != PCAN_ERROR_OK:
            # An error occurred, get a text describing the error and show it
            result = self.GetErrorText(result)
            print(result[1])
        else:
            # The message filter is configured to receive the IDs 2,3,4 and 5 on the PCAN-USB, Channel 1
            result = self.FilterMessages(chanel,from_id,to_id,fileter_mode)
            if result != PCAN_ERROR_OK:
                # An error occurred, get a text describing the error and show it
                result = objPCAN.GetErrorText(result)
                print(result[1])
            else:
                print("Filter successfully configured for IDs from %d to %d" % (from_id,to_id))

    def can_read(self,chanel=PCAN_USBBUS1): #默认参数：通道
         # All initialized channels are released
        readResult = PCAN_ERROR_OK,
        while (readResult[0] & PCAN_ERROR_QRCVEMPTY) != PCAN_ERROR_QRCVEMPTY:
            # Check the receive queue for new messages
            readResult = self.Read(chanel)
            if readResult[0] != PCAN_ERROR_QRCVEMPTY:
                # Process the received message 
                print("id = %x data=[%x %x %x %x %x %x %x %x]" 
                      % (readResult[1].ID,
                          readResult[1].DATA[0], 
                          readResult[1].DATA[1], 
                          readResult[1].DATA[2],
                          readResult[1].DATA[3],
                          readResult[1].DATA[4],
                          readResult[1].DATA[5],
                          readResult[1].DATA[6],
                          readResult[1].DATA[7]))                             
                can_read_callback(readResult[1])
            else:
                # An error occurred, get a text describing the error and show it
                result = objPCAN.GetErrorText(readResult[0])
                # print(result[1])
                # HandleReadError(readResult[0]) # Possible errors handling function, HandleError(function_result)

    def can_write(self, #所有参数可设置，不设置的时候有默认的
        chanel=PCAN_USBBUS1,
        msg_type=PCAN_MESSAGE_STANDARD,
        frame_id=0x100,
        send_data=[1,2,3,4]): #默认参数：通道，帧类型（标准），帧id，发送数据（列表）

        can_write_flag = "None"
        msg = TPCANMsg()
        msg.ID = frame_id
        msg.MSGTYPE = PCAN_MESSAGE_STANDARD
        msg.LEN = len(send_data)
        for i in range(0,msg.LEN): #从0到len-1,如果发送数据有5位，则是0到4
            msg.DATA[i] = send_data[i]
        
        #  The message is sent using the PCAN-USB Channel 1
        result = self.Write(chanel,msg)
        if result != PCAN_ERROR_OK:
            # An error occurred, get a text describing the error and show it
            result = self.GetErrorText(result)
            print(result)
            can_write_flag = "False"
        else:
            print("Message sent successfully")
            can_write_flag = "True"
        return can_write_flag

def runcan():
    global objPCAN
    global can_thread_destroy_flag
    while can_thread_destroy_flag:
        objPCAN.can_read()
    try:
        objPCAN.Uninitialize(PCAN_NONEBUS)
    except:
        print("已经关闭can口，不用重新关闭")


if __name__ == "__main__":
    can_thread_destroy_flag = True
    objPCAN = DriveCAN()
    objPCAN.can_init()
    objPCAN.can_filter()
    runcan()
    
##############################################################################################################
#       测试系统通信协议的一些宏定义
##############################################################################################################
#CAN帧的不同ID
SR_UART_BEGIN_FRAME = 0xC1
SR_UART_BEGIN_ACK_FRAME = 0xC2
SR_UART_END_FRAME = 0xC3
SR_UART_END_ACK_FRAME = 0xC4
SR_UART_MEG_FRAME = 0xC5
SR_CAN_BEGIN_FRAME = 0xC6
SR_CAN_BEGIN_ACK_FRAME = 0xC7
SR_CAN_END_FRAME = 0xC8
SR_CAN_END_ACK_FRAME = 0xC9
SR_CAN_MEG_FRAME = 0xCA
#波特率，UART和CAN通用
SR_BAUTRATE_50K_9600 = 0xB1
SR_BAUTRATE_100K_115200 = 0xB2
#外设的状态
SR_STATE_OK = 0xA1
SR_STATE_OFF = 0xA2
#默认的帧DATA
SR_DEFAULT_DATA = 0xFF

##############################################################################################################
#       主程序中用，全局访问的event
##############################################################################################################
import threading
uart_begin_event = threading.Event()
uart_end_event = threading.Event()
can_begin_event = threading.Event()
can_end_event = threading.Event()


##############################################################################################################
#       can接受数据后的回调函数，进行一系列置位操作，线程同步
##############################################################################################################
def can_read_callback(msg):
    global uart_ack_msg
    global can_ack_msg
    if msg.ID == SR_UART_BEGIN_ACK_FRAME:
        uart_begin_event.set() #收到UART开始帧ACK，置位，test_uart_task清位后等待UART测试结束
    if msg.ID == SR_UART_END_ACK_FRAME:
        uart_ack_msg = msg.copy() #收到结束帧的数据拷贝到贡献变量uart_ack_msg
        uart_end_event.set() #置位，test_uart_task清位后进行数据处理
    if msg.ID == SR_CAN_BEGIN_ACK_FRAME:
        can_begin_event.set()
    if msg.ID == SR_CAN_MEG_FRAME:

    if msg.ID == SR_CAN_END_ACK_FRAME:
        can_ack_msg = msg.copy()
        can_end_event.set()

##############################################################################################################
#       uart接受END ACK后的处理函数，将数据写入pcb_data，被task调用
##############################################################################################################
def test_uart_end_ack_process():
    global pcb_data
    global uart_ack_msg
    if uart_ack_msg.DATA[0] == SR_BAUTRATE_100K_115200:
        pcb_data[10][1] = uart_ack_msg.DATA[2] #丢包率
        pcb_data[11][1] = uart_ack_msg.DATA[3] #误码率
        pcb_data[12][1] = uart_ack_msg.DATA[4] #传输延时s
    elif uart_ack_msg.DATA[0] == SR_BAUTRATE_50K_9600:
        pass

##############################################################################################################
#       can接受END ACK后的处理函数，将数据写入pcb_data，被task调用
##############################################################################################################
def test_can_end_ack_process():
    global pcb_data
    global can_ack_msg
    if can_ack_msg.DATA[0] == SR_BAUTRATE_50K_9600:
        pcb_data[13][1] = uart_ack_msg.DATA[2] #丢包率
        pcb_data[14][1] = uart_ack_msg.DATA[3] #误码率
    elif can_ack_msg.DATA[0] == SR_BAUTRATE_100K_115200:
        pass

##############################################################################################################
#       uart通信任务，指定测试的波特率，被test_task()调用
##############################################################################################################
def test_uart_task(test_bautrate):
    SR_UART_BEGIN_CMD = [test_bautrate,#每次调用该函数，只改变波特率参数
                            SR_STATE_OK,
                            SR_DEFAULT_DATA,
                            SR_DEFAULT_DATA,
                            SR_DEFAULT_DATA,
                            SR_DEFAULT_DATA,
                            SR_DEFAULT_DATA,
                            SR_DEFAULT_DATA]
    re = can_write(PCAN_USBBUS1,PCAN_MESSAGE_STANDARD,SR_UART_BEGIN_FRAME,SR_UART_BEGIN_CMD)
    if re == "False":
        print("发送UART开始帧失败，请检查原因")
    else:
        print("发送UART开始帧成功，等待ACK")
        uart_begin_event.wait(timeout=10)
        if uart_begin_event.isSet() != True:
            print("未收到UART开始帧的ACK，CAN出问题")
        else:
            uart_begin_event.clear()
            print("收到UART开始帧ACK")
            uart_end_event.wait(timeout=120)
            if uart_end_event.isSet() !=True:
                print("未收到UART结束帧ACK")
            else:
                uart_end_event.clear()
                print("收到UART结束帧ACK")
                #处理函数
                test_uart_end_ack_process() #向pcb_data内写入数据

##############################################################################################################
#       can测试任务，指定某波特率，被总的test_task()调用
##############################################################################################################
def test_can_task(test_bautrate):
    SR_CAN_BEGIN_CMD = [test_bautrate,#每次调用该函数，只改变波特率参数
                        SR_STATE_OK,
                        SR_DEFAULT_DATA,
                        SR_DEFAULT_DATA,
                        SR_DEFAULT_DATA,
                        SR_DEFAULT_DATA,
                        SR_DEFAULT_DATA,
                        SR_DEFAULT_DATA]
    SR_CAN_END_CMD = [test_bautrate,#每次调用该函数，只改变波特率参数
                        1024,
                        SR_DEFAULT_DATA,
                        SR_DEFAULT_DATA,
                        SR_DEFAULT_DATA,
                        SR_DEFAULT_DATA,
                        SR_DEFAULT_DATA,
                        SR_DEFAULT_DATA]                    
    re = can_write(PCAN_USBBUS1,PCAN_MESSAGE_STANDARD,SR_CAN_BEGIN_FRAME,SR_CAN_BEGIN_CMD)
    if re == "False":
        print("发送CAN开始帧失败，请检查原因")
    else:
        print("发送CAN开始帧成功，等待ACK")
        can_begin_event.wait(timeout=10)
        if can_begin_event.isSet() != True:
            print("未收到CAN开始帧的ACK，CAN出问题")
        else:
            can_begin_event.clear()
            print("收到CAN开始帧ACK")
            #发送1024个can帧
            for i in range(1,1025):
                SR_CAMMSG = [test_bautrate,
                            i,  #发送的第i个帧数
                            SR_DEFAULT_DATA,
                            SR_DEFAULT_DATA,
                            SR_DEFAULT_DATA,
                            SR_DEFAULT_DATA,
                            SR_DEFAULT_DATA,
                            SR_DEFAULT_DATA]
                can_write(PCAN_USBBUS1,PCAN_MESSAGE_STANDARD,SR_CAN_MEG_FRAME,SR_CAMMSG)
            

            can_write(PCAN_USBBUS1,PCAN_MESSAGE_STANDARD,SR_CAN_END_FRAME,SR_CAN_END_CMD)
            print("发送CAN结束帧，等待ACK")
            can_end_event.wait(timeout=120)
            if can_end_event.isSet() !=True:
                print("未收到CAN结束帧ACK")
            else:
                can_end_event.clear()
                print("收到CAN结束帧ACK")
                #处理函数
                test_can_end_ack_process()

##############################################################################################################
#       测试任务，需要用线程运行
##############################################################################################################
def test_task():
    test_uart_task(SR_BAUTRATE_50K_9600)
    test_uart_task(SR_BAUTRATE_100K_115200)
    test_can_task(SR_BAUTRATE_50K_9600)
    test_can_task(SR_BAUTRATE_100K_115200)
