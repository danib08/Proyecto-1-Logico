import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from NRZI import NRZI
from hamming import Hamming

font = "Verdana"
root = tk.Tk()  # Main window
root.title("Proyecto 1")
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

            Hamming(root, user_input, 0, "1")

        else:
            messagebox.showerror("Error", "El número debe ser binario y de 12 dígitos")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")

# Create frames and canvas
conversion_frame = tk.Frame(master=root, bg="steelblue1", width=500, height=200)
nrzi_frame = tk.Frame(master=root, bg="steelblue1", width=500, height=400)
nrzi_canvas = tk.Canvas(master=nrzi_frame, bg="steelblue1", width=800, height=260, highlightthickness=0)

# Create widgets
title_label = tk.Label(master=conversion_frame, text="Proyecto 1", bg="steelblue1", font=(font, 12))
instr_label = tk.Label(master=conversion_frame, text="Ingrese un número binario de 12 dígitos:", bg="steelblue1", font=(font, 10))
paridad_label = tk.Label(master=conversion_frame, text="Elija la paridad:", bg="steelblue1", font=(font, 10))
button = tk.Button(master=conversion_frame, text="Hecho", command=click_binario, font=(font, 10))
entry = tk.Entry(master=conversion_frame)
radio_group = tk.IntVar()
radio1 = tk.Radiobutton(conversion_frame, text="Par", variable=radio_group, value=0, bg="steelblue1", activebackground="steelblue1")
radio2 = tk.Radiobutton(conversion_frame, text="Impar", variable=radio_group, value=1, bg="steelblue1", activebackground="steelblue1")

# # Hamming class
# hamming = Hamming(root)

# Create table
table = ttk.Treeview(conversion_frame, columns=("1", "2", "3", "4"), height=1, show="headings")
table.heading("1", text="Número binario insertado")
table.heading("2", text="Decimal")
table.heading("3", text="Octal")
table.heading("4", text="Hexadecimal")
table.column("1", minwidth=50, width=160, anchor="center")
table.column("2", minwidth=50, width=60, anchor="center")
table.column("3", minwidth=50, width=50, anchor="center")
table.column("4", minwidth=50, width=80, anchor="center")

# Place widgets
conversion_frame.pack(fill=tk.BOTH, expand=True)
nrzi_frame.pack(fill=tk.BOTH, expand=True)
title_label.pack()
instr_label.pack()
nrzi_canvas.pack()
entry.pack(pady=1)
paridad_label.pack()
radio1.pack()
radio2.pack()
button.pack(pady=2)

root.mainloop()
