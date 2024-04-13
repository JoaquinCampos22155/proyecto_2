import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.form_master import MasterPanel
from forms.form_login import App



class MenuHost:
    def __init__(self) -> None:
        self.ventana = tk.Tk()
        self.ventana.title('Menu Host')
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
        title = tk.Label(frame_form_top, text= "Menu Host", font=('Times', 20), fg="#000000", bg='#d7d7d7', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        
        #botones dentro del menu mesero
        btasicli = tk.Button(frame_form_top, text="Asignar cliente", font=('Times', 15, BOLD), bg='#272d2f', bd= 0, fg='#ffffff')
        btasicli.pack(fill=tk.X, padx=20, pady=10)
        
        btvercal = tk.Button(frame_form_top, text="Ver calificación", font=('Times', 15, BOLD), bg='#272d2f', bd= 0, fg='#ffffff')
        btvercal.pack(fill=tk.X, padx=20, pady=10)
        
        btmodare = tk.Button(frame_form_top, text="Modificar área", font=('Times', 15, BOLD), bg='#272d2f', bd= 0, fg='#ffffff')
        btmodare.pack(fill=tk.X, padx=20, pady=10)
        
        btcapare = tk.Button(frame_form_top, text="Capacidad de área", font=('Times', 15, BOLD), bg='#272d2f', bd= 0, fg='#ffffff')
        btcapare.pack(fill=tk.X, padx=20, pady=10)
        
        btregresarmh = tk.Button(frame_form_top, text="Regresar", font=('Times', 15, BOLD), bg='#272d2f', bd= 0, fg='#ffffff', command=self.fbtregresarmh)
        btregresarmh.pack(fill=tk.X, padx=20, pady=10)
        
        
        self.ventana.mainloop()
        
    def fbtregresarmh(self):
        self.ventana.destroy() 
        App()