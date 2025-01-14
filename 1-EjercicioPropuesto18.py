import tkinter as tk
from tkinter import messagebox
#Haga un algoritmo que muestre: código, nombres, salario bruto y salario neto.

class Empleado:
    def __init__(self, codigo, nombres, horas_trabajadas, valor_hora, retencion):
        self.codigo = codigo
        self.nombres = nombres
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.retencion = retencion

    def calcular_salario_bruto(self):
        return self.horas_trabajadas * self.valor_hora

    def calcular_salario_neto(self):
        salario_bruto = self.calcular_salario_bruto()
        descuento = salario_bruto * (self.retencion / 100)
        return salario_bruto - descuento

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Salario")

        # Etiquetas y entradas
        tk.Label(root, text="Código del empleado:").grid(row=0, column=0, padx=10, pady=5)
        self.codigo_entry = tk.Entry(root)
        self.codigo_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Nombres y Apellidos:").grid(row=1, column=0, padx=10, pady=5)
        self.nombres_entry = tk.Entry(root)
        self.nombres_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Horas trabajadas al mes:").grid(row=2, column=0, padx=10, pady=5)
        self.horas_entry = tk.Entry(root)
        self.horas_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Valor hora trabajada:").grid(row=3, column=0, padx=10, pady=5)
        self.valor_hora_entry = tk.Entry(root)
        self.valor_hora_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Porcentaje de retención:").grid(row=4, column=0, padx=10, pady=5)
        self.retencion_entry = tk.Entry(root)
        self.retencion_entry.grid(row=4, column=1, padx=10, pady=5)

        # Botón para calcular
        self.calcular_button = tk.Button(root, text="Calcular", command=self.calcular)
        self.calcular_button.grid(row=5, column=0, columnspan=2, pady=10)

    def calcular(self):
        try:
            # Captura de datos
            codigo = self.codigo_entry.get()
            nombres = self.nombres_entry.get()
            horas_trabajadas = float(self.horas_entry.get())
            valor_hora = float(self.valor_hora_entry.get())
            retencion = float(self.retencion_entry.get())

            # Crear objeto Empleado y calcular salarios
            empleado = Empleado(codigo, nombres, horas_trabajadas, valor_hora, retencion)
            salario_bruto = empleado.calcular_salario_bruto()
            salario_neto = empleado.calcular_salario_neto()

            # Mostrar resultados
            messagebox.showinfo("Resultados", f"Código: {codigo}\n"
                                            f"Nombres: {nombres}\n"
                                            f"Salario Bruto: ${salario_bruto:.2f}\n"
                                            f"Salario Neto: ${salario_neto:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos en todos los campos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
