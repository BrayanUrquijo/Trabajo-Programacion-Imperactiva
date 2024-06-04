# Integrante1: Brayan Urquijo – 202459407
# Integrante2: Jhorain Jaramillo – código2
# Integrante2: PrimerNombre SegundoApellido – código3
# Docente: Luis Germán Toro Pareja
# Número de grupo:

# Proyecto Final

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import string
import re

class CheckInStart(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Check-in App")
        self.configure(bg="#e0f7fa")
        self.geometry("800x600") 

        # Logo
        self.logo_image = Image.open("logo.png") 
        self.logo_image = self.logo_image.resize((200, 200))
        self.logo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = ttk.Label(self, image=self.logo, background="#e0f7fa")

        # Campos de entrada
        self.last_name_label = ttk.Label(self, text="Apellido:", background="#e0f7fa")
        self.last_name_entry = ttk.Entry(self, font=("Helvetica", 12))

        self.code_label = ttk.Label(self, text="Código:", background="#e0f7fa")
        self.code_entry = ttk.Entry(self, font=("Helvetica", 12))

        # Botón para continuar al check-in
        self.continue_button = ttk.Button(self, text="Continuar", command=self.continue_to_check_in, style="C.TButton")

        # Layout
        self.logo_label.grid(row=0, column=0, columnspan=2, pady=20, padx=10)

        self.last_name_label.grid(row=1, column=0, sticky="e", padx=10)
        self.last_name_entry.grid(row=1, column=1, padx=10)

        self.code_label.grid(row=2, column=0, sticky="e", padx=10)
        self.code_entry.grid(row=2, column=1, padx=10)

        self.continue_button.grid(row=3, column=0, columnspan=2, pady=20)

        # Centrar ventana en la pantalla
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"+{(screen_width - self.winfo_width()) // 2}+{(screen_height - self.winfo_height()) // 2}")

        # Estilo
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), background="#0288d1", foreground="black")
        style.configure("TEntry", font=("Helvetica", 12))
        style.configure("TLabel", font=("Helvetica", 12, "bold"), background="#e0f7fa", foreground="#0277bd")
        style.configure("C.TButton", font=("Helvetica", 12), background="#0288d1", foreground="black", relief="raised")

    def continue_to_check_in(self):
        # Aquí se verificaría si el usuario está registrado
        registered = False  # Cambiar esta lógica para verificar contra una base de datos real

        if registered:
            # Si está registrado, continuar al proceso de selección de vuelo
            self.destroy()
            app = CheckInProcess()
            app.mainloop()
        else:
            # Si no está registrado, pedir información adicional
            self.destroy()
            app = RegisterUser()
            app.mainloop()

class CheckInProcess(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Selección de Vuelo")
        self.configure(bg="#e0f7fa")
        self.geometry("800x600")  

        # Menú desplegable para seleccionar tipo de viaje
        self.trip_type_label = ttk.Label(self, text="Tipo de Viaje:", background="#e0f7fa")
        self.trip_type_var = tk.StringVar(self)
        self.trip_type_var.set("Solo Ida")
        self.trip_type_dropdown = ttk.OptionMenu(self, self.trip_type_var, "Solo Ida", "Ida y Vuelta")

        # Cantidad de pasajeros
        self.passenger_count_label = ttk.Label(self, text="Cantidad de Pasajeros:", background="#e0f7fa")
        self.passenger_count_entry = ttk.Entry(self, font=("Helvetica", 12))

        # Menús desplegables para seleccionar origen y destino
        self.origin_label = ttk.Label(self, text="Origen:", background="#e0f7fa")
        self.origin_var = tk.StringVar(self)
        self.origin_dropdown = ttk.Combobox(self, textvariable=self.origin_var, values=["Ciudad A", "Ciudad B", "Ciudad C"], font=("Helvetica", 12))

        self.destination_label = ttk.Label(self, text="Destino:", background="#e0f7fa")
        self.destination_var = tk.StringVar(self)
        self.destination_dropdown = ttk.Combobox(self, textvariable=self.destination_var, values=["Ciudad X", "Ciudad Y", "Ciudad Z"], font=("Helvetica", 12))

        # Fecha de viaje
        self.date_label = ttk.Label(self, text="Fecha de Viaje:", background="#e0f7fa")
        self.date_entry = ttk.Entry(self, font=("Helvetica", 12))

        # Menú desplegable para seleccionar tipo de servicio
        self.service_label = ttk.Label(self, text="Tipo de Servicio:", background="#e0f7fa")
        self.service_var = tk.StringVar(self)
        self.service_var.set("Aluminio")
        self.service_dropdown = ttk.OptionMenu(self, self.service_var, "Aluminio", "Diamante", "Premium")

        # Botón para buscar vuelos
        self.search_button = ttk.Button(self, text="Buscar Vuelos", command=self.search_flights, style="C.TButton")

        # Layout
        self.trip_type_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)
        self.trip_type_dropdown.grid(row=0, column=1, padx=10, pady=10)

        self.passenger_count_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.passenger_count_entry.grid(row=1, column=1, padx=10, pady=10)

        self.origin_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)
        self.origin_dropdown.grid(row=2, column=1, padx=10, pady=10)

        self.destination_label.grid(row=3, column=0, sticky="e", padx=10, pady=10)
        self.destination_dropdown.grid(row=3, column=1, padx=10, pady=10)

        self.date_label.grid(row=4, column=0, sticky="e", padx=10, pady=10)
        self.date_entry.grid(row=4, column=1, padx=10, pady=10)

        self.service_label.grid(row=5, column=0, sticky="e", padx=10, pady=10)
        self.service_dropdown.grid(row=5, column=1, padx=10, pady=10)

        self.search_button.grid(row=6, column=0, columnspan=2, pady=20)

        # Centrar ventana en la pantalla
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"+{(screen_width - self.winfo_width()) // 2}+{(screen_height - self.winfo_height()) // 2}")

        # Estilo
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), background="#0288d1", foreground="black")
        style.configure("TEntry", font=("Helvetica", 12))
        style.configure("TLabel", font=("Helvetica", 12, "bold"), background="#e0f7fa", foreground="#0277bd")
        style.configure("C.TButton", font=("Helvetica", 12), background="#0288d1", foreground="black", relief="raised")

    def search_flights(self):
        trip_type = self.trip_type_var.get()
        passenger_count = self.passenger_count_entry.get()
        origin = self.origin_var.get()
        destination = self.destination_var.get()
        date = self.date_entry.get()
        service = self.service_var.get()
        
        # Aquí iría la lógica para buscar vuelos según los criterios ingresados

class RegisterUser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registro de Usuario")
        self.configure(bg="#e0f7fa")
        self.geometry("800x600")  

        # Campos de entrada para la información del usuario
        self.first_name_label = ttk.Label(self, text="Primer Nombre:", background="#e0f7fa")
        self.first_name_entry = ttk.Entry(self, font=("Helvetica", 12))

        self.last_name_label = ttk.Label(self, text="Primer Apellido:", background="#e0f7fa")
        self.last_name_entry = ttk.Entry(self, font=("Helvetica", 12))

        self.gender_label = ttk.Label(self, text="Género:", background="#e0f7fa")
        self.gender_var = tk.StringVar(self)
        self.gender_dropdown = ttk.Combobox(self, textvariable=self.gender_var, values=["Masculino", "Femenino", "Otro"], font=("Helvetica", 12))

        self.nationality_label = ttk.Label(self, text="Nacionalidad:", background="#e0f7fa")
        self.nationality_entry = ttk.Entry(self, font=("Helvetica", 12))

        self.document_number_label = ttk.Label(self, text="Número de Documento:", background="#e0f7fa")
        self.document_number_entry = ttk.Entry(self, font=("Helvetica", 12))

        self.birthdate_label = ttk.Label(self, text="Fecha de Nacimiento (DD/MM/AAAA):", background="#e0f7fa")
        self.birthdate_entry = ttk.Entry(self, font=("Helvetica", 12))

        self.assistance_label = ttk.Label(self, text="Necesita Asistencia:", background="#e0f7fa")
        self.assistance_var = tk.StringVar(self)
        self.assistance_dropdown = ttk.Combobox(self, textvariable=self.assistance_var, values=["Sí", "No"], font=("Helvetica", 12))

        self.email_label = ttk.Label(self, text="Correo Electrónico:", background="#e0f7fa")
        self.email_entry = ttk.Entry(self, font=("Helvetica", 12))

        self.phone_label = ttk.Label(self, text="Número Celular:", background="#e0f7fa")
        self.phone_entry = ttk.Entry(self, font=("Helvetica", 12))

        # Campos de entrada para la información de pago
        self.card_number_label = ttk.Label(self, text="Número de Tarjeta (16 dígitos):", background="#e0f7fa")
        self.card_number_entry = ttk.Entry(self, font=("Helvetica", 12))

        self.cvv_label = ttk.Label(self, text="CVV (3 dígitos):", background="#e0f7fa")
        self.cvv_entry = ttk.Entry(self, font=("Helvetica", 12))

        # Botón para registrar usuario y continuar al check-in
        self.register_button = ttk.Button(self, text="Registrar y Continuar", command=self.register_user, style="C.TButton")

        # Layout
        self.first_name_label.grid(row=0, column=0, sticky="e", padx=10, pady=5)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.last_name_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.gender_label.grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.gender_dropdown.grid(row=2, column=1, padx=10, pady=5)

        self.nationality_label.grid(row=3, column=0, sticky="e", padx=10, pady=5)
        self.nationality_entry.grid(row=3, column=1, padx=10, pady=5)

        self.document_number_label.grid(row=4, column=0, sticky="e", padx=10, pady=5)
        self.document_number_entry.grid(row=4, column=1, padx=10, pady=5)

        self.birthdate_label.grid(row=5, column=0, sticky="e", padx=10, pady=5)
        self.birthdate_entry.grid(row=5, column=1, padx=10, pady=5)

        self.assistance_label.grid(row=6, column=0, sticky="e", padx=10, pady=5)
        self.assistance_dropdown.grid(row=6, column=1, padx=10, pady=5)

        self.email_label.grid(row=7, column=0, sticky="e", padx=10, pady=5)
        self.email_entry.grid(row=7, column=1, padx=10, pady=5)

        self.phone_label.grid(row=8, column=0, sticky="e", padx=10, pady=5)
        self.phone_entry.grid(row=8, column=1, padx=10, pady=5)

        self.card_number_label.grid(row=9, column=0, sticky="e", padx=10, pady=5)
        self.card_number_entry.grid(row=9, column=1, padx=10, pady=5)

        self.cvv_label.grid(row=10, column=0, sticky="e", padx=10, pady=5)
        self.cvv_entry.grid(row=10, column=1, padx=10, pady=5)

        self.register_button.grid(row=11, column=0, columnspan=2, pady=20)

        # Centrar ventana en la pantalla
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"+{(screen_width - self.winfo_width()) // 2}+{(screen_height - self.winfo_height()) // 2}")

        # Estilo
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), background="#0288d1", foreground="black")
        style.configure("TEntry", font=("Helvetica", 12))
        style.configure("TLabel", font=("Helvetica", 12, "bold"), background="#e0f7fa", foreground="#0277bd")
        style.configure("C.TButton", font=("Helvetica", 12), background="#0288d1", foreground="black", relief="raised")

    def register_user(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        gender = self.gender_var.get()
        nationality = self.nationality_entry.get()
        document_number = self.document_number_entry.get()
        birthdate = self.birthdate_entry.get()
        assistance = self.assistance_var.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        card_number = self.card_number_entry.get()
        cvv = self.cvv_entry.get()

        # Validar correo electrónico
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            messagebox.showerror("Error", "Correo electrónico inválido")
            return

        # Validar número celular colombiano
        phone_pattern = r'^3\d{9}$'
        if not re.match(phone_pattern, phone):
            messagebox.showerror("Error", "Número celular inválido")
            return

        # Validar número de tarjeta de crédito
        if not card_number.isdigit() or len(card_number) != 16:
            messagebox.showerror("Error", "Número de tarjeta inválido")
            return

        # Validar CVV
        if not cvv.isdigit() or len(cvv) != 3:
            messagebox.showerror("Error", "CVV inválido")
            return

        # Generar código único de pasajero
        user_code = self.generate_user_code(first_name)

        # Aquí se guardaría la información del usuario en la base de datos
        messagebox.showinfo("Registro Exitoso", f"Usuario registrado con código: {user_code}")
        self.destroy()
        app = CheckInProcess()
        app.mainloop()

    def generate_user_code(self, first_name):
        code = first_name[0].upper()
        code += ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return code

if __name__ == "__main__":
    app = CheckInStart()
    app.mainloop()
