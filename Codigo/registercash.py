import pandas as pd
from tkinter import *
from tkinter import messagebox
import subprocess
from json import load
from PIL import ImageTk, Image

# Carga los datos del usuario
with open('./datos/user.json', "r") as archivo:
    datos = load(archivo)
username = datos['username']

def back():
    registercash.destroy()
    subprocess.call(["python", "Codigo/menu.py"])

# Carga los datos del archivo CSV en el DataFrame 'df'
df = pd.read_csv(f"./datos/{username}_pagos.csv")

# Convierte el DataFrame en un diccionario
productos = df.set_index('ID').T.to_dict('list')

# Inicialización de la ventana
registercash = Tk()
registercash.title("Mi empresa/version 1.0.0/Registradora")
registercash.resizable(False, False)
screen_width = registercash.winfo_screenwidth()
screen_height = registercash.winfo_screenheight()

# Calcula la posición de la ventana
x = (screen_width / 2) - (900 / 2)
y = (screen_height / 2) - (700 / 2) - 50  # Resta 50 para mover la ventana hacia arriba

# Posiciona la ventana en el centro de la pantalla
registercash.geometry("900x700+%d+%d" % (x, y))
registercash.configure(bg="#17202A")

image = Image.open("./Images/registradora.png")
image = image.resize((900, 700))
photo = ImageTk.PhotoImage(image)
label = Label(registercash, image=photo)
label.place(x=0, y=0)

# Variables
codigo_producto = StringVar()
cantidad_producto = StringVar()
total_venta_text = StringVar()
total_venta_text.set("Total de la venta: $0")

# Creación de los widgets
codigo_producto_label = Label(
    registercash,
    text="Código del producto", 
    font=("Bahnschrift", 14, "bold"),
    bg="#232323", 
    fg="#FFFFFF"
)
codigo_producto_label.place(x=200, y=100)

codigo_producto_entry = Entry(registercash, textvariable=codigo_producto)
codigo_producto_entry.place(x=200, y=150)

nombre_producto_label = Label(
    registercash,
    text="Nombre del producto",
    bg="#232323", 
    fg="#FFFFFF",
    font=("Bahnschrift", 14, "bold")
)
nombre_producto_label.place(x=500, y=100)

nombre_producto_entry = Entry(registercash)
nombre_producto_entry.place(x=500, y=150)

precio_producto_label = Label(
    registercash,
    text="Precio del producto", 
    bg="#232323", 
    fg="#FFFFFF",
    font=("Bahnschrift", 14, "bold")
)
precio_producto_label.place(x=500, y=200)

precio_producto_entry = Entry(registercash)
precio_producto_entry.place(x=500, y=250)

cantidad_producto_label = Label(
    registercash, 
    text="Cantidad del producto",
    bg="#232323",
    fg="#FFFFFF",
    font=("Bahnschrift", 14, "bold")
)
cantidad_producto_label.place(x=200,y=200)

cantidad_producto_entry = Entry(registercash, textvariable=cantidad_producto)
cantidad_producto_entry.place(x=200,y=250)

total_venta_label = Label(registercash, textvariable=total_venta_text, bg="#232323", fg="#FFFFFF", font=("Bahnschrift", 14, "bold"))
total_venta_label.place(x=200, y=450)

def calcular_total(*args):
    try:
        codigo = int(codigo_producto.get())
        cantidad = int(cantidad_producto.get())
        if codigo in productos and cantidad <= int(productos[codigo][4]):  # Si hay suficientes productos en stock
            precio = float(productos[codigo][2])  # Obtiene el precio del producto y lo convierte a un número
            total = precio * cantidad  # Calcula el total de la venta
            total_venta_text.set(f"Total de la venta: ${total:.2f}")  # Actualiza el total de la venta
    except ValueError:
        pass  # Ignora el error si el código o la cantidad no son números enteros

# Llama a calcular_total cuando se cambia el código del producto o la cantidad
codigo_producto.trace("w", calcular_total)
cantidad_producto.trace("w", calcular_total)

def procesar_venta():
    try:
        codigo = int(codigo_producto.get())
        cantidad = int(cantidad_producto.get())
        if codigo in productos and cantidad <= int(productos[codigo][4]):  # Si hay suficientes productos en stock
            productos[codigo][4] = int(productos[codigo][4]) - cantidad  # Actualiza la cantidad de productos en stock
            df = pd.DataFrame.from_dict(productos, orient='index')  # Convierte el diccionario actualizado a un DataFrame
            df = df.rename(columns={0:"IDX", 1: "Nombre", 2: "Precio", 3:"Descripción", 4:"Unidades"})
            df.to_csv(f"./datos/{username}_pagos.csv", index_label="ID")  # Guarda el DataFrame actualizado en el archivo CSV
            messagebox.showinfo("Venta procesada", f"El total de la venta es {total_venta_text.get()}")
        else:
            messagebox.showerror("Error", "No hay suficientes productos en stock")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un código y una cantidad válidos")

procesar_venta_button = Button(
    registercash, 
    text="Procesar venta", 
    command=procesar_venta
)
procesar_venta_button.configure(
    bg="#222323",
    fg="#FFFFFF",
    font=("Bahnschrift", 14, "bold"),
    borderwidth=0,
    compound="center",
    activeforeground='#FFFFFF',
    activebackground='#222323'
)
procesar_venta_button.place(x=360, y=530)

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

codigo_producto.trace('w', autocompletar)

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

registercash.mainloop()
