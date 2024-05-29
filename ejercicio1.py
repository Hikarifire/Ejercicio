import os
import msvcrt
import time

usuarios = []

while True:
    print("""
    1. Inicio sesión
    2. Registrar usuario
    3. Eliminar usuario
    4 Salir""")

    opc = int(input("opción elegida: "))

    if opc==1:
        pass
    elif opc==2:
        print("Registrar usuario")
        nombre = input("Nombre: ")
        contrasena = input("Contraseña: ")
        usuario = {
            "Nombre": nombre,
            "Contrasena": contrasena,}
        usuarios.append(usuario)
    elif opc==3:
        print("Eliminar usuario")
    else:
        print("ADIOS!")
        time.sleep(2)
