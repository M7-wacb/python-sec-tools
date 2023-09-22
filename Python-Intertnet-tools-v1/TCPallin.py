from scapy.all import *
import sys
import threading
import ttkbootstrap as ttk
# ipd = str('192.168.43.13')
def TCPquankai(i):
    ipd = str(en1.get())
    pakage = IP(dst=ipd)/TCP(dport=[i],flags='S') #扫描程序
    rss = sr1(pakage,timeout=1) #发送报文
    # print(str(type(rss)))       #打印rss的type类型
    if (str(type(rss)) == "<class 'NoneType'>"):                            #STUB:判断是否为空，为空则判断为端口关闭
        print('the port {0} is down'.format(i))
    elif (rss.haslayer(TCP)):                                               #STUB:判断是否TCP报文
        if (rss.getlayer(TCP).flags == 0x12):                               #STUB:0x12端口开启状态
            lst.insert('',0,value=(ipd,i,'open'))
            print('open port')
        sendtwo = sr1(IP(dst=ipd)/TCP(dport=i,flags='A'),timeout=5) #完成三次握手
        if (rss.getlayer(TCP).flags == 0x14):                               #STUB:判段0x14为rst包，端口关闭
            print('port down')
            # lst.insert('',0,value=(ipd,i,'down'))
    elif (rss.haslayer(ICMP)):                                              #STUB:判断ICMP包，返回icmp错误报文说明端口不确定open/down
        if ((rss.gatlayer(ICMP).type) == 3 and int(rss.gatlayer(ICMP).code) in [1,2,3,5,7,10]): #STUB:同时符合条件类型为3和错误code为其中几种
            lst.insert('',0,value=(ipd,i,'None'))
            print('ICMP错误包，{0}不确定open/down'.format(i))
    # print(rss.getlayer(TCP).flags)# 查看rss的flags
def thred(kong):
    ong = []
    for i in kong:
        ong.append(threading.Thread(target=TCPquankai,args=(i,)))
    for i in ong:
        i.start()
def xh():
    TCPin = en2.get()
    kong = []
    if '-' in TCPin:
        print('是区间端口')
        cut = TCPin.split('-',1)
        portstart = int(cut[0])
        portstop = int(cut[1])
        for i in range(portstart,portstop+1):
            kong.append(i)
    elif "," in TCPin:
        print('多个参数')
        cut1 = TCPin.split(',',int(TCPin.count(',')))
        for i in cut1:
            port = int(i)
            kong.append(port)
    else:
        print('单个参数')
        port = int(TCPin)
        kong.append(port)
    print(kong)
    thred(kong)
TCPQ = ttk.Window(themename='solar',title='TCP openscan')
wi = int(TCPQ.winfo_screenwidth() / 1.8)
hi = int(TCPQ.winfo_screenheight() / 1.8)
TCPQ.geometry("{0}x{1}".format(wi,hi))
ttk.Button(TCPQ,text='S t a r t',bootstyle='info',command=xh,width=10).place(x=925,y=30)
en1 = ttk.Entry(TCPQ,bootstyle='info')
en2 = ttk.Entry(TCPQ,bootstyle='danger')
ttk.Label(TCPQ,text='TCP全开扫描工具',bootstyle='success',font=('微软雅黑',20)).place(x=10,y=20)
ttk.Label(TCPQ,text='IP address:',bootstyle='info',font=('微软雅黑',14)).place(x=570,y=8)
ttk.Label(TCPQ,text=' Port :',bootstyle='info',font=('微软雅黑',14)).place(x=600,y=58)
en1.place(x=700,y=10)
en2.place(x=700,y=60)
fm = ttk.Frame(height=100, width=250, bootstyle='dark')
fm.pack(side='bottom', pady=10, padx=0.1)
sourb = ttk.Scrollbar(fm, bootstyle="default-round")
sourb.pack(side='right', fill='y', ipadx=3)
lst = ttk.Treeview(fm, height=21, show='headings',bootstyle='dark')
lst.config(yscrollcommand=sourb.set)
sourb.config(command=lst.yview)
lst['columns'] = ('ip', 'port', 'status', '2', '3')
lst.heading('ip', text='ip')
lst.heading('port', text='port')
lst.heading('status', text='Status')
lst.column('port', width=200, anchor="s")
lst.column('ip', width=200, anchor='s')
lst.column('status',width=200,anchor='s')
lst.pack(side='bottom', pady=10)
TCPQ.mainloop()