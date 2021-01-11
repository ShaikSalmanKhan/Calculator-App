from tkinter import *
from random import choice


# button font, size, family
button_color = ["#a9294f", "gray", 'White', 'Brown', "#93af22", "#edefe0"]
BUTTON_COLOR =  choice(button_color)

font_family  =  ["Arial", "Courier"]
font_style   =  ["normal", "italic"]
BUTTON_FONT  =  (choice(font_family), 18, choice(font_style))


def change_color():
    """Changing background when user clicks on bg button"""
    BUTTON_COLOR = choice(button_color)
    zero_button.config(bg=BUTTON_COLOR)
    one_button.config(bg=BUTTON_COLOR)
    two_button.config(bg=BUTTON_COLOR)
    three_button.config(bg=BUTTON_COLOR)
    four_button.config(bg=BUTTON_COLOR)
    five_button.config(bg=BUTTON_COLOR)
    six_button.config(bg=BUTTON_COLOR)
    seven_button.config(bg=BUTTON_COLOR)
    eight_button.config(bg=BUTTON_COLOR)
    nine_button.config(bg=BUTTON_COLOR)
    decimal_button.config(bg=BUTTON_COLOR)
    equal_button.config(bg=BUTTON_COLOR)
    add_button.config(bg=BUTTON_COLOR)
    subtract_button.config(bg=BUTTON_COLOR)
    multiply_button.config(bg=BUTTON_COLOR)
    divide_button.config(bg=BUTTON_COLOR)
    clear_button.config(bg=BUTTON_COLOR)
    quit_button.config(bg=BUTTON_COLOR)
    bg_button.config(bg=BUTTON_COLOR)
    font_button.config(bg=BUTTON_COLOR)


def change_font():
    """Changing Font when user clicks on F button"""
    BUTTON_FONT  =  (choice(font_family), 18, choice(font_style))
    zero_button.config(font=BUTTON_FONT)
    one_button.config(font=BUTTON_FONT)
    two_button.config(font=BUTTON_FONT)
    three_button.config(font=BUTTON_FONT)
    four_button.config(font=BUTTON_FONT)
    five_button.config(font=BUTTON_FONT)
    six_button.config(font=BUTTON_FONT)
    seven_button.config(font=BUTTON_FONT)
    eight_button.config(font=BUTTON_FONT)
    nine_button.config(font=BUTTON_FONT)
    decimal_button.config(font=BUTTON_FONT)
    equal_button.config(font=BUTTON_FONT)
    add_button.config(font=BUTTON_FONT)
    subtract_button.config(font=BUTTON_FONT)
    multiply_button.config(font=BUTTON_FONT)
    divide_button.config(font=BUTTON_FONT)
    clear_button.config(font=BUTTON_FONT)
    quit_button.config(font=BUTTON_FONT)
    bg_button.config(font=BUTTON_FONT)
    font_button.config(font=BUTTON_FONT)


def submit_number(number):
    """inserting clicked button in entry box"""
    display.insert(END, number)
    # if decimal is pressed disable it
    if "." in display.get():
        decimal_button.config(state=DISABLED)


def operate(operator):
    """used to store first_number and operation"""
    global first_number
    global operation

    # storing the first_num & operation
    operation    = operator
    first_number = display.get()

    # delete the first number from the entry
    display.delete(0, END)

    # once user presses a operator he is not allowed to use it again
    add_button.config(state=DISABLED)
    subtract_button.config(state=DISABLED)
    multiply_button.config(state=DISABLED)
    divide_button.config(state=DISABLED)

    # activating the decimal button for second number
    decimal_button.config(state=NORMAL)


def equal():
    """this will perform add,sub,mul,div when user clicks on equal button"""
    if operation == "+":
        value = float(first_number) + float(display.get())
    elif operation == "-":
        value = float(first_number) - float(display.get())
    elif operation == "*":
        value = float(first_number) * float(display.get())
    elif operation == "/":
        if display.get() == "0":
            value = "ERROR"
        else:
            value = float(first_number) / float(display.get())

    # delete second number and insert calculation of both numbers
    display.delete(0, END)
    display.insert(0, value)

    # Calling the enable_button function
    enable_buttons()


def enable_buttons():
    """Enable all buttons after equal operation is performed"""
    if "." in display.get():
        decimal_button.config(state=DISABLED)
    else:
        decimal_button.config(state=NORMAL)
    add_button.config(state=NORMAL)
    subtract_button.config(state=NORMAL)
    multiply_button.config(state=NORMAL)
    divide_button.config(state=NORMAL)


def clear():
    """clear the display"""
    display.delete(0, END)
    # enable all buttons
    enable_buttons()


# Creating a window
window = Tk()
window.title("Calculator")
window.geometry("260x330")
window.resizable(0, 0)

# Creating a frames for display and buttons
display_frame = LabelFrame()
button_frame  = LabelFrame()
display_frame.pack()
button_frame.pack()

# -------------------------Display--------------------------------

display = Entry(display_frame)
display.config(width=40, borderwidth=10, font=("Arial", 28, "bold"), justify=RIGHT)
display.pack(padx=5, pady=5)

# -------------------------Button 0 to 9, decimal, equal --------------------------------
zero_button     =    Button(button_frame)
one_button      =    Button(button_frame)
two_button      =    Button(button_frame)
three_button    =    Button(button_frame)
four_button     =    Button(button_frame)
five_button     =    Button(button_frame)
six_button      =    Button(button_frame)
seven_button    =    Button(button_frame)
eight_button    =    Button(button_frame)
nine_button     =    Button(button_frame)
decimal_button  =    Button(button_frame)
equal_button    =    Button(button_frame)


# -------------------------Button 0 to 9 & decimal , equal configuration --------------------------------
zero_button.config(text="0", width=3, font=BUTTON_FONT, bg=BUTTON_COLOR, command=lambda: submit_number(0))
one_button.config(text="1", width=3, font=BUTTON_FONT, bg=BUTTON_COLOR, command=lambda: submit_number(1))
two_button.config(text="2", width=3, font=BUTTON_FONT, bg=BUTTON_COLOR, command=lambda: submit_number(2))
three_button.config(text="3", width=3, font=BUTTON_FONT, bg=BUTTON_COLOR, command=lambda: submit_number(3))
four_button.config(text="4", width=3, font=BUTTON_FONT, bg=BUTTON_COLOR, command=lambda: submit_number(4))
five_button.config(text="5", width=3, font=BUTTON_FONT, bg=BUTTON_COLOR, command=lambda: submit_number(5))
six_button.config(text="6", width=3, font=BUTTON_FONT, bg=BUTTON_COLOR, command=lambda: submit_number(6))
seven_button.config(text="7", width=3, font=BUTTON_FONT, bg=BUTTON_COLOR, command=lambda: submit_number(7))
eight_button.config(text="8", width=3, font=BUTTON_FONT, bg=BUTTON_COLOR, command=lambda: submit_number(8))
nine_button.config(text="9", width=3, font=BUTTON_FONT, bg=BUTTON_COLOR, command=lambda: submit_number(9))
decimal_button.config(text=".", width=3, font=BUTTON_FONT, bg=BUTTON_COLOR, command=lambda: submit_number("."))
equal_button.config(text="=", width=3, font=BUTTON_FONT, bg=BUTTON_COLOR, command=equal)

# -------------------------Button Add,Sub,Mul,Div --------------------------------
add_button       =   Button(button_frame)
subtract_button  =   Button(button_frame)
multiply_button  =   Button(button_frame)
divide_button    =   Button(button_frame)

# -------------------------Button Add,Sub,Mul,Div configuration --------------------------------
add_button.config(text="+", width=3 ,font=BUTTON_FONT, bg=BUTTON_COLOR, command=lambda:operate("+"))
subtract_button.config(text="-", width=3, font=BUTTON_FONT, bg=BUTTON_COLOR, command=lambda:operate("-"))
multiply_button.config(text="*", width=3, font=BUTTON_FONT, bg=BUTTON_COLOR, command=lambda:operate("*"))
divide_button.config(text="/", width=3, font=BUTTON_FONT, bg=BUTTON_COLOR, command=lambda:operate("/"))

# -------------------------Button clear, quit, bg, font & Configuration--------------------------------
clear_button     =   Button(button_frame)
quit_button      =   Button(button_frame)
bg_button        =   Button(button_frame)
font_button      =   Button(button_frame)


clear_button.config(text="C", width=3, font=BUTTON_FONT, bg=BUTTON_COLOR, command=clear)
quit_button.config(text="Q", width=3, font=BUTTON_FONT,  bg=BUTTON_COLOR, command=window.destroy)
bg_button.config(text="bg", width=3, font=BUTTON_FONT, bg=BUTTON_COLOR, command=change_color)
font_button.config(text="F", width=3, font=BUTTON_FONT,  bg=BUTTON_COLOR, command=change_font)

# -------------------------Button Position in Grid --------------------------------

# -------------------Zero Row (C,Q,bg,F) buttons--------------------
clear_button.grid(row=0, column=0, sticky="WE", ipadx=3, pady=1)
quit_button.grid(row=0, column=1, sticky="WE", ipadx=3, pady=1)
bg_button.grid(row=0, column=2, sticky="WE", ipadx=3, pady=1)
font_button.grid(row=0, column=3, sticky="WE", ipadx=3, pady=1)

# -------------------First Row (7,8,9,/) buttons--------------------
seven_button.grid(row=1, column=0, sticky="WE", ipadx=3, pady=1)
eight_button.grid(row=1, column=1, sticky="WE", ipadx=3, pady=1)
nine_button.grid(row=1, column=2, sticky="WE", ipadx=3, pady=1)
divide_button.grid(row=1, column=3, sticky="WE", ipadx=3, pady=1)

# -------------------Second Row (4,5,6,*) buttons--------------------
four_button.grid(row=2, column=0, sticky="WE", ipadx=3, pady=1)
five_button.grid(row=2, column=1, sticky="WE", ipadx=3, pady=1)
six_button.grid(row=2, column=2, sticky="WE", ipadx=3, pady=1)
multiply_button.grid(row=2, column=3, sticky="WE", ipadx=3, pady=1)

# -------------------Third Row (1,2,3,-) buttons--------------------
one_button.grid(row=3, column=0, sticky="WE", ipadx=3, pady=1)
two_button.grid(row=3, column=1, sticky="WE", ipadx=3, pady=1)
three_button.grid(row=3, column=2, sticky="WE", ipadx=3, pady=1)
subtract_button.grid(row=3, column=3, sticky="WE", ipadx=3, pady=1)

# -------------------Third Row (.,0,=,+) buttons--------------------
decimal_button.grid(row=4, column=0, sticky="WE", ipadx=3, pady=1)
zero_button.grid(row=4, column=1, sticky="WE", ipadx=3, pady=1)
equal_button.grid(row=4, column=2, sticky="WE", ipadx=3, pady=1)
add_button.grid(row=4, column=3, sticky="WE", ipadx=3, pady=1)

window.mainloop()