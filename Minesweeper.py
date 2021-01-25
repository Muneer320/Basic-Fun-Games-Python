from tkinter import *
import random
global total
total=0
def board():
    global value
    tk=Tk()
    but11=Button(tk,height=1,width=2,command=lambda:game(but11,tk))
    but12=Button(tk,height=1,width=2,command=lambda:game(but12,tk))
    but13=Button(tk,height=1,width=2,command=lambda:game(but13,tk))
    but14=Button(tk,height=1,width=2,command=lambda:game(but14,tk))
    but15=Button(tk,height=1,width=2,command=lambda:game(but15,tk))
    but21=Button(tk,height=1,width=2,command=lambda:game(but21,tk))
    but22=Button(tk,height=1,width=2,command=lambda:game(but22,tk))
    but23=Button(tk,height=1,width=2,command=lambda:game(but23,tk))
    but24=Button(tk,height=1,width=2,command=lambda:game(but24,tk))
    but25=Button(tk,height=1,width=2,command=lambda:game(but25,tk))
    but31=Button(tk,height=1,width=2,command=lambda:game(but31,tk))
    but32=Button(tk,height=1,width=2,command=lambda:game(but32,tk))
    but33=Button(tk,height=1,width=2,command=lambda:game(but33,tk))
    but34=Button(tk,height=1,width=2,command=lambda:game(but34,tk))
    but35=Button(tk,height=1,width=2,command=lambda:game(but35,tk))
    but41=Button(tk,height=1,width=2,command=lambda:game(but41,tk))
    but42=Button(tk,height=1,width=2,command=lambda:game(but42,tk))
    but43=Button(tk,height=1,width=2,command=lambda:game(but43,tk))
    but44=Button(tk,height=1,width=2,command=lambda:game(but44,tk))
    but45=Button(tk,height=1,width=2,command=lambda:game(but45,tk))
    but51=Button(tk,height=1,width=2,command=lambda:game(but51,tk))
    but52=Button(tk,height=1,width=2,command=lambda:game(but52,tk))
    but53=Button(tk,height=1,width=2,command=lambda:game(but53,tk))
    but54=Button(tk,height=1,width=2,command=lambda:game(but54,tk))
    but55=Button(tk,height=1,width=2,command=lambda:game(but55,tk))
    but11.grid(row=1,column=1)
    but12.grid(row=1,column=2)
    but13.grid(row=1,column=3)
    but14.grid(row=1,column=4)
    but15.grid(row=1,column=5)
    but21.grid(row=2,column=1)
    but22.grid(row=2,column=2)
    but23.grid(row=2,column=3)
    but24.grid(row=2,column=4)
    but25.grid(row=2,column=5)
    but31.grid(row=3,column=1)
    but32.grid(row=3,column=2)
    but33.grid(row=3,column=3)
    but34.grid(row=3,column=4)
    but35.grid(row=3,column=5)
    but41.grid(row=4,column=1)
    but42.grid(row=4,column=2)
    but43.grid(row=4,column=3)
    but44.grid(row=4,column=4)
    but45.grid(row=4,column=5)
    but51.grid(row=5,column=1)
    but52.grid(row=5,column=2)
    but53.grid(row=5,column=3)
    but54.grid(row=5,column=4)
    but55.grid(row=5,column=5)
    butlist=[but11,but12,but13,but14,but15,but21,but22,but23,but24,but25,
             but31,but32,but33,but34,but35,but41,but42,but43,but44,but45,
             but51,but52,but53,but54,but55]
    vallist=['1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4',
             '1','2','3','4','b','b','b','b','b']
    value={}
    random.shuffle(vallist)
    for i in range(25):
        value[butlist[i]]=vallist[i]
def game(b,tk):
    if value[b]=='b':
        gamebomb(b,tk)
    else:
        gamenumber(b,int(value[b]),tk)
def gamebomb(b,tk):
    global total
    tk.destroy()
    tkk=Tk()
    label=Label(tkk,text=str(total))
    label.grid(row=1,column=1)
    label_=Label(tkk,text='Game Over')
    label_.grid(row=2,column=1)
def gamenumber(b,n,tk):
    global value,total
    if n!=0:
        b['text']=n
        total+=n
        value[b]='0'
        if total==50:
            tk.destroy()
            ttk=Tk()
            label=Label(ttk,text='you won')
            label.grid(row=1,column=1)
board()
mainloop()