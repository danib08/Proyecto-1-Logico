import tkinter as tk
from tkinter import messagebox

window = tk.Tk()  # Ventana principal

def click_binario():  # Comprueba que el input sea un numero binario de 12 digitos
    try:
        user_input = entry.get()
        number = int(user_input)
        is_binary = True
        for i in range(len(user_input)):
            if user_input[i] != str(1) and user_input[i] != str(0):
                is_binary = False
                break
        if len(user_input) == 12 and isinstance(number, int) and is_binary:
            deci = int(user_input, 2)
            hexa = hex(deci)
            octa = oct(deci)
            messagebox.showinfo("Correcto", "Decimal: %s, Hexadecimal: %s, Octal: %s" % (deci, hexa, octa))
        else:
            messagebox.showerror("Error", "El número debe ser binario y de 12 dígitos")
    except ValueError:
        pass
        messagebox.showerror("Error", "Ingrese un número válido")

# Crear widgets
top_frame = tk.Frame(master=window, bg="skyblue1", width=500, height=200)
title = tk.Label(master=top_frame, text="Proyecto 1", bg="skyblue1")
instr = tk.Label(master=top_frame, text="Ingrese un número binario de 12 dígitos", bg="skyblue1")
button = tk.Button(master=top_frame, text="Hecho", command=click_binario)
entry = tk.Entry(master=top_frame)

# Colocar widgets
top_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
title.pack()
instr.pack()
button.pack()
entry.pack()

window.mainloop()
