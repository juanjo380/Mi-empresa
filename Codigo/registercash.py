import pandas as pd
from tkinter import *
from tkinter import messagebox
import subprocess

def back():
    registercash.destroy()
    subprocess.call(["python", "Codigo/menu.py"])

# Carga los datos del archivo CSV en el DataFrame 'df'
df = pd.read_csv('./datos/prueba@gmail.com_pagos.csv')

productos = df.set_index('ID').T.to_dict('list')

def get_updated_data():
    # Carga los datos más recientes del archivo CSV en el DataFrame 'df'
    df = pd.read_csv('./datos/prueba@gmail.com_pagos.csv')
    return df

# Convierte el DataFrame en un diccionario
productos = df.set_index('ID').T.to_dict('list')

# Inicialización de la ventana
registercash = Tk()
registercash.title("Registradora")
registercash.geometry("900x700")
registercash.configure(bg="#17202A")

#----------------------------------------------------------------------
# Variables
total_venta = StringVar()
total_venta.set("Total de la venta: $0")  # Valor inicial

# Creación del Label
total_venta_label = Label(registercash, textvariable=total_venta)

# Colocación del Label
total_venta_label.place(x= 200, y= 400)

def procesar_venta():
    codigo = int(codigo_producto.get())
    cantidad = int(cantidad_producto.get())
    if codigo in productos and cantidad <= int(productos[codigo][4]):  # Si hay suficientes productos en stock
        total = productos[codigo][2] * cantidad  # Calcula el total de la venta
        productos[codigo][4] = int(productos[codigo][4]) - cantidad  # Actualiza la cantidad de productos en stock
        df = pd.DataFrame.from_dict(productos, orient='index')  # Convierte el diccionario actualizado a un DataFrame
        df.to_csv('./datos/prueba@gmail.com_pagos.csv', index_label='ID')  # Guarda el DataFrame actualizado en el archivo CSV
        total_venta.set(f"Total de la venta: ${total}")  # Actualiza el total de la venta
        messagebox.showinfo("Venta procesada", f"El total de la venta es {total}")
    else:
        messagebox.showerror("Error", "No hay suficientes productos en stock")

# Variables
cantidad_producto = StringVar()

# Creación de los widgets
cantidad_producto_label = Label(registercash, text="Cantidad del producto")
cantidad_producto_label.place(x=200,y=200)

cantidad_producto_entry = Entry(registercash, textvariable=cantidad_producto)
cantidad_producto_entry.place(x=350,y=350)


procesar_venta_button = Button(
    registercash, 
    text="Procesar venta", 
    command=procesar_venta
)

procesar_venta_button.place(x=300,y=300)

#----------------------------------------------------------------------

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