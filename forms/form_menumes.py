import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.form_master import MasterPanel
from forms.form_login import App


class MenuMes:
    def __init__(self) -> None:
        self.ventana = tk.Tk()
        self.ventana.title('Menu Mesero')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#d7d7d7')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 500)
        
        #frame_panel
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#d7d7d7')
        frame_form.pack(expand=tk.YES, fill=tk.BOTH)
        
        #frame_form_top cuasi div
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#d7d7d7')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Menu Mesero", font=('Times', 20), fg="#000000", bg='#d7d7d7', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        #botones dentro del menu mesero
        btcue = tk.Button(frame_form_top, text="Cuenta", font=('Times', 15, BOLD), bg='#272d2f', bd= 0, fg='#ffffff')
        btcue.pack(fill=tk.X, padx=20, pady=10)
        
        btverped = tk.Button(frame_form_top, text="Ver pedido", font=('Times', 15, BOLD), bg='#272d2f', bd= 0, fg='#ffffff')
        btverped.pack(fill=tk.X, padx=20, pady=10)
        
        btmodped = tk.Button(frame_form_top, text="Modificar pedido", font=('Times', 15, BOLD), bg='#272d2f', bd= 0, fg='#ffffff')
        btmodped.pack(fill=tk.X, padx=20, pady=10)
        
        btregresarmm = tk.Button(frame_form_top, text="Regresar", font=('Times', 15, BOLD), bg='#272d2f', bd= 0, fg='#ffffff', command=self.fbtregresarmm)
        btregresarmm.pack(fill=tk.X, padx=20, pady=10)
        
        self.ventana.mainloop()
        
    #funcionesbotones    
    def fbtregresarmm(self):
        self.ventana.destroy() 
        App()