import tkinter as tk
from tkinter import messagebox


class ComparadorNumeros:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def comparar(self):
        if self.a > self.b:
            return "A es mayor que B."
        elif self.a < self.b:
            return "A es menor que B."
        else:
            return "A es igual a B."


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Comparar Numeros")

        # Etiquetas y entradas
        tk.Label(root, text="Valor de A:").grid(row=0, column=0, padx=5, pady=5)
        self.a_entry = tk.Entry(root)
        self.a_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Valor de B:").grid(row=1, column=0, padx=5, pady=5)
        self.b_entry = tk.Entry(root)
        self.b_entry.grid(row=1, column=1, padx=5, pady=5)

        # Botón para comparar
        comparar_button = tk.Button(root, text="Comparar", command=self.comparar)
        comparar_button.grid(row=2, column=0, columnspan=2, pady=10)

    def comparar(self):
        try:
            # Captura de datos
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())

            # Crear objeto y realizar comparación
            comparador = ComparadorNumeros(a, b)
            resultado = comparador.comparar()

            # Mostrar resultado
            messagebox.showinfo("Resultado", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")


# Configuración de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
