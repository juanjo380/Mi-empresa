from tkinter import *
from tkinter import messagebox
import pandas as pd
import os
import subprocess

def volver():
    statistics.destroy()
    subprocess.call(["python", "Codigo/menu.py"])

def cargar_estadisticas():
    if not os.path.exists('./datos/Estudiantes.csv'):
        messagebox.showerror("Error", "No se pudo encontrar el archivo CSV.")
        return

    df = pd.read_csv('./datos/Estudiantes.csv', encoding='utf-8')

    # Filtra los datos para incluir solo aquellos donde el campo 'Pedido' no esté vacío
    df = df[df['Pedido'].notna() & (df['Pedido'] != '')]

    # Impresiones de depuración
    print("Datos filtrados:")
    print(df)

    # Grupos de grados
    grados = ["6A", "6B", "7A", "7B", "8A", "9A", "10A", "11A"]
    resultados = {grado: 0.0 for grado in grados}  # Diccionario para almacenar resultados por grado

    # Iterar sobre cada grado
    for grado in grados:
        # Filtrar los datos para el grado actual
        datos = df[df['ID'] == grado]

        # Extraer los precios de los encargos y sumarlos
        total_precio = datos['Precio'].replace('', 0).astype(float).sum()

        # Almacenar el total en el diccionario de resultados
        resultados[grado] = total_precio

    # Impresiones de depuración
    print("Resultados:")
    print(resultados)

    # Actualiza la interfaz gráfica con los resultados
    for grado, total in resultados.items():
        label_text = f"Grado {grado}: Total Ganancias de encargos = ${total:.2f}"
        Label(statistics, text=label_text, font=("Bahnschrift", 14), bg='#17202A', fg="#FFFFFF").pack(anchor='w', padx=20, pady=5)


statistics = Tk()
statistics.title("Mi empresa/version 1.0.0/Estadísticas")
statistics.resizable(False, False)
screen_width = statistics.winfo_screenwidth()
screen_height = statistics.winfo_screenheight()

# Calcula la posición de la ventana
x = (screen_width / 2) - (900 / 2)
y = (screen_height / 2) - (700 / 2) - 50  # Resta 50 para mover la ventana hacia arriba

# Posiciona la ventana en el centro de la pantalla
statistics.geometry("900x700+%d+%d" % (x, y))
statistics.configure(bg="#17202A")

label_title = Label(
    statistics, 
    text="Estadísticas", 
    font=("Bahnschrift", 28, "bold"), 
    bg='#232323', 
    fg="#FFFFFF"
)
label_title.pack(pady=20)

button_volver = Button(
    statistics, 
    text="Volver",
    borderwidth=0, 
    compound="center",
    activeforeground='#FFFFFF',
    activebackground='#222323',
    command=volver
)
button_volver.configure(
    font=("Bahnschrift", 14, "bold"), 
    bg='#222323', 
    fg="#FFFFFF"
)
button_volver.place(x=10, y=10)

label_ventas = Label(
    statistics, 
    text="", 
    font=("Bahnschrift", 14), 
    bg='#17202A', 
    fg="#FFFFFF"
)

label_ventas.pack(
    anchor='w', 
    padx=20, 
    pady=5
)

cargar_estadisticas()  # Llama a la función después de que la ventana se haya creado y mostrado

statistics.mainloop()