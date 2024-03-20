import pandas as pd
from tkinter import *
from tkinter import messagebox
import subprocess

def back():
    registercash.destroy()
    subprocess.call(["python", "Codigo/menu.py"])

# Carga los datos del archivo CSV
df = pd.read_csv('./datos/prueba@gmail.com_pagos.csv')

# Convierte el DataFrame en un diccionario
productos = df.set_index('ID').T.to_dict('list')

# Inicialización de la ventana
registercash = Tk()
registercash.title("Registradora")
registercash.geometry("900x700")
registercash.configure(bg="#17202A")

# Funciones
def autocompletar(*args):
    codigo = codigo_producto.get()
    if codigo:  # Si el campo del código del producto no está vacío
        try:
            codigo = int(codigo)
            if codigo in productos:
                producto = productos[codigo]
                nombre_producto_entry.delete(0, END)
                nombre_producto_entry.insert(0, producto[1])  # Nombre del producto
                precio_producto_entry.delete(0, END)
                precio_producto_entry.insert(0, str(producto[2]))  # Precio del producto
        except ValueError:
            pass  # El código del producto no es un número, ignora
    else:  # Si el campo del código del producto está vacío
        nombre_producto_entry.delete(0, END)
        precio_producto_entry.delete(0, END)

# Variables
codigo_producto = StringVar()
codigo_producto.trace('w', autocompletar)

# Creación de widgets
codigo_producto_label = Label(
    registercash,
    text="Código del producto", 
    bg="#17202A", 
    fg="#FFFFFF"
)

codigo_producto_label.pack()

codigo_producto_entry = Entry(registercash, textvariable=codigo_producto)
codigo_producto_entry.pack()

nombre_producto_label = Label(
    registercash,
    text="Nombre del producto",
    bg="#17202A", 
    fg="#FFFFFF"
)

nombre_producto_label.pack()

nombre_producto_entry = Entry(registercash)
nombre_producto_entry.pack()

precio_producto_label = Label(
    registercash,
    text="Precio del producto", 
    bg="#17202A", 
    fg="#FFFFFF"
)

precio_producto_label.pack()

precio_producto_entry = Entry(registercash)
precio_producto_entry.pack()

button_back = Button(
    registercash, 
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

# Bucle principal
registercash.mainloop()