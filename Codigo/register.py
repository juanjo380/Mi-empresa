from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import subprocess
from PIL import Image, ImageTk
import hashlib

register = Tk()

register.title("Registrarse")
screen_width = register.winfo_screenwidth()
screen_height = register.winfo_screenheight()

# Calcula la posición de la ventana
x = (screen_width / 2) - (900 / 2)
y = (screen_height / 2) - (700 / 2) - 50  # Resta 50 para mover la ventana hacia arriba

# Posiciona la ventana en el centro de la pantalla
register.geometry("900x700+%d+%d" % (x, y))
register.configure(bg="#17202A")

def back():
    register.destroy()
    subprocess.call(["python", "Codigo/main_window.py"])

def open_window_login_close():
    register.destroy()  # Close current window
    subprocess.call(["python", "Codigo/login.py"])  # Open window login.py

def validate_and_register():
    email = entry_email.get()
    password = entry_password.get()
    domains = [
          "gmail.com",
          "hotmail.com", 
          "yahoo.com", 
          "outlook.com", 
          "correounivalle.com", 
          "gmail.co", "hotmail.co", 
          "yahoo.co", "outlook.co", 
          "correounivalle.co"
    ]

    if "@" not in email or not any(domain in email for domain in domains):
        messagebox.showerror("Error", "Correo inválido")
        return

    password_encrypted = hashlib.sha256(password.encode()).hexdigest()


    registered_users = []
    try:
        with open('./datos/registro.txt', 'r') as f:
            registered_users = [line.strip().split(', ') for line in f]
    except FileNotFoundError:
            
            # Check if email is already registered
            if any(user[0] == email for user in registered_users):
                messagebox.showerror("Error", "Correo ya registrado")
                entry_email.delete(0, 'end')
                return

            # Check if password is already used
            elif any(user[1] == password for user in registered_users):
                messagebox.showerror("Error", "Contraseña pobre")

    # Register new user in registro_inicio.txt
    with open('./datos/registro.txt', 'a') as f:
        f.write(f"{email},{password}\n")

    # Register new user in plane.txt with encrypted password
    with open('./datos/encry.txt', 'a') as f:
        f.write(f"{email},{password_encrypted}\n")

    messagebox.showinfo("Registro exitoso", "Usuario registrado correctamente")
    
    entry_email.delete(0, 'end')
    entry_password.delete(0, 'end')
    entrance_repeat_password.delete(0, 'end')
    
    #open_window_login_close() # Open window login.py when register is successfull


def check_email(*args):
    email = email_var.get()
    with open('./datos/registro.txt', 'r') as f:
        if any(user.split(',')[0] == email for user in f):
            messagebox.showerror("Error", "Este correo  ya está en uso.")
            entry_email.delete(0, 'end')


# Function for check password
def check_password(*args):
    password = password_var.get()
    with open('./datos/registro.txt', 'r') as f:
        if any(user.split(',')[1].strip() == password for user in f):
            messagebox.showerror("Error", "Contraseña no recomendada.")
            entry_password.delete(0, 'end')


# Function for check password
def check_repeat_password(*args):
    password = password_var.get()
    repeat_password = repeat_password_var.get()
    if len(password) == len(repeat_password) and password != repeat_password:
        messagebox.showerror("Error", "Contraseñas no coinciden")
        repeat_password_var.set('')



#--------------------------------------------------------------------------
image = Image.open("./Images/registro.png")
image = image.resize((900, 700))
photo = ImageTk.PhotoImage(image)
label = Label(register, image=photo)
label.place(x=0, y=0)


# Frame title main
frame_main_title = Frame(register, width=170, height=30, bg="#17202A")
frame_main_title.place(x=350, y=155)
title_main_frame = Label(
        frame_main_title,
        text="Registro",
        font=("Bahnschrift", 16, "bold"),
        fg='#FFFFFF',
        bg="#17202A"
)
title_main_frame.place(x=48, y=1)

#-------------------------------------------------------------------------

# Frame email
frame_email = Frame(register, width=190, height=80, bg="#17202A")
frame_email.place(x=350, y=218)
title_email = Label(
        frame_email,
        text="Correo electrónico",
        font=("Bahnschrift", 12),
        fg='#ffffff',
        bg="#17202A"
)
title_email.place(x=1, y=1)

email_var = StringVar(register)
email_var.trace("w", check_email)

entry_email = Entry(
    frame_email,
    font=("Bahnschrift", 10), 
    width=34
)
entry_email.place(x=1, y=30)
#-------------------------------------------------------------------------
# Frame password
frame_password = Frame(register, width=190, height=80, bg="#17202A")
frame_password.place(x=350, y=288)
title_pasword = Label(
        frame_password,
        text="Contraseña",
        font=("Bahnschrift", 12),
        fg='#ffffff',
        bg="#17202A"
)
title_pasword.place(x=1, y=1)

password_var = StringVar(register)
password_var.trace("w", check_password)

entry_password = Entry(
    frame_password,
    textvariable=password_var, 
    borderwidth=0, 
    font=("Bahnschrift", 10),
    width=34,
    show="•"
)
entry_password.place(x=1, y=30)

#-----------------------------------------------------------------------
repeat_password_var = StringVar()
repeat_password_var.trace("w", check_repeat_password)
# Container password all
frame_repeat_password = Frame(
    register, 
    width=190, 
    height=89, 
    bg="#17202A"
)
frame_repeat_password.place(x=350, y=358)
title_repeatpass = Label(
    frame_repeat_password,
    text="Confirmar contraseña",
    font=("Bahnschrift", 12),
    fg='#ffffff',
    bg="#17202A"
)
title_repeatpass.place(x=1, y=1)

repeat_password_var = StringVar()
repeat_password_var.trace("w", check_repeat_password)

# Variable for check password

entrance_repeat_password = Entry(
    frame_repeat_password,
    textvariable=repeat_password_var,
    font=("Bahnschrift", 10),
    width=34,
    show="•"
)
entrance_repeat_password.place(x=1, y=26)



#---------------------------------------------------------------------

# Button register
button_register = Button(
    register, 
    text="Registrarse",
    borderwidth=0, 
    compound="center",
    activeforeground='#FFFFFF',
    activebackground='#2E3F52',
    command=validate_and_register
)

button_register.configure(
    font=("Bahnschrift", 14, "bold"), 
    bg='#2E3F52', 
    fg="#FFFFFF"
)

button_register.place(x=380, y=450)

button_back = Button(
    register, 
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


register.mainloop()