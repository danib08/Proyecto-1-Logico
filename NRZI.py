import tkinter as tk

class NRZI:
    def __init__(self, bits, canvas):
        self.bits = bits
        self.canvas = canvas
        self.font = "Verdana"

    def draw(self):
        # Draw graphic
        self.canvas.delete("all")
        self.canvas.create_text(400, 20, text="Representación NRZI", font=(self.font, 12))
        self.canvas.create_text(145, 45, text="Amplitud", font=(self.font, 10))
        self.canvas.create_text(680, 150, text="Tiempo", font=(self.font, 10))

        self.canvas.create_line(150, 150, 650, 150, width=3, arrow=tk.LAST)
        self.canvas.create_line(150, 60, 150, 240, width=3, arrow=tk.FIRST)

        # Create divisions and place bits
        x = 191
        for i in self.bits:
            self.canvas.create_text(x - 20, 80, text=i, font=(self.font, 10))
            self.canvas.create_line(x, 80, x, 220, dash=(3, 5))
            x += 41

        self.algorithm()

    def algorithm(self):
        max_signal = 150 - 40
        min_signal = 150 + 40
        x = 150
        signal = False  # False if the current signal is off and true if it's on

        for i in self.bits:
            if i == "1":
                signal = not signal
                self.canvas.create_line(x, max_signal, x, min_signal, width=2)
            if signal:
                self.canvas.create_line(x, max_signal, x + 41, max_signal, width=2)
            else:
                self.canvas.create_line(x, min_signal, x + 41, min_signal, width=2)

            x += 41
