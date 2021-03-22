from tkinter import ttk
import tkinter as tk

class Hamming:
    def __init__(self, root, cod, paridad, cambio):
        self.toplevel = tk.Toplevel(root)
        self.toplevel.title("Código de Hamming")
        self.tabla = ttk.Treeview(self.toplevel)
        self.tabla2 = ttk.Treeview(self.toplevel)

        self.lista = list(cod)
        self.cambio = cambio
        self.paridad = paridad  # True si par y False si impar
        self.nuevocod = []
        self.indicador_paridad = ""

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
        self.cambio_digito()

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

        if not self.paridad:
            self.indicador_paridad = "Impar"

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
        else:
            indicador_paridad = "Par"

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
        
    def cambio_digito(self):
        error = "Error"
        bit_comprobacion = "0"

        if self.lista[self.cambio - 1] == "0":
            self.lista[self.cambio - 1] = "1"
        else:
            self.lista[self.cambio - 1] = "0"

        fila0 = [self.p1, self.p2, self.lista[0], self.p3, self.lista[1], self.lista[2], self.lista[3], self.p4, self.lista[4], self.lista[5], self.lista[6], self.lista[7],
                 self.lista[8], self.lista[9], self.lista[10], self.p5, self.lista[11], self.indicador_paridad, '']
        fila1 = [self.p1, "", self.lista[0], "", self.lista[1], "", self.lista[3], "", self.lista[4], "", self.lista[6], "", self.lista[8], "", self.lista[10],
                 "", self.lista[11], error, bit_comprobacion]
        fila2 = ["", self.p2, self.lista[0], "", "", self.lista[2], self.lista[3], "", "", self.lista[5], self.lista[6], "", "", self.lista[9], self.lista[10],
                 "", "", error, bit_comprobacion]
        fila3 = ["", "", "", self.p3, self.lista[1], self.lista[2], self.lista[3], "", "", "", "", self.lista[7], self.lista[8], self.lista[9], self.lista[10],
                 "", "", error, bit_comprobacion]
        fila4 = ["", "", "", "", "", "", "", self.p4, self.lista[4], self.lista[5], self.lista[6], self.lista[7], self.lista[8], self.lista[9], self.lista[10],
                 "", "", error, bit_comprobacion]
        fila5 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", self.p5, self.lista[11], error, bit_comprobacion]

        matriz = [
            [self.p1, "", self.lista[0], "", self.lista[1], "", self.lista[3], "", self.lista[4], "", self.lista[6], "", self.lista[8], "", self.lista[10], "",
             self.lista[11], error, bit_comprobacion],
            ["", self.p2, self.lista[0], "", "", self.lista[2], self.lista[3], "", "", self.lista[5], self.lista[6], "", "", self.lista[9], self.lista[10], "",
             "", error, bit_comprobacion],
            ["", "", "", self.p3, self.lista[1], self.lista[2], self.lista[3], "", "", "", "", self.lista[7], self.lista[8], self.lista[9], self.lista[10], "",
             "", error, bit_comprobacion],
            ["", "", "", "", "", "", "", self.p4, self.lista[4], self.lista[5], self.lista[6], self.lista[7], self.lista[8], self.lista[9], self.lista[10], "",
             "", error, bit_comprobacion],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", self.p5, self.lista[11], error, bit_comprobacion]]
        campo = [2, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16]

        lista_errores = []
        lista_bit_comprobacion = []

        for i in range(5):
            for j in range(17):
                if j == self.cambio - 1:
                    if matriz[i][campo[j]] == "0":
                        error = "Error"
                        bit_comprobacion = "1"
                        lista_errores.append(error)
                        lista_bit_comprobacion.append(bit_comprobacion)

                    elif matriz[i][campo[j]] == "1":
                        error = "Error"
                        bit_comprobacion = "0"
                        lista_errores.append(error)
                        lista_bit_comprobacion.append(bit_comprobacion)

                    else:
                        error = "Correcto"
                        bit_comprobacion = "0"
                        lista_errores.append(error)
                        lista_bit_comprobacion.append(bit_comprobacion)

        self.tabla2['columns'] = (
        "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10", "#11", "#12", "#13", "#14", "#15", "#16", "#17",
        "#18", "#19")
        self.tabla2.column("#0", width=200, minwidth=25)
        self.tabla2.column("#1", width=30)
        self.tabla2.column("#2", width=30)
        self.tabla2.column("#3", width=30)
        self.tabla2.column("#4", width=30)
        self.tabla2.column("#5", width=30)
        self.tabla2.column("#6", width=30)
        self.tabla2.column("#7", width=30)
        self.tabla2.column("#8", width=30)
        self.tabla2.column("#9", width=30)
        self.tabla2.column("#10", width=30)
        self.tabla2.column("#11", width=30)
        self.tabla2.column("#12", width=30)
        self.tabla2.column("#13", width=30)
        self.tabla2.column("#14", width=30)
        self.tabla2.column("#15", width=30)
        self.tabla2.column("#16", width=30)
        self.tabla2.column("#17", width=30)
        self.tabla2.column("#18", width=100)
        self.tabla2.column("#19", width=100)

        self.tabla2.heading("#0", text=" ")
        self.tabla2.heading("#1", text="p1")
        self.tabla2.heading("#2", text="p2")
        self.tabla2.heading("#3", text="d1")
        self.tabla2.heading("#4", text="p3")
        self.tabla2.heading("#5", text="d2")
        self.tabla2.heading("#6", text="d3")
        self.tabla2.heading("#7", text="d4")
        self.tabla2.heading("#8", text="p4")
        self.tabla2.heading("#9", text="d5")
        self.tabla2.heading("#10", text="d6")
        self.tabla2.heading("#11", text="d7")
        self.tabla2.heading("#12", text="d8")
        self.tabla2.heading("#13", text="d9")
        self.tabla2.heading("#14", text="d10")
        self.tabla2.heading("#15", text="d11")
        self.tabla2.heading("#16", text="p5")
        self.tabla2.heading("#17", text="d12")
        self.tabla2.heading("#18", text="Prueba de paridad")
        self.tabla2.heading("#19", text="Bit de paridad")

        self.tabla2.insert(parent='', index='end', text="Palabra de datos recibida", values=(
        self.p1, self.p2, self.lista[0], self.p3, self.lista[1], self.lista[2], self.lista[3], self.p4, self.lista[4], self.lista[5], self.lista[6], self.lista[7], self.lista[8],
        self.lista[9], self.lista[10], self.p5, self.lista[11], self.indicador_paridad, ''))
        self.tabla2.insert(parent='', index='end', text="p1", values=(
        self.p1, "", self.lista[0], "", self.lista[1], "", self.lista[3], "", self.lista[4], "", self.lista[6], "", self.lista[8], "", self.lista[10], "",
        self.lista[11], lista_errores[0], lista_bit_comprobacion[0]))
        self.tabla2.insert(parent='', index='end', text="p2", values=(
        "", self.p2, self.lista[0], "", "", self.lista[2], self.lista[3], "", "", self.lista[5], self.lista[6], "", "", self.lista[9], self.lista[10], "", "",
        lista_errores[1], lista_bit_comprobacion[1]))
        self.tabla2.insert(parent='', index='end', text="p3", values=(
        "", "", "", self.p3, self.lista[1], self.lista[2], self.lista[3], "", "", "", "", self.lista[7], self.lista[8], self.lista[9], self.lista[10], "", "",
        lista_errores[2], lista_bit_comprobacion[2]))
        self.tabla2.insert(parent='', index='end', text="p4", values=(
        "", "", "", "", "", "", "", self.p4, self.lista[4], self.lista[5], self.lista[6], self.lista[7], self.lista[8], self.lista[9], self.lista[10], "", "",
        lista_errores[3], lista_bit_comprobacion[3]))
        self.tabla2.insert(parent='', index='end', text="p5", values=(
        "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", self.p5, self.lista[11], lista_errores[4],
        lista_bit_comprobacion[4]))

        self.tabla2.pack()

