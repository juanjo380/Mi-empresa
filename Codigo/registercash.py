import pandas as pd
from tkinter import *
from tkinter import messagebox
import subprocess
from json import load
from PIL import ImageTk, Image

with open('./datos/user.json', "r") as archivo:
        datos = load(archivo)
username = datos['username']

def back():
    registercash.destroy()
    subprocess.call(["python", "Codigo/menu.py"])

# Carga los datos del archivo CSV en el DataFrame 'df'
df = pd.read_csv(f"./datos/{username}_pagos.csv")

productos = df.set_index('ID').T.to_dict('list')

# Convierte el DataFrame en un diccionario
productos = df.set_index('ID').T.to_dict('list')

# Inicialización de la ventana
registercash = Tk()
registercash.title("Mi empresa/version 1.0.0/Registradora")
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
        df = pd.DataFrame.from_dict(productos, orient='index' )# Convierte el diccionario actualizado a un DataFrame
        df = df.rename(columns={0:"IDX", 1: "Nombre", 2: "Precio", 3:"Descripción", 4:"Unidades"})
        df.to_csv(f"./datos/{username}_pagos.csv", index_label="ID")  # Guarda el DataFrame actualizado en el archivo CSV
        total_venta.set(f"Total de la venta: ${total}")  # Actualiza el total de la venta
        messagebox.showinfo("Venta procesada", f"El total de la venta es {total}")
    else:
        messagebox.showerror("Error", "No hay suficientes productos en stock")

# Variables
cantidad_producto = StringVar()

# Creación de los widgets
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


procesar_venta_button = Button(
    registercash, 
    text="Procesar venta", 
    command=procesar_venta
)

procesar_venta_button.place(x=500,y=500)

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

pagaCon = Label(
    registercash,
    text="Paga con",
    bg="#232323", 
    fg="#FFFFFF",
    font=("Bahnschrift", 14, "bold")
)
pagaCon.configure(
    bg="#17202A", 
    fg="#FFFFFF",
    font=("Bahnschrift", 14, "bold")
    )

paga_Con_var = StringVar()

paga_Con = Entry(
    registercash,
    textvariable=paga_Con_var  # Asigna la variable de control al Entry
)

paga_Con.place(x=200, y=350)

def calculate_change(total_cost, amount_paid):
    return amount_paid - total_cost

paga_Con_var = StringVar()

paga_Con = Entry(
    registercash,
    textvariable=paga_Con_var  # Asigna la variable de control al Entry
)

devuelta = StringVar()

devuelta_label = Label(
    registercash,
    textvariable=devuelta,  # Asigna la variable de control a la etiqueta
    bg="#17202A", 
    fg="#FFFFFF",
    font=("Bahnschrift", 14, "bold")
)

def on_paga_Con_change(*args):
    total_cost = float(precio_producto_entry.get())  # Asegúrate de que precio_producto_entry esté definido y sea un Entry
    try:
        amount_paid = float(paga_Con_var.get())  # Usa la variable de control para obtener la cantidad pagada
        change = calculate_change(total_cost, amount_paid)
        devuelta.set(f"Devuelta: {change}")  # Actualiza la variable de control con el cambio calculado
    except ValueError:
        # Esto se ejecutará si paga_Con_var no puede convertirse a float, es decir, si el usuario no ha introducido un número válido
        pass

# Configura la función on_paga_Con_change para que se llame cuando la variable paga_Con_var cambie
paga_Con_var.trace("w", on_paga_Con_change)

devuelta_label.place(x=500, y=300)  # Coloca la etiqueta en la interfaz de usuario



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