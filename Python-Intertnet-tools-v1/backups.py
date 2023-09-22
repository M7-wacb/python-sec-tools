#
# from scapy.all import *
# import time
# import sys
# import threading
# import ttkbootstrap as ttk
# import tkinter as tk
# from ttkbootstrap.scrolled import ScrolledText
# fomo = True
# wlan = "Intel(R) Wireless-AC 9560 160MHz"
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
#
# def thred():
#     ipd = enty.get()
#     for i in range(1, 255):
#         ip = ('{0}.{1}'.format(ipd, i))
#         str(ip)
#         lst.append(ip)
#     kong = []
#     for i in lst:
#         kong.append(threading.Thread(target=ARPscapy,args=(i,)))
#     for i in kong:
#         i.start()
#     min()
#     time.sleep(1)
# arpsc = ttk.Window(themename='darkly')
# w = int(arpsc.winfo_screenwidth() / 1.8)
# h = int(arpsc.winfo_screenheight() / 1.8)
# arpsc.geometry('{0}x{1}'.format(w,h))
# arpsc.title('ArpScan')
# print('创建列表')
# enty = ttk.Entry(arpsc,bootstyle='info')
# enty.place(x=200,y=30)
# enty.delete(0,'end')
# enty.insert(0,'format x.x.x')
# ttk.Label(arpsc,text="insert IP address:",font=('微软雅黑',11)).place(x=45,y=33)
# # ttk.Panedwindow(arpsc,bootstyle='info').pack(fill='x',pady=75)                #横线 占用空间
# # ttk.Separator(fm,bootstyle='info',).pack(fill='x',padx=1,pady=70)
# def min():
#     global lst
#     fm = ttk.Frame(height=100, width=250, bootstyle='dark')
#     fm.pack(side='bottom', pady=10, padx=0.1)
#     sourb = ttk.Scrollbar(fm, bootstyle="default-round")
#     sourb.pack(side='right', fill='y', ipadx=3)
#     lst = ttk.Treeview(fm,height=21,show = 'headings')
#     lst.config(yscrollcommand=sourb.set)           #TODO:属于固定用法 绑定滚轮
#     sourb.config(command=lst.yview)                #TODO:固定用法 配置滚动条
#     lst['columns'] = ('website','status','1','2','3')
#     lst.heading('website',text= 'website')
#     lst.heading('status',text= 'Status code')
#     lst.heading('1',text=' ')
#     lst.column('status',width=200, anchor="s")
#     lst.column('website',width=200,anchor='s')
#     for i in ches:
#         lst.insert('',0,values = (i,200))
#     lst.pack(side = 'bottom',pady = 10)
#
#
#
# ttk.Button(arpsc,text=' start ',command = thred,bootstyle=('info','success-outline-toolbutton')).place(x=420,y=30)
# arpsc.mainloop()


#SECTION:-----First Keybordwrite backup
# from pynput.keyboard import Key, Listener
# import pynput
# import ttkbootstrap as ttk
# def keybrd():
# 	def on_p(key):
# 		print(f'{key}')
# 	def on_r(key):
# 		if key == Key.esc:
# 			return False
# 	with Listener(on_press=on_p,on_release=on_r) as listener:
# 		listener.join()
# 	eher=pynput.keyboard.Controller()
# 	eher.press(pynput.keyboard.Key.enter) 	#模拟键盘
# 	eher.release(pynput.keyboard.Key.enter) #释放键盘
#
# kybdmain = ttk.Window(title='keyboard',themename='darkly')
# hi = int(kybdmain.winfo_screenheight() / 1.6 )
# wi = int(kybdmain.winfo_screenwidth() / 3)
# kybdmain.geometry('{0}x{1}+100+100'.format(wi,hi))   #窗口尺寸
# ttk.Button(kybdmain,text=' S t a r t ',width=22,bootstyle=('DANGER','success-outline-toolbutton')).place(x=220,y=40)
#
# kybdmain.mainloop()


#SECTION:----- Second keybdwrite backup
# from pynput.keyboard import Key, Listener
# import pynput
# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *
# from ttkbootstrap.scrolled import ScrolledText
# import threading
# def keybrd():
# 	def on_p(key):
# 		print(f'{key}')
# 		st.insert(END, f'{key}'+'\n')
# 	def on_r(key):
# 		if key == Key.esc:
# 			return False
# 	with Listener(on_press=on_p,on_release=on_r) as listener:
# 		listener.join()
# 	eher=pynput.keyboard.Controller()
# 	eher.press(pynput.keyboard.Key.enter) 	#模拟键盘
# 	eher.release(pynput.keyboard.Key.enter) #释放键盘
#
# def thred():
# 	t = threading.Thread(target=keybrd)
# 	t.setDaemon(True)
# 	t.start()
#
# kybdmain = ttk.Window(title='keyboard',themename='solar')
# hi = int(kybdmain.winfo_screenheight() / 1.6 )
# wi = int(kybdmain.winfo_screenwidth() / 3)
# kybdmain.geometry('{0}x{1}+100+100'.format(wi,hi))   #窗口尺寸
# ttk.Button(kybdmain,text=' S t a r t ',width=18,bootstyle=('INFO','success-outline-toolbutton'),command=thred).place(x=80,y=40)
# ttk.Button(kybdmain,text=' S t o p ',width=18,bootstyle=('INFO','success-outline-toolbutton'),command=kybdmain.quit).place(x=360,y=40)
# F =ttk.Frame(kybdmain,bootstyle='light',width=635,height=550)
# F.pack(side = 'bottom')
#

# st = ScrolledText(F,height=25,padding=10,autohide=True)
# st.pack(side = 'right')
#
# kybdmain.mainloop()

#SECTION:------first nmap backup
# import nmap
# import sys
# import ttkbootstrap as ttk
# import threading
# import win32clipboard as cl
# import win32con
# def nmsP():
#     ip = get1.get()
#     nm = nmap.PortScanner()
#     nm.scan(hosts=ip,ports=None,arguments='-sP')
#     sql_lib = [(ip,nm[ip]['status']['state'])for ip in nm.all_hosts()]
#     for host,inf in sql_lib:
#         lst.insert("",0,values=(host,inf))
#         print(host,'is',inf)
# def thead():
#     nmsps = threading.Thread(target=nmsP)
#     nmsps.setDaemon(True)
#     nmsps.start()
#
# nmspmain = ttk.Window(themename='solar')
# w = int(nmspmain.winfo_screenwidth() / 1.8)
# h = int(nmspmain.winfo_screenheight() / 1.8)
# nmspmain.geometry('{0}x{1}'.format(w,h))
# nmspmain.title('nmap Scan')
# ttk.Button(nmspmain,text='S t a r t',command=thead,bootstyle='info').place(x=340,y=30)
# get1 = ttk.Entry(nmspmain,bootstyle='info',width=18)
# get1.place(x=150,y=30)
# #SECTION:设置画布 表格 滚轮
# fm = ttk.Frame(height=100, width=250, bootstyle='dark')
# fm.pack(side='bottom', pady=10, padx=0.1)
# sourb = ttk.Scrollbar(fm, bootstyle="default-round")
# sourb.pack(side='right', fill='y', ipadx=3)
# lst = ttk.Treeview(fm, height=21, show='headings',bootstyle='dark')
# lst.config(yscrollcommand=sourb.set)
# sourb.config(command=lst.yview)
# lst['columns'] = ('website', 'status', '1', '2', '3')
# lst.heading('website', text='website')
# lst.heading('status', text='Status code')
# lst.heading('1', text=' ')
# lst.column('status', width=200, anchor="s")
# lst.column('website', width=200, anchor='s')
# lst.pack(side='bottom', pady=10)
#
# menu = ttk.Menu(nmspmain, tearoff=False)
# def ma(event):
#     menu.post(event.x_root, event.y_root)
# nmspmain.bind("<Button-3>", ma)
# def binf():
#     lists = lst.selection()
#     listen =lst.set(lists)
#     lis = listen['website']
#     print(lis)
#     cll(lis)
# def cll(lis):
#     cl.OpenClipboard()
#     cl.EmptyClipboard()
#     cl.SetClipboardData(win32con.CF_UNICODETEXT, lis)
#     cl.CloseClipboard()
# #192.168.43
# menu.add_command(label='粘贴', command=binf)
# menu.add_command(label='全选', command=binf)
# nmspmain.mainloop()

# import nmap
# import syss
# import ttkbootstrap as ttk
# import threading

# ip = '192.168.43.13'
# port = '1-1000'
# nm = nmap.PortScanner()
# nm.scan(hosts=ip,ports=port,arguments='-sV')
# #nm.scan(hosts='192.168.245.131',ports='1-1000',arguments='-sV')
# for ip in nm.all_hosts():
#     if nm[ip].state() == 'up':
#         print('ip:{0} is open ,Surviving ports:{1}'.format(ip,nm[ip]['tcp'].keys()))
#         for port in nm[ip].all_tcp():
#             if nm[ip]['tcp'][port]['state'] == 'open':
#                 print ('port:{0} is open'.format(port))


#SECTION:openfile backup firet
# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *
# from tkinter.filedialog import askopenfilename
# root = ttk.Window()
# def open_file():
#     path = askopenfilename()
#     print(path)
#     if not path:
#         return
# ttk.Button(root, text="打开文件", command=open_file).pack(fill=X, padx=10, pady=10)
# root.mainloop()

#SECTION:dir Scan

# from tkinter.filedialog import askopenfilename
# import ttkbootstrap as ttk
# import requests
# import threading
# import time
# lsts = []
# # ru = "https://www.baidu.com/"
# def openwrite(files):
#     ru = EN1.get()
#     with open(mode="r",file=files,encoding='utf-8') as i:
#         for ii in i:
#             iii = ii.replace('\n','')
#             lsts.append("{0}{1}".format(ru,iii))
#         i.close()
#     print(lsts)
#
# def req(url):
#     repsone = requests.get(url)
#     if repsone.status_code == 200 or repsone.status_code == 401 or repsone.status_code == 403:
#         lst.insert('',0,value=(url,repsone))
#         print(url,'is {0}'.format(repsone.status_code))
#     else:
#         print(url,'is Not found')
#
# def openfile():
#     path =askopenfilename()
#     print(path)
#     txt.insert('insert',path)
#     openwrite(files=path)
# def more_xc():
#     kong = []
#     for i in lsts:
#         kong.append(threading.Thread(target=req,args=(i,)))
#     for i in kong:
#         i.start()
#     for i in kong:
#         i.join()
# def more_mxc():
#     w = threading.Thread(target=more_xc)
#     w.setDaemon(True)
#     w.start()
#
# dirfors = ttk.Window(themename='solar')
# wi = int(dirfors.winfo_screenwidth() / 1.8)
# hi = int(dirfors.winfo_screenheight() / 1.8)
# dirfors.geometry("{0}x{1}".format(wi,hi))
#
# ttk.Label(dirfors,text='Dir Scan Tools',bootstyle='success',font=('微软雅黑',22)).place(x=10,y=10)
# ttk.Button(dirfors,text='openfile',command=openfile,bootstyle=('info','success-outline-toolbutton')).place(x=700,y=60)
# ttk.Button(dirfors,text=' S t a r t ',bootstyle=('success','success-outline-toolbutton'),command=more_mxc,width=15).place(x=810,y=60)
# ttk.Label(dirfors,text='website:',bootstyle='success',font=('微软雅黑',16)).place(x=580,y=12)
# txt = ttk.Text(dirfors,height=1,width=40,font=('微软雅黑',8))
# txt.place(x=350,y=60)
# EN1 = ttk.Entry(dirfors,bootstyle='info',width=28)
# EN1.place(x=700,y=15)
#
# fm = ttk.Frame(height=100, width=250, bootstyle='dark')
# fm.pack(side='bottom', pady=10, padx=0.1)
# sourb = ttk.Scrollbar(fm, bootstyle="default-round")
# sourb.pack(side='right', fill='y', ipadx=3)
# lst = ttk.Treeview(fm, height=21, show='headings',bootstyle='dark')
# lst.config(yscrollcommand=sourb.set)
# sourb.config(command=lst.yview)
# lst['columns'] = ('website', 'status', '1', '2', '3')
# lst.heading('website', text='website')
# lst.heading('status', text='Status code')
# lst.heading('1', text=' ')
# lst.column('status', width=200, anchor="s")
# lst.column('website', width=300, anchor='s')
# lst.pack(side='bottom', pady=10)
#
# dirfors.mainloop()