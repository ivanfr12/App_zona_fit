import tkinter as tk
from tkinter import ttk


# Creamos una ventana
ventana = tk.Tk()
# Redimensionar la ventana
ventana.geometry("600x400")
# Modificar el titulo
ventana.title('Nueva ventana')
# Color de la ventna
ventana.configure(background='#1d2d44')

def saludar(nombre):
    print(f"Saludos {nombre}")

# Botones
boton1 = ttk.Button(ventana, text='Enviar', command=lambda: saludar('Pedro'))
boton1.pack(pady=20)


# Hacemos vivible la ventana
ventana.mainloop()