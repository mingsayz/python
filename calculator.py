from tkinter import *
from math import *

## main
window = Tk()
window.title("Calculator")

frame1 = Frame(window)
frame1.grid(row=0,column=0,columnspan=2,sticky = N)

frame2_1 = Frame(window)
frame2_1.grid(row=1,column=0,sticky = W)

frame2_2 = Frame(window)
frame2_2.grid(row=1,column=1,sticky=E)

frame2_3 = Frame(window)
frame2_3.grid(row=2,column=0,sticky=W)

frame3 = Frame(window)
frame3.grid(row=3,column=0,sticky=W)

entry1 = Entry(frame1,width=45,bg="light green")
entry1.grid()

## number button
num_pad_list = [
    '7','8','9',
    '4','5','6',
    '1','2','3',
    '0','.']

r=0
c=0

for btn_text in num_pad_list :
    def click(x=btn_text):
        entry1.insert(END,x)
    Button(frame2_1,text=btn_text,width=5,command=click).grid(row=r,column=c)
    c = c + 1
    if c > 2:
        c = 0
        r = r + 1



operator_list = [
    '*','/',
    '+','-',
    '(',')',
    '=','C']
r = 0
c = 0

for operator_text in operator_list :
    def click2(x=operator_text):
        if x == "=":
            try :
                result = str(eval(entry1.get()))
                entry1.insert(END,"="+result)
            except Exception as ex:
                print("error!",ex)
                entry1.delete(0,END)
                entry1.insert(0,ex)

        elif x == "C":
            entry1.delete(0,END)
        else :
            entry1.insert(END,x)
    Button(frame2_2,text=operator_text,width=5,command=click2).grid(row=r,column=c)
    c = c + 1
    if c > 1:
        c = 0
        r = r + 1

math_functions = [
    'sin','cos',
    'tan','exp']

r=0
c=0

for math_function in math_functions:
    def click3(x=math_function):
        if x == '=':
            try :
                result = entry1.get()
                result = str(x(result))
                entry1.insert(END,"="+result)
            except Exception as ex:
                print("calculation error!",ex)
                entry1.delete(0,END)
                entry1.insert(0,ex)
        else :
            entry1.insert(END,x)
    Button(frame3,text=math_function,width=5,command=click3).grid(row=r,column=c)
    c = c + 1
    if c > 1:
        c = 0
        r = r + 1

window.mainloop()
