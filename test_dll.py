# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 14:39:35 2020

@author: SZC
"""
import clr

printdll=clr.AddReference('SDK.NET.Interface')
print(printdll)
from NiceLabel.SDK import *
sdkFilesPath = 'C:\\Program Files\\NiceLabel\\NiceLabel 2019\\bin.net'
PrintEngineFactory.SDKFilesPath = sdkFilesPath
PrintEngineFactory.PrintEngine.Initialize()
label = PrintEngineFactory.PrintEngine.OpenLabel("SimpleSample1.lbl")
print(label)
label.Variables["Name"].SetValue("SZC")
label.Variables["Company"].SetValue("SZC")
label.Variables["Title"].SetValue("SZC")
label.Variables["Email"].SetValue("SZC")
label.Variables["Phone"].SetValue("SZC")
label.Print(1)
