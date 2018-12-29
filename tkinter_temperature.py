# -*- coding: utf-8 -*-

from Tkinter import *

def process():
    temperature = float(e1.get())
    mytemp = (temperature-32)*5/9
    e2.insert(0,str(mytemp))

def process_2():
    temperature = float(e2.get())
    mytemp = (temperature*9/5) + 32
    e1.insert(0,str(mytemp))

window=Tk()
I1 = Label(window,text='섭씨')
I2 = Label(window,text='화씨')
I1.grid(row=0,column=0)
I2.grid(row=1,column=0)
# I1.pack()
# I2.pack()

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
# e1.pack()
# e2.pack()

b1 = Button(window,text='화씨->섭씨',command = process)
b2 = Button(window,text='섭씨->화씨',command = process_2)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
# b1.pack()
# b2.pack()
window.mainloop()
