import tkinter as tk
from tkinter import messagebox, simpledialog
import os

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Contactos")
        self.root.geometry("300x200")
        
        # Definimos un separador que no se espera en un nombre
        self.separator = "!"
        
        self.create_file()
        self.create_widgets()
    
    def create_file(self):
        if not os.path.exists("amigosContacto.txt"):
            open("amigosContacto.txt", "w", encoding="utf-8").close()
    
    def create_widgets(self):
        self.create_btn = tk.Button(self.root, text="Agregar", command=self.create_contact)
        self.create_btn.pack(pady=10)
        
        self.read_btn = tk.Button(self.root, text="Mostrar", command=self.read_contacts)
        self.read_btn.pack(pady=10)
        
        self.update_btn = tk.Button(self.root, text="Editar", command=self.update_contact)
        self.update_btn.pack(pady=10)
        
        self.delete_btn = tk.Button(self.root, text="Eliminar", command=self.delete_contact)
        self.delete_btn.pack(pady=10)
    
    def create_contact(self):
        name = simpledialog.askstring("Crear Contacto", "Ingrese el nombre del contacto:")
        if name:
            phone = simpledialog.askstring("Crear Contacto", "Ingrese el número telefónico:")
            if phone:
                # Importante: validamos que el nombre no incluya el separador
                if self.separator in name:
                    messagebox.showwarning("Advertencia", f"El nombre no debe incluir el separador '{self.separator}'.")
                    return
                registro = name.strip() + self.separator + phone.strip()
                with open("amigosContacto.txt", "a", encoding="utf-8") as file:
                    file.write(registro + "\n")
                messagebox.showinfo("Éxito", "Contacto creado exitosamente")
            else:
                messagebox.showwarning("Advertencia", "El número telefónico es obligatorio.")
    
    def read_contacts(self):
        try:
            with open("amigosContacto.txt", "r", encoding="utf-8") as file:
                contacts = file.readlines()
            if contacts:
                formatted_contacts = ""
                for contact in contacts:
                    contact = contact.strip()
                    if self.separator in contact:
                        # Separamos y limpiamos ambos lados
                        name, phone = contact.split(self.separator, 1)
                        formatted_contacts += f"{name.strip()}!{phone.strip()}\n"
                    else:
                        # En caso de que no se encuentre el separador
                        formatted_contacts += contact + "\n"
                messagebox.showinfo("Contactos", formatted_contacts)
            else:
                messagebox.showinfo("Contactos", "No hay contactos")
        except FileNotFoundError:
            messagebox.showinfo("Contactos", "No hay contactos")
    
    def update_contact(self):
        name_to_update = simpledialog.askstring("Actualizar Contacto", "Ingrese el nombre del contacto a actualizar:")
        if name_to_update:
            with open("amigosContacto.txt", "r", encoding="utf-8") as file:
                contacts = file.readlines()
            
            new_name = simpledialog.askstring("Actualizar Contacto", "Ingrese el nuevo nombre del contacto:")
            new_phone = simpledialog.askstring("Actualizar Contacto", "Ingrese el nuevo número telefónico:")
            
            if new_name is None or new_phone is None:
                messagebox.showwarning("Advertencia", "Se requieren ambos campos para actualizar.")
                return

            # Validamos nuevamente que el nuevo nombre no contenga el separador
            if self.separator in new_name:
                messagebox.showwarning("Advertencia", f"El nombre no debe incluir el separador '{self.separator}'.")
                return

            found = False
            with open("amigosContacto.txt", "w", encoding="utf-8") as file:
                for contact in contacts:
                    original_contact = contact.strip()
                    if self.separator in original_contact:
                        current_name, current_phone = original_contact.split(self.separator, 1)
                        # Comparamos de forma insensible a mayúsculas y eliminando espacios
                        if current_name.strip().lower() == name_to_update.strip().lower():
                            file.write(new_name.strip() + self.separator + new_phone.strip() + "\n")
                            found = True
                        else:
                            file.write(original_contact + "\n")
                    else:
                        # Para registros sin separador, se realiza la comparación
                        if original_contact.strip().lower() == name_to_update.strip().lower():
                            file.write(new_name.strip() + self.separator + new_phone.strip() + "\n")
                            found = True
                        else:
                            file.write(original_contact + "\n")
            if found:
                messagebox.showinfo("Éxito", "Contacto actualizado exitosamente")
            else:
                messagebox.showwarning("Advertencia", "Contacto no encontrado")
    
    def delete_contact(self):
        name_to_delete = simpledialog.askstring("Borrar Contacto", "Ingrese el nombre del contacto a borrar:")
        if name_to_delete:
            found = False
            with open("amigosContacto.txt", "r", encoding="utf-8") as file:
                contacts = file.readlines()
            with open("amigosContacto.txt", "w", encoding="utf-8") as file:
                for contact in contacts:
                    original_contact = contact.strip()
                    if self.separator in original_contact:
                        current_name, _ = original_contact.split(self.separator, 1)
                        if current_name.strip().lower() != name_to_delete.strip().lower():
                            file.write(original_contact + "\n")
                        else:
                            found = True
                    else:
                        if original_contact.strip().lower() != name_to_delete.strip().lower():
                            file.write(original_contact + "\n")
                        else:
                            found = True
            if found:
                messagebox.showinfo("Éxito", "Contacto borrado exitosamente")
            else:
                messagebox.showwarning("Advertencia", "Contacto no encontrado")
            
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
