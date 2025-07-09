from usuario_db import UsuarioDB
from auth import Auth

class App:
    def __init__(self):
        self.db = UsuarioDB()
        self.auth = Auth(self.db)

    def menu(self):
        while True:
            print("\n1. Registrar Usuario \n2. Iniciar sesion \n3. Salir")
            opcion = input("Selecciona una opcion: ")
            if opcion == '1':
                u = input("Nombre de usuario: ")
                p = input("Contraseña: ")
                self.auth.registrar(u, p)
            elif opcion == '2':
                u = input("Nombre de usuario: ")
                p = input("Contraseña: ")
                self.auth.login(u, p)
            elif opcion == '3':
                self.db.cerrar()
                print("Hasta luego!")
                break
            else:
                print("Opcion invalida, utilice otra")

