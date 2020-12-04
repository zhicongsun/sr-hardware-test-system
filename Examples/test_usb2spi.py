# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:44:41 2020

@author: SZC
"""

from ctypes import *
import platform
from time import sleep
from usb_device import *
from usb2spi import *
from sys import *

class DriveUSB2SPI():
    def __init__(self,
        config_mode = SPI_MODE_SOFT_HDX,
        config_master = SPI_MASTER,
        config_cpol = 0,
        config_cpha = 0,
        config_lsbfirst = SPI_MSB,
        config_selpolarity = SPI_SEL_LOW,
        config_clockspeedhz = 500000):

        self.DevIndex = 0
        self.DevHandles = (c_uint * 20)()
        # 扫描设备
        self.ret = USB_ScanDevice(byref(self.DevHandles))
        if(self.ret == 0):
            print("没有SPI设备连接")
        else:
            print("有 %d SPI设备连接!" % self.ret)
            # 打开设备
            self.ret = USB_OpenDevice(self.DevHandles[self.DevIndex])
            if(bool(self.ret)==False):
                print("打开SPI设备失败")
            else:
                print("成功打开SPI设备")
                # 获取设备信息
                USB2XXXInfo = DEVICE_INFO()
                USB2XXXFunctionString = (c_char * 256)()
                self.ret = DEV_GetDeviceInfo(self.DevHandles[self.DevIndex],byref(USB2XXXInfo),byref(USB2XXXFunctionString))
                if(bool(self.ret)==False):
                    print("Get device infomation faild!")
                else:
                    print("USB2XXX device infomation:")
                    print("--Firmware Name: %s"%bytes(USB2XXXInfo.FirmwareName).decode('ascii'))
                    print("--Firmware Version: v%d.%d.%d"%((USB2XXXInfo.FirmwareVersion>>24)&0xFF,(USB2XXXInfo.FirmwareVersion>>16)&0xFF,USB2XXXInfo.FirmwareVersion&0xFFFF))
                    print("--Hardware Version: v%d.%d.%d"%((USB2XXXInfo.HardwareVersion>>24)&0xFF,(USB2XXXInfo.HardwareVersion>>16)&0xFF,USB2XXXInfo.HardwareVersion&0xFFFF))
                    print("--Build Date: %s"%bytes(USB2XXXInfo.BuildDate).decode('ascii'))
                    print("--Serial Number: ",end='')
                    for i in range(0, len(USB2XXXInfo.SerialNumber)):
                        print("%08X"%USB2XXXInfo.SerialNumber[i],end='')
                    print("")
                    print("--Function String: %s"%bytes(USB2XXXFunctionString.value).decode('ascii'))
                    
                    # 配置初始化SPI
                    SPIConfig = SPI_CONFIG()
                    SPIConfig.Mode = config_mode      # 硬件半双工模式
                    SPIConfig.Master = config_master    # 主机模式
                    SPIConfig.CPOL = config_cpol
                    SPIConfig.CPHA = config_cpha
                    SPIConfig.LSBFirst = config_lsbfirst
                    SPIConfig.SelPolarity = config_selpolarity
                    SPIConfig.ClockSpeedHz = config_clockspeedhz
                    self.ret = SPI_Init(self.DevHandles[self.DevIndex],SPI2_CS0,byref(SPIConfig))
                    if(self.ret != SPI_SUCCESS):
                        print("初始化SPI失败")
                    else:
                        print("成功初始化SPI")
    def spi_master_read(self):
        self.ReadBuffer = (c_ubyte * 16)()
        self.ret = SPI_ReadBytes(self.DevHandles[self.DevIndex],SPI2_CS0,byref(self.ReadBuffer),len(self.ReadBuffer))
        if(self.ret != SPI_SUCCESS):
            print("SPI读取数据失败")
        else:
            print("SPI 读取的数据为:")
            for i in range(0,len(self.ReadBuffer)):
                print("%02X " % self.ReadBuffer[i],end='')
            print("")

    def spi_master_write(self):
        self.WriteBuffer = (c_ubyte * 16)()
        for i in range(0,len(self.WriteBuffer)):
            self.WriteBuffer[i] = i
        self.ret = SPI_WriteBytes(self.DevHandles[self.DevIndex],SPI2_CS0,byref(self.WriteBuffer),len(self.WriteBuffer))
        if(self.ret != SPI_SUCCESS):
            print("SPI发送数据失败")
        else:
            print("SPI发送数据成功")

    def spi_master_write_and_read(self):
        self.ret = SPI_WriteReadBytes(self.DevHandles[self.DevIndex],SPI2_CS0,byref(self.WriteBuffer),len(self.WriteBuffer),byref(self.ReadBuffer),len(self.ReadBuffer),10)
        if(self.ret != SPI_SUCCESS):
            print("SPI 写读数据失败")
        else:
            print("SPI 写读的数据为:")
            for i in range(0,len(self.ReadBuffer)):
                print("%02X " % self.ReadBuffer[i],end='')
            print("")
    
    def spi_close(self):
        self.ret = USB_CloseDevice(self.DevHandles[self.DevIndex])
        DLL_FreeLib()#释放dll资源
        if(bool(self.ret)):
            print("成功关闭SPI设备")
        else:
            print("无法关闭SPI设备")

if __name__ == '__main__': 
    objSPI = DriveUSB2SPI()
    objSPI.spi_master_write()
    objSPI.spi_master_read()
    objSPI.spi_master_write_and_read()
    objSPI.spi_close()
