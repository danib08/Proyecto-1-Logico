import tkinter as tk

window = tk.Tk()  # Ventana principal

top_frame = tk.Frame(master=window, bg="skyblue1")

# Crear widgets
title = tk.Label(master=top_frame, text="Proyecto 1", bg="skyblue1")
instr = tk.Label(master=top_frame, text="Ingrese un número binario de 12 dígitos", bg="skyblue1")
button = tk.Button(master=top_frame, text="Hecho")
entry = tk.Entry(master=top_frame)

def click_button1():
    input = entry.get()

# Colocar widgets
top_frame.pack()
title.pack()
instr.pack()
button.pack()
entry.pack()

window.mainloop()
