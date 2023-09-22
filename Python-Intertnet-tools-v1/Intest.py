import tkinter as tk
import os
def Py():
    wind = tk.Tk()
    wind.geometry('600x600')
    wind.title('internet test')
    pronse = os.system('ping -n 2 www.baidu.com')
    if pronse == 0:
        pshow = tk.Label(wind, text='Internet OK', fg='black', bg='white')
        pshow.pack()
    else:
        psshow = tk.Label(wind, text='Internet Error', fg='black', bg='white')
        psshow.pack()
    wind.mainloop()
# Py()