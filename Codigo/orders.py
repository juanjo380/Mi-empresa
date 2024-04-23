from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
from PIL import ImageTk, Image
import pandas as pd
import os
import csv

orders = Tk()

orders.title("Mi empresa/version 1.0.0/Pedidos")
orders.resizable(False, False)
screen_width = orders.winfo_screenwidth()
screen_height = orders.winfo_screenheight()

# Calcula la posición de la ventana
x = (screen_width / 2) - (900 / 2)
y = (screen_height / 2) - (700 / 2) - 50  # Resta 50 para mover la ventana hacia arriba

# Posiciona la ventana en el centro de la pantalla
orders.geometry("1000x700+%d+%d" % (x, y))
orders.configure(bg="#17202A")
orders.resizable(False, False)

image = Image.open("./Images/pedidos.png")
image = image.resize((1000, 700))
photo = ImageTk.PhotoImage(image)
label = Label(orders, image=photo)
label.place(x=0, y=0)

# Verifica que el archivo CSV existe
if not os.path.exists('./datos/Estudiantes.csv'):
    print("No se pudo encontrar el archivo CSV.")
else:
    # Lee el archivo CSV
    df = pd.read_csv('./datos/Estudiantes.csv', encoding='utf-8')

    # Crea la tabla
    tabla = ttk.Treeview(orders)

    # Configura las columnas de la tabla
tabla['columns'] = ('ID','Estudiante','Pedido','Precio','Abono')

#columnas
tabla.column('#0', width=0, stretch=NO)
tabla.column('ID', anchor=CENTER, width=50)
tabla.column('Estudiante', anchor=CENTER, width=230)
tabla.column('Pedido', anchor=CENTER, width=200)
tabla.column('Precio', anchor=CENTER, width=100)
tabla.column('Abono', anchor=CENTER, width=100)

# Encabezado de las columnas
tabla.heading('#0', text='', anchor=CENTER)
tabla.heading('ID', text='ID', anchor=CENTER)
tabla.heading('Estudiante', text='Estudiante', anchor=CENTER)
tabla.heading('Pedido', text='Pedido', anchor=CENTER)
tabla.heading('Precio', text='Precio', anchor=CENTER)
tabla.heading('Abono', text='Abono', anchor=CENTER)


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
            tabla.see(row)  # Desplaza la vista de la tabla hasta el estudiante seleccionado
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
    text="--Pedidos--",
    bg="#232323",
    fg="#FFFFFF"
)

label.configure(
    font=("Bahnschrift", 28, "bold")
)

label.place(x=500, y=100)

#------------------------------------------------------------------

def pedido():
    # Obtiene el estudiante seleccionado de la tabla
    selected = tabla.selection()

    if selected:
        # Crea una nueva ventana
        order_window = Toplevel(orders)
        order_window.title("Agregar pedido")

        # Crea las entradas para el pedido y el precio
        order_entry = Entry(order_window)
        order_entry.pack()
        price_entry = Entry(order_window)
        price_entry.pack()

        # Crea un botón para agregar el pedido y el precio al estudiante
        add_button = Button(order_window, text="Agregar", command=lambda: add_order(selected[0], order_entry.get(), price_entry.get()))
        add_button.pack()
    else:
        print("No se seleccionó ningún estudiante.")

def add_order(student, order, price):
    # Obtiene los valores del estudiante
    values = tabla.item(student)['values']

    # Agrega el pedido y el precio a los valores del estudiante
    values.append(order)
    values.append(price)

    # Actualiza el estudiante en la tabla
    tabla.item(student, values=values)

    # Agrega el pedido y el precio al archivo CSV
    with open('./datos/Estudiantes.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(values)

    tabla.update()


button_order = Button(
    orders, 
    text="Hacer Pedido",
    borderwidth=0, 
    compound="center",
    activeforeground='#FFFFFF',
    activebackground='#222323',
    command=pedido,
    
)

button_order.configure(
    font=("Bahnschrift", 14, "bold"), 
    bg='#222323', 
    fg="#FFFFFF"
)

button_order.place(x=200, y=450)

#------------------------------------------------------------------

def abono():
    pass

button_abono = Button(
    orders, 
    text="Abonar Pedido",
    borderwidth=0, 
    compound="center",
    activeforeground='#FFFFFF',
    activebackground='#222323',
)

button_abono.configure(
    font=("Bahnschrift", 14, "bold"), 
    bg='#222323', 
    fg="#FFFFFF"
)

button_abono.place(x=400, y=450)
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