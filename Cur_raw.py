#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# tyjiao @ 2020-12-20 23:31:47

import serial
import binascii  
import struct 
import datetime
import time
import ctypes
import matplotlib.pyplot as plt
import numpy as np

# input('press ENTER to start')

# 格式转换
def hex2float(h):
    i = int(h,16)
    cp = ctypes.pointer(ctypes.c_int(i))
    fp = ctypes.cast(cp,ctypes.POINTER(ctypes.c_float))
    return fp.contents.value

# 创建serial实例
serialport = serial.Serial()
serialport.port = '/dev/cu.usbserial-AK06YINR'
serialport.baudrate = 9600
serialport.parity = 'N'
serialport.bytesize = 8
serialport.stopbits = 1
serialport.timeout = 0.1

# 发送数据
def send_data():
    d=bytes.fromhex('01 03 00 2A 00 02 E5 C3')
    serialport.write(d)

# 接收数据 
def recv_data():
    str1 = serialport.readline()
    mystr = ''
    data = binascii.b2a_hex(str1)
    strings = str(data)

    for index,x in enumerate(strings):
        if 7 < index < 16:
            mystr += x
    current = hex2float(mystr) 
    return current

# 获取日期
def get_time():
    t = time.time()
    now = float(round(t * 1000)/1000)
    return now

#积分
def get_column(current,last_time,now):
    column = current*(now - last_time)
    return column

#绘图
ax = []                    # 定义一个 x 轴的空列表用来接收动态的数据
ay = []                    # 定义一个 y 轴的空列表用来接收动态的数据
plt.ion()                  # 开启一个画图的窗口
def draw_data(current,time,i):
    if i < 15 :
        ax.append(time)               # 添加 i 到 x 轴的数据中
        ay.append(current)            # 添加 i 的平方到 y 轴的数据中
    else :
        ax[:-1] = ax[1:]
        ay[:-1] = ay[1:]
        ax[-1] = time
        ay[-1] = current

    plt.clf()                  # 清除之前画的图
    plt.plot(ax,ay)            # 画出当前 ax 列表和 ay 列表中的值的图形
    plt.pause(0.05)             # 暂停一秒
    plt.ioff()                 # 关闭画图的窗口

#####################################################################
start_time = get_time()
last_time = start_time
column_int = 0
i=0

while 1:
    try:
        serialport.open()
        # 发送数据
        send_data()
        # 接收数据  
        current = recv_data()
        # 获取日期
        local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        now = get_time(0.7)
        column = get_column(current,last_time,now)
        column_int = column+column_int
        print ('%.4f'%current,'%.3f'%(now - start_time),'%.3f'%column_int,local_time)    #毫秒级时间戳
        time.sleep(0.5)
        serialport.close()
        last_time = now

        #draw_data(current,now-start_time,i)

        i=i+1
        # 写入文件
        f1 = open('current.csv','a')
        f1.write(str('%.4f'%current),str('%.3f'%(now - start_time)),str('%.3f'%(column_int)),str(local_time))
        f1.close
    except:
        pass

