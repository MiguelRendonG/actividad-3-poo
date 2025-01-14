import tkinter as tk
from tkinter import messagebox
import math
#Dados los valores A, B y C que son los parámetros de una ecuación de segundo grado, elaborar un algoritmo para hallar las posibles soluciones de dicha ecuación

class EcuacionSegundoGrado:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_raices(self):
        if self.a == 0:
            return "El coeficiente A no puede ser 0, ya que no sería una ecuación de segundo grado."

        discriminante = self.b**2 - 4 * self.a * self.c

        if discriminante > 0:
            raiz1 = (-self.b + math.sqrt(discriminante)) / (2 * self.a)
            raiz2 = (-self.b - math.sqrt(discriminante)) / (2 * self.a)
            return f"Dos raíces reales:\nRaíz 1: {raiz1:.2f}\nRaíz 2: {raiz2:.2f}"
        elif discriminante == 0:
            raiz = -self.b / (2 * self.a)
            return f"Una raíz real:\nRaíz: {raiz:.2f}"
        else:
            return "No tiene raíces reales, ya que el discriminante es negativo."


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Ecuación de Segundo Grado")

        tk.Label(root, text="Valor de A:").grid(row=0, column=0, padx=5, pady=5)
        self.a_entry = tk.Entry(root)
        self.a_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Valor de B:").grid(row=1, column=0, padx=5, pady=5)
        self.b_entry = tk.Entry(root)
        self.b_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="Valor de C:").grid(row=2, column=0, padx=5, pady=5)
        self.c_entry = tk.Entry(root)
        self.c_entry.grid(row=2, column=1, padx=5, pady=5)


        calcular_button = tk.Button(root, text="Calcular Raíces", command=self.calcular)
        calcular_button.grid(row=3, column=0, columnspan=2, pady=10)

    def calcular(self):
        try:
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())
            
            ecuacion = EcuacionSegundoGrado(a, b, c)
            resultado = ecuacion.calcular_raices()

            messagebox.showinfo("Resultado", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
