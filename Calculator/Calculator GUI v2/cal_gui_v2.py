from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("Calculator")
root.resizable(0,0)

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, padx=50, pady=10, columnspan=5)

buttimg = ImageTk.PhotoImage(Image.open("buttonframe.png"))
one1 = ImageTk.PhotoImage(Image.open("1.png"))
one2 = ImageTk.PhotoImage(Image.open("2.png"))
one3 = ImageTk.PhotoImage(Image.open("3.png"))
one4 = ImageTk.PhotoImage(Image.open("4.png"))
one5 = ImageTk.PhotoImage(Image.open("5.png"))
one6 = ImageTk.PhotoImage(Image.open("6.png"))
one7 = ImageTk.PhotoImage(Image.open("7.png"))
one8 = ImageTk.PhotoImage(Image.open("8.png"))
one9 = ImageTk.PhotoImage(Image.open("9.png"))
one0 = ImageTk.PhotoImage(Image.open("0.png"))
oneplus = ImageTk.PhotoImage(Image.open("plus.png"))
oneminus  = ImageTk.PhotoImage(Image.open("minus.png"))
onemutiply = ImageTk.PhotoImage(Image.open("multiply.png"))
onedivide = ImageTk.PhotoImage(Image.open("divide.png"))
oneequal = ImageTk.PhotoImage(Image.open("equal.png"))
oneclear = ImageTk.PhotoImage(Image.open("C.png"))

def button_click(number):
    global num
    exist = str(e.get())
    e.delete(0, END)
    e.insert(0, exist + str(number))
    num = exist + str(number)


def button_add():
    global f_num
    global operand
    first_num = e.get()
    operand = "addition"
    f_num = float(first_num)
    e.delete(0, END)

def button_equal():
    if operand == "addition":
        second_num = e.get()
        e.delete(0, END)
        e.insert(0, f_num + float(second_num))
    elif operand == "subtraction":
        second_num = e.get()
        e.delete(0, END)
        e.insert(0, f_num - float(second_num))
    elif operand == "multiplication":
        second_num = e.get()
        e.delete(0, END)
        e.insert(0, f_num * float(second_num))
    elif operand == "division":
        second_num = e.get()
        e.delete(0, END)
        e.insert(0, f_num / float(second_num))


def button_subtract():
    first_num = e.get()
    global f_num
    global operand
    operand = StringVar()
    operand = "subtraction"
    f_num = float(first_num)
    e.delete(0, END)


def button_multiply():
    first_num = e.get()
    global f_num
    global operand
    operand = StringVar()
    operand = "multiplication"
    f_num = float(first_num)
    e.delete(0, END)


def button_divide():
    first_num = e.get()
    global f_num
    global operand
    operand = StringVar()
    operand = "division"
    f_num = float(first_num)
    e.delete(0, END)


def clear():
    e.delete(0, END)


button_1 = Button(root, image = one1, command=lambda: button_click(1))
button_2 = Button(root, image = one2, command=lambda: button_click(2))
button_3 = Button(root, image = one3, command=lambda: button_click(3))
button_4 = Button(root, image = one4, command=lambda: button_click(4))
button_5 = Button(root, image = one5, command=lambda: button_click(5))
button_6 = Button(root, image = one6, command=lambda: button_click(6))
button_7 = Button(root, image = one7, command=lambda: button_click(7))
button_8 = Button(root, image = one8, command=lambda: button_click(8))
button_9 = Button(root, image = one9, command=lambda: button_click(9))
button_0 = Button(root, image = one0, command=lambda: button_click(0))
button_point = Button(root, text=".", padx=42, pady=20, command=button_click, state = DISABLED)
button_add = Button(root,image = oneplus, command=button_add)
button_subtract = Button(root,image = oneminus, command=button_subtract)
button_multiply = Button(root, image = onemutiply, command=button_multiply)
button_divide = Button(root,image = onedivide, command=button_divide)

button_equal = Button(root,image = oneequal, command=button_equal)
button_clear = Button(root,image = oneclear, command=clear)

# arranging buttons
button_1.grid(row=3, column=1)
button_2.grid(row=3, column=2)
button_3.grid(row=3, column=3)

button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_6.grid(row=2, column=3)

button_7.grid(row=1, column=1)
button_8.grid(row=1, column=2)
button_9.grid(row=1, column=3)

button_0.grid(row=4, column=0, columnspan=3)
button_point.grid(row=4, column=3)
button_add.grid(row=1, column=4)
button_subtract.grid(row=2, column=4)
button_multiply.grid(row=3, column=4)
button_divide.grid(row=4, column=4)
button_clear.grid(row=5, column=0, columnspan=3)
button_equal.grid(row=5, column=3, columnspan=3)

credits = messagebox.showinfo("Credits", "Thank You for choosing our application\nThis application was created by Akash Shanmugaraj")
root.mainloop()
