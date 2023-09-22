# from scapy.all import *
# import time
# import sys
# import threading
# import ttkbootstrap as ttk
# import tkinter as tk
# # wlan = "Intel(R) Wireless-AC 9560 160MHz"
# # ipd = '192.168.43'            #输入ip
# # lst = []
# # def ARPscapy(ip):
# #         try:
# #             ld=Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(hwdst='00:00:00:00:00:00',pdst=ip)
# #             res=srp1(ld,timeout=0.1,verbose=0,iface=wlan)
# #             if res:
# #                 print(ip+'->在线')
# #             else:
# #                 print(ip,'->not')
# #         except:
# #             print('ERROR')
# #
# # for i in range(1,255):
# #     ip = ('{0}.{1}'.format(ipd, i))
# #     lst.append(str(ip))
# # def thred():
# #     kong = []
# #     for i in lst:
# #         kong.append(threading.Thread(target=ARPscapy,args=(i,)))
# #     for i in kong:
# #         i.start()
# # thred()
#
#
# arpsc = ttk.Window(themename='darkly')
# w = int(arpsc.winfo_screenwidth() / 1.8)
# h = int(arpsc.winfo_screenheight() / 1.8)
# arpsc.geometry('{0}x{1}'.format(w,h))
# arpsc.title('ArpScan')
# fm = ttk.Frame(height=150,width=250)
# fm.pack(side='bottom',pady = 0.1,padx = 0.1)
# sourb = ttk.Scrollbar(fm,bootstyle="default-round")
# sourb.pack(side='right',fill='y',ipadx=3)
#
# lst = ttk.Treeview(fm,height=25,show = 'headings')
# lst.config(yscrollcommand=sourb.set)           #TODO:属于固定用法 绑定滚轮
# sourb.config(command=lst.yview)                #TODO:固定用法 配置滚动条
#
# lst['columns'] = ('website','status','1','2','3')
# lst.heading('website',text= 'website')
# lst.heading('status',text= 'Status code')
# lst.heading('1',text=' ')
# lst.column('status',width=200, anchor="s")
# lst.column('website',width=200,anchor='s')
# brf = [(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2),(1,2)]
# for i,l in brf:
#     lst.insert('',0,values = (i,l))
# lst.pack(side = 'bottom',pady = 1)
#
# def apped():
#     lst.insert('',0,values = ('ni','hao'))
# ttk.Button(arpsc,text='click',command = apped,bootstyle='info').place(x=10,y=10)
#
#
#
#
# arpsc.mainloop()




# from scapy.all import *
# import time
# import sys
# import threading
# import ttkbootstrap as ttk
# import tkinter as tk
# from ttkbootstrap.scrolled import ScrolledText
# fomo = True
# wlan = "Intel(R) Wireless-AC 9560 160MHz"
# ipd = '192.168.43'            #输入ip
# lst = []
# ches = []
# def ARPscapy(ip):
#         try:
#             ld=Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(hwdst='00:00:00:00:00:00',pdst=ip)
#             res=srp1(ld,timeout=0.001,verbose=0,iface=wlan)
#             if res:
#                 print(ip+'->在线')
#                 ches.append(ip)
#             else:
#                 print(ip,'->not')
#         except:
#             print('ERROR')
#
# for i in range(1,255):
#     ip = ('{0}.{1}'.format(ipd, i))
#     str(ip)
#     lst.append(ip)
# def thred(a):
#     kong = []
#     for i in lst:
#         kong.append(threading.Thread(target=ARPscapy,args=(i,)))
#         # ARPscapy(i)
#     for i in kong:
#         i.start()
#     deltable()
#     time.sleep(1)
#     tables(aa=a)
# arpsc = ttk.Window(themename='darkly')
# w = int(arpsc.winfo_screenwidth() / 1.8)
# h = int(arpsc.winfo_screenheight() / 1.8)
# arpsc.geometry('{0}x{1}'.format(w,h))
# arpsc.title('ArpScan')
# fm = ttk.Frame(height=100,width=250,bootstyle='dark')
# fm.pack(side='bottom',pady = 10,padx = 0.1)
# sourb = ttk.Scrollbar(fm,bootstyle="default-round")
# sourb.pack(side='right',fill='y',ipadx=3)
#
# def tables(aa):
#     global a
#     global lst
#     if aa == 1:
#         print('创建列表')
#         lst = ttk.Treeview(fm,height=20,show = 'headings')
#         lst.config(yscrollcommand=sourb.set)           #TODO:属于固定用法 绑定滚轮
#         sourb.config(command=lst.yview)                #TODO:固定用法 配置滚动条
#         lst['columns'] = ('website','status','1','2','3')
#         lst.heading('website',text= 'website')
#         lst.heading('status',text= 'Status code')
#         lst.heading('1',text=' ')
#         lst.column('status',width=200, anchor="s")
#         lst.column('website',width=200,anchor='s')
#         lst.pack(side = 'bottom',pady = 10)
#     a = 2
#     chess(lst)
# def chess(lst):
#     for i in ches:
#         lst.insert('',0,values = (i,200))
# def deltable():
#
#
# a = 1
# ttk.Button(arpsc,text='click',command = lambda : thred(a),bootstyle='info').place(x=10,y=10)
# arpsc.mainloop()

from scapy.all import *
import time
import sys
import threading
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.scrolled import ScrolledText
import win32clipboard as cl
import win32con
fomo = True
wlan = "Intel(R) Wireless-AC 9560 160MHz"
lst = []
ches = []
def ARPscapy(ip):
        try:
            ld=Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(hwdst='00:00:00:00:00:00',pdst=ip)
            res=srp1(ld,timeout=0.1,verbose=0,iface=wlan)
            if res:
                print(ip+'->在线')
                ches.append(ip)
            else:
                print(ip,'->not')
        except:
            print('ERROR')


def thred():
    ipd = enty.get()
    for i in range(1, 255):
        ip = ('{0}.{1}'.format(ipd, i))
        str(ip)
        lst.append(ip)
    kong = []
    for i in lst:
        kong.append(threading.Thread(target=ARPscapy,args=(i,)))
    for i in kong:
        i.start()
    min()
    time.sleep(1)
arpsc = ttk.Window(themename='darkly')
w = int(arpsc.winfo_screenwidth() / 1.8)
h = int(arpsc.winfo_screenheight() / 1.8)
arpsc.geometry('{0}x{1}'.format(w,h))
arpsc.title('ArpScan')
print('创建列表')
enty = ttk.Entry(arpsc,bootstyle='info')
enty.place(x=200,y=30)
enty.delete(0,'end')
enty.insert(0,'format x.x.x')
ttk.Label(arpsc,text="insert IP address:",font=('微软雅黑',11)).place(x=45,y=33)
# ttk.Panedwindow(arpsc,bootstyle='info').pack(fill='x',pady=75)                #横线 占用空间
# ttk.Separator(fm,bootstyle='info',).pack(fill='x',padx=1,pady=70)



def min():
    global lst
    fm = ttk.Frame(height=100, width=250, bootstyle='dark')
    fm.pack(side='bottom', pady=10, padx=0.1)
    sourb = ttk.Scrollbar(fm, bootstyle="default-round")
    sourb.pack(side='right', fill='y', ipadx=3)
    lst = ttk.Treeview(fm,height=21,show = 'headings',bootstyle='dark')
    lst.config(yscrollcommand=sourb.set)           #TODO:属于固定用法 绑定滚轮
    sourb.config(command=lst.yview)                #TODO:固定用法 配置滚动条
    lst['columns'] = ('website','status','1','2','3')
    lst.heading('website',text= 'website')
    lst.heading('status',text= 'Status code')
    lst.heading('1',text=' ')
    lst.column('status',width=200, anchor="s")
    lst.column('website',width=200,anchor='s')
    for i in ches:
        lst.insert('',0,values = (i,200))
    lst.pack(side = 'bottom',pady = 10)

menu = ttk.Menu(arpsc, tearoff=False)
def ma(event):
    menu.post(event.x_root, event.y_root)
arpsc.bind("<Button-3>", ma)
def binf():
    lists = lst.selection()
    listen =lst.set(lists)
    lis = listen['website']
    print(lis)
    cll(lis)
def cll(lis):
    cl.OpenClipboard()
    cl.EmptyClipboard()
    cl.SetClipboardData(win32con.CF_UNICODETEXT, lis)
    cl.CloseClipboard()
#192.168.43

menu.add_command(label='粘贴', command=binf)
menu.add_command(label='全选', command=binf)






ttk.Button(arpsc,text=' start ',command = thred,bootstyle=('info','success-outline-toolbutton')).place(x=420,y=30)
arpsc.mainloop()
