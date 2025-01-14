import tkinter as tk
from tkinter import messagebox
#Elaborar un algoritmo que entre el nombre de un empleado, su salario básico por hora y el número de horas trabajadas en el mes; escriba su nombre y salario mensual si éste es mayor de $450.000, de lo contrario escriba sólo el nombre

class Empleado:
    def __init__(self, nombre, salario_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_hora = salario_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_mensual(self):
        return self.salario_hora * self.horas_trabajadas


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Salario Mensual")

    
        tk.Label(root, text="Nombre del empleado:").grid(row=0, column=0, padx=5, pady=5)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Salario básico por hora:").grid(row=1, column=0, padx=5, pady=5)
        self.salario_hora_entry = tk.Entry(root)
        self.salario_hora_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="Horas trabajadas en el mes:").grid(row=2, column=0, padx=5, pady=5)
        self.horas_trabajadas_entry = tk.Entry(root)
        self.horas_trabajadas_entry.grid(row=2, column=1, padx=5, pady=5)

     
        calcular_button = tk.Button(root, text="Calcular Salario", command=self.calcular)
        calcular_button.grid(row=3, column=0, columnspan=2, pady=10)

    def calcular(self):
        try:
           
            nombre = self.nombre_entry.get()
            salario_hora = float(self.salario_hora_entry.get())
            horas_trabajadas = int(self.horas_trabajadas_entry.get())

          
            if not nombre:
                raise ValueError("El campo de nombre no puede estar vacío.")

           
            empleado = Empleado(nombre, salario_hora, horas_trabajadas)
            salario_mensual = empleado.calcular_salario_mensual()

           
            if salario_mensual > 450000:
                mensaje = f"Nombre: {nombre}\nSalario mensual: ${salario_mensual:,.2f}"
            else:
                mensaje = f"Nombre: {nombre}\n"

            messagebox.showinfo("Resultado", mensaje)

        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
