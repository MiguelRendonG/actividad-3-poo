import tkinter as tk
from tkinter import messagebox
import math
#Dado el valor del lado en un triángulo equilátero, haga un algoritmo que obtenga el perímetro, el valor de la altura y el área del triángulo.

class TrianguloEquilatero:
    def __init__(self, lado):
        self.lado = lado

    def calcular_perimetro(self):
        return 3 * self.lado

    def calcular_altura(self):
        return (math.sqrt(3) / 2) * self.lado

    def calcular_area(self):
        return (math.sqrt(3) / 4) * (self.lado ** 2)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculos de Triángulo Equilátero")

        # Etiqueta y entrada para el lado
        tk.Label(root, text="Valor del lado:").grid(row=0, column=0, padx=10, pady=5)
        self.lado_entry = tk.Entry(root)
        self.lado_entry.grid(row=0, column=1, padx=10, pady=5)

        # Botón para calcular
        self.calcular_button = tk.Button(root, text="Calcular", command=self.calcular)
        self.calcular_button.grid(row=1, column=0, columnspan=2, pady=10)

    def calcular(self):
        try:
            # Captura de datos
            lado = float(self.lado_entry.get())

            # Crear objeto TrianguloEquilatero y calcular resultados
            triangulo = TrianguloEquilatero(lado)
            perimetro = triangulo.calcular_perimetro()
            altura = triangulo.calcular_altura()
            area = triangulo.calcular_area()

            # Mostrar resultados
            messagebox.showinfo("Resultados", f"Lado: {lado}\n"
                                            f"Perímetro: {perimetro:.2f}\n"
                                            f"Altura: {altura:.2f}\n"
                                            f"Área: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor válido para el lado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
