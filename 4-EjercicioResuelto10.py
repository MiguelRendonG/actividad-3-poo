import tkinter as tk
from tkinter import messagebox
#Pago de Matricula Universidad

class Estudiante:
    def __init__(self, numero_inscripcion, nombres, patrimonio, estrato):
        self.numero_inscripcion = numero_inscripcion
        self.nombres = nombres
        self.patrimonio = patrimonio
        self.estrato = estrato

    def calcular_matricula(self):
        base_matricula = 50000
        if self.patrimonio > 2000000 and self.estrato > 3:
            incremento = 0.03 * self.patrimonio
        else:
            incremento = 0
        return base_matricula + incremento


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Matrícula")


        tk.Label(root, text="Número de Inscripción:").grid(row=0, column=0, padx=5, pady=5)
        self.inscripcion_entry = tk.Entry(root)
        self.inscripcion_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Nombres:").grid(row=1, column=0, padx=5, pady=5)
        self.nombres_entry = tk.Entry(root)
        self.nombres_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="Patrimonio:").grid(row=2, column=0, padx=5, pady=5)
        self.patrimonio_entry = tk.Entry(root)
        self.patrimonio_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(root, text="Estrato Social:").grid(row=3, column=0, padx=5, pady=5)
        self.estrato_entry = tk.Entry(root)
        self.estrato_entry.grid(row=3, column=1, padx=5, pady=5)

       
        calcular_button = tk.Button(root, text="Calcular Matrícula", command=self.calcular)
        calcular_button.grid(row=4, column=0, columnspan=2, pady=10)

    def calcular(self):
        try:
     
            numero_inscripcion = self.inscripcion_entry.get()
            nombres = self.nombres_entry.get()
            patrimonio = float(self.patrimonio_entry.get())
            estrato = int(self.estrato_entry.get())

     
            if not numero_inscripcion or not nombres:
                raise ValueError("Los campos de inscripción y nombres no pueden estar vacíos.")

          
            estudiante = Estudiante(numero_inscripcion, nombres, patrimonio, estrato)
            matricula = estudiante.calcular_matricula()

      
            messagebox.showinfo(
                "Resultado",
                f"Número de Inscripción: {numero_inscripcion}\n"
                f"Nombres: {nombres}\n"
                f"Pago de Matrícula: ${matricula:,.2f}"
            )
        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
