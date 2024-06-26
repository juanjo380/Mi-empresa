from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import subprocess
from PIL import Image, ImageTk


user_data = None

#Ventana de resgistro
def registerwindow():
    mainwindow.destroy()
    subprocess.call(["python", "Codigo/register.py"])

#Ventana de inicio de sesion
def loginwindow():
    mainwindow.destroy()
    subprocess.call(["python", "Codigo/login.py"])
    


#Ventana informacion
def aboutuswindow():
    mainwindow.destroy()
    subprocess.call(["python", "Codigo/aboutus.py"])

mainwindow = Tk()

#caracteristicas de la ventana
mainwindow.title("Mi empresa/version 1.0.0/")
mainwindow.resizable(False, False)
screen_width = mainwindow.winfo_screenwidth()
screen_height = mainwindow.winfo_screenheight()

# Calcula la posición de la ventana
x = (screen_width / 2) - (900 / 2)
y = (screen_height / 2) - (700 / 2) - 50  # Resta 50 para mover la ventana hacia arriba

# Posiciona la ventana en el centro de la pantalla
mainwindow.geometry("900x700+%d+%d" % (x, y))
mainwindow.configure(bg="#17202A")

# Imagen de fondo
image = Image.open("./Images/Fondo.png")
image = image.resize((900, 700))
photo = ImageTk.PhotoImage(image)
label = Label(mainwindow, image=photo)
label.place(x=0, y=0)


button_register = Button(
    mainwindow, 
    text="Registrarse",
    borderwidth=0, 
    compound="center",
    activeforeground='#FFFFFF',
    command=registerwindow
)
button_register.configure(
    font=("Bahnschrift", 14, "bold"), 
    bg='#020304', 
    fg="#FFFFFF"
)
button_register.place(x=5, y=10)

#---------------------------------------------------------------------

# Log in button
button_login = Button(
    mainwindow, 
    text = "Iniciar sesión",
    borderwidth=0, 
    compound="center",
    activeforeground='#FFFFFF',
    command=loginwindow
)
button_login.configure(
    font=("Bahnschrift", 14, "bold"), 
    bg='#020304', 
    fg="#FFFFFF"
)
button_login.place(x=120, y=10)

button_about = Button(
    mainwindow, 
    text = "Acerca de nosotros",
    borderwidth=0, 
    compound="center",
    activeforeground='#FFFFFF',
    command=aboutuswindow
)

button_about.configure(
    font=("Bahnschrift", 14, "bold"), 
    bg='#020304', 
    fg="#FFFFFF"
)
button_about.place(x=250, y=10)

mainwindow.mainloop()