from tkinter.filedialog import askopenfilename
import ttkbootstrap as ttk
import requests
import threading
import time
lsts = []
# ru = "https://www.baidu.com/"
def openwrite(files):
    ru = EN1.get()
    with open(mode="r",file=files,encoding='utf-8') as i:
        for ii in i:
            iii = ii.replace('\n','')
            lsts.append("http://{0}.{1}".format(iii,ru))
        i.close()
    print(lsts)

def req(url):
    repsone = requests.get(url)
    if repsone.status_code == 200 or repsone.status_code == 401 or repsone.status_code == 403:
        lst.insert('',0,value=(url,repsone))
        print(url,'is {0}'.format(repsone.status_code))
    else:
        print(url,'is Not found')

def openfile():
    path =askopenfilename()
    print(path)
    txt.insert('insert',path)
    openwrite(files=path)
def more_xc():
    kong = []
    for i in lsts:
        kong.append(threading.Thread(target=req,args=(i,)))
    for i in kong:
        i.start()
    for i in kong:
        i.join()
def more_mxc():
    w = threading.Thread(target=more_xc)
    w.setDaemon(True)
    w.start()

dirfors = ttk.Window(themename='solar')
wi = int(dirfors.winfo_screenwidth() / 1.8)
hi = int(dirfors.winfo_screenheight() / 1.8)
dirfors.geometry("{0}x{1}".format(wi,hi))

ttk.Label(dirfors,text='Dir Scan Tools',bootstyle='success',font=('微软雅黑',22)).place(x=10,y=10)
ttk.Button(dirfors,text='openfile',command=openfile,bootstyle=('info','success-outline-toolbutton')).place(x=700,y=60)
ttk.Button(dirfors,text=' S t a r t ',bootstyle=('success','success-outline-toolbutton'),command=more_mxc,width=15).place(x=810,y=60)
ttk.Label(dirfors,text='website:',bootstyle='success',font=('微软雅黑',16)).place(x=580,y=12)
txt = ttk.Text(dirfors,height=1,width=40,font=('微软雅黑',8))
txt.place(x=350,y=60)
EN1 = ttk.Entry(dirfors,bootstyle='info',width=28)
EN1.place(x=700,y=15)

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
lst.column('website', width=300, anchor='s')
lst.pack(side='bottom', pady=10)

dirfors.mainloop()