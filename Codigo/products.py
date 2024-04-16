from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk
from json import load
import pandas as pd
import os
from data import get_updated_data


product_window = Tk()

#------------------------------------------------------

image = Image.open("./Images/productos.png")
image = image.resize((900, 700))
photo = ImageTk.PhotoImage(image)
label = Label(product_window, image=photo)
label.place(x=0, y=0)

#------------------------------------------------------

product_window.title("Productos")
screen_width = product_window.winfo_screenwidth()
screen_height = product_window.winfo_screenheight()

# Calcula la posición de la ventana
x = (screen_width / 2) - (900 / 2)
y = (screen_height / 2) - (700 / 2) - 50  # Resta 50 para mover la ventana hacia arriba

# Posiciona la ventana en el centro de la pantalla
product_window.geometry("900x700+%d+%d" % (x, y))
product_window.configure(bg="#17202A")

def back():
    product_window.destroy()
    subprocess.call(["python","Codigo/menu.py"])
#label
label = Label(
    product_window, 
    text="Tus productos",
    bg="#A3051A",
    fg="#FFFFFF"
)

label.configure(
    font=("Bahnschrift", 28, "bold")
)

label.place(x=350, y=130)
#tabla
table = ttk.Treeview(product_window)

# Def columnas
with open('./datos/user.json', "r") as archivo:
        datos = load(archivo)
username = datos['username']
df = pd.read_csv(f"./datos/{username}_pagos.csv")

table['columns'] = ('ID','Nombre','Precio', 'Descripción','Unidades disponibles')

#columnas
table.column('#0', width=0, stretch=NO)
table.column('ID', anchor=CENTER, width=100)
table.column('Nombre', anchor=CENTER, width=120)
table.column('Descripción', anchor=W, width=200)
table.column('Precio', anchor=CENTER, width=120)
table.column('Unidades disponibles', anchor=CENTER, width=120)

#encabezados de las columnas
table.heading('#0', text='', anchor=CENTER)
table.heading('ID', text='ID', anchor=CENTER)
table.heading('Nombre', text='Nombre', anchor=CENTER)
table.heading('Descripción', text='Descripción', anchor=CENTER)
table.heading('Precio', text='Precio', anchor=CENTER)
table.heading('Unidades disponibles', text='Unidades disponibles', anchor=CENTER)

# Limpia la tabla
for i in table.get_children():
    table.delete(i)

# Obtiene los datos actualizados
df = get_updated_data(username)

for index, row in df.iterrows():
    try:
        # Intenta insertar los valores en la tabla
        table.insert('', 'end', values=(row['ID'], row['Nombre'], row['Precio'], row['Descripción'], row['Unidades']))
    except Exception as e:
        # Imprime cualquier error que ocurra
        print(f"Error al insertar fila {index}: {e}")

#--------------------------------------------------------------
table.place(x=120, y=250)
#--------------------------------------------------------------
back_button = Button(
    product_window, 
    text="Volver",
    borderwidth=0, 
    compound="center",
    activeforeground='#FFFFFF',
    activebackground='#222323',
    command=back
)

back_button.configure(
    font=("Bahnschrift", 14, "bold"), 
    bg='#222323', 
    fg="#FFFFFF"
)

back_button.place(x=10, y=10)

def search_product():
    # Obtén el código del producto de la entrada
    product_code_or_name = search_entry.get()

    # Recorre todas las filas de la tabla
    for row in table.get_children():
        # Si el código del producto o el nombre en la fila coincide con el código del producto o el nombre buscado
        if str(table.item(row)['values'][0]) == product_code_or_name or table.item(row)['values'][1] == product_code_or_name:
            # Selecciona la fila
            table.selection_set(row)
            return
        
    # Si el producto no se encuentra, muestra un mensaje
    messagebox.showinfo("Error", "Producto no encontrado")

# Entry para la búsqueda
search_entry = Entry(product_window, borderwidth=0, bg="#FFFFFF", fg="#17202A")
search_entry.place(x=120, y=210)

# Botón para la búsqueda
search_button = Button(
    product_window, 
    text="Buscar",
    command=search_product, 
    borderwidth=0, 
    bg="#A3051A", 
    fg="#FFFFFF"
)

search_button.configure(font=("Bahnschrift", 13, "bold"))
search_button.place(x=220, y=200)

product_window.mainloop()