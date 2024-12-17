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

# Creamos una etiqueta(label)
etiqueta = ttk.Label(ventana, text='Saludos')

# Cambiar el texto usando el metodo configure
etiqueta.configure(text='Nos vemos...')

# Cambiar el texto con ayuda de la llave text
etiqueta['text'] = 'Adios'



# Publicamos el componente
etiqueta.pack(pady=20)

# Hacemos vivible la ventana
ventana.mainloop()