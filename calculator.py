from tkinter import *
import math as mt

root = Tk()
root.title('Simple Calculator')
root.geometry('600x300')
root.resizable(0,0)

#Screen

castbutt = " "
text_input = StringVar()
link_enter = Entry(root, width = 200,textvariable = text_input).place(x = 20, y = 5)


#Buttons

b0  = Button(root, text="0", command = lambda: click("0"), activeforeground="red", pady=2, padx=3)
b0.place(x=20, y=250)

b00 = Button(root, text="00",  command = lambda: click("00"), activeforeground="red", pady=2, padx=1)
b00.place(x=68, y=250)

bdot = Button(root, text=" . ", command = lambda: click("."), activeforeground="red", pady=2, padx=2)
bdot.place(x=120, y=250)

b1 = Button(root, text="1 ", command = lambda: click("1"), activeforeground="red", pady=2, padx=3)
b1.place(x=20, y=220)

b2 = Button(root, text="2", command = lambda: click("2"), activeforeground="red", pady=2, padx=3)
b2.place(x=70, y=220)

b3 = Button(root, text="3", command = lambda: click("3"), activeforeground="red", pady=2, padx=3)
b3.place(x=120, y=220)

b4 = Button(root, text="4",command = lambda: click("4"), activeforeground="red", pady=2, padx=3)
b4.place(x=20, y=190)

b5 = Button(root, text="5", command = lambda: click("5"), activeforeground="red", pady=2, padx=3)
b5.place(x=70, y=190)

b6 = Button(root, text="6", command = lambda: click("6"), activeforeground="red", pady=2, padx=3)
b6.place(x=120, y=190)

b7 = Button(root, text="7", command = lambda: click("7"), activeforeground="red", pady=2, padx=3)
b7.place(x=20, y=160)

b8 = Button(root, text="8", command = lambda: click("8"), activeforeground="red", pady=2, padx=3)
b8.place(x=70, y=160)

b9 = Button(root, text="9", command = lambda: click("9"), activeforeground="red", pady=2, padx=3)
b9.place(x=120, y=160)

#function  button

bequl  = Button(root, text="=", command = lambda: calculate_answer(), activeforeground="red", pady=2, padx=3)
bequl.place(x=170, y=250)

bplus  = Button(root, text="+", command = lambda: click("+"), activeforeground="red", pady=2, padx=3)
bplus.place(x=170, y=220)

bminus  = Button(root, text="-", command = lambda: click("-"), activeforeground="red", pady=2, padx=3)
bminus.place(x=170, y=190)

bmul = Button(root, text="*", command = lambda: click("*"), activeforeground="red", pady=2, padx=3)
bmul.place(x=170, y=160)

bdiv = Button(root, text="÷", command = lambda: click("/"), activeforeground="red", pady=2, padx=2)
bdiv.place(x=170, y=130)
'''
bmr = Button(root, text="mr", command = lambda: btn_click(""), activeforeground="red", pady=2, padx=1)
bmr.place(x=120, y=130)

bm_minus = Button(root, text="m-", command = lambda: btn_click(""), activeforeground="red", pady=2, padx=1)
bm_minus.place(x=70, y=130)

bm_plus = Button(root, text="m+", command = lambda: btn_click(""), activeforeground="red", pady=2, padx=1)
bm_plus.place(x=20, y=130)

bplus_or_min = Button(root, text="+/-", command = lambda: btn_click(""), activeforeground="red", pady=2, padx=2)
bplus_or_min.place(x=20, y=100)
'''
bperc = Button(root, text="%", command = lambda: click("%"), activeforeground="red", pady=2, padx=3)
bperc.place(x=70, y=100)

blbrac = Button(root, text=" (", command = lambda: click("("), activeforeground="red", pady=2, padx=4)
blbrac.place(x=120, y=100)

brbrac = Button(root, text=")", command = lambda: click(")"), activeforeground="red", pady=2, padx=4)
brbrac.place(x=170, y=100)

bAC = Button(root, text="AC", command = lambda: clear(), activeforeground="red", pady=2, padx=3)
bAC.place(x=20, y=70)
'''
bpower = Button(root, text="^", command = lambda: click("^"), activeforeground="red", pady=2, padx=3)
bpower.bind("<Button-1>",  scientific)
bpower.place(x=70, y=70)
'''
bdel = Button(root, text="del", activeforeground="red", pady=2, padx=0.5)
bdel.place(x=120, y=70)

bpi = Button(root, text="pi", activeforeground="red", pady=2, padx=0.5)
bpi.place(x=170, y=70)

#Methods



def click(button):
    global castbutt
    castbutt = castbutt + str(button)
    text_input.set(castbutt)

def clear():
    global castbutt
    castbutt = " "
    text_input.set(" ")

def calculate_answer():
    global castbutt
    result = str(eval(castbutt))
    text_input.set(result)
    castbutt = " "

def scientific():
    pass

    
'''
def pow():
    global castbutt
    result = str(eval(castbutt**castbutt))
    text_input.set(result)
    castbutt = " "
'''
root.mainloop()
