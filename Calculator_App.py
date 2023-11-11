from tkinter import Button, Frame, StringVar, Label
from tkinter.tix import Tk
#----------------------------------------------------------------------------------
def button_press(num):
    global equation_text
    equation_text=equation_text+str(num)
    equation_label.set(equation_text)
#----------------------------------------------------------------------------------
def equal():
    global equation_text
    try:
        total=str(eval(equation_text))
        equation_label.set(total)
        equation_text=total
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text=""
    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text=""    
#----------------------------------------------------------------------------------
def clear():
    global equation_text
    equation_label.set("")
    equation_text=""
#----------------------------------------------------------------------------------
window=Tk()
window.title("Calculator")
window.geometry("420x430")
window.resizable(False,False)
window.configure(bg="#17161b")
#----------------------------------------------------------------------------------
equation_text=""

equation_label=StringVar()

label=Label(window, textvariable=equation_label, font=('consolas',25), fg="#fff", bg="black", width=24, height=2)
label.pack()
#----------------------------------------------------------------------------------
frame=Frame(window, bg="#17161b")
frame.pack()
#----------------------------------------------------------------------------------
Clear=Button(frame, text='C', height=1, width=5, font=('consolas',25), fg="#fff", bg="#3697f5", command=lambda : clear())
Clear.grid(row=4,column=0)
#----------------------------------------------------------------------------------
Equal=Button(frame, text='=', height=1, width=5, font=('consolas',25), fg="#fff", bg="orange", command=lambda: equal())
Equal.grid(row=4,column=3)
#----------------------------------------------------------------------------------
addition=Button(frame, text='+', height=1, width=5, font=('consolas',25), fg="#fff", bg="black", command=lambda: button_press('+'))
addition.grid(row=3,column=3)
#----------------------------------------------------------------------------------
substraction=Button(frame, text='-', height=1, width=5, font=('consolas',25), fg="#fff", bg="black", command=lambda: button_press('-'))
substraction.grid(row=2,column=3)
#----------------------------------------------------------------------------------
multiply=Button(frame, text='*', height=1, width=5, font=('consolas',25), fg="#fff", bg="black", command=lambda: button_press('*'))
multiply.grid(row=1,column=3)
#----------------------------------------------------------------------------------
divide=Button(frame, text='/', height=1, width=5, font=('consolas',25), fg="#fff", bg="black", command=lambda: button_press('/'))
divide.grid(row=0,column=3)
#----------------------------------------------------------------------------------
mode=Button(frame, text='%', height=1, width=5, font=('consolas',25), fg="#fff", bg="black", command=lambda: button_press('%'))
mode.grid(row=0,column=2)
#----------------------------------------------------------------------------------
decimal=Button(frame, text='.', height=1, width=5, font=('consolas',25), fg="#fff", bg="black", command=lambda: button_press('.'))
decimal.grid(row=4,column=2)
#----------------------------------------------------------------------------------
openbrace=Button(frame, text='(', height=1, width=5, font=('consolas',25), fg="#fff", bg="black", command=lambda: button_press('('))
openbrace.grid(row=0,column=0)
#----------------------------------------------------------------------------------
closebrace=Button(frame, text=')', height=1, width=5, font=('consolas',25), fg="#fff", bg="black", command=lambda: button_press(')'))
closebrace.grid(row=0,column=1)
#----------------------------------------------------------------------------------
button1=Button(frame, text=7, height=1, width=5, font=('consolas',25), fg="#fff", bg="black", command=lambda: button_press(7))
button1.grid(row=1,column=0)
#----------------------------------------------------------------------------------
button2=Button(frame, text=8, height=1, width=5, font=('consolas',25), fg="#fff", bg="black", command=lambda: button_press(8))
button2.grid(row=1,column=1)
#----------------------------------------------------------------------------------
button3=Button(frame, text=9, height=1, width=5, font=('consolas',25), fg="#fff", bg="black", command=lambda: button_press(6))
button3.grid(row=1,column=2)
#----------------------------------------------------------------------------------
button4=Button(frame, text=4, height=1, width=5, font=('consolas',25), fg="#fff", bg="black", command=lambda: button_press(4))
button4.grid(row=2,column=0)
#----------------------------------------------------------------------------------
button5=Button(frame, text=5, height=1, width=5, font=('consolas',25), fg="#fff", bg="black", command=lambda: button_press(5))
button5.grid(row=2,column=1)
#----------------------------------------------------------------------------------
button6=Button(frame, text=6, height=1, width=5, font=('consolas',25), fg="#fff", bg="black", command=lambda: button_press(6))
button6.grid(row=2,column=2)
#----------------------------------------------------------------------------------
button7=Button(frame, text=1, height=1, width=5, font=('consolas',25), fg="#fff", bg="black", command=lambda: button_press(1))
button7.grid(row=3,column=0)
#----------------------------------------------------------------------------------
button8=Button(frame, text=2, height=1, width=5, font=('consolas',25), fg="#fff", bg="black", command=lambda: button_press(2))
button8.grid(row=3,column=1)
#----------------------------------------------------------------------------------
button9=Button(frame, text=3, height=1, width=5, font=('consolas',25), fg="#fff", bg="black", command=lambda: button_press(3))
button9.grid(row=3,column=2)
#----------------------------------------------------------------------------------
button10=Button(frame, text=0, height=1, width=5, font=('consolas',25), fg="#fff", bg="black", command=lambda: button_press(0))
button10.grid(row=4,column=1)
#----------------------------------------------------------------------------------
window.mainloop()
