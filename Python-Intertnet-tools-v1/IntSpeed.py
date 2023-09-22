import psutil,time,threading
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import speedtest
import inspect

root = ttk.Window(themename='darkly')
root.geometry('800x300')
def _():
        meter = ttk.Meter(                  #SECTION--创建⚪进度条
                metersize=180,
                padding=50,
                amountused=0,
                metertype="semi",
                subtext="up speed:(mb/s)",
                subtextstyle="warning",
                interactive=False,
                bootstyle='primary',
                )
        meter.pack(side=ttk.LEFT, padx=5)
        while True:
                meter.configure(amountused=round(getNet(),2))       #ttk的插件
def __():
        meters = ttk.Meter(
                metersize=180,
                padding=50,
                amountused=0,
                metertype="semi",
                subtext="download speed:(mb/s)",
                subtextstyle="warning",
                interactive=False,
                bootstyle='primary',
                )
        meters.pack(side='right', padx=5)
        while True:
                meters.configure(amountused=round(getNet(),2))
def getNet():
    time.sleep(1)
    test = speedtest.Speedtest()
    test.get_servers()
    stack = inspect.stack()
    if stack[1].function == '_':
        recv = int(test.upload() / 1024 / 1024)
        print('up:',recv)
        return recv
    elif stack[1].function == '__':
        recv = int(test.download() /1024 /1024)
        print('dow:',recv)
        return recv

k = threading.Thread(target=__)                 #SECTION--多线程执行
k.setDaemon(True)                               #SECTION--守护进程
k.start()                                       #SECTION--start

t = threading.Thread(target=_)
t.setDaemon(True)
t.start()
root.mainloop()
