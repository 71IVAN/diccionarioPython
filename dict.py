x   
#Llenar diccionario y agregarle metodo crud
nbaPlayer = {}

while True:  
    print("## Guarda tus jugadores favoritos de la NBA ##")
    print("Opciones:")
    print("1. Agregar jugador")
    print("2. Consultar jugador")
    print("3. Actualizar jugador")
    print("4. Eliminar jugador")
    print("5. Salir")
        
    opcion = int(input("Elige una opción (1-5): "))
    
    if opcion == 1:
        name = input("Ingrese el nombre del jugador: ")
        number = input("Ingrese el número del jugador: ")
    
        nbaPlayer[name] = number
        
        print("Jugador agregado.")
        
    elif opcion == 2:
        name = input("Ingrese el nombre del jugador que desea consultar: ")
        if name in nbaPlayer:
            print(f"Nombre: {name}, Número: {nbaPlayer[name]}")
        else:
            print("Jugador inexistente")
    
    elif opcion == 3:
        name = input("Ingrese el nombre del jugador que desea actualizar: ")
        if name in nbaPlayer:
            new_number = input("Ingrese el nuevo número del jugador: ")
            nbaPlayer[name] = new_number
            print(f"Número de {name} actualizado.")
        else:
            print("Jugador inexistente")
    
    elif opcion == 4:
        name = input("Ingrese el nombre del jugador que desea eliminar: ")
        if name in nbaPlayer:
            del nbaPlayer[name]
            print(f"{name} eliminado.")
        else:
            print("Jugador inexistente")
    
    elif opcion == 5:
        print("Chao")
        break
    
    else:
        print("Opción no válida. Por favor, elige una opción válida (1-5).")

print("Diccionario final de jugadores:")
print(nbaPlayer)


    