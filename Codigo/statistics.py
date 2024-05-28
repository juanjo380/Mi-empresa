from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import subprocess

statistics = Tk()

statistics.title("Mi empresa/version 1.0.0/Estadísticas")
statistics.resizable(False, False)
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
total_encargos = StringVar()
total_encargos.set("Total encargos: 0")
total_encargos = Label(
    statistics,
    textvariable=total_encargos,
    bg='#17202A',
    fg='#FFFFFF'
)

total_encargos.place()
#------------------------------------------
sold_products_var = StringVar()
sold_products_var.set("Productos vendidos: 0")
sold_products_label = Label(
    statistics, 
    textvariable=sold_products_var, 
    bg="#17202A", 
    fg="#FFFFFF"
)

sold_products_label.place(x=100, y=100)
#------------------------------------------
total_earnings_var = StringVar()
total_earnings_var.set("Ganancias totales: 0")
total_earnings_label = Label(
    statistics, 
    textvariable=total_earnings_var, 
    bg="#17202A", 
    fg="#FFFFFF"
)

total_earnings_label.place(x=100, y=140)
#------------------------------------------
total_6A = StringVar()
total_6A.set("Ganancias totales 6A: 0")

total_6A = Label(
    statistics, 
    textvariable=total_6A, 
    bg="#17202A",
    fg="#FFFFFF"
)

total_6A.place(x=100, y=170)
#------------------------------------------
total_6B = StringVar()
total_6B.set("Ganancias totales 6B: 0")

total_6B = Label(
    statistics, 
    textvariable=total_6B, 
    bg="#17202A", 
    fg="#FFFFFF"
)

total_6B.place(x=100, y=190)
#------------------------------------------
total_7A = StringVar()
total_7A.set("Ganancias totales 7A: 0")

total_7A = Label(
    statistics, 
    textvariable=total_7A, 
    bg="#17202A",
    fg="#FFFFFF"
)

total_7A.place(x=100, y=220)
#------------------------------------------
total_7B = StringVar()
total_7B.set("Ganancias totales 7B: 0")

total_7B = Label(
    statistics, 
    textvariable=total_7B, 
    bg="#17202A", 
    fg="#FFFFFF"
)

total_7B.place(x=100, y=260)
#------------------------------------------
total_8A = StringVar()
total_8A.set("Ganancias totales 8A: 0")

total_8A = Label(
    statistics, 
    textvariable=total_8A, 
    bg="#17202A", 
    fg="#FFFFFF"
)

total_8A.place(x=100, y=300)
#------------------------------------------
total_9A = StringVar()
total_9A.set("Ganancias totales 9A: 0")

total_9A = Label(
    statistics, 
    textvariable=total_9A, 
    bg="#17202A", 
    fg="#FFFFFF"
)

total_9A.place(x=100, y=330)
#------------------------------------------
total_10A = StringVar()
total_10A.set("Ganancias totales 10A: 0")

total_10A = Label(
    statistics, 
    textvariable=total_10A, 
    bg="#17202A", 
    fg="#FFFFFF"
)

total_10A.place(x=100, y=370)
#------------------------------------------
total_11A = StringVar()
total_11A.set("Ganancias totales 11A: 0")

total_11A = Label(
    statistics, 
    textvariable=total_11A,
    bg="#17202A", 
    fg="#FFFFFF"
)

total_11A.place(x=100, y=400)
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