from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
from PIL import ImageTk, Image
import pandas as pd
import os

orders = Tk()

orders.title("Pedidos")
orders.geometry("1200x700")
orders.configure(bg="#17202A")
orders.resizable(False, False)

# Verifica que el archivo CSV existe
if not os.path.exists('./datos/Estudiantes.csv'):
    print("No se pudo encontrar el archivo CSV.")
else:
    # Lee el archivo CSV
    df = pd.read_csv('./datos/Estudiantes.csv', encoding='ISO-8859-1')

    # Crea la tabla
    tabla = ttk.Treeview(orders)

    # Configura las columnas de la tabla
    tabla['columns'] = list(df.columns)
    for column in df.columns:
        tabla.column('#0', width=0, stretch=NO)
        tabla.heading('#0', text='', anchor=CENTER)
        tabla.column(column, width=100)
        tabla.heading(column, text=column)

    # Agrega las filas a la tabla
    for index, row in df.iterrows():
        tabla.insert('', 'end', values=list(row))

    # Coloca la tabla en la interfaz de usuario
    tabla.place(x=200,y=200)

#--------------------------------------------------------------------------

def search_student():
    studentcode = search_entry.get()
    
    for row in tabla.get_children():
        if str(tabla.item(row)['values'][0]) == studentcode:
            tabla.selection_set(row)
            return

search_entry = Entry(
    orders,
    font=("Bahnschrift", 14),
    borderwidth=0
)

search_entry.place(x=200, y=150)

search_button = Button(
    orders, 
    text="Buscar",
    borderwidth=0, 
    compound="center",
    activeforeground='#FFFFFF',
    activebackground='#222323',
    command=search_student
)

search_button.configure(
    font=("Bahnschrift", 14, "bold"), 
    bg='#222323', 
    fg="#FFFFFF"
)

search_button.place(x=400, y=150)

#--------------------------------------------------------------------------
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

label.place(x=500, y=100)

#------------------------------------------------------------------

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