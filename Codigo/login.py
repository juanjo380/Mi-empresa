from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import subprocess
from PIL import Image, ImageTk
from data import initiation
from json import dump

login = Tk()
login.title("Mi empresa/version 1.0.0/Iniciar sesión")
screen_width = login.winfo_screenwidth()
screen_height = login.winfo_screenheight()

# Calcula la posición de la ventana
x = (screen_width / 2) - (900 / 2)
y = (screen_height / 2) - (700 / 2) - 50  # Resta 50 para mover la ventana hacia arriba

# Posiciona la ventana en el centro de la pantalla
login.geometry("900x700+%d+%d" % (x, y))
login.configure(bg="#17202A")

image = Image.open("./Images/login.png")
image = image.resize((900, 700))
photo = ImageTk.PhotoImage(image)
label = Label(login, image=photo)
label.place(x=0, y=0)

def open_window_menu_close():
    login.destroy()
    subprocess.call(["python", "Codigo/menu.py"])
#--------------------------------------------------------------
def verify_credentials():
    with open("./datos/registro.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            email, password = line.strip().split(",") 
            
            if email == entry_email.get() and password == entry_password.get():
                messagebox.showinfo("Bienvenido","Bienvenido empresario")
                initiation(email)
                user = {'username': email}
                with open('./datos/user.json', "w") as archivo:
                    dump(user, archivo)
                entry_email.delete(0, 'end')
                entry_password.delete(0, 'end')
                open_window_menu_close()
                return  

        messagebox.showerror("Error", "credenciales incorrectas")
        entry_email.delete(0, 'end')
        entry_password.delete(0, 'end')
#--------------------------------------------------------------
frame_login = Frame(
    login,
    width=100,
    height=100,
    bg="#17202A",
    bd=5
)

frame_login.pack(pady=200)

label_login = Label(
    login,
    text = "Iniciar Sesión",
    font = ("Bahnschrift",15, "bold"),
    bg ="#17202A",
    fg='#ffffff'
)
label_login.place(x=385,y=180)

label_email = Label(
    frame_login,
    text="Correo electrónico",
    font=("Bahnschrift", 15, "bold"),
    bg="#17202A",
    fg='#ffffff'
)  

label_email.pack(pady=10)

entry_email = Entry(
    frame_login, 
    font=("Bahnschrift", 10),
    width=34
)

entry_email.pack(pady=10)

label_password = Label(
    frame_login, 
    text="Contraseña",
    font=("Bahnschrift", 15, "bold"),
    fg='#ffffff',
    bg="#17202A"
)

label_password.pack(pady=10)

entry_password = Entry(
    frame_login,
    font=("Bahnschrift", 10),
    show="•",
    width=34
)
entry_password.pack(pady=10)

login_button = Button(
    login, 
    text="Iniciar sesión", 
    fg="#ffffff", 
    font=("Bahnschrift", 12, "bold"),
    bg="#2E3F52",
    activeforeground='#FFFFFF',
    activebackground='#2E3F52',
    width=15,
    height=1,
    borderwidth=0,
    command=verify_credentials
)
login_button.place(x=370,y=415)

#--------------------------------------------------------------

def back():
    login.destroy()
    subprocess.call(["python", "Codigo/main_window.py"])

button_back = Button(
    login, 
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




login.mainloop()