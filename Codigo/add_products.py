from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk
from data import add_product
from json import load



#--------------------------------------------------------------
window_addproducts = Tk()
window_addproducts.title("Mi empresa/version 1.0.0/añadir productos")
window_addproducts.resizable(False, False)
screen_width = window_addproducts.winfo_screenwidth()
screen_height = window_addproducts.winfo_screenheight()

# Calcula la posición de la ventana
x = (screen_width / 2) - (900 / 2)
y = (screen_height / 2) - (700 / 2) - 50  # Resta 50 para mover la ventana hacia arriba

# Posiciona la ventana en el centro de la pantalla
window_addproducts.geometry("900x700+%d+%d" % (x, y))
window_addproducts.configure(bg="#17202A")

#--------------------------------------------------------------

image = Image.open("./Images/añadir.png")
image = image.resize((900, 700))
photo = ImageTk.PhotoImage(image)
label = Label(window_addproducts, image=photo)
label.place(x=0, y=0)

#--------------------------------------------------------------
def add_product_table():
    with open('./datos/user.json', "r") as archivo:
        datos = load(archivo)
    Id = add_product(datos['username'], [dish_name.get(), price_dish.get(), description_dish.get(), availability_dish.get()])
    messagebox.showinfo("Éxito", "Se ha guardado exitosamente")
    dish_name.delete(0, 'end')
    price_dish.delete(0, 'end')
    description_dish.delete(0, 'end')
    availability_dish.delete(0, 'end')
#--------------------------------------------------------------

def eliminar_producto():
    pass

#--------------------------------------------------------------

def back():
    window_addproducts.destroy()
    subprocess.call(["python", "Codigo/menu.py"])

button_back = Button(
    window_addproducts, 
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

#--------------------------------------------------------------

name_dish = Label(
    window_addproducts,
    text="Nombre"
)

name_dish.config(
    font=("Bahnschrift", 12, "bold"),
    bg="#232323",
    fg="#FFFFFF"
)

name_dish.place(x=250, y=200)

# Label description


desc_dish = Label(
    window_addproducts, 
    text="Descripción"
)

desc_dish.config(
    font=("Bahnschrift", 12, "bold"),
    bg="#232323",
    fg="#FFFFFF"
)

desc_dish.place(x=250, y=300)
#--------------------------------------------------------------

price_dish = Label(
    window_addproducts, 
    text="Precio"
)

price_dish.config(
    font=("Bahnschrift", 12, "bold"),
    bg="#232323",
    fg="#FFFFFF"
)
price_dish.place(x=500, y=200)
#--------------------------------------------------------------

avaiable_dish = Label(
    window_addproducts, 
    text="Unidades disponibles"
)

avaiable_dish.config(
    font=("Bahnschrift", 12, "bold"),
    bg="#232323",
    fg="#FFFFFF"
)
avaiable_dish.place(x=500, y=300)

#--------------------------------------------------------------

# Entries
var_name = StringVar()
dish_name = Entry(window_addproducts, textvariable=var_name)
dish_name.place(x=250, y=230)

# Entry description

# Temporal Value
var_description = StringVar()
#--------------------------------------------------------------
description_dish = Entry(window_addproducts, textvariable=var_description)
description_dish.place(x=250, y=335)

# Entry price

# Temporal Value
var_price = StringVar()

price_dish = Entry(window_addproducts, textvariable=var_price)
price_dish.place(x=500, y=230)

# Entry availability

# Temporal Value
var_availability = StringVar()

availability_dish = Entry(window_addproducts, textvariable=var_availability)
availability_dish.place(x=500, y=335)

#--------------------------------------------------------------

# Buttons

# Button add
add_info_button = Button(window_addproducts, text="Añadir")
add_info_button.configure(
    width=15,
    height=1,
    bg="#2275ae",
    fg="#FFFFFF",
    borderwidth=0,
    compound="center",
    font=("Bahnschrift", 15, "bold"),
    command=add_product_table
)
add_info_button.place(x=350, y=415)

# Label title add dishes
title_restaurant_dish = Label(
    window_addproducts, 
    text="Añade un producto!"
)

title_restaurant_dish.configure(
    font=("Bahnschrift", 20, "bold"), 
    bg="#232323",
    fg="#FFFFFF",
)
title_restaurant_dish.place(x=320, y=150)


window_addproducts.mainloop()