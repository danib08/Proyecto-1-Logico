from tkinter import ttk
import tkinter as tk

class Hamming:
    def __init__(self, root, cod, paridad, digito):
        self.toplevel = tk.Toplevel(root)
        self.tabla = ttk.Treeview(self.toplevel)
        self.lista = list(cod)
        self.digito = digito
        self.paridad = 0   # 0 si par y 1 si impar
        self.nuevocod = []

        self.p1 = "1"
        self.p2 = "1"
        self.p3 = "1"
        self.p4 = "1"
        self.p5 = "1"

        self.start()

    def start(self):
        self.bits()
        self.show()
        self.nuevo_codigo()

    def bits(self):
        self.p1 = str(int(self.lista[0]) ^ int(self.lista[1]) ^ int(self.lista[3]) ^ int(self.lista[4]) ^
                 int(self.lista[6]) ^ int(self.lista[8]) ^ int(self.lista[10]) ^ int(self.lista[11]))
        self.p2 = str(int(self.lista[0]) ^ int(self.lista[2]) ^ int(self.lista[3]) ^ int(self.lista[5]) ^
                 int(self.lista[6]) ^ int(self.lista[9]) ^ int(self.lista[10]))
        self.p3 = str(int(self.lista[1]) ^ int(self.lista[2]) ^ int(self.lista[3]) ^ int(self.lista[7]) ^
                 int(self.lista[8]) ^ int(self.lista[9]) ^ int(self.lista[10]))
        self.p4 = str(int(self.lista[4]) ^ int(self.lista[5]) ^ int(self.lista[6]) ^ int(self.lista[7]) ^
                 int(self.lista[8]) ^ int(self.lista[9]) ^ int(self.lista[10]))
        self.p5 = str(int(self.lista[11]))

        if self.paridad == 1:
            if self.p1 == "1":
                self.p1 = "0"
            else:
                self.p1 = "1"

            if self.p2 == "1":
                self.p2 = "0"
            else:
                self.p2 = "1"

            if self.p3 == "1":
                self.p3 = "0"
            else:
                self.p3 = "1"

            if self.p4 == "1":
                self.p4 = "0"
            else:
                self.p4 = "1"

            if self.p5 == "1":
                self.p5 = "0"
            else:
                self.p5 = "1"

    def show(self):
        self.tabla['columns'] = (
            "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10", "#11", "#12", "#13", "#14", "#15", "#16",
            "#17")
        self.tabla.column("#0", width=200, minwidth=25, anchor="center")
        self.tabla.column("#1", width=30)
        self.tabla.column("#2", width=30)
        self.tabla.column("#3", width=30)
        self.tabla.column("#4", width=30)
        self.tabla.column("#5", width=30)
        self.tabla.column("#6", width=30)
        self.tabla.column("#7", width=30)
        self.tabla.column("#8", width=30)
        self.tabla.column("#9", width=30)
        self.tabla.column("#10", width=30)
        self.tabla.column("#11", width=30)
        self.tabla.column("#12", width=30)
        self.tabla.column("#13", width=30)
        self.tabla.column("#14", width=30)
        self.tabla.column("#15", width=30)
        self.tabla.column("#16", width=30)
        self.tabla.column("#17", width=30)

        self.tabla.heading("#0", text=" ")
        self.tabla.heading("#1", text="p1")
        self.tabla.heading("#2", text="p2")
        self.tabla.heading("#3", text="d1")
        self.tabla.heading("#4", text="p3")
        self.tabla.heading("#5", text="d2")
        self.tabla.heading("#6", text="d3")
        self.tabla.heading("#7", text="d4")
        self.tabla.heading("#8", text="p4")
        self.tabla.heading("#9", text="d5")
        self.tabla.heading("#10", text="d6")
        self.tabla.heading("#11", text="d7")
        self.tabla.heading("#12", text="d8")
        self.tabla.heading("#13", text="d9")
        self.tabla.heading("#14", text="d10")
        self.tabla.heading("#15", text="d11")
        self.tabla.heading("#16", text="p5")
        self.tabla.heading("#17", text="d12")

        self.tabla.insert(parent='', index='end', text="Palabra de datos (sin paridad)", values=('', '', self.lista[0],
            '', self.lista[1], self.lista[2], self.lista[3], '', self.lista[4], self.lista[5], self.lista[6],
            self.lista[7], self.lista[8], self.lista[9], self.lista[10], '', self.lista[11]))

        self.tabla.insert(parent='', index='end', text="p1", values=(self.p1, "", self.lista[0], "", self.lista[1], "",
            self.lista[3], "", self.lista[4], "", self.lista[6], "", self.lista[8], "", self.lista[10], "", self.lista[11]))

        self.tabla.insert(parent='', index='end', text="p2", values=("", self.p2, self.lista[0], "", "", self.lista[2],
            self.lista[3], "", "", self.lista[5], self.lista[6], "", "", self.lista[9], self.lista[10], "", ""))

        self.tabla.insert(parent='', index='end', text="p3", values=("", "", "", self.p3, self.lista[1], self.lista[2],
            self.lista[3], "", "", "", "", self.lista[7], self.lista[8], self.lista[9], self.lista[10], "", ""))

        self.tabla.insert(parent='', index='end', text="p4", values=("", "", "", "", "", "", "", self.p4, self.lista[4],
            self.lista[5], self.lista[6], self.lista[7], self.lista[8], self.lista[9], self.lista[10], "", ""))

        self.tabla.insert(parent='', index='end', text="p5", values=("", "", "", "", "", "", "", "", "", "", "", "", "",
                                                                     "", "", self.p5, self.lista[11]))

        self.tabla.insert(parent='', index='end', text="Palabra de datos (con paridad)", values=(self.p1, self.p2,
            self.lista[0], self.p3, self.lista[1], self.lista[2], self.lista[3], self.p4, self.lista[4], self.lista[5],
            self.lista[6], self.lista[7], self.lista[8], self.lista[9], self.lista[10], self.p5, self.lista[11]))

        self.tabla.pack()

    def nuevo_codigo(self):
        self.nuevocod.append(self.p1)
        self.nuevocod.append(self.p2)
        self.nuevocod.append(self.lista[0])
        self.nuevocod.append(self.p3)
        self.nuevocod.append(self.lista[1])
        self.nuevocod.append(self.lista[2])
        self.nuevocod.append(self.lista[3])
        self.nuevocod.append(self.p4)
        self.nuevocod.append(self.lista[4])
        self.nuevocod.append(self.lista[5])
        self.nuevocod.append(self.lista[6])
        self.nuevocod.append(self.lista[7])
        self.nuevocod.append(self.lista[8])
        self.nuevocod.append(self.lista[9])
        self.nuevocod.append(self.lista[10])
        self.nuevocod.append(self.p5)
        self.nuevocod.append(self.lista[11])
