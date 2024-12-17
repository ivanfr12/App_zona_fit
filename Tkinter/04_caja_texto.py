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


def mostrar():
    texto = caja_texto.get() # Recuperamos el valor de la caja de texto
    print(f'Texto proporcionado: {texto}')
    etiqueta['text'] = texto

# Caja de texto
caja_texto = ttk.Entry(ventana, font=('Arial', 15))
caja_texto.pack(pady=20)



# Agreagamos un boton
boton = ttk.Button(ventana, text='Enviar', command=mostrar)
boton.pack(pady=20)

# Agregamos una etiqueta
etiqueta = ttk.Label(ventana, text='Valor inicial')
etiqueta.pack(pady=20)
ventana.mainloop()