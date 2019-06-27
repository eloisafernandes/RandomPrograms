from tkinter import *

def somar():
    resul["text"] = resul["text"] + " + "

def subr():
    resul["text"] = resul["text"] + " - "

def multr():
    resul["text"] = resul["text"] + " * "

def divr():
    resul["text"] = resul["text"] + " / "

def p1():
    resul["text"] = resul["text"] + "1"
def p2():
    resul["text"] = resul["text"] + "2"
def p3():
    resul["text"] = resul["text"] + "3"
def p4():
    resul["text"] = resul["text"] + "4"
def p5():
    resul["text"] = resul["text"] + "5"
def p6():
    resul["text"] = resul["text"] + "6"
def p7():
    resul["text"] = resul["text"] + "7"
def p8():
    resul["text"] = resul["text"] + "8"
def p9():
    resul["text"] = resul["text"] + "9"
def p0():
    resul["text"] = resul["text"] + "0"
def pont():
    resul["text"] = resul["text"] + "."
def cc():
    resul["text"] = ""

def resultado():
    a = resul["text"].split(" ")
    
    if (a[1] == "+"):
        resul["text"] = float(a[0]) + float(a[2])
    elif (a[1] == "-"):
        resul["text"] = float(a[0]) - float(a[2])
    elif (a[1] == "*"):
        resul["text"] = float(a[0]) * float(a[2])
    elif (a[1] == "/"):
        resul["text"] = float(a[0]) / float(a[2])
    else:
        error["text"] = "ERROR"
    
   
window = Tk()
window.title("Mini Calculadora")
window.geometry('180x250+100+50')
#window.geometry('alturaXlargura+MargemEsquerda+MargemTopo')

resul = Label(window, text="", font="arial 12")
error = Label(window, text="", font="arial 12")

soma = Button(window, text="+", command=somar)
sub = Button(window, text="-", command=subr)
mult = Button(window, text="*", command=multr)
div = Button(window, text="/", command=divr)

b1 = Button(window, text="1", command=p1)
b2 = Button(window, text="2", command=p2)
b3 = Button(window, text="3", command=p3)

b4 = Button(window, text="4", command=p4)
b5 = Button(window, text="5", command=p5)
b6 = Button(window, text="6", command=p6)

b7 = Button(window, text="7",command=p7)
b8 = Button(window, text="8",command=p8)
b9 = Button(window, text="9",command=p9)
b0 = Button(window, text="0",command=p0)

c = Button(window, text="C", command=cc)
P = Button(window, text=".", command=pont)
igual = Button(window, text="=", command=resultado)

resul.grid(row=0,column=0,columnspan=4)
error.grid(row=1,column=0,columnspan=4)
b1.grid(row=2,column=0, padx= 5, pady=10)
b2.grid(row=2,column=1, padx= 5, pady=10)
b3.grid(row=2,column=2, padx= 5, pady=10)
soma.grid(row=2,column=3, padx= 5, pady=10)

b4.grid(row=3,column=0, padx= 5, pady=10)
b5.grid(row=3,column=1, padx= 5, pady=10)
b6.grid(row=3,column=2, padx= 5, pady=10)
sub.grid(row=3,column=3, padx= 5, pady=10)

b7.grid(row=4,column=0, padx= 5, pady=10)
b8.grid(row=4,column=1, padx= 5, pady=10)
b9.grid(row=4,column=2, )
mult.grid(row=4,column=3, padx= 5, pady=10)

b0.grid(row=5,column=0, padx= 5, pady=10)
c.grid(row=5,column=1, padx= 5, pady=10)
P.grid(row=5,column=2, padx= 5, pady=10)
igual.grid(row=5,column=3, padx= 5, pady=10)
window.mainloop()

