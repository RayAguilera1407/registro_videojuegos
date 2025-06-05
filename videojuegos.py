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

    if opcion == "1":
        codigo = int(input("Ingrese el código del videojuego: "))
        nombre = input("Ingrese el nombre del videojuego: ")
        genero = input("Ingrese el genero del videojuego: ")

        print("\nPlataformas disponibles")
        print("1. PC")
        print("2. PS5")
        print("3. Xbox Series X")
        print("4. Nintendo Switch")

        plataforma_codigo = int(input("Seleccione el número de la plataforma: "))
        plataforma = plataformas[plataforma_codigo - 1]

        videojuego = {
            "codigo": codigo,
            "nombre": nombre,
            "genero": genero,
            "plataforma": plataforma
        }
        
        videojuegos.append(videojuegos)
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
        pass
    elif opcion == "4":
        pass
    elif opcion =="5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida.")
