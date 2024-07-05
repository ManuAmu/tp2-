class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}\nTeléfono: {self.telefono}\nEmail: {self.email}\n"


class Agenda:
    def __init__(self):
        self.contactos = []

    def menu(self):
        while True:
            print("\n--- Menú de Opciones ---")
            print("1. Crear contacto")
            print("2. Borrar contacto")
            print("3. Editar contacto")
            print("4. Lista de contactos")
            print("5. Buscar contacto")
            print("6. Cerrar agenda")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_contacto()
            elif opcion == "2":
                self.borrar_contacto()
            elif opcion == "3":
                self.editar_contacto()
            elif opcion == "4":
                self.lista_contactos()
            elif opcion == "5":
                self.buscar_contacto()
            elif opcion == "6":
                print("Cerrando agenda...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def crear_contacto(self):
        print("\n--- Crear contacto ---")
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        contacto_nuevo = Contacto(nombre, telefono, email)
        self.contactos.append(contacto_nuevo)
        print("Contacto creado exitosamente.")

    def borrar_contacto(self):
        print("\n--- Borrar contacto ---")
        nombre = input("Ingrese el nombre del contacto a borrar: ")
        contactos_eliminados = [c for c in self.contactos if c.nombre == nombre]
        if contactos_eliminados:
            for contacto in contactos_eliminados:
                self.contactos.remove(contacto)
            print(f"Contacto(s) con nombre '{nombre}' eliminado(s) correctamente.")
        else:
            print(f"No se encontró ningún contacto con nombre '{nombre}'.")

    def editar_contacto(self):
        print("\n--- Editar contacto ---")
        nombre = input("Ingrese el nombre del contacto a editar: ")
        contacto_encontrado = False
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                nuevo_telefono = input(f"Nuevo teléfono para '{nombre}': ")
                nuevo_email = input(f"Nuevo email para '{nombre}': ")
                contacto.telefono = nuevo_telefono
                contacto.email = nuevo_email
                print("Contacto editado correctamente.")
                contacto_encontrado = True
                break
        if not contacto_encontrado:
            print(f"No se encontró ningún contacto con nombre '{nombre}'.")

    def lista_contactos(self):
        print("\n--- Lista de contactos ---")
        if self.contactos:
            for contacto in self.contactos:
                print(contacto)
        else:
            print("La agenda está vacía.")

    def buscar_contacto(self):
        print("\n--- Buscar contacto ---")
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        contactos_encontrados = [c for c in self.contactos if c.nombre == nombre]
        if contactos_encontrados:
            for contacto in contactos_encontrados:
                print(contacto)
        else:
            print(f"No se encontró ningún contacto con nombre '{nombre}'.")

# Ejemplo de uso:
if __name__ == "__main__":
    mi_agenda = Agenda()
    mi_agenda.menu()
