import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import random 
import string



class CheckInStart(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("check-in app")
        self.configure(bg="#e0f7fa")
        self.geometry("800x600") #este es el tamaño inicial (posiblmente se edite)

        #logo
        self.logo_image = Image.open("logo.png")
        self.logo_image = self.logo_image.resize((200,200))
        self.logo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = ttk.Label(self, image=self.logo, background="#e0f7fa")

        #campos de entrada 
        self.last_name_label = ttk.Label(self, text="Apellido: ", background="#e0f7fa")
        self.last_name_entry = ttk.Entry(self, font=("Helvetica", 12))
        
        self.code_label = ttk.Label(self, text="código:", background="#e0f7fa")
        self.code_entry = ttk.Entry(self, font=("Helvetica", 12))

        #boton para el check in
        self.continue_button = ttk.Button(self, text="continuar", command=self.continue_to_check_in, style="C.TButton")

        #layout
        self.logo_label.grid(row=0, column=0, columnspan=2, pady=20, padx=10)

        self.last_name_label.grid(row=1,column=0, sticky="e",padx=10)
        self.last_name_entry.grid(row=1, column=1, padx=10)

        self.code_label.grid(row=2, column=0, sticky="e", padx=10)
        self.code_entry.grid(row=2, column=1, padx=10)

        self.continue_button.grid(row=3, column=0, columnspan=2, pady=20)
        
        #centro la ventana
        self.update_idletasks()
        screen_width = self.winfo_screen_width()
        screen_height= self.winfo_screenheight()
        self.geometry(f"+{(screen_width - self.winfo_width())//2}+ {(screen_height -self.winfo_height())//2}")

        #estilo
        style = ttk.style()
        style.configure("TButton", font=("Helvetica",12), background="#0288d1", foreground="black")
        style.configure("TEntry", font=("Helvetica",12))
        style.configure("TLabel", font=("Helvetica",12,"bold"),background="#e0f7fa",foreground="#0277bd")
        style.configure("C.TButton", font=("Helvetica",12), background="#0299d1",foreground="black", relief="raised")



class CheckInProcesss(tk.Tk):
   def __init__(self):
      super().__init__()
      self.title("seleccion de vuelo")
      self.configure(bg="#e0f7fa")
      self.geometry("800x600")

    #menu desplegable para el tipo de viaje 
      self.trip_type_label = ttk.Label(self, text ="Tipo de viaje:", background="#e0f7fa")
      self.trip_type_var = tk.StringVar(self)
      self.trip_type_var.set("solo ida")
      self.trip_type_dropdpwn = ttk.OptionMenu(self, self.trip_type_var, "solo ida", "Ida y Vuelta")

      #cantidad de pasajeros 
      self.passenger_count_label = ttk.Label(self, text="Cantidad de Pasajeros: ", background="#e0f7fa")
      self.passenger_count_entry = ttk.Entry(self,font=("Helvetica", 12))

      #menus para seleccionar origen y destino
      self.origin_label = ttk.Label(self, text= "Origen:", backgorund="#e0f7fa")
      self.origin_var = tk.StringVar(self)
      self.origin_dropdown = ttk.Combobox(self, textvariable= self.origin_var, values=["ciudad x", "ciudad y", "ciudad z"], font=("Helvetica",12))

      self.destination_label = ttk.Label(self, text= "Destino:", backgorund="#e0f7fa")
      self.destination_var = tk.StringVar(self)
      self.destination_dropdown = ttk.Combobox(self, textvariable= self.destination_var, values=["ciudad x", "ciudad y", "ciudad z"], font=("Helvetica",12))

      #fecha de viaje
      self.date_label = ttk.Label(self, tecxt="Fecha de Viaje: ", background="#e0f7fa")
      self.date_entry = ttk.Entry(self, font=("Helvetica",12))

      #menu desplegable para seleccionar tipo de servicio 
      self.service_label = ttk.Label(self, text="tipo de servivicio", background="#e0f7fa")
      self.service_var = tk.StringVar(self)
      self.service_var.set("Aluminio")
      self.service_dropdown = ttk.OptionMenu(self, self.service_var, "Aluminio", "Diamante", "Premium")

      #Boton para buscar vuelos
      self.search_button = ttk.Button(self, text="Buscar Vuelos", command= self.search_flights, style="C.TButton")

      #Layout
      self.trip_type_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)
      self.trip_type_label.grid(row=0, column=1, padx=10, pady=10)

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

      self.search_button.grid(row=6, column=0, columspan=2, pady=20)


      #centrar ventana en la pantalla
      self.update_idletasks()
      screen_width = self.winfo_screenwidth()
      screen_height = self.winfo_screenheight()
      self.geometry(f"+{(screen_width- self.winfo_width())// 2} + {(screen_height - self.winfo_heght())//2}")

      #estilo 
      style = ttk.Style()
      style.configure("TButton", font=("Helvetica",12),background="#0288d1", foreground="black")
      style.configure("TEntry", font=("Helvetica",12))
      style.configure("TLabel", font=("Helvetica",12, "bold"),background="#e0f7fa", foreground="#0277bd")
      style.configure("C.TButton", font=("Helvetica",12),background="#0288d1", foreground="black", relief="raised")

      def search_flights():
         trip_type = self.trip_type_var.get()
         passenger_count = self.passenger_count_entry.get()
         origin = self.origin_var.get()
         destination = self.destination_var.get()
         date = self.date_entry.get()
         service = self.service_var.get()

class RegisterUser(tk.Tk):
   def __init__(self):
      super().__init__()
      self.title("registro de Usuario")
      self.configure(bg="#e0f7fa")
      self.geometry("800x600")

      #campos de entrada para la info del usuario
      self.first_name_label= ttk.Label(self, text="Primer Nombre: ", background="#e0f7fa")
      self.first_name_entry = ttk.Entry(self, font=("Helvetica", 12))

      self.last_name_label= ttk.Label(self, text="Primer Apellido: ", background="#e0f7fa")
      self.last_name_entry = ttk.Entry(self, font=("Helvetica", 12))

      self.gender_label= ttk.Label(self, text="Género: ", background="#e0f7fa")
      self.gender_var = tk.StringVar(self)
      self.gender_dropdown= ttk.Combobox(self, textvariable=self.gender_var,values=["Masculino", "Femenino", "Otro"], font=("Helvetica",12))     
      
      self.nationality = tk.Entry(self, font=("helvetica,12"))
      self.nationality_label.grid(row=3, column=0, sticky="e", padx=10, pady=5)
      self.nationality_entry.grid(row=3, column=1, padx=10, pady=5)

      self.document_number_label.grid(row=4, column=0, sticky="e", padx= 10, pady=5)
      self.document_number_entry.grid(row=4, column=1, padx=10, pady=5)

      self.birthdate_label.grid(row=5, column=0, sticky="e", padx=10,  pady=5)
      self.birthdate_entry.grid(row=5, column=1, padx=10, pady=5)

      self.assistance_label.grid(row=6,column=0,sticky="e", padx=10,pady=5)
      self.assistance_entry.grid(row=6, column=1, padx=10, pady=5)

      self.email_label.grid(row=7, column=0, sticky="e" , padx=10,pady=5)
      self.email_entry.grid(row=7, column=1,padx=10,pady=5)

      self.phone_label.grid(row=8, column=0, sticky="e", padx=10, pady=5)
      self.phone_entry.grid(row=8,column=1,padx=10, pady=5 )

      self.card_number_label.grid(row=9, column=0, sticky="e", padx=10, pady=5)
      self.card_number_entry.grid(row=9, column=1, padx=10, pady=5)

      self.cvv_label.grid(row=10, column=0, sticky="e", padx=10, pady=5)
      self.cvv_entry.grid(row=10,column=1,padx=10,pady=5)

      self.register_button.grid(row=11, column=0, columnspan=2, pady=20)

      #centrar ventana
      self.update_idletasks()
      screen_width= self.winfo_screenwidth()
      screen_height = self.winfo_screenheight()
      self.geometry(f"+{(screen_width - self.winfo_width())// 2}+{(screen_height -self.winfo_height())// 2}")

      #Estilo
      style = ttk.style()
      style.configure("TButton", font=("Helvetica",12),background="#0288d1", foreground="black")
      style.configure("TEntry", font=("Helvetica",12))
      style.configure("TLabel", font=("Helvetica", 12, "bold"), backgound="#e0f7fa", foreground="#0277bd")
      style.configure("C.TButton", font=("Helvetica", 12), background="#0288d1", foreground="black", relief="raised")

      def continue_to_check_in(self):
            global CheckInProcesss
            #aqui se iria la logica para verificar si el usuario esta en registrado
            #si lo esta entonces se procede al cehck in
            #si no esta hay que registrarlo
            #si el codigo es correcto se procede al check in
           #si no entonces se muestra el mensaje de error
            registered= True
            if registered: 
               self.destroy() 
               app = CheckInProcesss()
               app.mainlopp()
            else:
               self.destroy()
               app = RegisterUser()
               app.mainloop()

def register_user(self):
         global last_name, gender, nationality, document_number, email, birthdate,assistance, phone, card_number, cvv
         first_name= self.first_name_entry.get()
         last_name= self.last_name_entry.get()
         gender= self.gender_var.get()
         nationality= self.nationality_entry.get()
         document_number= self.document_number_entry.get()
         birthdate= self.birthdate_entry.get()
         assistance= self.assitance_var.get()
         email= self.email_entry.get()
         phone= self.phone_entry.get()
         card_number= self.card_number_entry.get()
         cvv= self.cvv_entry.get()

         #AQUI IRIA LA LOGICA PARA VALIDAR LOS CAMPOS VACIOS!!!

         #generar codigo unico de pasajero
         user_code= self.generate_user_code(first_name)

         #aqui se guardaria la info en la base de datos
         messagebox.showinfo("Registro Exitoso",f"usuario registrado con coigo:{user_code}")
         self.destroy()
         app = CheckInProcesss()
         app.mainloop()

def generate_user_code(Self, first_name):
         code = first_name[0].upper()
         code += "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
         return code

if __name__ == "__main__":
   app = CheckInStart()
   app.mainloop()
         







