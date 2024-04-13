import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl

class App:
    def __init__(self) -> None:
        self.ventana = tk.Tk()
        self.ventana.title('Inicio de sesion')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#d7d7d7')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 500)
        
        
        logo = utl.leer_imagen("./imagenes/chef.jpg", (200,200))
        
        #frame_imagen
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady= 10, bg='#d7d7d7')
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#272d2f')
        label.place(x=0, y=0, relwidth=1, relheight=1)
        
        #frame_panel
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#d7d7d7')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        
        #frame_form_top
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Inicio de sesión", font=('Times', 20), fg="#000000", bg='#d7d7d7', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        
        #frame_in
        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#d7d7d7')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
        
        #etiquetas
        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Times', 14), fg="#ffffff", bg='#272d2f', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)  
        
        etiqueta_contrasena = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14), fg="#ffffff", bg='#272d2f', anchor="w")
        etiqueta_contrasena.pack(fill=tk.X, padx=20, pady=5)
        self.contrasena = ttk.Entry(frame_form_fill, font=('Times', 14), )
        self.contrasena.pack(fill=tk.X, padx=20, pady=10) 
        self.contrasena.config(show="*") 
        
        inicio = tk.Button(frame_form_fill, text="Iniciar sesion", font=('Times', 15, BOLD), bg='#272d2f', bd= 0, fg='#ffffff')
        inicio.pack(fill=tk.X, padx=20, pady=20)
        
        cerrar = tk.Button(frame_form_fill, text="Salir", font=('Times', 15, BOLD), bg='#272d2f', bd= 0, fg='#ffffff', command=self.salir)
        cerrar.pack(fill=tk.X, padx=20, pady=20)
        self.ventana.mainloop()
        
    def salir(self):
        self.ventana.destroy()