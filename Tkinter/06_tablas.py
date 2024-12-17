import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

# Creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.configure(background='#1d2d44')
ventana.title('Manejo de tabla')


# configurar el grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=0)

# Definir estilo
estilo = ttk.Style()
estilo.theme_use('clam') # prepara para el manejo de tema oscuro
estilo.configure('Treeview', background='black',
                 foreground='white',
                 fieldbackground='black',
                 rowheigth=30)
estilo.map('Treeview', background=[('selected', '#3a86ff')])


# Definir las columnas
columnas = ('ID', 'Nombre', 'Edad')
tabla = ttk.Treeview(ventana, columns=columnas, show='headings')


# Cabeceros a la tabla
tabla.heading('ID', text='ID', anchor=tk.CENTER)
tabla.heading('Nombre', text='Nombre', anchor=tk.W)
tabla.heading('Edad', text='Edad', anchor=tk.W)

# Formato a las columnas
tabla.column('ID', width=80)
tabla.column('Nombre', width=120)
tabla.column('Edad', width=120)

# Cargar datos a la tabla
datos = ((1, 'Alejandra', 25), (2, 'Matias', 30))
#datos = ((1, 'Alejandra', 25), (2, 'Matias', 30)) + ((1, 'Alejandra', 25), (2, 'Matias', 30)) + ((1, 'Alejandra', 25), (2, 'Matias', 30)) + ((1, 'Alejandra', 25), (2, 'Matias', 30)) + ((1, 'Alejandra', 25), (2, 'Matias', 30)) + ((1, 'Alejandra', 25), (2, 'Matias', 30)) + ((1, 'Alejandra', 25), (2, 'Matias', 30)) + ((1, 'Alejandra', 25), (2, 'Matias', 30)) + ((1, 'Alejandra', 25), (2, 'Matias', 30))
for persona in datos:
    tabla.insert(parent='', index=tk.END, values=persona)
    
# Agregamos un scrollbar
scrollbar = ttk.Scrollbar(ventana, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscroll= scrollbar.set)
scrollbar.grid(row=0, column=1, sticky=tk.NS)

# Mostrar registro seleccionado
def mostrar_registro_seleccionado(event):
    print('Ejecutando el metodo mostrar_registro_seleccionado')
    elemento_seleccionado = tabla.selection()[0] # solo precesamos el primer registro
    elemento = tabla.item(elemento_seleccionado) # Item
    persona = elemento['values'] # tupla de persona
    print(persona)
    showinfo(title='Persona Seleccionada', message=f'Persona {persona}')
    

# asociar el evento select de la tabla
tabla.bind('<<TreeviewSelect>>', mostrar_registro_seleccionado)

# Publicamos la tabla
tabla.grid(row=0, column=0, sticky=tk.NSEW)




ventana.mainloop()