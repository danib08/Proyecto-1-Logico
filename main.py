import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from NRZI import NRZI

font = "Verdana"
root = tk.Tk()  # Main window
root.resizable(False, False)

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
            hexa = hex(deci)[2:].upper()
            octa = oct(deci)[2:].upper()

            table.delete(*table.get_children())
            table.insert("", 0, values=(user_input, deci, hexa, octa))
            table.pack()

            draw_nrzi = NRZI(user_input, nrzi_canvas)
            draw_nrzi.draw()
        else:
            messagebox.showerror("Error", "El número debe ser binario y de 12 dígitos")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")

# Create frames and canvas
conversion_frame = tk.Frame(master=root, bg="steelblue1", width=500, height=200)
nrzi_frame = tk.Frame(master=root, bg="steelblue1", width=800, height=400)
nrzi_canvas = tk.Canvas(master=nrzi_frame, bg="steelblue1", width=800, height=260, highlightthickness=0)

# Create widgets
title_label = tk.Label(master=conversion_frame, text="Proyecto 1", bg="steelblue1", font=(font, 12))
instr_label = tk.Label(master=conversion_frame, text="Ingrese un número binario de 12 dígitos", bg="steelblue1", font=(font, 10))
button = tk.Button(master=conversion_frame, text="Hecho", command=click_binario, font=(font, 10))
entry = tk.Entry(master=conversion_frame)

# Create table
table = ttk.Treeview(conversion_frame, columns=("#1", "#2", "#3", "#4"))
table.heading("#1", text="Número binario insertado")
table.heading("#2", text="Decimal")
table.heading("#3", text="Octal")
table.heading("#4", text="Hexadecimal")

# Place widgets
conversion_frame.pack(fill=tk.BOTH, expand=True)
nrzi_frame.pack(fill=tk.BOTH, expand=True)
title_label.pack()
instr_label.pack()
nrzi_canvas.pack()
button.pack(pady=5)
entry.pack()

root.mainloop()
