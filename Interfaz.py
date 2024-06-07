# Integrante1: Brayan Urquijo – 202459407
# Integrante2: Jhorain Jaramillo – código2
# Integrante2: PrimerNombre SegundoApellido – código3
# Docente: Luis Germán Toro Pareja
# Número de grupo:

# Proyecto Final
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import io 

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

