from pynput import mouse
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText
import threading
import pynput

def mous():
    with pynput.mouse.Events() as evt:      #惯用with带入
        for i in evt:                       #循环
            if isinstance(i,pynput.mouse.Events.Move):  #匹配鼠标移动输出x.y坐标
                print(i.x,i.y)
                st.insert(END,"{0}x{1}\n".format(i.x,i.y))
            elif isinstance(i,pynput.mouse.Events.Click):   #匹配鼠标的点击并输出
                print(i.x,i.y,i.button,i.pressed)
            elif isinstance(i,pynput.mouse.Events.Scroll):  #匹配鼠标滚轮
                print((i.x,i.y,i.dx,i.dy))

        i = evt.get(1)      #最长等待时间

def thred():
    w= threading.Thread(target=mous)
    w.setDaemon(True)
    w.start()

kybdmain = ttk.Window(title='keyboard',themename='solar')
hi = int(kybdmain.winfo_screenheight() / 1.6 )
wi = int(kybdmain.winfo_screenwidth() / 3)
kybdmain.geometry('{0}x{1}+100+100'.format(wi,hi))   #窗口尺寸
ttk.Button(kybdmain,text=' S t a r t ',width=18,bootstyle=('INFO','success-outline-toolbutton'),command=thred).place(x=80,y=40)
ttk.Button(kybdmain,text=' S t o p ',width=18,bootstyle=('INFO','success-outline-toolbutton'),command=kybdmain.quit).place(x=360,y=40)
F =ttk.Frame(kybdmain,bootstyle='light',width=635,height=550)
F.pack(side = 'bottom')

#SECTION:滚轮
st = ScrolledText(F,height=25,padding=10,autohide=True)
st.pack(side = 'right')

kybdmain.mainloop()
