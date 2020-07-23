# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:54:06 2020

@author: Wenfei
"""


class testglobal:
    def __init__(self):#生成类的时候就自动连接串口
        print("生成")
        
    def changeglobal(self):
        global i
        i="changed"
        
"""主函数"""
if __name__ == "__main__":
    i = "unchanged"
    print(i)
    test = testglobal()
    test.changeglobal()
    print(i)