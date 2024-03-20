from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
from PIL import ImageTk, Image

orders = Tk()

orders.title("Pedidos")
orders.geometry("900x700")
orders.configure(bg="#17202A")
orders.resizable(False, False)


def back():
    orders.destroy()
    subprocess.call(["python","Codigo/menu.py"])

label = Label(
    orders, 
    text="Pedidos",
    bg="#17202A",
    fg="#FFFFFF"
)

label.configure(
    font=("Bahnschrift", 28, "bold")
)

label.place(x=340, y=150)

button_back = Button(
    orders, 
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


orders.mainloop()