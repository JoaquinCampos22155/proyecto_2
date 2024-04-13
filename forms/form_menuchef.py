import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.form_master import MasterPanel
from forms.form_login import App

            
class MenuChef():
    #funcion boton
    
    def __init__(self) -> None:
        self.ventana = tk.Tk()
        self.ventana.title('Menu Chef')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#d7d7d7')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 500)
        
        #frame_panel
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#d7d7d7')
        frame_form.pack(expand=tk.YES, fill=tk.BOTH)
        
        #frame_form_top
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#d7d7d7')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Menu Chef", font=('Times', 20), fg="#000000", bg='#d7d7d7', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        
        btagrpla = tk.Button(frame_form_top, text="Agregar plato", font=('Times', 15, BOLD), bg='#272d2f', bd= 0, fg='#ffffff')
        btagrpla.pack(fill=tk.X, padx=20, pady=10)
        
        btagrbeb = tk.Button(frame_form_top, text="Agregar bebida", font=('Times', 15, BOLD), bg='#272d2f', bd= 0, fg='#ffffff')
        btagrbeb.pack(fill=tk.X, padx=20, pady=10)
        
        btrealped = tk.Button(frame_form_top, text="Realizar Pedido", font=('Times', 15, BOLD), bg='#272d2f', bd= 0, fg='#ffffff')
        btrealped.pack(fill=tk.X, padx=20, pady=10)
        
        btconfped = tk.Button(frame_form_top, text="Confirmar pedido", font=('Times', 15, BOLD), bg='#272d2f', bd= 0, fg='#ffffff')
        btconfped.pack(fill=tk.X, padx=20, pady=10)
        
        btregresarmc = tk.Button(frame_form_top, text="Regresar", font=('Times', 15, BOLD), bg='#272d2f', bd= 0, fg='#ffffff', command=self.fbtregresarmc)
        btregresarmc.pack(fill=tk.X, padx=20, pady=10)
        
        #visualizar
        self.ventana.mainloop()
    
    #funcionesbotones    
    def fbtregresarmc(self):
        self.ventana.destroy() 
        App()
        
    
        
        