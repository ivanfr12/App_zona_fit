import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

from cliente_dao import ClienteDAO
from cliente import Cliente

class App(tk.Tk):
    COLOR_VENTANA = '#1d2d44'
    
    # Metodos a utilizar
    def __init__(self):
        super().__init__()
        self.id_cliente = None
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.cargar_tabla()
        self.mostrar_botones()
        
        
    # Configurar ventana    
    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit App')
        self.configure(bg=self.COLOR_VENTANA)
        # Aplicamos estilos
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam') # Preparamos los estilos para el modo oscuro
        self.estilos.configure(self, background=App.COLOR_VENTANA,
                               foreground='black',
                               fieldbackgorund='white')
    
    # Configurar el grid
    def configurar_grid(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        
    # Mostrar el titulo
    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)',
                             font=('Arial', 20),
                             background=App.COLOR_VENTANA,
                             foreground='white')    
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)
        
    def mostrar_formulario(self):
        self.frame_forma =ttk.Frame()
        # nombre
        nombre_l = ttk.Label(self.frame_forma, text='Nombre: ')
        nombre_l.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)
        self.nombre_t = ttk.Entry(self.frame_forma)
        self.nombre_t.grid(row=0, column=1)
        
       
        # Apellido
        apellido_l = ttk.Label(self.frame_forma, text='Apellido: ')
        apellido_l.grid(row=1, column=0, sticky=tk.W, pady=30, padx=5)
        self.apellido_t = ttk.Entry(self.frame_forma)
        self.apellido_t.grid(row=1, column=1)
        
        # Membresia
        membresia_l = ttk.Label(self.frame_forma, text='Membresía: ')
        membresia_l.grid(row=2, column=0, sticky=tk.W, pady=30, padx=5)
        self.membresia_t = ttk.Entry(self.frame_forma)
        self.membresia_t.grid(row=2, column=1)
    
         # Publicar el frame de forma
        self.frame_forma.grid(row=1, column=0)
        
        
        
    def cargar_tabla(self):
        # Creamos un frame para la tabla
        self.frame_tabla = ttk.Frame(self)
        # Definimos los estilos de la tabla
        self.estilos.configure('Treeview', background= 'black',
                               foreground= 'white',
                               fielbackground= 'black',
                               rowheight= 20)
        # Definimos las columnas
        columnas = ('ID', 'Nombre', 'Apellido', 'Membresia')
        # Creamos el objeto tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show='headings')
        # Publicamos la tabla
        self.tabla.grid(row=0, column=0)
        
        # Mostramos el frame de tabla
        self.frame_tabla.grid(row=1, column=1, padx=20)
    
    # Agreagamos los cabeceros
        self.tabla.heading('ID', text='ID', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresía', anchor=tk.W)
        
        # Definimos la columnas
        self.tabla.column('ID', anchor=tk.CENTER, width=50)
        self.tabla.column('Nombre', anchor=tk.W, width=100)
        self.tabla.column('Apellido', anchor=tk.W, width=100)
        self.tabla.column('Membresia', anchor=tk.W, width=100)
        
        # Cargamos los datos de la base de datos
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END,
                              values=(cliente.id, cliente.nombre,
                              cliente.apellido, cliente.membresia))
            
            
        # Agregamos el scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL,
                                  command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='NS')
        
        # Asociar el evento slect
        self.tabla.bind('<<TreeviewSelect>>', self.cargar_cliente)
        
    
    def mostrar_botones(self):
        self.frame_botones = ttk.Frame()
        # Crear botones
        agregar_boton = ttk.Button(self.frame_botones, text='Guardar',
                                   command=self.validar_cliente)
        agregar_boton.grid(row=0, column=0, padx=30)
        
        # Publicar el frame de botones
        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=20)
        
        # Botones eliminar
        eliminar_boton = ttk.Button(self.frame_botones, text='Eliminar',
                                    command=self.eliminar_cliente)
        eliminar_boton.grid(row=0, column=1, padx=30)
            
        # Boton de limpiar
        limpiar_boton = ttk.Button(self.frame_botones, text='Limpiar',
                                   command=self.limpiar_datos)
        limpiar_boton.grid(row=0, column=2, padx=30)
        
        # Aplicar estilos a los botones
        self.estilos.configure('TButton', background='#005f73')
        self.estilos.map('TButton', background=[('active', '#0a9396')])
        
    def validar_cliente(self):
        # VAlidar los campos
        if(self.nombre_t.get() and self.apellido_t.get() and self.membresia_t.get()):
            if self.validar_membresia():
                self.guardar_cliente()
            else:
                showerror(title='Atencion', message='El valor de membresia no es numerico')
                self.membresia_t.delete(0, tk.END)
                self.membresia_t.focus_set()
        else:
            showerror(title='Atencion', message='Todos los campos son obligatorios')
            self.nombre_t.focus_set()
                
    def validar_membresia(self):
        try:
            int(self.membresia_t.get())
            return True
        except:
            return False
        
    
    def guardar_cliente(self):
        # Recuperar los valores de las cajas de texto
        nombre = self.nombre_t.get()
        apellido = self.apellido_t.get()
        membresia = self.membresia_t.get()
        # Validamos el valor del self.id_cliente
        if self.id_cliente is None:
            cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
            ClienteDAO.insertar(cliente)
            showinfo(title='Agregar', message='Cliente agregado...')
        else: # Actualizar
            cliente = Cliente(self.id_cliente, nombre, apellido, membresia)
            ClienteDAO.actualizar(cliente)
            showinfo(title='Actualizar', message='Cliente actualizado...')
        # volvemos a mostrar los datos y limpiamos el formulario
        self.recargar_datos()
        
    def cargar_cliente(self, event):
        # Recuperar el cliente seleccionado
        elemento_seleccionado = self.tabla.selection()[0]
        elemento = self.tabla.item(elemento_seleccionado)
        cliente_t = elemento['values'] #  tupla de valores de cliente seleccionado
        # Recuperar cada valor del cliente
        self.id_cliente = cliente_t[0]
        nombre = cliente_t[1]
        apellido = cliente_t[2]
        membresia = cliente_t[3]
        # Antes de cargar, limpiar el formulario
        self.limpiar_formulario()
        # Cargar los valores del formulario
        self.nombre_t.insert(0, nombre)
        self.apellido_t.insert(0, apellido)
        self.membresia_t.insert(0, membresia)
        
        
    def recargar_datos(self):
        # Recuperar los datos de la base de datos
        self.cargar_tabla()
        # Limpiar los datos
        self.limpiar_datos()
        
        
    
    def eliminar_cliente(self):
        if self.id_cliente is None:
            showerror(title='Atencion', message='No hay cliente seleccionado')
        else:
            cliente = Cliente(id=self.id_cliente)
            ClienteDAO.eliminar(cliente)
            showinfo(title='Eliminado', message='Cliente Eliminado...')
            self.recargar_datos()
        
    def limpiar_datos(self):
        self.limpiar_formulario()
        self.id_cliente = None
    
    def limpiar_formulario(self):
        self.nombre_t.delete(0, tk.END)
        self.apellido_t.delete(0, tk.END)
        self.membresia_t.delete(0, tk.END)
    
    
# Prueba de app
if __name__ == '__main__':
    app = App()
    app.mainloop()
    