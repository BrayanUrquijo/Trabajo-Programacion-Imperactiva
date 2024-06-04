import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CheckInStart(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sky-Voyage")
        self.configure(bg="#ffffff")
        self.geometry("400x300")

        # Logo
        self.logo_image = Image.open("logo.png")
        self.logo_image = self.logo_image.resize((100, 100))
        self.logo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(self, image=self.logo, bg="#ffffff")

        # Campos de entrada
        self.code_label = tk.Label(self, text="Código", bg="#ffffff")
        self.code_entry = tk.Entry(self, font=("Helvetica", 12))

        self.last_name_label = tk.Label(self, text="Apellido", bg="#ffffff")
        self.last_name_entry = tk.Entry(self, font=("Helvetica", 12))

        # Botón para realizar check-in
        self.checkin_button = tk.Button(self, text="Realizar Check-In", command=self.continue_to_check_in, bg="#00a651", fg="#ffffff")

        # Layout
        self.logo_label.pack(pady=10)
        self.code_label.pack()
        self.code_entry.pack(pady=5)
        self.last_name_label.pack()
        self.last_name_entry.pack(pady=5)
        self.checkin_button.pack(pady=20)

    def continue_to_check_in(self):
        self.destroy()
        app = FlightSelection()
        app.mainloop()

class FlightSelection(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sky-Voyage")
        self.configure(bg="#ffffff")
        self.geometry("400x300")

        # Campos de entrada
        self.trip_type_label = tk.Label(self, text="Tipo de Viaje", bg="#ffffff")
        self.trip_type_var = tk.StringVar(self)
        self.trip_type_var.set("Solo Ida")
        self.trip_type_dropdown = tk.OptionMenu(self, self.trip_type_var, "Solo Ida", "Ida y Vuelta")

        self.passenger_count_label = tk.Label(self, text="Cantidad de Pasajeros", bg="#ffffff")
        self.passenger_count_entry = tk.Entry(self, font=("Helvetica", 12))

        self.origin_label = tk.Label(self, text="Origen", bg="#ffffff")
        self.origin_var = tk.StringVar(self)
        self.origin_dropdown = ttk.Combobox(self, textvariable=self.origin_var, values=["Ciudad A", "Ciudad B", "Ciudad C"], font=("Helvetica", 12))

        self.destination_label = tk.Label(self, text="Destino", bg="#ffffff")
        self.destination_var = tk.StringVar(self)
        self.destination_dropdown = ttk.Combobox(self, textvariable=self.destination_var, values=["Ciudad X", "Ciudad Y", "Ciudad Z"], font=("Helvetica", 12))

        self.date_label = tk.Label(self, text="Fecha de Viaje", bg="#ffffff")
        self.date_entry = tk.Entry(self, font=("Helvetica", 12))

        self.service_label = tk.Label(self, text="Tipo de Servicio", bg="#ffffff")
        self.service_var = tk.StringVar(self)
        self.service_var.set("Aluminio")
        self.service_dropdown = tk.OptionMenu(self, self.service_var, "Aluminio", "Diamante", "Premium")

        # Botón para buscar vuelos
        self.search_button = tk.Button(self, text="Buscar Vuelos", command=self.search_flights, bg="#00a651", fg="#ffffff")

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

    def search_flights(self):
        self.destroy()
        app = FlightResults()
        app.mainloop()

class FlightResults(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sky-Voyage")
        self.configure(bg="#ffffff")
        self.geometry("400x300")

        # Información del vuelo
        self.flight_info_label = tk.Label(self, text="Vuelos Disponibles", bg="#ffffff")
        self.flight_info_label.pack(pady=10)

        # Ejemplo de vuelos disponibles (en una lista de botones)
        self.flight_button1 = tk.Button(self, text="07:05 - 08:45\nDesde: 2,290,075", command=self.select_flight, bg="#e6e6e6")
        self.flight_button2 = tk.Button(self, text="08:50 - 10:30\nDesde: 2,614,725", command=self.select_flight, bg="#e6e6e6")
        self.flight_button3 = tk.Button(self, text="12:30 - 14:00\nDesde: 2,520,725", command=self.select_flight, bg="#e6e6e6")

        # Layout
        self.flight_button1.pack(pady=5)
        self.flight_button2.pack(pady=5)
        self.flight_button3.pack(pady=5)

    def select_flight(self):
        self.destroy()
        app = FlightDetails()
        app.mainloop()

class FlightDetails(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sky-Voyage")
        self.configure(bg="#ffffff")
        self.geometry("400x300")

        # Información del vuelo
        self.flight_info_label = tk.Label(self, text="Detalles del Vuelo", bg="#ffffff")
        self.flight_info_label.pack(pady=10)

        # Ejemplo de detalles del vuelo
        self.detail_label = tk.Label(self, text="Origen: Bogotá\nDestino: Cartagena\nDuración: 1h 40m\nClase: Económica\nPrecio: 2,290,075", bg="#ffffff")
        self.detail_label.pack(pady=10)

        # Botones de selección de servicio
        self.service_button1 = tk.Button(self, text="Aluminio", command=self.select_service, bg="#00a651", fg="#ffffff")
        self.service_button2 = tk.Button(self, text="Diamante", command=self.select_service, bg="#00a651", fg="#ffffff")
        self.service_button3 = tk.Button(self, text="Premium", command=self.select_service, bg="#00a651", fg="#ffffff")

        # Layout
        self.service_button1.pack(pady=5)
        self.service_button2.pack(pady=5)
        self.service_button3.pack(pady=5)

    def select_service(self):
        self.destroy()
        app = SeatSelection()
        app.mainloop()

class SeatSelection(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sky-Voyage")
        self.configure(bg="#ffffff")
        self.geometry("400x300")

        # Selección de asientos
        self.seat_selection_label = tk.Label(self, text="Selección de Asientos", bg="#ffffff")
        self.seat_selection_label.pack(pady=10)

        self.seat_map = tk.Frame(self, bg="#ffffff")
        self.seat_map.pack()

        for row in range(6):
            for col in range(6):
                seat_button = tk.Button(self.seat_map, text=f"{chr(65+row)}{col+1}", width=4, bg="#e6e6e6", command=lambda r=row, c=col: self.select_seat(r, c))
                seat_button.grid(row=row, column=col, padx=5, pady=5)

        # Botón para confirmar selección
        self.confirm_button = tk.Button(self, text="Seleccionar", command=self.confirm_selection, bg="#00a651", fg="#ffffff")
        self.confirm_button.pack(pady=20)

    def select_seat(self, row, col):
        # Aquí se puede agregar la lógica para seleccionar un asiento
        print(f"Seat {chr(65+row)}{col+1} selected")

    def confirm_selection(self):
        # Aquí se puede agregar la lógica para confirmar la selección
        print("Selection confirmed")
        self.destroy()

if __name__ == "__main__":
    app = CheckInStart()
    app.mainloop()
