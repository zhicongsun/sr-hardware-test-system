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
                # print("A message was received")
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
                # ProcessMessage(result[1],result[2]) # Possible processing function, ProcessMessage(msg,timestamp)
            else:
                # An error occurred, get a text describing the error and show it
                result = objPCAN.GetErrorText(readResult[0])
                # print(result[1])
                # HandleReadError(readResult[0]) # Possible errors handling function, HandleError(function_result)

    def can_write(self,chanel=PCAN_USBBUS1,msg_type=PCAN_MESSAGE_STANDARD,frame_id=0x100,send_data=[1,2,3,4]): #默认参数：通道，帧类型（标准），帧id，发送数据（列表）
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
        else:
            print("Message sent successfully")
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
    # objPCAN.can_read()
    # objPCAN.can_write()
    
   
