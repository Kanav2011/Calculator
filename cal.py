import tkinter
from tkinter import *

root = Tk()
root.title("amazing calculator")
root.geometry("520x600")
root.resizable(False, False)
root.configure(bg="black")

equation = ""

b1 = Button(root, width = 5, height = 3, text = "1")


def show(value):
    global equation
    equation += value
    label_result.config(text = equation)

def clear():
    global equation
    equation = ""
    label_result.config(text = equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "Error"
            equation = ""
    label_result.config(text = result)

def back():
    string = result;  
   
 
    print();  
   
 
    for i in range(0, len(string)):  
        print(string[i], end="  "); 




label_result = Label(root, width=90, height = 2, text = "", justify = "right", bd = 3, font = ("Cursive", 30), bg = "White")
label_result.pack()


#row 1
Button(root, width = 5, height = 2, text = "C", font = ("Cursive", 22), bd = 2, fg = "black", bg = "gold", command = lambda:clear()).place(x = 10, y = 100)
Button(root, width = 5, height = 2, text = "/", font = ("Cursive", 22), bd = 2, fg = "blue", bg = "grey", command = lambda:show("/")).place(x = 110, y = 100)
Button(root, width = 5, height = 2, text = "x", font = ("Cursive", 22), bd = 2, fg = "blue", bg = "grey", command = lambda:show("*")).place(x = 210, y = 100)
Button(root, width = 5, height = 2, text = "-", font = ("Cursive", 22), bd = 2, fg = "blue", bg = "grey", command = lambda:show("-")).place(x = 310, y = 100)
Button(root, width = 5, height = 2, text = "+", font = ("Cursive", 22), bd = 2, fg = "blue", bg = "grey", command = lambda:show("+")).place(x = 410, y = 100)
#row 2
Button(root, width = 5, height = 2, text = "1", font = ("Cursive", 22), bd = 2, fg = "blue", bg = "grey", command = lambda:show("1")).place(x = 10, y = 200)
Button(root, width = 5, height = 2, text = "2", font = ("Cursive", 22), bd = 2, fg = "blue", bg = "grey", command = lambda:show("2")).place(x = 110, y = 200)
Button(root, width = 5, height = 2, text = "3", font = ("Cursive", 22), bd = 2, fg = "blue", bg = "grey", command = lambda:show("3")).place(x = 210, y = 200)
#row 3
Button(root, width = 5, height = 2, text = "4", font = ("Cursive", 22), bd = 2, fg = "blue", bg = "grey", command = lambda:show("4")).place(x = 10, y = 300)
Button(root, width = 5, height = 2, text = "5", font = ("Cursive", 22), bd = 2, fg = "blue", bg = "grey", command = lambda:show("5")).place(x = 110, y = 300)
Button(root, width = 5, height = 2, text = "6", font = ("Cursive", 22), bd = 2, fg = "blue", bg = "grey", command = lambda:show("6")).place(x = 210, y = 300)
#row 4
Button(root, width = 5, height = 2, text = "7", font = ("Cursive", 22), bd = 2, fg = "blue", bg = "grey", command = lambda:show("7")).place(x = 10, y = 400)
Button(root, width = 5, height = 2, text = "8", font = ("Cursive", 22), bd = 2, fg = "blue", bg = "grey", command = lambda:show("8")).place(x = 110, y = 400)
Button(root, width = 5, height = 2, text = "9", font = ("Cursive", 22), bd = 2, fg = "blue", bg = "grey", command = lambda:show("9")).place(x = 210, y = 400)
#row 5
Button(root, width = 5, height = 2, text = " ←", font = ("Cursive", 22), bd = 2, fg = "black", bg = "gold", command = lambda:back("←")).place(x = 10, y = 500)
Button(root, width = 5, height = 2, text = "0", font = ("Cursive", 22), bd = 2, fg = "blue", bg = "grey", command = lambda:show("0")).place(x = 110, y = 500)
Button(root, width = 5, height = 2, text = ".", font = ("Cursive", 22), bd = 2, fg = "blue", bg = "grey", command = lambda:show(".")).place(x = 210, y = 500)
#enter
Button(root, width = 11, height = 11, text = "Enter", font = ("Cursive", 22), bd = 2, fg = "black", bg = "gold", command = lambda:calculate()).place(x = 310, y = 200)

