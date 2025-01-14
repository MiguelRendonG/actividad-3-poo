import tkinter as tk
from tkinter import ttk, messagebox
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base + self.altura + self.hipotenusa()

    def hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def tipo_triangulo(self):
        hip = self.hipotenusa()
        if self.base == self.altura == hip:
            return "Equilátero"
        elif self.base == self.altura or self.base == hip or self.altura == hip:
            return "Isósceles"
        else:
            return "Escaleno"

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras Geométricas")
        self.geometry("500x500")

        self.tabs = ttk.Notebook(self)
        self.tabs.pack(expand=1, fill="both")

        self.create_tabs()

    def create_tabs(self):
        self.circle_tab()
        self.rectangle_tab()
        self.square_tab()
        self.triangle_tab()

    def circle_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="Círculo")

        ttk.Label(tab, text="Radio:").grid(row=0, column=0, padx=10, pady=10)
        self.radio_entry = ttk.Entry(tab)
        self.radio_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Button(tab, text="Calcular", command=self.calculate_circle).grid(row=1, column=0, columnspan=2, pady=10)

    def calculate_circle(self):
        try:
            radio = float(self.radio_entry.get())
            circle = Circulo(radio)
            area = circle.area()
            perimetro = circle.perimetro()
            messagebox.showinfo("Resultados", f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un valor numérico válido.")

    def rectangle_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="Rectángulo")

        ttk.Label(tab, text="Base:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(tab, text="Altura:").grid(row=1, column=0, padx=10, pady=10)

        self.base_rect = ttk.Entry(tab)
        self.base_rect.grid(row=0, column=1, padx=10, pady=10)

        self.altura_rect = ttk.Entry(tab)
        self.altura_rect.grid(row=1, column=1, padx=10, pady=10)

        ttk.Button(tab, text="Calcular", command=self.calculate_rectangle).grid(row=2, column=0, columnspan=2, pady=10)

    def calculate_rectangle(self):
        try:
            base = float(self.base_rect.get())
            altura = float(self.altura_rect.get())
            rect = Rectangulo(base, altura)
            area = rect.area()
            perimetro = rect.perimetro()
            messagebox.showinfo("Resultados", f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

    def square_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="Cuadrado")

        ttk.Label(tab, text="Lado:").grid(row=0, column=0, padx=10, pady=10)
        self.lado_entry = ttk.Entry(tab)
        self.lado_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Button(tab, text="Calcular", command=self.calculate_square).grid(row=1, column=0, columnspan=2, pady=10)

    def calculate_square(self):
        try:
            lado = float(self.lado_entry.get())
            square = Cuadrado(lado)
            area = square.area()
            perimetro = square.perimetro()
            messagebox.showinfo("Resultados", f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un valor numérico válido.")

    def triangle_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="Triángulo")

        ttk.Label(tab, text="Base:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(tab, text="Altura:").grid(row=1, column=0, padx=10, pady=10)

        self.base_tri = ttk.Entry(tab)
        self.base_tri.grid(row=0, column=1, padx=10, pady=10)

        self.altura_tri = ttk.Entry(tab)
        self.altura_tri.grid(row=1, column=1, padx=10, pady=10)

        ttk.Button(tab, text="Calcular", command=self.calculate_triangle).grid(row=2, column=0, columnspan=2, pady=10)

    def calculate_triangle(self):
        try:
            base = float(self.base_tri.get())
            altura = float(self.altura_tri.get())
            tri = TrianguloRectangulo(base, altura)
            area = tri.area()
            perimetro = tri.perimetro()
            hipotenusa = tri.hipotenusa()
            tipo = tri.tipo_triangulo()
            messagebox.showinfo(
                "Resultados",
                f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}\nHipotenusa: {hipotenusa:.2f}\nTipo: {tipo}",
            )
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

# Ejecutar la aplicación
if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
