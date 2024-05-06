from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import subprocess
from PIL import Image, ImageTk

menu = Tk()
menu.title("Mi empresa/version 1.0.0/Menu")
menu.resizable(False, False)
screen_width = menu.winfo_screenwidth()
screen_height = menu.winfo_screenheight()

# Calcula la posición de la ventana
x = (screen_width / 2) - (900 / 2)
y = (screen_height / 2) - (700 / 2) - 50  # Resta 50 para mover la ventana hacia arriba

# Posiciona la ventana en el centro de la pantalla
menu.geometry("900x700+%d+%d" % (x, y))
menu.configure(bg="#17202A")

def back():
    menu.destroy()
    subprocess.call(["python", "Codigo/main_window.py"])

def add_products():
    menu.destroy()
    subprocess.call(["python", "Codigo/add_products.py"])

def registercash():
    menu.destroy()
    subprocess.call(["python", "Codigo/registercash.py"])

def products():
    menu.destroy()
    subprocess.call(["python","Codigo/products.py"])

def orders():
    menu.destroy()
    subprocess.call(["python","Codigo/orders.py"])

#def statistics():
    #menu.destroy()
    #subprocess.call(["python","Codigo/statistics.py"])

image = Image.open("./Images/menu.png")
image = image.resize((900, 700))
photo = ImageTk.PhotoImage(image)
label = Label(menu, image=photo)
label.place(x=0, y=0)

label = Label(
    menu,
    text="¿Qué deseas hacer?", 
    font=("Bahnschrift", 18, "bold"), 
    bg='#222323', 
    fg="#FFFFFF"
)

label.place(x=350, y=30)

button_back = Button(
    menu, 
    text="Volver",
    borderwidth=0, 
    compound="center",
    activeforeground='#FFFFFF',
    activebackground='#222323',
    command=back
)

button_back.configure(
    font=("Bahnschrift", 14, "bold"), 
    bg='#222323', 
    fg="#FFFFFF"
)

button_back.place(x=10, y=10)

button_addproducts = Button(
    menu, 
    text="Añadir productos",
    borderwidth=0, 
    compound="center",
    activeforeground='#FFFFFF',
    activebackground='#232323',
    command=add_products
)

button_addproducts.configure(
    font=("Bahnschrift", 14, "bold"), 
    bg='#232323', 
    fg="#FFFFFF"
)

button_addproducts.place(x=350, y=130)
#--------------------------------------------#
button_products = Button(
    menu, 
    text="Productos",
    borderwidth=0, 
    compound="center",
    activeforeground='#FFFFFF',
    activebackground='#232323',
    command=products
)

button_products.configure(
    font=("Bahnschrift", 14, "bold"), 
    bg='#232323', 
    fg="#FFFFFF"
)

button_products.place(x=350, y=230)
#--------------------------------------------#
button_orders = Button(
    menu, 
    text="Pedidos",
    borderwidth=0, 
    compound="center",
    activeforeground='#FFFFFF',
    activebackground='#232323',
    command=orders
)

button_orders.configure(
    font=("Bahnschrift", 14, "bold"), 
    bg='#232323', 
    fg="#FFFFFF"
)

button_orders.place(x=350, y=340)

button_register_cash = Button(
    menu, 
    text="Registradora",
    borderwidth=0, 
    compound="center",
    activeforeground='#FFFFFF',
    activebackground='#232323',
    command=registercash
)

button_register_cash.configure(
    font=("Bahnschrift", 14, "bold"), 
    bg='#232323', 
    fg="#FFFFFF"
)

button_register_cash.place(x=350, y=440)

button_statistics = Button(
    menu, 
    text="Estadisticas",
    borderwidth=0, 
    compound="center",
    activeforeground='#FFFFFF',
    activebackground='#232323',
    #command=statistics
)

button_statistics.configure(
    font=("Bahnschrift", 14, "bold"), 
    bg='#232323', 
    fg="#FFFFFF"
)

button_statistics.place(x=350, y=540)



menu.mainloop()