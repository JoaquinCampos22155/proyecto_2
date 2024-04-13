import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
from forms.form_login import App 
class MasterPanel:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Master panel')
        w, h = self.ventana.winfo_screenmmwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        
        logo = utl.leer_imagen("./imagenes/chef.jpg", (200, 200))

        label = tk.Label( self.ventana, image=logo, bg='#ffffff')
        label.place(x=0, y=0, relheight=1, relwidth=1)
        self.ventana.mainloop()  
    #funcionesbotones    
    def fbtregresarmc(self):
        self.ventana.destroy() 
        App()      