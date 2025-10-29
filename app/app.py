import database, utils, datetime

def app():

    db = database.connect()

    while True:
        # menu
        print("------ Users --------")
        print("1: Añadir un usuario")
        print("2: Ver usuarios")
        print("3: Buscar usuario por email")
        print("4: Eliminar usuario por email")
        print("5: Login")
        print("----- Purchases -----")
        print("6: Añadir un compra (embedded)")
        print("7: Añadir un compra (referenced)")
        print("Escribe 'exit' para salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            email = input("Email: ")
            while not utils.validar_email(email):
                email = input("Introduce un email correcto: ")
            password = input("Contraseña: ")
            # validar si el email ya esta registrado en la app
            if database.find_by_email(db, "users", email):
                print("Email ya registrado en la app")
            else:
                # creamos una variable tipo dict(diccionario) igual que un JSON
                data = {
                    "nombre": nombre,
                    "email": email,
                    "password": utils.encriptar(password)
                }
                database.insertUser(db, "users", data)

        if opcion == "2":
            usersObj = database.findUsers(db, "users")
            # if len(dict(usersObj)) == 0:
            #     print("No hay usuarios registrados")
            #     app()
            for user in usersObj: 
                print(user)
        
        if opcion == "3":
            email = input("Email: ")
            user = database.find_by_email(db, "users", email)
            if user:
                print(user)
            else:
                print("Usuario no encontrado")

        if opcion == "4":
            email = input("Email: ")
            if database.delete_by_email(db, "users", email):
                print(f"Usuario con email {email} eliminado correctamente")
            else:
                print(f"Usuario con email {email} no encontrado")

        if opcion == "5":
            email = input("Email: ")
            password = input("Contraseña: ")
            user = dict(database.find_by_email(db, "users", email))
            if user and utils.validar_password(password, user["password"]):
                print("Login OK")
            else:
                print("Datos incorrectos")

        if opcion == "6":
            email = input("Email del usuario: ")
            producto = input("Producto: ")
            cantidad = input("Cantidad: ")
            precio = input("Precio: ")
            data = {
                "producto": producto,
                "cantidad":cantidad,
                "precio": precio,
                "fecha": datetime.datetime.now()
            }
            database.insertPurchaseEmb(db, "users", email, data)

        if opcion == "7":
            email = input("Email del usuario: ")
            user = database.find_by_email(db, "users", email)
            if user:
                producto = input("Producto: ")
                cantidad = input("Cantidad: ")
                precio = input("Precio: ")
                data = {
                    "producto": producto,
                    "cantidad":cantidad,
                    "precio": precio,
                    "fecha": datetime.datetime.now()
                }
                user = dict(user)
                data["user_id"] = user["_id"]
                database.insertPurchaseRef(db, "purchases", data)
            else:
                print("No existe usuario con ese email")

        if opcion == "exit":
            print("Bye")
            exit()
app()