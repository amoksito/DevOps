"""
Jugando con Tk.
OPP: programación orientada a objetos
"""

# Mis constantes.

decla = "❤❤Maru es la más linda❤❤"

import tkinter as tk

# Propiedades ROOT window

ventana = tk.Tk()
ventana.title(decla)
ventana.geometry("800x600+560+240")
ventana.resizable(True, True)

# Etíquetas

# Etíqueta Ppal

title = tk.Label(
ventana,
text='MARU LOVE ENTREVISTA',
font=('Arial 16 bold'),
bg='#D693BD',
fg='#9C0063'
)
title.pack()

# Etíqueta Ingresar Texto

nombre_label = tk.Label(ventana, text='¿Cuál es tu nombre?')
nombre_inp = tk.Entry(ventana)
nombre_label.pack()
nombre_inp.pack()

# Widget comprobar calentura

calentura_check = tk.Checkbutton(
ventana,
text='Apretame si te calienta Maru'
)
calentura_check.pack()

# Widget medir calentura

calentura_medidor_label = tk.Label(
    ventana,
    text='¿Qué tanto te calienta Maru?'
)

calentura_medidor_label = tk.Label(
ventana, 
text="Definir calentura numéricamente (0-100): ")
calentura_medidor_inp = tk.Spinbox(ventana, from_=0, to=100, increment=5)
calentura_medidor_label.pack()

calentura_medidor_inp.pack()

# Selector de actividad

actividad_label = tk.Label(
    ventana,
    text='¿Qué te gustaría hacer con Maru?'
)
actividad_inp = tk.Listbox(ventana, height=1)

# add choices

actividad_seleccion = (
    "Cafecito",
    "Película",
    "Adentro-Afuera",
    "Anal"
)

for actividad in actividad_seleccion:
    actividad_inp.insert(tk.END, actividad)

actividad_label.pack()
actividad_inp.pack()

ventana.mainloop()

"""

root.title("Maru Love")
root.geometry('640x480+300+300')
root.resizable(False, False)

label = Label(root, text=decla)
label.pack()
root.mainloop()
"""
