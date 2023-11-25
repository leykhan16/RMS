from tkinter import *

import random

import time

import datetime

root = Tk()

root.geometry("1600x800")

root.title("Restaurant Management System")

Tops = Frame(root, width=1600, relief=SUNKEN)

Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)

f1.pack(side=LEFT)

localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font=('helvetica', 50, 'bold'), text="HOTEL BLUE WHALE ", fg="Black", bd=10, anchor='w')

lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')

lblInfo.grid(row=1, column=0)

rand = StringVar()

Fries = StringVar()

Noodles = StringVar()

Soup = StringVar()

Burger = StringVar()

Sandwich = StringVar()

Drinks = StringVar()

Cost = StringVar()

Service_Charge = StringVar()

Tax = StringVar()

SubTotal = StringVar()

Total = StringVar()

def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)

    # Rest of your Ref function code...

    txtCost.delete(0, END)
    txtCost.insert(END, CostofMeal)

    # Rest of your Ref function code...

lblReference = Label(f1, font=('arial', 16, 'bold'), text="Order No.", bd=16, anchor='w')

lblReference.grid(row=0, column=0)

txtReference = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4, width=26,
                     justify='right')

txtReference.grid(row=0, column=1)

lblFries = Label(f1, font=('arial', 16, 'bold'), text="Fries Meal", bd=16, anchor='w')

lblFries.grid(row=1, column=0)

txtFries = Entry(f1, font=('arial', 16, 'bold'), textvariable=Fries, bd=10, insertwidth=4, width=26, justify='right')

txtFries.grid(row=1, column=1)

# Add similar code for other food items (Noodles, Soup, Burger, Sandwich, Drinks)

lblCost = Label(f1, font=('arial', 16, 'bold'), text="Cost of Meal", bd=16, anchor='w')

lblCost.grid(row=7, column=0)

txtCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=4, width=26, justify='right')

txtCost.grid(row=7, column=1)

# Add similar code for other labels and entry widgets (Service_Charge, Tax, SubTotal, Total)

btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Total",
                  bg="powder blue", command=Ref)

btnTotal.grid(row=10, column=1)

# Add similar code for other buttons

root.mainloop()
