import nmap
import sys
import ttkbootstrap as ttk
import threading
import win32clipboard as cl
import win32con
def nmsP():
    ip = get1.get()
    nm = nmap.PortScanner()
    nm.scan(hosts=ip,ports=None,arguments='-sP')
    sql_lib = [(ip,nm[ip]['status']['state'])for ip in nm.all_hosts()]
    for host,inf in sql_lib:
        lst.insert("",0,values=(host,inf))
        print(host,'is',inf)
def thead():
    nmsps = threading.Thread(target=nmsP)
    nmsps.setDaemon(True)
    nmsps.start()

nmspmain = ttk.Window(themename='solar')
w = int(nmspmain.winfo_screenwidth() / 1.8)
h = int(nmspmain.winfo_screenheight() / 1.8)
nmspmain.geometry('{0}x{1}'.format(w,h))
nmspmain.title('nmap Scan')
ttk.Label(nmspmain,text='nmap sP 检测工具',bootstyle='SUCCESS',font=('微软雅黑',20)).place(x=10,y=1)
ttk.Button(nmspmain,text='S t a r t',command=thead,bootstyle='info').place(x=950,y=30)
get1 = ttk.Entry(nmspmain,bootstyle='info',width=20)
get1.place(x=730,y=30)
#SECTION:设置画布 表格 滚轮
fm = ttk.Frame(height=100, width=250, bootstyle='dark')
fm.pack(side='bottom', pady=10, padx=0.1)
sourb = ttk.Scrollbar(fm, bootstyle="default-round")
sourb.pack(side='right', fill='y', ipadx=3)
lst = ttk.Treeview(fm, height=21, show='headings',bootstyle='dark')
lst.config(yscrollcommand=sourb.set)
sourb.config(command=lst.yview)
lst['columns'] = ('website', 'status', '1', '2', '3')
lst.heading('website', text='website')
lst.heading('status', text='Status code')
lst.heading('1', text=' ')
lst.column('status', width=200, anchor="s")
lst.column('website', width=200, anchor='s')
lst.pack(side='bottom', pady=10)

menu = ttk.Menu(nmspmain, tearoff=False)
def ma(event):
    menu.post(event.x_root, event.y_root)
nmspmain.bind("<Button-3>", ma)
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
nmspmain.mainloop()