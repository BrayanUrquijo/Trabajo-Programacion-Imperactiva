# Integrante1: Brayan Urquijo – 202459407
# Integrante2: Jhorain Jaramillo – 202459537
# Integrante2: Valentina Betancourt Caicedo – 202459411
# Docente: Luis Germán Toro Pareja

# Proyecto Final

import tkinter as tk
from tkinter.messagebox import *
from PIL import Image, ImageTk
from tkinter import ttk
from datetime import datetime
import random
import string
import re
    

# Ventana principal
root = tk.Tk()
root.title("SuperFly - Login")
root.geometry("300x300")
root.configure(bg="white")
root.iconbitmap("SuperFly.ico")
# Se crea un lienzo para los componentes (botones, títulos, etc)
marco = tk.Frame(root, bg="white")
marco.pack(pady=30)


imagen_original = Image.open("Logo.png")
imagen_redimensionada = imagen_original.resize((100, 100))  # Cambia el tamaño a 100x100 píxeles
Logo = ImageTk.PhotoImage(imagen_redimensionada)

# Agregar la imagen redimensionada
logo_label = tk.Label(marco, image=Logo, bg="white")
logo_label.grid(row=0, columnspan=2, pady=10)

# Crear las etiquetas y entradas para "Código"
codigo_label = tk.Label(marco, text="Código", bg="white")
codigo_label.grid(row=1, column=0, padx=10, pady=5)

codigo_entry = tk.Entry(marco)
codigo_entry.grid(row=1, column=1, padx=10, pady=5)

# Crear las etiquetas y entradas para "Apellido"
apellido_label = tk.Label(marco, text="Apellido", bg="white")
apellido_label.grid(row=2, column=0, padx=10, pady=5)

apellido_entry = tk.Entry(marco)
apellido_entry.grid(row=2, column=1, padx=10, pady=5)

# Abrir Y Leer La Ultima Línea De datos_personas.txt

def leer_ultima_linea(nombre_archivo):
    with open(nombre_archivo, 'r') as file:
        lineas = file.readlines()
    return lineas[-1]

# Abrir Datos_Vuelos_finales

with open("Datos_Vuelos_Finales", "r") as datos:
    datos_save = datos.read()

# Convertir la cadena en una lista de líneas

data = datos_save.splitlines()

# Crear una matriz vacía

matriz = []

# Crear una lista vacía para cada 

iteracion = []

# Crear listas vacías para cada tipo de clase

vuelo = []
fecha = []
hora_salida = []
hora_llegada = []
valor_min = []
valor_medio = []
valor_max = []
ciudad_origen = []
ciudad_destino = []

# Iterar sobre cada línea en los datos

for i in range(len(data)):
    linea_1 = data[i]
    iteracion.append(linea_1)

# Bucle Para Limpiar La Lista De Iteración

for i in range(len(iteracion)):
    iteracion[i] = iteracion[i].replace(',', '').replace('[', '').replace(']', '').replace("'", "")

# Bucle Para Separar La Lista De Iteración En Una Matriz y Corregir Santa Marta

for i in range(len(iteracion)):
    matriz.append(iteracion[i].split())
    if matriz[i][7] == "Santa":
        matriz[i][7] = "Santa Marta"
        matriz[i].pop(8)
    elif matriz[i][8] == "Santa":
        matriz[i][8] = "San Marta"
        matriz[i].pop(9)

# Separamos El Contenido De La Matriz En Listas Para Obtener Cada Tipo De Clase En Diferentes Listas

for i in range(len(matriz)):
    if matriz[i][0]:
        vuelo.append(matriz[i][0])
    if matriz[i][1]:
        fecha.append(matriz[i][1])
    if matriz[i][2]:
        hora_salida.append(matriz[i][2])
    if matriz[i][3]:
        hora_llegada.append(matriz[i][3])
    if matriz[i][4]:
        valor_min.append(matriz[i][4])
    if matriz[i][5]:
        valor_medio.append(matriz[i][5])
    if matriz[i][6]:
        valor_max.append(matriz[i][6])
    if matriz[i][7]:
        ciudad_origen.append(matriz[i][7])
    if matriz[i][8]:
        ciudad_destino.append(matriz[i][8])

def abrir_ventana_seleccion_asientos():
    # Crear la ventana de selección de asientos
    ventana_asientos = tk.Toplevel(root)
    ventana_asientos.title("SuperFly - Selección de Asientos")
    ventana_asientos.geometry("800x600")
    ventana_asientos.iconbitmap("SuperFly.ico")

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
        posicion_user = []
        lbl = tk.Label(marco_asientos, text=str(r+1))
        lbl.grid(row=r+1, column=0)
        for c in range(num_columnas):
            filas_asiento = ["A", "B", "C", "D", "E", "F"]
            clase = "Aluminio" if r >= 8 else "Diamante" if r >= 4 else "Premium"
            color = "red3" if clase == "Premium" else "red2" if clase == "Diamante" else "red4"
            btn = tk.Button(marco_asientos, bg=color, width=2, height=1, command=lambda posicion = [r+1, filas_asiento[c]]: posicion_user.append(posicion))
            btn.grid(row=r+1, column=c+1, padx=2, pady=2)
    
    # Función para guardar la posición del asiento seleccionado

    def guardar_posicion():
        ultima_linea = int(leer_ultima_linea("datos_personas.txt"))
        print(len(posicion_user))
        if len(posicion_user) == ultima_linea:
            with open('datos_asientos.txt', 'a') as file:
                for posicion in posicion_user:
                    file.write(f"{posicion}\n")
        elif posicion_user != ultima_linea:
            showwarning(title="Error", message=f"Por favor seleccione los asientos para {ultima_linea} pasajeros")
            posicion_user.clear()

    # Crear las etiquetas para las clases
    lbl_premium = tk.Label(marco_clases, text="Premium", bg="red3", width=10)
    lbl_premium.pack(pady=5)

    lbl_diamante = tk.Label(marco_clases, text="Diamante", bg= "red2", width=10)
    lbl_diamante.pack(pady=5)

    lbl_aluminio = tk.Label(marco_clases, text="Aluminio", bg="red4", width=10)
    lbl_aluminio.pack(pady=5)

    # Botón de selección
    btn_seleccionar = tk.Button(ventana_asientos, text="Seleccionar", bg="red3", fg="white", command= lambda : (guardar_posicion(), nueva_ventana_compra(), guardar_paquete_diamante(), actualizar_precio_premium()))
    btn_seleccionar.pack(pady=20)

# Boton Para Elegir El Tipo De Viaje

def boton_tipo_viaje():
    if btn_tip_viaje['text'] == "solo ida":
        btn_tip_viaje.config(text="ida y vuelta")
    else:
        btn_tip_viaje.config(text="solo ida")

# Funcion Para Abrir Ventana De Busqueda De Vuelos

def abrir_nueva_ventana():
    root.withdraw()
    global origen_var, destino_var, entrada_fecha, nueva_ventana
    # Crear la nueva ventana
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("SuperFly - Búsqueda de Vuelos")
    nueva_ventana.geometry("800x400")
    nueva_ventana.iconbitmap("SuperFly.ico")

    # Crear el encabezado
    encabezado = tk.Frame(nueva_ventana, bg="red2")
    encabezado.pack(side="top", fill="x")

    # Título de la aplicación
    titulo = tk.Label(encabezado, text="SuperFly", bg="red2", fg="white", font=("Arial", 24))
    titulo.pack(pady=10)

    # Crear la barra de navegación
    barra_navegacion = tk.Frame(nueva_ventana, bg="red4")
    barra_navegacion.pack(side="top", fill="x")

    # Botón de navegación "Solo ida" "ida y vuelta"
    global btn_tip_viaje 
    btn_tip_viaje= tk.Button(barra_navegacion, text="Solo ida", relief="flat", bg="lightsteelblue", command= boton_tipo_viaje )
    btn_tip_viaje.pack(side="left", padx=10, pady=5)

    # Agregar combobox para seleccionar cantidad de personas

    personas_label = tk.Label(barra_navegacion, text="Personas:", bg="lightsteelblue")
    personas_label.pack(side="right", padx=5, pady=5)
    
    personas_combobox = ttk.Combobox(barra_navegacion, values=[str(i) for i in range(1, 11)], width=3)
    personas_combobox.current(0)  # Set default value to 1
    personas_combobox.pack(side="right", padx=5, pady=5)

    def guardar_personas():
        personas = personas_combobox.get()
        with open('datos_personas.txt', 'a') as file:
            file.write(f"{personas}\n")
        


    # Crear el marco para el formulario de búsqueda
    marco_busqueda = tk.Frame(nueva_ventana, bg='white', bd=2, relief=tk.GROOVE)
    marco_busqueda.pack(pady=20, padx=20, fill='x')

    # Variables de control
    origen_var = tk.StringVar()
    destino_var = tk.StringVar()

    # Funciones de devolución de llamada para actualizar las selecciones
    def actualizar_origen(*args):
        origen_seleccionado = origen_var.get()
        actualizar_fechas()

    def actualizar_destino(*args):
        destino_seleccionado = destino_var.get()
        actualizar_fechas()
    
    # Función para actualizar las fechas disponibles
    def actualizar_fechas():
        origen_seleccionado = origen_var.get()
        destino_seleccionado = destino_var.get()
        fechas_disponibles = []
        for i in range(len(matriz)):
            if ciudad_origen[i] == origen_seleccionado and ciudad_destino[i] == destino_seleccionado:
                fechas_disponibles.append(fecha[i])
        # Actualizar el selector de fecha con las nuevas fechas disponibles
        entrada_fecha['values'] = list(set(fechas_disponibles))

    # Establecer las funciones de devolución de llamada
    origen_var.trace_add("write", actualizar_origen)
    destino_var.trace_add("write", actualizar_destino)

    # Campos de entrada para Origen y Destino
    lbl_origen = tk.Label(marco_busqueda, text="Origen:", bg='white')
    lbl_origen.grid(row=0, column=0, padx=10, pady=5)
    entrada_origen = ttk.Combobox(marco_busqueda, values=list(set(ciudad_origen)), textvariable=origen_var)
    entrada_origen.grid(row=0, column=1, padx=10, pady=5)

    lbl_destino = tk.Label(marco_busqueda, text="Destino:", bg='white')
    lbl_destino.grid(row=0, column=2, padx=10, pady=5)
    entrada_destino = ttk.Combobox(marco_busqueda, values=list(set(ciudad_destino)), textvariable=destino_var)
    entrada_destino.grid(row=0, column=3, padx=10, pady=5)

    # Selector de fecha

    lbl_fecha = tk.Label(marco_busqueda, text="Ida:", bg='white')
    lbl_fecha.grid(row=0, column=4, padx=10, pady=5)
    entrada_fecha = ttk.Combobox(marco_busqueda)
    entrada_fecha.grid(row=0, column=5, padx=10, pady=5)

    # Botón de búsqueda
    btn_buscar = tk.Button(marco_busqueda, text="Buscar", bg="red3", fg="white", command= lambda : (guardar_personas(), mostrar_vuelos()))
    btn_buscar.grid(row=1, columnspan=6, pady=20)

# Función para guardar los datos ingresados por el usuario

def guardar_datos():
    global codigo, apellido
    codigo = codigo_entry.get()
    apellido = apellido_entry.get()
    usuario_base_datos()

# Si el usuario no esta en la base de datos, se le pedirá que se registre

def usuario_base_datos():
    usuario_registrado =[]
    with open('datos_checkin.txt', 'r') as file:
        for line in file:
            usuario_registrado.append(line.strip().split(','),)
    if [codigo, apellido] in usuario_registrado:
                showinfo(title="Bienvenido Usuario", message="Nos alegra verte de nuevo en SuperFly")
                abrir_nueva_ventana()
    else:
        showinfo(title="Usuario no encontrado", message="El usuario no se encuentra en la base de datos, por favor regístrese")
        nueva_ventana_registro()
        
# Crear el botón para realizar el check-in

checkin_button = tk.Button(marco, text="Realizar Check-in", bg="red3", fg="black", command=guardar_datos)
checkin_button.grid(row=3, columnspan=2, pady=10)

# Funcion para mostrar la hora de los vuelos filtrados

def vuelos_a_mostrar():
    global hora_s, hora_l, valor_mi, valor_me, valor_ma, origen_seleccionado, destino_seleccionado, codigo
    origen_seleccionado = origen_var.get()
    destino_seleccionado = destino_var.get() 
    hora_s = []
    hora_l = []
    valor_mi = []
    valor_me = []
    valor_ma = []
    codigo = []

    for i in range(len(matriz)):
        if ciudad_origen[i] == origen_seleccionado and ciudad_destino[i] == destino_seleccionado and fecha[i] == entrada_fecha.get():
            hora_s.append(hora_salida[i])
            hora_l.append(hora_llegada[i])
            valor_mi.append(valor_min[i])
            valor_me.append(valor_medio[i])
            valor_ma.append(valor_max[i])
            codigo.append(vuelo[i])

# Función para guardar los datos de registro

def guardar_datos_registro():
    nombre_us = entrada_primer_nombre.get()
    apellido_us = entrada_primer_apellido.get()
    genero_us = entrada_genero.get()
    nacionalidad_us = entrada_nacionalidad.get()
    numero_documento_us = entrada_numero_documento.get()
    fecha_nacimiento_us = entrada_fecha_nacimiento.get()
    asistencia_us = entrada_asistencia.get()
    correo_us = entrada_correo.get()
    numero_celular_us = entrada_numero_celular.get()
    ventana_codigo_checkin()
    if len(nombre_us and apellido_us and genero_us and nacionalidad_us and numero_documento_us and fecha_nacimiento_us and asistencia_us and correo_us and numero_celular_us) != 0:
        with open('datos_registro.txt', 'a') as file:
            file.write(f"{nombre_us},{apellido_us},{genero_us},{nacionalidad_us},{numero_documento_us},{fecha_nacimiento_us},{asistencia_us},{correo_us},{numero_celular_us}\n")
        abrir_nueva_ventana()    
    else:
        showwarning(title="Error", message="Por favor llene todos los campos")

# Función para mostrar los vuelos

def mostrar_vuelos():
    nueva_ventana.withdraw()
    global ventana_vuelos
    # Crear la nueva ventana
    ventana_vuelos = tk.Toplevel(root)
    ventana_vuelos.title("SuperFly - Vuelos Disponibles")
    ventana_vuelos.geometry("1000x600")
    ventana_vuelos.iconbitmap("SuperFly.ico")

    # Crear el encabezado
    encabezado = tk.Frame(ventana_vuelos, bg="red2")
    encabezado.pack(side="top", fill="x")

    # Título de la aplicación
    titulo = tk.Label(encabezado, text="Superfly", bg="red2", fg="white", font=("Arial", 24))
    titulo.pack(pady=10)

    # Crear la barra de navegación
    barra_navegacion = tk.Frame(ventana_vuelos, bg="red3")
    barra_navegacion.pack(side="top", fill="x")

    # Agregar combobox para filtrar los vuelos por mejor precio o directo
    filtro_combobox = ttk.Combobox(barra_navegacion, values=["Mejor Precio", "Directo"], width=12)
    filtro_combobox.current(0)  
    filtro_combobox.pack(side="left", padx=10, pady=5)

    # Crear el marco para los vuelos
    marco_vuelos = tk.Frame(ventana_vuelos)
    marco_vuelos.pack(pady=20)

    vuelos = vuelos_a_mostrar()
    
    # Crear un vuelo
    for i in range(len(hora_s)):
        vuelo_frame = tk.Frame(marco_vuelos, relief=tk.SOLID, bd=2, bg="ghost white")
        vuelo_frame.pack(fill="x", pady=10)

        # Convertir las horas a objetos datetime
        hora_salida = datetime.strptime(hora_s[i], "%H:%M:%S")
        hora_llegada = datetime.strptime(hora_l[i], "%H:%M:%S")

        # Calcular la duración del vuelo
        duracion = hora_llegada - hora_salida
        minutos = duracion.seconds // 60  # Convertir la duración a minutos

        # Convertir los minutos a horas y minutos
        horas = minutos // 60
        minutos = minutos % 60

        # Título del vuelo
        if horas > 0:
            vuelo_title = tk.Label(vuelo_frame, text=f"{i+1} - Hora De Salida {hora_s[i]} - Hora De Llegada {hora_l[i]} - Duración: {horas} horas {minutos} minutos", font=("Helvetica", 12), bg="red2", fg="white")
        else:
            vuelo_title = tk.Label(vuelo_frame, text=f"{i+1} - Hora De Salida {hora_s[i]} - Hora De Llegada {hora_l[i]} - Duración: {minutos} minutos", font=("Helvetica", 12), bg="red2", fg="white")
        vuelo_title.pack(side="left", padx=10)

        # Precio del vuelo
        vuelo_price = tk.Label(vuelo_frame, text=f"Desde COP {valor_mi[i]} hasta COP {valor_ma[i]}", font=("Arial", 12), bg="#fff", fg="#228B22")
        vuelo_price.pack(fill="x", pady=10)

        # Botón de selección
        btn_seleccionar = tk.Button(vuelo_frame, text="Seleccionar", bg="red3", fg="white", command=abrir_ventana_seleccion_paquete)
        btn_seleccionar.pack(side="right", padx=10)

# Funcion Guardar Paquete De Vuelo Aluminio

def guardar_paquete_aluminio():
    paquete_text.insert(tk.END, "Aluminio")

# Funcion Guardar Paquete De Vuelo Diamante

def guardar_paquete_diamante():
    paquete_text.insert(tk.END, "Diamante")

# Funcion Guardar Paquete De Vuelo Premium

def guardar_paquete_premium():
    paquete_text.insert(tk.END, "Premium")

# Funcion Elegir Asiento Para Aluminio Y Mandarlo A Datos_Asientos

def elegir_asiento_aluminio():
    num_columnas = 6
    for i in range(9, 12):
        sillas_aluminio = []
        for e in range(num_columnas):
            filas_asiento = ["A", "B", "C", "D", "E", "F"]
            posicion = [i+1, filas_asiento[e]]
            sillas_aluminio.append(posicion)

    # Elegir una Silla Al Azar
    silla_elegida = random.choice(sillas_aluminio)

    with open('datos_asientos.txt', 'a') as file:
        file.write(f"{silla_elegida}\n")

    return silla_elegida
    
# Funcion Elegir Asiento Para Diamante Y Mandarlo A Datos_Asientos

def elegir_asiento_diamante():
    num_columnas = 6
    sillas_diamante = []
    for i in range(5,8):
        for e in range(num_columnas):
            filas_asiento = ["A", "B", "C", "D", "E", "F"]
            posicion = [i+1, filas_asiento[e]]
            sillas_diamante.append(posicion)

    # Elegir una silla al azar
    silla_elegida = random.choice(sillas_diamante)

    with open('datos_asientos.txt', 'a') as file:
        file.write(f"{silla_elegida}\n")

    return silla_elegida

valor_paquete = int

# Funcion para calcular el precio total a pagar con el vuelo seleccionado y el número de personas

def calcular_total_pagar():
    total_pagar = valor_paquete * int(leer_datos_personas())
    return total_pagar

# Funcion Actualizar El Precio Para El Paquete De Vuelo Aluminio

def actualizar_precio_aluminio():
    global valor_paquete
    valor_paquete = valor_mi[0]
    return valor_paquete

# Funcio Actualizar El Precio Para El Paquete De Vuelo Diamante

def actualizar_precio_diamante():
    global valor_paquete
    valor_paquete = valor_me[0]
    return valor_paquete

# Funcion Actualizar El Precio Para El Paquete De Vuelo Premium

def actualizar_precio_premium():
    global valor_paquete
    valor_paquete = valor_ma[0]
    return valor_paquete

# crea una nueva ventana que le permita al usuario ver que vuelo escogio y que paquete

def nueva_ventana_compra():
    ventana_seleccion_asientos.withdraw()
    global paquete_text, texto_vuelo, ventana_compra, origen, destino
    origen = origen_seleccionado
    destino = destino_seleccionado
    texto_vuelo = f"{origen_seleccionado} - {destino_seleccionado}"
    ventana_compra = tk.Toplevel(root)
    ventana_compra.title("SuperFly - Registro De Compra")
    ventana_compra.geometry("800x600")
    ventana_compra.iconbitmap("SuperFly.ico")

    # Crear el encabezado
    encabezado = tk.Frame(ventana_compra, bg="red2")
    encabezado.pack(side="top", fill="x")

    # Título de la ventana
    titulo = tk.Label(encabezado, text="Resumen de Compra", bg="red2", fg="white", font=("Arial", 24))
    titulo.pack(pady=10)

    # Mostrar el vuelo seleccionado
    vuelo_label = tk.Label(ventana_compra, text="Vuelo seleccionado:", font=("Arial", 18))
    vuelo_label.pack(pady=10)

    vuelo_text = tk.Text(ventana_compra, height=5, width=50)
    vuelo_text.insert(tk.END, texto_vuelo)
    vuelo_text.pack()

    # Mostrar el paquete seleccionado
    paquete_label = tk.Label(ventana_compra, text="Paquete seleccionado:", font=("Arial", 18))
    paquete_label.pack(pady=10)

    paquete_text = tk.Text(ventana_compra, height=5, width=50)
    paquete_text.pack()

    # Botón para continuar con el pago
    btn_continuar_pago = tk.Button(ventana_compra, text="Continuar con el Pago", bg="red3", fg="white", command=nueva_ventana_tarjeta)
    btn_continuar_pago.pack(pady=20)

# Funcion Elegir Paquete De Vuelo

def abrir_ventana_seleccion_paquete():
    ventana_vuelos.withdraw()
    global ventana_seleccion_asientos
    ventana_seleccion_asientos = tk.Toplevel(root)
    ventana_seleccion_asientos.title("SuperFly - Seleccionar Paquete De Vuelo")
    ventana_seleccion_asientos.geometry("800x700")
    ventana_seleccion_asientos.iconbitmap("SuperFly.ico")

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
    btn_seleccionar_aluminio = tk.Button(frame_aluminio, text="Seleccionar", bg="red3", fg="white", command= lambda : (nueva_ventana_compra(), guardar_paquete_aluminio(), elegir_asiento_aluminio(), actualizar_precio_aluminio()))
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
    btn_seleccionar_diamante = tk.Button(frame_diamante, text="Seleccionar", bg="red3", fg="white", command= lambda : (nueva_ventana_compra(), guardar_paquete_diamante(), elegir_asiento_diamante(), actualizar_precio_diamante()))
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
    btn_seleccionar_premium = tk.Button(frame_premium, text="Seleccionar", bg="red3", fg="white", command= lambda : (abrir_ventana_seleccion_asientos()))
    btn_seleccionar_premium.pack(pady=10)

# Funcion para abrir ventana de registro

def nueva_ventana_registro():
    global nueva_ventana_r, entrada_primer_nombre, entrada_primer_apellido, entrada_genero, entrada_nacionalidad, entrada_numero_documento, entrada_fecha_nacimiento, entrada_asistencia, entrada_correo, entrada_numero_celular
    marco_registro = tk.Frame(root)  
    marco_registro.pack()
    nueva_ventana_r = tk.Toplevel(root)
    nueva_ventana_r.title("Superfly - Registro de Usuario")
    nueva_ventana_r.geometry("800x600")
    nueva_ventana_r.iconbitmap("SuperFly.ico")
    
    # Crear el encabezado
    encabezado = tk.Frame(nueva_ventana_r, bg="red2")
    encabezado.pack(side="top", fill="x")

    # Título de la aplicación
    titulo = tk.Label(encabezado, text="SuperFly - Registro De Usuario", bg="red2", fg="white", font=("Arial", 24))
    titulo.pack(pady=10)

    # Crear el marco para el formulario de registro
    marco_registro = tk.Frame(nueva_ventana_r, bg="ghost white", bd=2, relief=tk.GROOVE)
    marco_registro.pack(pady=20, padx=20, fill='x')
    
    # Actualizar la ventana para que cada dato que se debe pedir sean botones y que al presionarlos sea una entrada para poder ingresar el dato
    # Primer nombre
    lbl_primer_nombre = tk.Label(marco_registro, text="Primer Nombre:", bg="ghost white")
    lbl_primer_nombre.grid(row=0, column=0, padx=10, pady=5)
    entrada_primer_nombre = tk.Entry(marco_registro)
    entrada_primer_nombre.grid(row=0, column=1, padx=10, pady=5)

    # Primer apellido
    lbl_primer_apellido = tk.Label(marco_registro, text="Primer Apellido:", bg="ghost white")
    lbl_primer_apellido.grid(row=0, column=2, padx=10, pady=5)
    entrada_primer_apellido = tk.Entry(marco_registro)
    entrada_primer_apellido.grid(row=0, column=3, padx=10, pady=5)

    # Género
    lbl_genero = tk.Label(marco_registro, text="Género:", bg="ghost white")
    lbl_genero.grid(row=1, column=0, padx=10, pady=5)
    opciones_genero = ["Femenino", "Masculino", "No Binario", "Otro"]
    entrada_genero = ttk.Combobox(marco_registro, values=opciones_genero)
    entrada_genero.grid(row=1, column=1, padx=10, pady=5)

    # Nacionalidad
    lbl_nacionalidad = tk.Label(marco_registro, text="Nacionalidad:", bg="ghost white")
    lbl_nacionalidad.grid(row=1, column=2, padx=10, pady=5)
    entrada_nacionalidad = tk.Entry(marco_registro)
    entrada_nacionalidad.grid(row=1, column=3, padx=10, pady=5)

    # Número de documento
    lbl_numero_documento = tk.Label(marco_registro, text="Número de Documento:", bg="ghost white")
    lbl_numero_documento.grid(row=2, column=0, padx=10, pady=5)
    entrada_numero_documento = tk.Entry(marco_registro)
    entrada_numero_documento.grid(row=2, column=1, padx=10, pady=5)

    # Fecha de Nacimiento
    lbl_fecha_nacimiento = tk.Label(marco_registro, text="Fecha de Nacimiento (DD/MM/AAAA):", bg="ghost white")
    lbl_fecha_nacimiento.grid(row=2, column=2, padx=10, pady=5)
    entrada_fecha_nacimiento = tk.Entry(marco_registro)
    entrada_fecha_nacimiento.grid(row=2, column=3, padx=10, pady=5)

    # Asistencia durante el vuelo
    lbl_asistencia = tk.Label(marco_registro, text="Necesita Asistencia durante el vuelo:", bg="ghost white")
    lbl_asistencia.grid(row=3, column=0, padx=10, pady=5)
    opciones_asistencia = ["Si", "No"]
    entrada_asistencia = ttk.Combobox(marco_registro, values=opciones_asistencia)
    entrada_asistencia.grid(row=3, column=1, padx=10, pady=5)

    # Correo electrónico
    lbl_correo = tk.Label(marco_registro, text="Correo Electrónico:", bg="ghost white")
    lbl_correo.grid(row=3, column=2, padx=10, pady=5)
    entrada_correo = tk.Entry(marco_registro)
    entrada_correo.grid(row=3, column=3, padx=10, pady=5)

    # Funcion que valida el correo ingresado si es correcto deja acceder a guardar_datos_registro

    def validar():
        telefono = entrada_numero_celular.get()
        if telefono.isdigit() and len(telefono) == 10:
            showwarning(title="Número Válido", message="Número válido")
            guardar_datos_registro()
            if re.match(r"[^@]+@[^@]+\.[^@]+", correo):
                showwarning(title="Correo Válido", message="Correo válido")
                guardar_datos_registro()
            else:
                showwarning(title="Correo Inválido", message="Correo inválido")
        else:
            showwarning(title="Número Inválido", message="Número inválido")
        correo = entrada_correo.get()

    # Número Celular
    lbl_numero_celular = tk.Label(marco_registro, text="Número Celular:", bg="ghost white")
    lbl_numero_celular.grid(row=4, column=0, padx=10, pady=5)
    entrada_numero_celular = tk.Entry(marco_registro)
    entrada_numero_celular.grid(row=4, column=1, padx=10, pady=5)

    # Botón de registro
    continuar_button = tk.Button(marco_registro, text="Continuar", bg='red2', fg='black', command= lambda : (validar()))
    continuar_button.grid(row=5, columnspan=4, pady=10)

# Funcion Para leer La Datos Personas Y Elegir La Ultima Posicion En Lista

def leer_datos_personas():
    with open('datos_personas.txt', 'r') as file:
        datos_personas = [line.strip() for line in file]
    return datos_personas[-1]

# Funcion para abrir ventana de tarjeta y pago

def nueva_ventana_tarjeta():
    ventana_compra.withdraw()
    global nueva_ventana_t
    marco_tarjeta = tk.Frame(root)  
    marco_tarjeta.pack()
    nueva_ventana_t = tk.Toplevel(root)
    nueva_ventana_t.title("SuperFly - Pago Con Tarjeta")
    nueva_ventana_t.geometry("800x600")
    nueva_ventana_t.iconbitmap("SuperFly.ico")

    # Crear el encabezado
    encabezado = tk.Frame(nueva_ventana_t, bg="red2")
    encabezado.pack(side="top", fill="x")

    # Título de la aplicación
    titulo = tk.Label(encabezado, text="Superfly", bg="red2", fg="white", font=("Arial", 24))
    titulo.pack(pady=10)

    # Título del marco
    titulo_tarjeta = tk.Label(nueva_ventana_t, text="Datos de la Tarjeta", font=("Arial", 24))
    titulo_tarjeta.pack(pady=10)


    # Crear el marco para el formulario de registro
    marco_tarjeta = tk.Frame(nueva_ventana_t, bg='ghost white', bd=2, relief=tk.GROOVE)
    marco_tarjeta.pack(pady=20, padx=20, fill='x')
    
    # Tipo de tarjeta
    lbl_tipo_tarjeta = tk.Label(marco_tarjeta, text="Tipo de Tarjeta:", bg="ghost white")
    lbl_tipo_tarjeta.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    opciones_tarjeta = ["Débito", "Crédito"]
    entrada_tipo_tarjeta = ttk.Combobox(marco_tarjeta, values=opciones_tarjeta)
    entrada_tipo_tarjeta.grid(row=0, column=1, padx=10, pady=5)

    # Nombre del titular
    lbl_nombre_titular = tk.Label(marco_tarjeta, text="Nombre del Titular:", bg="ghost white")
    lbl_nombre_titular.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entrada_nombre_titular = tk.Entry(marco_tarjeta)
    entrada_nombre_titular.grid(row=1, column=1, padx=10, pady=5)

    # Número de tarjeta
    lbl_numero_tarjeta = tk.Label(marco_tarjeta, text="Número de Tarjeta:", bg='ghost white')
    lbl_numero_tarjeta.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entrada_numero_tarjeta = tk.Entry(marco_tarjeta)
    entrada_numero_tarjeta.grid(row=2, column=1, padx=10, pady=5)

    # Fecha de expiración
    lbl_fecha_expiracion = tk.Label(marco_tarjeta, text="Fecha de Expiración:", bg='ghost white')
    lbl_fecha_expiracion.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    opciones_mes = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    entrada_mes = ttk.Combobox(marco_tarjeta, values=opciones_mes)
    entrada_mes.grid(row=3, column=1, padx=10, pady=5)

    opciones_anio = ["2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032"]
    entrada_anio = ttk.Combobox(marco_tarjeta, values=opciones_anio)
    entrada_anio.grid(row=3, column=2, padx=10, pady=5)

    # CVV
    lbl_cvv = tk.Label(marco_tarjeta, text="CVV:", bg='ghost white')
    lbl_cvv.grid(row=4, column=0, padx=10, pady=5, sticky="w")

    entrada_cvv = tk.Entry(marco_tarjeta)
    entrada_cvv.grid(row=4, column=1, padx=10, pady=5)


    # Botón de continuar
    continuar_button = tk.Button(marco_tarjeta, text="Continuar", bg='red2', fg='black', command= lambda :  ventana_resumen_compra(texto_vuelo, leer_datos_personas, calcular_total_pagar))
    continuar_button.grid(row=5, columnspan=3, pady=10)

# Crear una ventana de resumen de compra que contiene el vuelo seleccionado por el usuario en la ventana de "mostrar_vuelos", el número de personas y el valor total a pagar

def ventana_resumen_compra(texto_vuelo, leer_datos_personas, calcular_total_pagar):
    nueva_ventana_t.withdraw()
    # Crear la ventana de resumen de compra
    global ventana_resumen
    ventana_resumen = tk.Toplevel(root)
    ventana_resumen.title("SuperFly - Resumen de Compra")
    ventana_resumen.geometry("500x400")
    ventana_resumen.iconbitmap("SuperFly.ico")

    # Crear el marco para los componentes
    marco_resumen = tk.Frame(ventana_resumen, bg='white')
    marco_resumen.pack(pady=30)

    # Mostrar el vuelo seleccionado
    vuelo_label = tk.Label(marco_resumen, text="Vuelo seleccionado:", bg='white')
    vuelo_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

    vuelo_entry = tk.Entry(marco_resumen)
    vuelo_entry.insert(0, texto_vuelo)
    vuelo_entry.configure(state='readonly')
    vuelo_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    # Mostrar el número de personas
    personas_label = tk.Label(marco_resumen, text="Número de personas:", bg='white')
    personas_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

    personas_entry = tk.Entry(marco_resumen)
    personas_entry.insert(0, leer_datos_personas())
    personas_entry.configure(state='readonly')
    personas_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    # Mostrar el total a pagar
    total_label = tk.Label(marco_resumen, text="Total a pagar:", bg='white')
    total_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

    total_entry = tk.Entry(marco_resumen, font=("Arial", 16, "bold"))
    total_entry.insert(0, calcular_total_pagar())
    total_entry.configure(state='readonly')
    total_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    # Botón de pagar
    pagar_button = tk.Button(marco_resumen, text="Pagar", bg='red3', fg='black', command= lambda : (crear_ventana_tiquete()))
    pagar_button.grid(row=3, columnspan=2, pady=10)

# Funcion abrir datos_registro y volverlo una matriz para tomar la primera posición en columna y la ultima posicion en fila

def abrir_datos_registro():
    with open('datos_registro.txt', 'r') as file:
        datos_registro = [line.strip().split(",") for line in file]
    return datos_registro

# Funcion tomar la primera posicion de la columna ultima posicion en la fila

def nombre_registro():
    datos_registro = abrir_datos_registro()
    return datos_registro[-1][0]

# Funcion tomar la segunda posicion de la columna ultima posicion en la fila

def apellido_registro():
    datos_registro = abrir_datos_registro()
    return datos_registro[-1][1]

# Combinar estos dos datos en una sola variable

def nombre_completo():
    nombre = nombre_registro()
    apellido = apellido_registro()
    return f"{nombre} {apellido}"


# Funcion para crear la ventana del tiquete

def crear_ventana_tiquete():
    generar_codigo_checkin()
    ventana_resumen.withdraw()
    nombre = nombre_completo()
    ventana_tiquete = tk.Toplevel(root)
    ventana_tiquete.title("SuperFly - Tiquete")
    ventana_tiquete.geometry("1000x600")
    ventana_tiquete.iconbitmap("SuperFly.ico") 
    # Create a frame for the airline logo
    logo_frame = tk.Frame(ventana_tiquete, bg="red")
    logo_frame.pack(side="left", fill="y")

    # Create the airline logo label
    logo_label = tk.Label(logo_frame, text="SuperFly", font=("Arial", 24, "bold"), fg="white", bg="red")
    logo_label.pack(pady=10)

    # Create a frame for the boarding pass details
    boarding_pass_frame = tk.Frame(ventana_tiquete, bg="white")
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
    passenger_name_entry.insert(0, nombre)
    passenger_name_entry.grid(row=0, column=1, sticky="w")

    # Create frames for the flight details
    flight_details_frame = tk.Frame(boarding_pass_frame, bg="white")
    flight_details_frame.pack(pady=10)

    # Create labels and entries for origin, destination, flight number, date, and time
    origin_label = tk.Label(flight_details_frame, text="Origen", font=("Arial", 12))
    origin_label.grid(row=0, column=0, sticky="w")

    origin_entry = tk.Entry(flight_details_frame, font=("Arial", 12))
    origin_entry.insert(0, origen)
    origin_entry.grid(row=0, column=1, sticky="w")

    destination_label = tk.Label(flight_details_frame, text="Destino", font=("Arial", 12))
    destination_label.grid(row=1, column=0, sticky="w")

    destination_entry = tk.Entry(flight_details_frame, font=("Arial", 12))
    destination_entry.insert(0, destino)
    destination_entry.grid(row=1, column=1, sticky="w")

    flight_number_label = tk.Label(flight_details_frame, text="Vuelo", font=("Arial", 12))
    flight_number_label.grid(row=0, column=2, sticky="w")

    flight_number_entry = tk.Entry(flight_details_frame, font=("Arial", 12))
    flight_number_entry.insert(0, codigo[0])
    flight_number_entry.grid(row=0, column=3, sticky="w")

    date_label = tk.Label(flight_details_frame, text="Fecha", font=("Arial", 12))
    date_label.grid(row=1, column=2, sticky="w")

    date_entry = tk.Entry(flight_details_frame, font=("Arial", 12))
    date_entry.insert(0, entrada_fecha.get())
    date_entry.grid(row=1, column=3, sticky="w")

    time_label = tk.Label(flight_details_frame, text="Hora", font=("Arial", 12))
    time_label.grid(row=2, column=2, sticky="w")

    time_entry = tk.Entry(flight_details_frame, font=("Arial", 12))
    time_entry.insert(0, hora_s[0])
    time_entry.grid(row=2, column=3, sticky="w")

# Funcion para generar el codigo de check-ing y guardarlo en un archivo datos_checkin.txt el deberá ser un código único, generado automáticamente. La letra inicial del nombre del usuario y contará con 6 dígitos alfanuméricos.

def generar_codigo_checkin():
    nombre = nombre_registro()
    codigo = nombre[0] + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    with open('datos_checkin.txt', 'a') as file:
        file.write(f"{nombre},{codigo}\n")
    return codigo

# Funcion para crear una ventana emergente

def ventana_codigo_checkin():
    # Crear una nueva ventana emergente
    ventana_codigo = tk.Toplevel(root)
    ventana_codigo.title("Código de Check-in")
    ventana_codigo.geometry("300x200")

    # Obtener el código de check-in generado
    codigo_checkin = generar_codigo_checkin()

    # Crear una etiqueta para mostrar el código de check-in
    codigo_label = tk.Label(ventana_codigo, text=f"Código de Check-in: {codigo_checkin}", font=("Arial", 12))
    codigo_label.pack(pady=20)

    # Crear un botón para cerrar la ventana emergente
    cerrar_button = tk.Button(ventana_codigo, text="Cerrar", command=ventana_codigo.destroy)
    cerrar_button.pack()

# Iniciar el bucle principal de la aplicación
if __name__ == "__main__":
 root.mainloop()
