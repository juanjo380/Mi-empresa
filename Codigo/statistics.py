from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import subprocess

statistics = Tk()

statistics.title("Estadísticas")
statistics.geometry("900x700")
statistics.configure(bg="#17202A")


def back():
    statistics.destroy()
    subprocess.call(["python", "Codigo/menu.py"])
#------------------------------------------
sold_products_var = StringVar()
sold_products_var.set("Productos vendidos: 0")
sold_products_label = Label(statistics, textvariable=sold_products_var, bg="#17202A", fg="#FFFFFF")
sold_products_label.place(x=100, y=100)
#------------------------------------------
total_earnings_var = StringVar()
total_earnings_var.set("Ganancias totales: 0")
total_earnings_label = Label(statistics, textvariable=total_earnings_var, bg="#17202A", fg="#FFFFFF")
total_earnings_label.place(x=100, y=130)  
#------------------------------------------
button_back = Button(
    statistics, 
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

statistics.mainloop()