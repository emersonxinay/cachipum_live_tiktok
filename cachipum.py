'''crear un programa de consola para 
el juego de piedra, papel y tijera'''

# nivel básico
import random
while True:
    print("Ingrese una opción valida o escribe s para salir:")
    
    usuario = input("ingrese piedra, papel o tijera: ")
    if (usuario == "piedra" or usuario == "papel" or usuario == "tijera" ):

        opciones = ['piedra', 'papel', 'tijera']
        computador = random.choice(opciones)

        # todas las opciones para que gane el usuario
        if ((usuario=="papel" and computador=="piedra" )or(usuario=="piedra" and computador == "tijera")or(usuario =="tijera" and computador == "papel")):
            print(f"Ganaste al computador: usuario eligio: {usuario}, computador eligio: {computador}  ")
        # la opción para que empaten
        elif (usuario == computador):
            print(f"Empataron: usuario eligio {usuario}, computador eligio: {computador} ")
        else:
            print(f"Perdiste contra el computador: usuario eligio {usuario}, computador eligio: {computador} ")

    elif usuario == "s".lower():
        print("Saliendo del juego...")
        break

    else:
        print("Opción no valida")


# nivel intermedio