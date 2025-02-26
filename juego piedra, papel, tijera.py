# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:19:45 2025

@author: Ricardo.Quijano
"""

import random


def jugar_contracomputadora():
    opciones = ["Piedra", "Papel", "Tijera"]

  
    print("Jugador, elige: Piedra, Papel o Tijera")
    jugador = input().capitalize()
    
  
    if jugador not in opciones:
        print("Elección inválida. Elige entre Piedra, Papel o Tijera.")
        return

   
    computadora = random.choice(opciones)
    
    print(f"Tú elegiste: {jugador}")
    print(f"La computadora eligió: {computadora}")
    
 
    if jugador == computadora:
        print("¡Es un empate!")
    elif (jugador == "Piedra" and computadora == "Tijera") or \
         (jugador == "Papel" and computadora == "Piedra") or \
         (jugador == "Tijera" and computadora == "Papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste! La computadora gana.")


def jugar_entre2():
    opciones = ["Piedra", "Papel", "Tijera"]

    
    print("Jugador 1, elige: Piedra, Papel o Tijera")
    jugador1 = input().capitalize()
    
   
    if jugador1 not in opciones:
        print("Elección inválida. El Jugador 1 debe elegir entre Piedra, Papel o Tijera.")
        return


    print("Jugador 2, elige: Piedra, Papel o Tijera")
    jugador2 = input().capitalize()


    if jugador2 not in opciones:
        print("Elección inválida. El Jugador 2 debe elegir entre Piedra, Papel o Tijera.")
        return

    print(f"Jugador 1 eligió: {jugador1}")
    print(f"Jugador 2 eligió: {jugador2}")
    

    if jugador1 == jugador2:
        print("¡Es un empate!")
    elif (jugador1 == "Piedra" and jugador2 == "Tijera") or \
         (jugador1 == "Papel" and jugador2 == "Piedra") or \
         (jugador1 == "Tijera" and jugador2 == "Papel"):
        print("¡Jugador 1 gana!")
    else:
        print("¡Jugador 2 gana!")


def main():
    while True:
        print("\n¡Bienvenido al juego de Piedra, Papel o Tijera!")
        print("¿Quieres jugar contra la computadora o entre dos jugadores?")
        print("1. Jugar contra la computadora")
        print("2. Jugar entre dos jugadores")
        print("3. Salir")

        opcion = input("Selecciona una opción (1/2/3): ")

      
        if opcion == "1":
            jugar_contracomputadora()
        elif opcion == "2":
            jugar_entre2()
        elif opcion == "3":
            print("¡Gracias por jugar! ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Por favor selecciona 1, 2 o 3.")


main()
