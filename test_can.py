# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:51:24 2020

@author: SZC
"""  
import PCANBasic
from PCANBasic import *

class DriveCAN(PCANBasic):
    
    def can_init(self):
        # The Plug & Play Channel (PCAN-PCI) is initialized
        result = self.Initialize(PCAN_USBBUS1, PCAN_BAUD_500K)
        if result != PCAN_ERROR_OK:
            # An error occurred, get a text describing the error and show it
            result = self.GetErrorText(result)
            print(result[1])
        else:
            print ("PCAN-USB (Ch-1) was initialized")
    def can_read(self):
         # All initialized channels are released
        readResult = PCAN_ERROR_OK,
        while (readResult[0] & PCAN_ERROR_QRCVEMPTY) != PCAN_ERROR_QRCVEMPTY:
            # Check the receive queue for new messages
            readResult = objPCAN.Read(PCAN_USBBUS1)
            if readResult[0] != PCAN_ERROR_QRCVEMPTY:
                # Process the received message
                print("A message was received")
                print("[%x %x %x %x %x %x %x %x]" 
                      % (readResult[1].DATA[0], 
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
                print(result[1])
                # HandleReadError(readResult[0]) # Possible errors handling function, HandleError(function_result)
                
if __name__ == "__main__":
    objPCAN = DriveCAN()
    objPCAN.can_init()
    objPCAN.can_read()
    
   
