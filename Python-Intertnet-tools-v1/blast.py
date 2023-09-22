import itertools
import sys
import ttkbootstrap as ttk
import threading
jg = "生成规则如下：\n分为两个模式：\n第一个模式输入两个参数:\n生成字典个数,no\n第二个模式为用户自选信息字典:\n生成字典数量,yes,用户自定义的字典信息\n字典生成在当前目录下的a1.txt"

def blasts():
    such = int(one.get())         #SECTION:生成字典数量
    suc = str(two.get())    #SECTION:yes or no 是否自定义内容生成字典
    modd = str(three.get())     #SECTION:自定义用户内容
    mod = '1234567890qwertyuiopasdfghjklzxcvbnm'
    while 1:
        if suc == "yes":
            mode=itertools.permutations(modd,such)
            # a=open(file='../biji/a1.txt', mode='w')
            a = open(file='a1.txt',mode='w')
            for i in mode:
                a.write("".join(i))
                a.write("".join('\n'))
        elif suc == "no":
            mode = itertools.permutations(mod, such)
            # a = open(file='../biji/a1.txt', mode='w')
            a = open(file='a1.txt',mode='w')
            for i in mode:
                a.write("".join(i))
                a.write("".join('\n'))
        else:
            print('输入yes/no')
            continue
        break
def thred():
    blst = threading.Thread(target=blasts)
    blst.setDaemon(True)
    blst.start()


blastmain = ttk.Window(themename='solar',title='字典生成器')
hei = int (blastmain.winfo_screenheight() / 2.5 )
wei = int (blastmain.winfo_screenwidth() / 2.5 )
blastmain.geometry("{1}x{0}".format(hei,wei))
ttk.Label(blastmain,text='Python字典生成器',font=('微软雅黑',20)).pack(anchor='n')
# fm = ttk.Frame(blastmain,bootstyle='anger',width=635,height=700)
eror = ttk.Label(blastmain,text=jg,font=('微软雅黑',11),bootstyle='success')
one = ttk.Entry(blastmain,bootstyle='warning',width='10')
two = ttk.Entry(blastmain,bootstyle='warning',width='10')
three = ttk.Entry(blastmain,bootstyle='warning',width='25')
one.place(x=90,y=60)
two.place(x=90,y=110)
three.place(x=90,y=160)
# fm.pack(side='right')
eror.place(x=400,y=70)
ttk.Button(blastmain,text=' R U N ',bootstyle=("LIGHT",'success-outline-toolbutton'),command=thred).place(x=90,y=210)
blastmain.mainloop()