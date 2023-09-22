import tkinter as tk
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import time
from Intest import Py as intest
import threading
#SECTION:函数部分
def Intest():
    intest()
def speed():
    os.system('python IntSpeed.py')          #TODO:利用os调用同目录下的文件

def thred(func):
    t= threading.Thread(target=func)    #TODO:多线程创建
    t.setDaemon(True)       #TODO:线程守护
    t.start()
def arpscan():
    os.system('python arpscan.py')
def keybdwt():
    os.system('python keybordwrite.py')
def mouses():
    os.system('python Mouse.py')
def blasts():
    os.system('python blast.py')
def nmapSp():
    os.system('python nmsP.py')
def nmSV():
    os.system('python nmapsV.py')
def TCPquank():
    os.system('python TCPallin.py')
def dirscan():
    os.system('python dirfor.py')
def wistscan():
    os.system('python wistscan.py')
#SECTION:创建主窗口
man = ttk.Window(themename="solar")          #TODO:主参数darkly        litera
hi = int(man.winfo_screenheight() / 2 +100)
wi = int(man.winfo_screenwidth() / 2+100)
man.geometry('{0}x{1}+100+100'.format(wi,hi))   #窗口尺寸
# man.resizable(0,0)                      #不允许改变大小
#SECTION:创建画布和多页面切换的总布局
note = ttk.Notebook(man,height=30,bootstyle='default',padding=(0,47,0,0))
fone = ttk.Frame(man,bootstyle='dark')
ftwo = ttk.Frame(man,bootstyle='dark')
fthree = ttk.Frame(man,bootstyle='dark')
#SECTION:创建新的按钮按键，并放置
BUl1 = ttk.Button(fone,text='网络测试模块',bootstyle=(LIGHT,'success-outline-toolbutton'),command=Intest,width=15)
BUl2 = ttk.Button(fone,text='网速测试模块',bootstyle=(LIGHT,'success-outline-toolbutton'),command=lambda : thred(speed),width=15)      #TODO:多线程
BUT1 = ttk.Button(ftwo,text='arp扫描模块',bootstyle=(LIGHT,'success-outline-toolbutton'),width=15,command=lambda : thred(arpscan))
BUT2 = ttk.Button(ftwo,text="nmapsP",bootstyle=(LIGHT,'success-outline-toolbutton'),width=15,command=lambda : thred(nmapSp))
BUT3 = ttk.Button(ftwo,text='nmsV',bootstyle=(LIGHT,'success-outline-toolbutton'),width=15,command=lambda : thred(nmSV))
BUT4 = ttk.Button(ftwo,text='TCP全开扫描',bootstyle=(LIGHT,'success-outline-toolbutton'),width=15,command=lambda : thred(TCPquank))
BUT5 = ttk.Button(ftwo,text='dir scan',bootstyle=(LIGHT,'success-outline-toolbutton'),width=15,command=lambda : thred(dirscan))
BUT6 = ttk.Button(ftwo,text='wist scan',bootstyle=(LIGHT,'success-outline-toolbutton'),width=15,command=lambda : thred(dirscan))
BUTH1 = ttk.Button(fthree,text='键盘记录',bootstyle=(LIGHT,'success-outline-toolbutton'),width=15,command=lambda : thred(keybdwt))
BUTH2 = ttk.Button(fthree,text='鼠标记录',bootstyle=(LIGHT,'success-outline-toolbutton'),width=15,command=lambda : thred(mouses))
BUTH3 = ttk.Button(fthree,text='字典生成',bootstyle=(LIGHT,'success-outline-toolbutton'),width=15,command=lambda : thred(blasts))
BUl1.place(x=wi / 38.4,y=hi / 15)
BUl2.place(x=wi / 4.9,y=hi / 15)
BUT1.place(x=wi / 38.4,y=hi / 15)
BUT2.place(x=wi / 4.9,y=hi / 15)
BUT3.place(x=wi / 2.6,y=hi / 15)
BUT4.place(x=wi / 1.75,y=hi / 15)
BUT5.place(x=wi / 1.32,y=hi / 15)
BUT6.place(x=wi / 38.4 , y=hi / 6)
BUTH1.place(x=wi / 38.4,y=hi / 15)
BUTH2.place(x=wi / 4.9,y=hi / 15)
BUTH3.place(x=wi / 2.6,y=hi / 15)
#SECTION:添加画布到多页面
EROR = '警告,本工具仅用于学习交流,作者在此声明一切行为用途与本人无关,本工具未经授权严禁私自用\n于商业用途(目前本工具处于开发阶段,尚未成型,功能还请理性看待.)'
note.add(fone,text=' 网络测试工具 ')
note.add(ftwo,text=' 内网常用工具 ')
note.add(fthree,text=' 常用工具模块 ')
note.add(ttk.Label(note,text=EROR+' '*274,font=('微软雅黑',15)),text=' 工具介绍 ',sticky='nw')      #填充使页面全部展开
note.pack(padx=0,fill=Y,side='left')
#添加主标题和窗口title
ttk.Label(man,text='Python网络工具v1.0',bootstyle='light',font=('微软雅黑',20)).place(x=1,y=1)
man.title('Python网络工具v1.0')



man.mainloop()











# man = ttk.Window(themename="darkly")          #主参数
# frm = ttk.Frame(man)
# frm.pack(padx=5,fill=Y,side="left")
# nob = ttk.Notebook(frm,height=100)
# nob.pack(padx=10,fill=Y,side='left')
# nob.add(ttk.Label(nob,text=' '*240),text='真')
# nob.add(ttk.Label(nob,text='welcome'),text='   主 页  ')
# nob.add(ttk.Label(nob,text='to'),text='  附 页  ')
# hi = int(man.winfo_screenheight() / 2)
# wi = int(man.winfo_screenwidth() / 2)
# man.geometry('{0}x{1}'.format(wi,hi))   #窗口尺寸
# man.resizable(0,0)                      #不允许改变大小


# man = ttk.Window(themename="darkly")          #主参数
# frm = ttk.Frame(man)                          #一个画布
# frm.pack(pady=0.1,fill=Y,side="left")         #放置画布
# nob = ttk.Notebook(man,height=10,bootstyle='default',padding=(0,47,0,0))   #ttk的Notebook 表示分框 pandding表示大小 左上右下
# nob.pack(padx=0,fill=Y,side='left')
# nob.add(ttk.Label(nob,text='本工具未经授权禁止擅自进行商业用途'+' '*300,font=('微软雅黑',20)),text='    工 具 介 绍    ',sticky='nw')
# nob.add(ttk.Label(nob,text='welcome'),text='     网络测试工具    ')
# nob.add(ttk.Label(nob,text='to'),text='    附 页    ')
# nob.add(frm,text='dudu')
# hi = int(man.winfo_screenheight() / 2 +100)
# wi = int(man.winfo_screenwidth() / 2+100)
# man.geometry('{0}x{1}+100+100'.format(wi,hi))   #窗口尺寸
# man.resizable(0,0)                      #不允许改变大小
# ttk.Label(man,text='Python便捷工具v1.0',font=("微软雅黑",20),bootstyle='secondary').place(anchor=NW)
# man.title('Python便利工具v1.0')
# ttk.Button(frm,text=10000)
