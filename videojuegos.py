#Trabajo práctico.

videojuegos = []
plataformas = []

while True:
    print("\n--- MENÚ DE VIEOJUEGOS ---")
    print("1. Registrar videojuego")
    print("2. Ver videojuegos")
    print("3.-Modificar videojuego")
    print("4. Eliminar videojuego")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")
    try:
        if opcion == "1":
            codigo = int(input("Ingrese el código del videojuego: "))
            try:
                while True:
                    if codigo>0:
                        break
                    else:
                        print("Error! debe ingresar un número positivos!")
            except ValueError:
                print("Error! no debe ingresar letras!! solo números!!")
            nombre = input("Ingrese el nombre del videojuego: ").strip().lower()
            genero = input("Ingrese el genero del videojuego: ").strip().lower()

            print("\nPlataformas disponibles")
            print("1. PC")
            print("2. PS5")
            print("3. Xbox Series X")
            print("4. Nintendo Switch")

            plataforma_codigo = int(input("Seleccione el número de la plataforma: "))
            try:
                while True:
                    if plataforma_codigo>0:
                        break
                else:
                    print("Error! debe ingresar un número mayor a 0!")
            except ValueError:
                print("Error!! debe ingresar solo números!!!")
            plataforma = plataformas[plataforma_codigo - 1]

            videojuego = {
                "codigo": codigo,
                "nombre": nombre,
                "genero": genero,
                "plataforma": plataforma
            }
            
            videojuegos.append(videojuego)
            print("Videojuego registrado correctamente.")

        elif opcion == "2":
            if len(videojuegos)==0:
                print("No hay videojuegos registrados.")
            else:
                print("\n--- LISTA DE VIDEOJUEGOS ---")
                for v in videojuegos:
                    for juego in v:
                        print(juego, "=>", v[juego])
                    #print(f"Códido: {v['codigo']}, Nombre: {v['nombre']}, Género: {v['genero']}, Plataforma{v['plataforma']}")
        elif opcion == "3":
            codigo = int(input("Ingrese el código del videojuego a modificar: "))
            try:
                while True:
                    if codigo>0:
                        break
                    else:
                        print("Error! debe ingresar un número positivo!")
            except ValueError:
                print("Error! debe ingresar solo números!")
            encontrado = False
            for v in videojuegos:
                if v['codigo'] == codigo:
                    v['nombre'] == input("Nuevo nombre: ").strip().lower()
                    v['genero'] == input("Nuevo género: ").strip().lower()

                    print("\nPlataformas disponibles:")
                    print("1. PC")
                    print("2. PS5")
                    print("3. Xbox Series X")
                    print("4. Nintendo Switch")

                    plataforma_codigo = int(input("Seleccione el número de la nueva plataforma: "))
                    v["plataforma"] = plataformas[plataforma_codigo - 1]

                    print("Videojuego modificado correctamente.")
                    encontrado = True
                    break
                if not encontrado:
                    print("Videojuego no encontrado.")

        elif opcion == "4":
            codigo = int(input("Ingrese el código del videojuego a eliminar: "))
            try:
                while True:
                    if codigo>0:
                        break
                    else:
                        print("Error! debe ingresar un número positivo!")
            except ValueError:
                print("Error! debe ser solo números.")
            eliminado = False
            for v in videojuegos:
                if v['codigo'] == codigo:
                    videojuegos.remove(v)
                    print("Videojuego eliminado correctamente.")
                    eliminado = True
            if not eliminado:
                print("Videojuego no encontrado.")

        elif opcion =="5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")
    except ValueError:
        print("Error! debe ingresar solo números del 1 al 4!!!")