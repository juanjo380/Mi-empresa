from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import subprocess
from PIL import Image, ImageTk

aboutus = Tk()

image = Image.open("./Images/acerca.png")
image = image.resize((900, 700))
photo = ImageTk.PhotoImage(image)
label = Label(aboutus, image=photo)
label.place(x=0, y=0)

aboutus.title("Mi empresa/version 1.0.0/Acerca de mi")
screen_width = aboutus.winfo_screenwidth()
screen_height = aboutus.winfo_screenheight()

# Calcula la posición de la ventana
x = (screen_width / 2) - (900 / 2)
y = (screen_height / 2) - (700 / 2) - 50  # Resta 50 para mover la ventana hacia arriba

# Posiciona la ventana en el centro de la pantalla
aboutus.geometry("900x700+%d+%d" % (x, y))
aboutus.configure(bg="#17202A")

def back():
    aboutus.destroy()
    subprocess.call(["python", "Codigo/main_window.py"])

button_back = Button(
    aboutus, 
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


text = Label(
    aboutus,
    text='''
    He creado "Mi empresa" para ti, 
    con el fin de ayudar a tu empresa
    a tener un mejor control
    de sus ventas y productos.

    La contabilidad es, 
    la herramienta más importante 
    para cualquier empresa,
    ya que, nos permite saber 
    como llevamos nuestro negocio
    y que tan bien o mal nos va.

    _______________________________________

    Juan José Bolaños (Desarrollador)
    Egresado del Colegio Mayor ciudad de buga
    Actual estudiante de la universidad del valle
    Ingenierio en sistemas en proceso

    "Si la pasión te impulsa, deja que la razón tome las riendas"
    -Benjamin Franklin

    -Contactanos-
    Correo: juanjobose380@gmail.com
    Número: +57 317 605 5855

    ''',
    justify=LEFT,
    bg="#232323"
)

text.configure(
    font=("Bahnschrift", 14, "bold"),
    fg="#FFFFFF"
)

text.place(x=5, y=50)
aboutus.mainloop()