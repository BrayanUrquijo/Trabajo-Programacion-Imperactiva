import tabulate as Tb


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

# for para encontrar en una linea de la matriz la ciudad de origen y destino seleccionada por el usuario y mandar la fecha

ciudad_origen_seleccionada = "Cali"
ciudad_destino_seleccionada = "Bogota"

for i in range(len(matriz)):
    if ciudad_origen[i] == ciudad_origen_seleccionada and ciudad_destino[i] == ciudad_destino_seleccionada:
        print("--------------------------")
        print(f"Vuelo: {vuelo[i]}")
        print(f"Fecha: {fecha[i]}")
        print(f"Hora de Salida: {hora_salida[i]}")
        print(f"Hora de Llegada: {hora_llegada[i]}")
        print(f"Valor Minimo: {valor_min[i]}")
        print(f"Valor Medio: {valor_medio[i]}")
        print(f"Valor Maximo: {valor_max[i]}")
        print(f"Ciudad Origen: {ciudad_origen[i]}")
        print(f"Ciudad Destino: {ciudad_destino[i]}")


# print("--------------------------")
# print(Tb.tabulate(vuelo))
# print("--------------------------")
# print(Tb.tabulate(fecha))
# print("--------------------------")
# print(Tb.tabulate(hora_salida))
# print("--------------------------")
# print(Tb.tabulate(hora_llegada))
# print("--------------------------")
# print(Tb.tabulate(valor_min))
# print("--------------------------")
# print(Tb.tabulate(valor_medio))
# print("--------------------------")
# print(Tb.tabulate(valor_max))
# print("--------------------------")
# print(Tb.tabulate(ciudad_origen))
# print("--------------------------")
# print(Tb.tabulate(ciudad_destino))
# print("--------------------------")


