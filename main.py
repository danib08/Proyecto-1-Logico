import tkinter as tk
from tkinter import messagebox
from NRZI import NRZI

font = "Verdana"
window = tk.Tk()  # Main window

def click_binario():  # Makes sure the input is a 12 bit binary number
    try:
        user_input = entry.get()
        number = int(user_input)
        is_binary = True
        for i in range(len(user_input)):
            if user_input[i] != str(1) and user_input[i] != str(0):
                is_binary = False
                break
        if len(user_input) == 12 and isinstance(number, int) and is_binary:
            entry.delete(0, 'end')
            deci = int(user_input, 2)
            hexa = hex(deci)
            octa = oct(deci)
            # messagebox.showinfo("Correcto", "Decimal: %s, Hexadecimal: %s, Octal: %s" % (deci, hexa, octa))
            draw_nrzi = NRZI(user_input, nrzi_canvas)
            draw_nrzi.draw()
        else:
            messagebox.showerror("Error", "El número debe ser binario y de 12 dígitos")
    except ValueError:
        pass
        messagebox.showerror("Error", "Ingrese un número válido")

# Create widgets
top_frame = tk.Frame(master=window, bg="skyblue1", width=500, height=200)
nrzi_frame = tk.Frame(master=window, bg="black", width=800, height=400)
nrzi_canvas = tk.Canvas(master=nrzi_frame, bg="plum1", width=800, height=260, highlightthickness=0)

title_label = tk.Label(master=top_frame, text="Proyecto 1", bg="skyblue1", font=(font, 12))
instr_label = tk.Label(master=top_frame, text="Ingrese un número binario de 12 dígitos", bg="skyblue1", font=(font, 10))
button = tk.Button(master=top_frame, text="Hecho", command=click_binario)

entry = tk.Entry(master=top_frame)

# Place widgets
top_frame.pack(fill=tk.BOTH, expand=True)
nrzi_frame.pack(fill=tk.BOTH, expand=True)
title_label.pack()
instr_label.pack()
nrzi_canvas.pack()
button.pack()
entry.pack()

window.mainloop()
