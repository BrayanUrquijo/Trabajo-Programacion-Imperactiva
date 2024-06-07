# Integrante1: Brayan Urquijo – 202459407
# Integrante2: Jhorain Jaramillo – código2
# Integrante2: PrimerNombre SegundoApellido – código3
# Docente: Luis Germán Toro Pareja
# Número de grupo:

# Proyecto Final
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

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

# print(matriz[0])

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
    ventana_asientos.title("Sky-Voyage")
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
            color = "slateblue" if clase == "Premium" else "mediumpurple" if clase == "Diamante" else "darkslateblue"
            btn = tk.Button(marco_asientos, bg=color, width=2, height=1)
            btn.grid(row=r+1, column=c+1, padx=2, pady=2)

    # Crear las etiquetas para las clases
    lbl_premium = tk.Label(marco_clases, text="Premium", bg="slateblue", width=10)
    lbl_premium.pack(pady=5)

    lbl_diamante = tk.Label(marco_clases, text="Diamante", bg= "mediumpurple", width=10)
    lbl_diamante.pack(pady=5)

    lbl_aluminio = tk.Label(marco_clases, text="Aluminio", bg="darkslateblue", width=10)
    lbl_aluminio.pack(pady=5)

    # Botón de selección
    btn_seleccionar = tk.Button(ventana_asientos, text="Seleccionar", bg="darkviolet", fg="white")
    btn_seleccionar.pack(pady=20)

def boton_tipo_viaje():
    if btn_tip_viaje['text'] == "solo ida":
        btn_tip_viaje.config(text="ida y vuelta")
    else:
        btn_tip_viaje.config(text="solo ida")


def abrir_nueva_ventana():
    # Crear la nueva ventana
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Sky-Voyage")
    nueva_ventana.geometry("800x400")

    # Crear el encabezado
    encabezado = tk.Frame(nueva_ventana, bg="royalblue")
    encabezado.pack(side="top", fill="x")

    # Título de la aplicación
    titulo = tk.Label(encabezado, text="Sky-Voyage", bg="royalblue", fg="white", font=("Arial", 24))
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
    
    personas_combobox = ttk.Combobox(barra_navegacion, values=[str(i) for i in range(1, 11)], width=3)
    personas_combobox.current(0)  # Set default value to 1
    personas_combobox.pack(side="right", padx=5, pady=5)

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
root.title("Sky-Voyage")
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

# Iniciar el bucle principal de la aplicación
if __name__ == "__main__":
 root.mainloop()

