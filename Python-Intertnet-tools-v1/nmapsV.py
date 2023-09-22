import nmap
import sys
import ttkbootstrap as ttk
import threading
import win32clipboard as cl
import win32con
def nmsVs(port):
    ip = F1.get()
    nm = nmap.PortScanner()
    nm.scan(hosts=ip,ports=port,arguments='-sV')
    #nm.scan(hosts='192.168.245.131',ports='1-1000',arguments='-sV')
    for ip in nm.all_hosts():
        if nm[ip].state() == 'up':
            print('ip:{0} is open ,Surviving ports:{1}'.format(ip,nm[ip]['tcp'].keys()))
            # for i in port:
            #     lst.insert('',0,value=(ip,i))
            for port in nm[ip].all_tcp():
                if nm[ip]['tcp'][port]['state'] == 'open':
                    print ('port:{0} is open'.format(port))
                    lst.insert('',0,value=(ip,port))
# def thred():
#     nmsVm = threading.Thread(target=nmsVs)
#     nmsVm.setDaemon(True)
#     nmsVm.start()
def thred(kong):
    lis = []
    for i in kong:
        lis.append(threading.Thread(target=nmsVs,args=(str(i),)))
    for i in lis:
        i.start()
def xh():
    TCPin = F2.get()
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
def thed():
    w = threading.Thread(target=xh)
    w.setDaemon(True)
    w.start()
nmsVmain = ttk.Window(themename='solar',title='nmsV')
hi = int(nmsVmain.winfo_screenheight() / 1.8)
wi = int(nmsVmain.winfo_screenwidth() / 1.8)
nmsVmain.geometry("{0}x{1}".format(wi,hi))
ttk.Button(nmsVmain,text=" S t a r t ",bootstyle=("LIGHT",'success-outline-toolbutton'),command=xh,width=10).place(x=920,y=35)
ttk.Label(nmsVmain,text='nmapSV参数扫描工具',bootstyle='SUCCESS',font=('微软雅黑',20)).place(x=100,y=10)
F1 = ttk.Entry(nmsVmain,bootstyle='LIGHT')
F2 = ttk.Entry(nmsVmain,bootstyle='LIGHT')
ttk.Label(nmsVmain,text='IP address:',bootstyle='LIGHT',font=('微软雅黑',13)).place(x=560,y=20)
ttk.Label(nmsVmain,text='Port:',bootstyle='LIGHT',font=('微软雅黑',13)).place(x=610,y=60)
F1.place(x=700,y=20)
F2.place(x=700,y=60)
fm = ttk.Frame(height=100, width=250, bootstyle='dark')
fm.pack(side='bottom', pady=10, padx=0.1)
sourb = ttk.Scrollbar(fm, bootstyle="default-round")
sourb.pack(side='right', fill='y', ipadx=3)
lst = ttk.Treeview(fm, height=21, show='headings',bootstyle='dark')
lst.config(yscrollcommand=sourb.set)
sourb.config(command=lst.yview)
lst['columns'] = ('ip', 'status', '1', '2', '3')
lst.heading('ip', text='ip')
lst.heading('status', text='Status code')
lst.heading('1', text=' ')
lst.column('status', width=200, anchor="s")
lst.column('ip', width=200, anchor='s')
lst.pack(side='bottom', pady=10)

menu = ttk.Menu(nmsVmain, tearoff=False)
def ma(event):
    menu.post(event.x_root, event.y_root)
nmsVmain.bind("<Button-3>", ma)
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
menu.add_command(label='复制', command=binf)
menu.add_command(label='全选', command=binf)






nmsVmain.mainloop()