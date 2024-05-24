# Integrante1: PrimerNombre SegundoApellido – código1
# Integrante2: PrimerNombre SegundoApellido – código2
# Integrante2: PrimerNombre SegundoApellido – código3
# Docente: Luis Germán Toro Pareja
# Número de grupo:
# Proyecto Final

import customtkinter as ctk
from tkinter import PhotoImage

root = ctk.CTk()
logo = PhotoImage(file="SuperFly.png")

root.title("Super Fly")
root.geometry("500x600+350+200")
root.resizable(0, 0)
root.iconbitmap("SuperFly.ico")

root.mainloop()

