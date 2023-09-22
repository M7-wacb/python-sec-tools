from pynput.keyboard import Key, Listener
import pynput
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText
import threading
def keybrd():
	def on_p(key):
		print(f'{key}')
		st.insert(END, f'{key}'+'\n')
	def on_r(key):
		if key == Key.esc:
			return False
	with Listener(on_press=on_p,on_release=on_r) as listener:
		listener.join()
	eher=pynput.keyboard.Controller()
	eher.press(pynput.keyboard.Key.enter) 	#模拟键盘
	eher.release(pynput.keyboard.Key.enter) #释放键盘

def thred():
	t = threading.Thread(target=keybrd)
	t.setDaemon(True)
	t.start()

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