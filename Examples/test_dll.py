# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 14:39:35 2020

@author: SZC
"""
# import clr

# printdll=clr.AddReference('SDK.NET.Interface')#FindAssembly也可以
# print(printdll)
# from NiceLabel.SDK import *
# sdkFilesPath = 'C:\\Program Files\\NiceLabel\\NiceLabel 2019\\bin.net'
# PrintEngineFactory.SDKFilesPath = sdkFilesPath
# PrintEngineFactory.PrintEngine.Initialize()
# label = PrintEngineFactory.PrintEngine.OpenLabel("SimpleSample1.nlbl")
# print(label)
# label.Variables["Name"].SetValue("SZC")
# label.Variables["Company"].SetValue("SZC")
# label.Variables["Title"].SetValue("SZC")
# label.Variables["Email"].SetValue("SZC")
# label.Variables["Phone"].SetValue("SZC")
# label.Print(1)


import ctypes

Objdll = ctypes.windll.LoadLibrary("Winpplb")  
Objdll = ctypes.WinDLL("Winpplb")   
Objdll.B_Get_DLL_Version(1)


st = r"\\?\USB#VID_1664&PID_08F0#90621E801655#{a5dcbf10-6530-11d2-901f-00c04fb951ed}"
res = Objdll.B_CreatePrn(12,st)
print(res)
# lenofbuf = Objdll.B_GetUSBBufferLen()+1
# print(lenofbuf)
# pbuf = ctypes.c_char_p()
# aa = Objdll.B_EnumUSB(pbuf)
# print(aa)
# buf1 = ctypes.c_char_p()
# len1 = ctypes.c_int(20)
# buf2 = ctypes.c_char_p()
# len2 = ctypes.c_int(77)
# aaa = Objdll.B_GetUSBDeviceInfo(1, buf1, ctypes.byref(len1), buf2, ctypes.byref(len2))
# print(aaa)
