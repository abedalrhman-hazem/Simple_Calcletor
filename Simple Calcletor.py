from tkinter import *

expression=''
#global vaerabl
def press(userInput):
    global expression
    expression = expression + str(userInput)
    equation.set(expression)

def equalpress():

    try:
        global expression
        result = str(eval(expression)) 
        equation.set(result)
        expression=""
    except:
        equation.set("Error")

def clear():
    global expression
    expression =""
    equation.set("")



gui = Tk()
gui.title("Simple Calcletor")
gui.geometry("280x250")

titleLabal =Label(gui, text="Simple Calcletor" ,fg="blue", font=("century 20 bold"))
titleLabal.grid(columnspan=4, pady=20)

equation=StringVar()

expressionField = Entry(gui,textvariable=equation)
expressionField.grid(columnspan=4, padx=5, pady=10,ipadx=70 )


btn1 = Button(gui , text="1", command=lambda: press(1) ,height=1, width=7)
btn1.grid(row=2,column=0)

btn2 = Button(gui , text="2", command=lambda: press(2) ,height=1, width=7)
btn2.grid(row=2,column=1)

btn3 = Button(gui , text="3", command=lambda: press(3) ,height=1, width=7)
btn3.grid(row=2,column=2)

btn4 = Button(gui , text="4", command=lambda: press(4) ,height=1, width=7)
btn4.grid(row=3,column=0)

btn5 = Button(gui , text="5", command=lambda: press(5) ,height=1, width=7)
btn5.grid(row=3,column=1)

btn6 = Button(gui , text="6", command=lambda: press(6) ,height=1, width=7)
btn6.grid(row=3,column=2)

btn7 = Button(gui , text="7", command=lambda: press(7) ,height=1, width=7)
btn7.grid(row=4,column=0)

btn8 = Button(gui , text="8", command=lambda: press(8) ,height=1, width=7)
btn8.grid(row=4,column=1)

btn9 = Button(gui , text="9", command=lambda: press(9) ,height=1, width=7)
btn9.grid(row=4,column=2)

btn0 = Button(gui , text="0", command=lambda: press(0) ,height=1, width=7)
btn0.grid(row=5,column=0)

dotbtn = Button(gui , text=".",command=lambda: press('.'),height=1, width=7)
dotbtn.grid(row=5,column=1)

equalbtn = Button(gui , text="=",command=equalpress ,height=1, width=7,bg="blue")
equalbtn.grid(row=5,column=2)

plusbtn = Button(gui , text="+",command=lambda: press('+'),height=1, width=7)
plusbtn.grid(row=2,column=3)

mainusbtn = Button(gui , text="-",command=lambda: press('-'),height=1, width=7)
mainusbtn.grid(row=3,column=3)

multiplybtn = Button(gui , text="*",command=lambda: press('*'),height=1, width=7)
multiplybtn.grid(row=4,column=3)

divdebtn = Button(gui , text="/",command=lambda: press('/'),height=1, width=7)
divdebtn.grid(row=5,column=3)

clearbtn = Button(gui , text="c",command=clear ,height=1, width=7)
clearbtn.grid(row=6,column=0)

gui.mainloop()