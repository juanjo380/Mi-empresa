from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import subprocess

statistics = Tk()

statistics.title("Mi empresa/version 1.0.0/Estadísticas")
screen_width = statistics.winfo_screenwidth()
screen_height = statistics.winfo_screenheight()

# Calcula la posición de la ventana
x = (screen_width / 2) - (900 / 2)
y = (screen_height / 2) - (700 / 2) - 50  # Resta 50 para mover la ventana hacia arriba

# Posiciona la ventana en el centro de la pantalla
statistics.geometry("900x700+%d+%d" % (x, y))
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