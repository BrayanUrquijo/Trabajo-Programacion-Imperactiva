import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox

def abrir_ventana_seleccion_asientos():

    # Crear la ventana de selección de asientos
    ventana_asientos = tk.Toplevel(root)
    ventana_asientos.title("Superfly")
    ventana_asientos.geometry("800x600")

    # Título de la selección de asientos
    lbl_seleccion_asientos = tk.Label(ventana_asientos, text="Selección de Asientos", font=("Arial", 16))
    lbl_seleccion_asientos.pack(pady=10)

    # Crear el marco para el asiento y las etiquetas de clase
    marco_wrapper = tk.Frame(ventana_asientos)
    marco_wrapper.pack(pady=10)

    marco_asientos = tk.Frame(marco_wrapper)
    marco_asientos.pack(side="left")

    marco_clases = tk.Frame(marco_wrapper)
    marco_clases.pack(padx=20, side="right")  # Añadí un relleno a la derecha para separar las etiquetas de clase

    # Crear etiquetas para las columnas
    columnas = ["A", "B", "C", "D", "E", "F"]
    for i, columna in enumerate(columnas):
        lbl = tk.Label(marco_asientos, text=columna)
        lbl.grid(row=0, column=i+1)

    # Crear los botones para los asientos (72 asientos, 12 filas x 6 columnas)
    num_filas = 12
    num_columnas = 6

    for r in range(num_filas):
        lbl = tk.Label(marco_asientos, text=str(r+1))
        lbl.grid(row=r+1, column=0)
        for c in range(num_columnas):
            clase = "Aluminio" if r >= 8 else "Diamante" if r >= 4 else "Premium"
            color = "mediumpurple" if clase == "Premium" else "slateblue" if clase == "Diamante" else "darkslateblue"
            btn = tk.Button(marco_asientos, bg=color, width=2, height=1)
            btn.grid(row=r+1, column=c+1, padx=2, pady=2)

    # Crear las etiquetas para las clases
    lbl_premium = tk.Label(marco_clases, text="Premium", bg="mediumpurple", width=10)
    lbl_premium.pack(pady=5)

    lbl_diamante = tk.Label(marco_clases, text="Diamante", bg= "slateblue", width=10)
    lbl_diamante.pack(pady=5)

    lbl_aluminio = tk.Label(marco_clases, text="Aluminio", bg="darkslateblue", width=10)
    lbl_aluminio.pack(pady=5)

    # Botón de selección
    btn_seleccionar = tk.Button(ventana_asientos, text="Seleccionar", bg="darkviolet", fg="white", command=mostrar_vuelos)
    btn_seleccionar.pack(pady=20)

def boton_tipo_viaje():
    if btn_tip_viaje['text'] == "solo ida":
        btn_tip_viaje.config(text="ida y vuelta")
    else:
        btn_tip_viaje.config(text="solo ida")


def abrir_nueva_ventana():
    # Crear la nueva ventana
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Superfly")
    nueva_ventana.geometry("800x400")

    # Crear el encabezado
    encabezado = tk.Frame(nueva_ventana, bg="mediumpurple")
    encabezado.pack(side="top", fill="x")

    # Título de la aplicación
    titulo = tk.Label(encabezado, text="Superfly", bg="mediumpurple", fg="white", font=("Arial", 24))
    titulo.pack(pady=10)

    # Crear la barra de navegación
    barra_navegacion = tk.Frame(nueva_ventana, bg="navy")
    barra_navegacion.pack(side="top", fill="x")

    # Botón de navegación "Solo ida" "ida y vuelta"
    global btn_tip_viaje 
    btn_tip_viaje= tk.Button(barra_navegacion, text="Solo ida", relief="flat", bg="lightsteelblue", command= boton_tipo_viaje )
    btn_tip_viaje.pack(side="left", padx=10, pady=5)

    # Agregar combobox para seleccionar cantidad de personas

    personas_label = tk.Label(barra_navegacion, text="Personas:", bg="lightsteelblue")
    personas_label.pack(side="right", padx=5, pady=5)
    
    global personas_combobox
    personas_combobox = ttk.Combobox(barra_navegacion, values=[str(i) for i in range(1, 11)], width=3)
    personas_combobox.current(0)  # Set default value to 1
    personas_combobox.pack(side="right", padx=5, pady=5)



    # Crear el marco para el formulario de búsqueda
    marco_busqueda = tk.Frame(nueva_ventana, bg='white', bd=2, relief=tk.GROOVE)
    marco_busqueda.pack(pady=20, padx=20, fill='x')

    # Campos de entrada para Origen y Destino
    lbl_origen = tk.Label(marco_busqueda, text="Origen:", bg='white')
    lbl_origen.grid(row=0, column=0, padx=10, pady=5)
    entrada_origen = ttk.Combobox(marco_busqueda, values=["Bogotá (BOG)", "Medellín (MDE)", "Cali (CLO)", "Cartagena (CTG)", "Barranquilla (BAQ)"])
    entrada_origen.grid(row=0, column=1, padx=10, pady=5)

    lbl_destino = tk.Label(marco_busqueda, text="Destino:", bg='white')
    lbl_destino.grid(row=0, column=2, padx=10, pady=5)
    entrada_destino = ttk.Combobox(marco_busqueda, values=["Buenos Aires (EZE)", "Santiago (SCL)", "Lima (LIM)", "Ciudad de México (MEX)", "Madrid (MAD)"])
    entrada_destino.grid(row=0, column=3, padx=10, pady=5)

    # Selector de fecha
    lbl_fecha = tk.Label(marco_busqueda, text="Ida:", bg='white')
    lbl_fecha.grid(row=0, column=4, padx=10, pady=5)
    entrada_fecha = ttk.Combobox(marco_busqueda, values=["9/06/2024", "10/06/2024", "11/06/2024", "12/06/2024", "13/06/2024"])
    entrada_fecha.grid(row=0, column=5, padx=10, pady=5)

    # Botón de búsqueda
    btn_buscar = tk.Button(marco_busqueda, text="Buscar", bg="darkviolet", fg="white", command=abrir_ventana_seleccion_asientos)
    btn_buscar.grid(row=1, columnspan=6, pady=20)

# Función para guardar los datos ingresados por el usuario
def guardar_datos():
    codigo = codigo_entry.get()
    apellido = apellido_entry.get()
    # Aquí puedes guardar los datos en un archivo, base de datos, etc.
    # Para este ejemplo, solo imprimiremos los datos en la consola
    print(f"Código: {codigo}, Apellido: {apellido}")
    # Ejemplo de guardar en un archivo de texto
    with open('datos_checkin.txt', 'a') as file:
        file.write(f"Código: {codigo}, Apellido: {apellido}\n")
    
    # Llamar a la función para abrir la nueva ventana
    abrir_nueva_ventana()

# Ventana principal
root = tk.Tk()
root.title("Superfly")
root.geometry("300x300")
root.configure(bg='white')

# Se crea un lienzo para los componentes (botones, títulos, etc)
marco = tk.Frame(root, bg='white')
marco.pack(pady=30)


imagen_original = Image.open('Logo.png')
imagen_redimensionada = imagen_original.resize((100, 100))  # Cambia el tamaño a 100x100 píxeles
Logo = ImageTk.PhotoImage(imagen_redimensionada)

# Agregar la imagen redimensionada
logo_label = tk.Label(marco, image=Logo, bg='white')
logo_label.grid(row=0, columnspan=2, pady=10)

# Crear las etiquetas y entradas para "Código"
codigo_label = tk.Label(marco, text="Código", bg='white')
codigo_label.grid(row=1, column=0, padx=10, pady=5)

codigo_entry = tk.Entry(marco)
codigo_entry.grid(row=1, column=1, padx=10, pady=5)

# Crear las etiquetas y entradas para "Apellido"
apellido_label = tk.Label(marco, text="Apellido", bg='white')
apellido_label.grid(row=2, column=0, padx=10, pady=5)

apellido_entry = tk.Entry(marco)
apellido_entry.grid(row=2, column=1, padx=10, pady=5)

# Crear el botón para realizar el check-in
checkin_button = tk.Button(marco, text="Realizar Check-in", bg='darkviolet', fg='black', command=guardar_datos)
checkin_button.grid(row=3, columnspan=2, pady=10)

# crea otra ventana que filtre los vuelos por : mejor precio, directo
vuelos = {
    "BOG-CAR": [
        {"hora_salida": "07:05", "hora_llegada": "14:25", "precio": 2290075, "directo": True},
        {"hora_salida": "03:59", "hora_llegada": "15:30", "precio": 2614725, "directo": False},
        {"hora_salida": "23:10", "hora_llegada": "15:30", "precio": 2520725, "directo": False},
    ],
    # ... otros vuelos
}




def mostrar_vuelos():
    # Crear la nueva ventana
    ventana_vuelos = tk.Toplevel(root)
    ventana_vuelos.title("Superfly")
    ventana_vuelos.geometry("800x600")

    # Crear el encabezado
    encabezado = tk.Frame(ventana_vuelos, bg="mediumpurple")
    encabezado.pack(side="top", fill="x")

    # Título de la aplicación
    titulo = tk.Label(encabezado, text="Superfly", bg="mediumpurple", fg="white", font=("Arial", 24))
    titulo.pack(pady=10)


    # Crear la barra de navegación
    barra_navegacion = tk.Frame(ventana_vuelos, bg="navy")
    barra_navegacion.pack(side="top", fill="x")

        # crear las fechas 
    dates_frame = ttk.Frame(ventana_vuelos)
    prices_frame = ttk.Frame(ventana_vuelos)
    

    #datos x para ver si funciona
    dates_labels = [
        "Mier. 19 Jun.",
        "Mier. 19 jun. ",
        "Jue. 20 Jun.",
        "Jue. 20 Jun.",
        "Vie. 21 Jun.",
    ]
    prices_labels = [
        "COP 2.290.075",
        "COP 2.290.075",
        "COP 2.290.075",
        "COP 2.290.075",        
        "COP 2.290.075",
    ]
    
   
    
    for i in range(len(dates_labels)):
        dates_label = ttk.Label(dates_frame, text=dates_labels[0])
        dates_label.grid(row=0, column=i)
        prices_label = ttk.Label(prices_frame, text=prices_labels[0])
        prices_label.grid(row=0, column=i)
    # Place the frames
    dates_frame.pack()
    prices_frame.pack()
    
    # Agregar combobox para filtrar los vuelos por mejor precio o directo
    filtro_combobox = ttk.Combobox(barra_navegacion, values=["Mejor Precio", "Directo"], width=12)
    filtro_combobox.current(0)  
    filtro_combobox.pack(side="left", padx=10, pady=5)

    # Crear el marco para los vuelos
    marco_vuelos = tk.Frame(ventana_vuelos)
    marco_vuelos.pack(pady=20)

    # Crear un vuelo
    for ruta, vuelos_ruta in vuelos.items():
        for vuelo in vuelos_ruta:
            vuelo_frame = tk.Frame(marco_vuelos, relief=tk.SOLID, bd=2, bg="lavender")
            vuelo_frame.pack(fill="x", pady=10)

            # Título del vuelo
            
            vuelo_title = tk.Label(vuelo_frame, text=f"{ruta} - {vuelo['hora_salida']} - {vuelo['hora_llegada']}", font=("Helvetica", 12), bg="mediumpurple")
            vuelo_title.pack(side="left", padx=10)
            

            # Detalles del vuelo
            vuelo_details = tk.Label(vuelo_frame, text=f"Directo: {vuelo['directo']} - Precio: COP {vuelo['precio']}", font=("Arial", 12), bg="#fff")
            vuelo_details.pack(side="left", padx=10)

            # Precio del vuelo
            vuelo_price = tk.Label(vuelo_frame, text="Desde COP 2.290.075", font=("Arial", 12), bg="#fff", fg="#228B22")
            vuelo_price.pack(fill="x", pady=10)

            # Botón de selección
            btn_seleccionar = tk.Button(vuelo_frame, text="Seleccionar", bg="darkviolet", fg="white", command= abrir_ventana_seleccion_paquete)
            btn_seleccionar.pack(side="right", padx=10)


    btn_siguiente = tk.Button(marco_vuelos, text="Siguiente", bg="darkviolet", fg="white", command=nueva_ventana_registro)
    btn_siguiente.pack(pady=20)

def abrir_ventana_seleccion_paquete():
    ventana_seleccion_asientos = tk.Toplevel(root)
    ventana_seleccion_asientos.title("Seleccionar Servicio")
    ventana_seleccion_asientos.geometry("800x700")

    # Frame para el servicio "Aluminio"
    frame_aluminio = tk.Frame(ventana_seleccion_asientos, bg="white")
    frame_aluminio.pack(pady=20)

    # Label para el nombre del servicio "Aluminio"
    lbl_aluminio = tk.Label(frame_aluminio, text="Aluminio", font=("Arial", 18), bg="white")
    lbl_aluminio.pack()

    # Label para las comodidades del servicio "Aluminio"
    lbl_comodidades_aluminio = tk.Label(frame_aluminio, text="Comodidades: 1 artículo personal (bolso) (Debe caber debajo del asiento)\n1 equipaje de mano (10 kg) (Desde $195.100 COP)\nEquipaje de bodega (23 kg) (Desde $175.600 COP)\nAsiento Economy (Aleatoria-clasificado Aluminio)", bg="white")
    lbl_comodidades_aluminio.pack()

    # Label para los requisitos del servicio "Aluminio"
    lbl_requisitos_aluminio = tk.Label(frame_aluminio, text="Requisitos: Cambios de vuelo (No es permitido)\nReembolso (No es permitido)", bg="white")
    lbl_requisitos_aluminio.pack()

    # Botón para seleccionar el servicio "Aluminio"
    btn_seleccionar_aluminio = tk.Button(frame_aluminio, text="Seleccionar", bg="darkviolet", fg="white", command=nueva_ventana_registro)
    btn_seleccionar_aluminio.pack(pady=10)

    # Frame para el servicio "Diamante"
    frame_diamante = tk.Frame(ventana_seleccion_asientos, bg="white")
    frame_diamante.pack(pady=20)

    # Label para el nombre del servicio "Diamante"
    lbl_diamante = tk.Label(frame_diamante, text="Diamante", font=("Arial", 18), bg="white")
    lbl_diamante.pack()

    # Label para las comodidades del servicio "Diamante"
    lbl_comodidades_diamante = tk.Label(frame_diamante, text="Comodidades: 1 artículo personal (bolso) (Debe caber debajo del asiento)\n1 equipaje de bodega (23 kg) (Debe caber en el compartimiento superior)\n1 equipaje de mano (10 kg) (Entrega el equipaje en el counter)\nAsiento Economy (Filas específicas disponibles de manera aleatoria)", bg="white")
    lbl_comodidades_diamante.pack()

    # Label para los requisitos del servicio "Diamante"
    lbl_requisitos_diamante = tk.Label(frame_diamante, text="Requisitos: Cambios de vuelo (No es permitido)\nReembolso (No es permitido)", bg="white")
    lbl_requisitos_diamante.pack()

    # Botón para seleccionar el servicio "Diamante"
    btn_seleccionar_diamante = tk.Button(frame_diamante, text="Seleccionar", bg="darkviolet", fg="white", command=nueva_ventana_registro)
    btn_seleccionar_diamante.pack(pady=10)

    # Frame para el servicio "Premium"
    frame_premium = tk.Frame(ventana_seleccion_asientos, bg="white")
    frame_premium.pack(pady=20)

    # Label para el nombre del servicio "Premium"
    lbl_premium = tk.Label(frame_premium, text="Premium", font=("Arial", 18), bg="white")
    lbl_premium.pack()

    # Label para las comodidades del servicio "Premium"
    lbl_comodidades_premium = tk.Label(frame_premium, text="Comodidades: 1 artículo personal (bolso) (Debe caber debajo del asiento)\n1 equipaje de mano (10 kg) (Debe caber en el compartimiento superior)\n1 equipaje de bodega (23 kg) (Entrega el equipaje en el counter)\nAsiento Plus (Sujeto a disponibilidad-clasificado Premium)", bg="white")
    lbl_comodidades_premium.pack()

    # Label para los requisitos del servicio "Premium"
    lbl_requisitos_premium = tk.Label(frame_premium, text="Requisitos: Cambios de vuelo (Sin cargo por cambio, antes del vuelo)\nReembolso (No es permitido)", bg="white")
    lbl_requisitos_premium.pack()

    # Botón para seleccionar el servicio "Premium"
    btn_seleccionar_premium = tk.Button(frame_premium, text="Seleccionar", bg="darkviolet", fg="white", command=nueva_ventana_compra)
    btn_seleccionar_premium.pack(pady=10)

def nueva_ventana_compra():
    # crea una nueva ventana que le permita al usuario ver que vuelo escogio y que paquete
    ventana_compra = tk.Toplevel(root)
    ventana_compra.title("Superfly")
    ventana_compra.geometry("800x600")

    # Crear el encabezado
    encabezado = tk.Frame(ventana_compra, bg="mediumpurple")
    encabezado.pack(side="top", fill="x")

    # Título de la ventana
    titulo = tk.Label(encabezado, text="Resumen de Compra", bg="mediumpurple", fg="white", font=("Arial", 24))
    titulo.pack(pady=10)

    # Mostrar el vuelo seleccionado
    vuelo_label = tk.Label(ventana_compra, text="Vuelo seleccionado:", font=("Arial", 18))
    vuelo_label.pack(pady=10)

    vuelo_text = tk.Text(ventana_compra, height=5, width=50)
    vuelo_text.insert(tk.END, vuelo_seleccionado)
    vuelo_text.pack()

    # Mostrar el paquete seleccionado
    paquete_label = tk.Label(ventana_compra, text="Paquete seleccionado:", font=("Arial", 18))
    paquete_label.pack(pady=10)

    paquete_text = tk.Text(ventana_compra, height=5, width=50)
    paquete_text.insert(tk.END, "Aluminio")
    paquete_text.pack()

    # Botón para continuar con el pago
    btn_continuar_pago = tk.Button(ventana_compra, text="Continuar con el Pago", bg="darkviolet", fg="white", command=nueva_ventana_registro)
    btn_continuar_pago.pack(pady=20)

def nueva_ventana_registro():
    marco_registro = tk.Frame(root)  
    marco_registro.pack()
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Superfly")
    nueva_ventana.geometry("800x600")

    # Crear el encabezado
    encabezado = tk.Frame(nueva_ventana, bg="mediumpurple")
    encabezado.pack(side="top", fill="x")

    # Título de la aplicación
    titulo = tk.Label(encabezado, text="Superfly", bg="mediumpurple", fg="white", font=("Arial", 24))
    titulo.pack(pady=10)

    # Crear el marco para el formulario de registro
    marco_registro = tk.Frame(nueva_ventana, bg='lavender', bd=2, relief=tk.GROOVE)
    marco_registro.pack(pady=20, padx=20, fill='x')
    
    # Actualizar la ventana para que cada dato que se debe pedir sean botones y que al presionarlos sea una entrada para poder ingresar el dato
    # Primer nombre
    lbl_primer_nombre = tk.Label(marco_registro, text="Primer Nombre:", bg='white')
    lbl_primer_nombre.grid(row=0, column=0, padx=10, pady=5)
    entrada_primer_nombre = tk.Entry(marco_registro)
    entrada_primer_nombre.grid(row=0, column=1, padx=10, pady=5)

    # Primer apellido
    lbl_primer_apellido = tk.Label(marco_registro, text="Primer Apellido:", bg='white')
    lbl_primer_apellido.grid(row=0, column=2, padx=10, pady=5)
    entrada_primer_apellido = tk.Entry(marco_registro)
    entrada_primer_apellido.grid(row=0, column=3, padx=10, pady=5)

    # Género
    lbl_genero = tk.Label(marco_registro, text="Género:", bg='white')
    lbl_genero.grid(row=1, column=0, padx=10, pady=5)
    opciones_genero = ["Femenino", "Masculino", "No Binario", "Otro"]
    entrada_genero = ttk.Combobox(marco_registro, values=opciones_genero)
    entrada_genero.grid(row=1, column=1, padx=10, pady=5)

    # Nacionalidad
    lbl_nacionalidad = tk.Label(marco_registro, text="Nacionalidad:", bg='white')
    lbl_nacionalidad.grid(row=1, column=2, padx=10, pady=5)
    entrada_nacionalidad = tk.Entry(marco_registro)
    entrada_nacionalidad.grid(row=1, column=3, padx=10, pady=5)

    # Número de documento
    lbl_numero_documento = tk.Label(marco_registro, text="Número de Documento:", bg='white')
    lbl_numero_documento.grid(row=2, column=0, padx=10, pady=5)
    entrada_numero_documento = tk.Entry(marco_registro)
    entrada_numero_documento.grid(row=2, column=1, padx=10, pady=5)

    # # Botón de registro
    # btn_registro = tk.Button(marco_registro, text="Registrarse", bg="darkviolet", fg="white", command=nueva_ventana_tarjeta)
    # btn_registro.grid(row=5, column=0, padx=10, pady=5, sticky="se")
    # entrada_numero_documento = tk.Entry(marco_registro)
    # entrada_numero_documento.grid(row=5, column=1, padx=10, pady=5, sticky="se")

    # Fecha de Nacimiento
    lbl_fecha_nacimiento = tk.Label(marco_registro, text="Fecha de Nacimiento (DD/MM/AAAA):", bg='white')
    lbl_fecha_nacimiento.grid(row=2, column=2, padx=10, pady=5)
    entrada_fecha_nacimiento = tk.Entry(marco_registro)
    entrada_fecha_nacimiento.grid(row=2, column=3, padx=10, pady=5)

    # Asistencia durante el vuelo
    lbl_asistencia = tk.Label(marco_registro, text="Necesita Asistencia durante el vuelo:", bg='white')
    lbl_asistencia.grid(row=3, column=0, padx=10, pady=5)
    opciones_asistencia = ["Si", "No"]
    entrada_asistencia = ttk.Combobox(marco_registro, values=opciones_asistencia)
    entrada_asistencia.grid(row=3, column=1, padx=10, pady=5)

    # Correo electrónico
    lbl_correo = tk.Label(marco_registro, text="Correo Electrónico:", bg='white')
    lbl_correo.grid(row=3, column=2, padx=10, pady=5)
    entrada_correo = tk.Entry(marco_registro)
    entrada_correo.grid(row=3, column=3, padx=10, pady=5)

    # Número Celular
    lbl_numero_celular = tk.Label(marco_registro, text="Número Celular:", bg='white')
    lbl_numero_celular.grid(row=4, column=0, padx=10, pady=5)
    entrada_numero_celular = tk.Entry(marco_registro)
    entrada_numero_celular.grid(row=4, column=1, padx=10, pady=5)

    # Botón de registro
    continuar_button = tk.Button(marco_registro, text="Continuar", bg='darkviolet', fg='black', command= nueva_ventana_tarjeta)
    continuar_button.grid(row=5, columnspan=4, pady=10)

def nueva_ventana_tarjeta():
    marco_tarjeta = tk.Frame(root)  
    marco_tarjeta.pack()
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Superfly")
    nueva_ventana.geometry("800x600")

    # Crear el encabezado
    encabezado = tk.Frame(nueva_ventana, bg="mediumpurple")
    encabezado.pack(side="top", fill="x")

    # Título de la aplicación
    titulo = tk.Label(encabezado, text="Superfly", bg="mediumpurple", fg="white", font=("Arial", 24))
    titulo.pack(pady=10)

    # Título del marco
    titulo_tarjeta = tk.Label(nueva_ventana, text="Datos de la Tarjeta", font=("Arial", 24))
    titulo_tarjeta.pack(pady=10)


    # Crear el marco para el formulario de registro
    marco_tarjeta = tk.Frame(nueva_ventana, bg='lavender', bd=2, relief=tk.GROOVE)
    marco_tarjeta.pack(pady=20, padx=20, fill='x')
    
    # Tipo de tarjeta
    lbl_tipo_tarjeta = tk.Label(marco_tarjeta, text="Tipo de Tarjeta:", bg='white')
    lbl_tipo_tarjeta.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    opciones_tarjeta = ["Débito", "Crédito"]
    entrada_tipo_tarjeta = ttk.Combobox(marco_tarjeta, values=opciones_tarjeta)
    entrada_tipo_tarjeta.grid(row=0, column=1, padx=10, pady=5)

    # Nombre del titular
    lbl_nombre_titular = tk.Label(marco_tarjeta, text="Nombre del Titular:", bg='white')
    lbl_nombre_titular.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entrada_nombre_titular = tk.Entry(marco_tarjeta)
    entrada_nombre_titular.grid(row=1, column=1, padx=10, pady=5)

    # Número de tarjeta
    lbl_numero_tarjeta = tk.Label(marco_tarjeta, text="Número de Tarjeta:", bg='white')
    lbl_numero_tarjeta.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entrada_numero_tarjeta = tk.Entry(marco_tarjeta)
    entrada_numero_tarjeta.grid(row=2, column=1, padx=10, pady=5)

    # Fecha de expiración
    lbl_fecha_expiracion = tk.Label(marco_tarjeta, text="Fecha de Expiración:", bg='white')
    lbl_fecha_expiracion.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    opciones_mes = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    entrada_mes = ttk.Combobox(marco_tarjeta, values=opciones_mes)
    entrada_mes.grid(row=3, column=1, padx=10, pady=5)

    opciones_anio = ["2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032"]
    entrada_anio = ttk.Combobox(marco_tarjeta, values=opciones_anio)
    entrada_anio.grid(row=3, column=2, padx=10, pady=5)

    # CVV
    lbl_cvv = tk.Label(marco_tarjeta, text="CVV:", bg='white')
    lbl_cvv.grid(row=4, column=0, padx=10, pady=5, sticky="w")

    entrada_cvv = tk.Entry(marco_tarjeta)
    entrada_cvv.grid(row=4, column=1, padx=10, pady=5)


    # Botón de continuar
    continuar_button = tk.Button(marco_tarjeta, text="Continuar", bg='darkviolet', fg='black', command=lambda: ventana_resumen_compra(vuelo_seleccionado, num_personas, total_pagar))
    continuar_button.grid(row=5, columnspan=3, pady=10)

    # Crear una ventana de resumen de compra que contiene el vuelo seleccionado por el usuario en la ventana de "mostrar_vuelos", el número de personas y el valor total a pagar

def ventana_resumen_compra(vuelo, num_personas, total_pagar):
    # Crear la ventana de resumen de compra
    ventana_resumen = tk.Toplevel(root)
    ventana_resumen.title("Resumen de Compra")
    ventana_resumen.geometry("500x400")

    # Crear el marco para los componentes
    marco_resumen = tk.Frame(ventana_resumen, bg='white')
    marco_resumen.pack(pady=30)

    # Mostrar el vuelo seleccionado
    vuelo_label = tk.Label(marco_resumen, text="Vuelo seleccionado:", bg='white')
    vuelo_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

    vuelo_entry = tk.Entry(marco_resumen)
    vuelo_entry.insert(0, vuelo)
    vuelo_entry.configure(state='readonly')
    vuelo_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    # Mostrar el número de personas
    personas_label = tk.Label(marco_resumen, text="Número de personas:", bg='white')
    personas_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

    personas_entry = tk.Entry(marco_resumen)
    personas_entry.insert(0, num_personas)
    personas_entry.configure(state='readonly')
    personas_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    # Mostrar el total a pagar
    total_label = tk.Label(marco_resumen, text="Total a pagar:", bg='white')
    total_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

    total_entry = tk.Entry(marco_resumen, font=("Arial", 16, "bold"))
    total_entry.insert(0, total_pagar)
    total_entry.configure(state='readonly')
    total_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    # Botón de pagar
    pagar_button = tk.Button(marco_resumen, text="Pagar", bg='darkviolet', fg='black', command= crear_ventana_tiquete)
    pagar_button.grid(row=3, columnspan=2, pady=10)

# Llamar a la función ventana_resumen_compra con los valores correspondientes
vuelo_seleccionado = "BOG-CAR"
num_personas = 2
total_pagar = 4600000

def  crear_ventana_tiquete(nombre, origen, numero_vuelo, fecha, destino, hora):
   
    # Create a frame for the airline logo
    logo_frame = tk.Frame(root, bg="red")
    logo_frame.pack(side="left", fill="y")

    # Create the airline logo label
    logo_label = tk.Label(logo_frame, text="Cheap Airline", font=("Arial", 24, "bold"), fg="white", bg="red")
    logo_label.pack(pady=10)

    # Create a frame for the boarding pass details
    boarding_pass_frame = tk.Frame(root, bg="white")
    boarding_pass_frame.pack(side="right", fill="both", expand=True)

    # Create the boarding pass header
    header_frame = tk.Frame(boarding_pass_frame, bg="navy blue")
    header_frame.pack(fill="x")

    # Create the boarding pass header label
    header_label = tk.Label(header_frame, text="Pase de abordaje", font=("Arial", 16, "bold"), fg="white", bg="navy blue")
    header_label.pack(pady=10)

    # Create a frame for the passenger details
    passenger_details_frame = tk.Frame(boarding_pass_frame, bg="white")
    passenger_details_frame.pack(pady=10)

    # Create the passenger name label
    passenger_name_label = tk.Label(passenger_details_frame, text="Nombre Pasajero", font=("Arial", 12))
    passenger_name_label.grid(row=0, column=0, sticky="w")

    # Create the passenger name entry
    passenger_name_entry = tk.Entry(passenger_details_frame, font=("Arial", 12))
    passenger_name_entry.insert(0, "Alejandro Sierra")
    passenger_name_entry.grid(row=0, column=1, sticky="w")

    # Create frames for the flight details
    flight_details_frame = tk.Frame(boarding_pass_frame, bg="white")
    flight_details_frame.pack(pady=10)

    # Create labels and entries for origin, destination, flight number, date, and time
    origin_label = tk.Label(flight_details_frame, text="Origen", font=("Arial", 12))
    origin_label.grid(row=0, column=0, sticky="w")

    origin_entry = tk.Entry(flight_details_frame, font=("Arial", 12))
    origin_entry.insert(0, "BOG")
    origin_entry.grid(row=0, column=1, sticky="w")

    destination_label = tk.Label(flight_details_frame, text="Destino", font=("Arial", 12))
    destination_label.grid(row=1, column=0, sticky="w")

    destination_entry = tk.Entry(flight_details_frame, font=("Arial", 12))
    destination_entry.insert(0, "CAR")
    destination_entry.grid(row=1, column=1, sticky="w")

    flight_number_label = tk.Label(flight_details_frame, text="Vuelo", font=("Arial", 12))
    flight_number_label.grid(row=0, column=2, sticky="w")

    flight_number_entry = tk.Entry(flight_details_frame, font=("Arial", 12))
    flight_number_entry.insert(0, "A 001")
    flight_number_entry.grid(row=0, column=3, sticky="w")

    date_label = tk.Label(flight_details_frame, text="Fecha", font=("Arial", 12))
    date_label.grid(row=1, column=2, sticky="w")

    date_entry = tk.Entry(flight_details_frame, font=("Arial", 12))
    date_entry.insert(0, "20/06/2024")
    date_entry.grid(row=1, column=3, sticky="w")

    time_label = tk.Label(flight_details_frame, text="Hora", font=("Arial", 12))
    time_label.grid(row=2, column=2, sticky="w")

    time_entry = tk.Entry(flight_details_frame, font=("Arial", 12))
    time_entry.insert(0, "07:05 am")
    time_entry.grid(row=2, column=3, sticky="w")
    # Llamar a la función crear_ventana_tiquete con los valores correspondientes
    nombre = "John Doe"
    origen = "BOG"
    numero_vuelo = "SF123"
    fecha = "2022-12-31"
    destino = "CAR"
    hora = "08:00"

    crear_ventana_tiquete(nombre, origen, numero_vuelo, fecha, destino, hora)

# Crear la ventana de resumen de compra con el vuelo seleccionado
    # ventana_resumen_compra(vuelo_seleccionado, num_personas, total_pagar)

if __name__ == "__main__":
    # Iniciar el bucle principal de la aplicación
    root.mainloop()