import  random
#
# print(u'Bienvenido a BlackJack')
#
#
# def suma(lista):
#
#     return sum(lista)
#
# def pedirNumero(lista):
#     n = random.randint(1,13)
#     if n >=10:
#         n = 10
#     lista.append(n)
#     return  n
#
# cartasPC = []
# cartasJugador = []
# opcionestotal = ['1','2','3','4']
# def inicio():
#     for _ in range(2):
#         pedirNumero(cartasPC)
#         pedirNumero(cartasJugador)
#
# def ganador():
#     if suma(cartasPC)>=suma(cartasJugador) and suma(cartasPC)<=21:
#         return False
#     else:
#         return True
#
# salir = True
# pedir = True
# while salir:
#     inicio()
#     while pedir:
#         print(f'Cartas del PC {cartasPC} - {suma(cartasPC)}')
#         print(f'Cartas del Jugador {cartasJugador} - {suma(cartasJugador)}')
#
#         print('''Opciones:
#         1. Pedir Carta
#         2. Plantarse
#         3. Mostrar resultados
#         4. Salir''')
#         opcion = ''
#         try:
#             while not opcion.isdigit():
#                 opcion =int(input('Seleccione opción'))
#         except:
#             print('Error al seleccionar opción. Ingrese un numero permitido [1-4]')
#
#         if opcion==1:
#             print(f'Aqui tiene su carta  {pedirNumero(cartasJugador)}')
#
#             if suma(cartasJugador)>21:
#                 print('Se ha pasado, ha ganado el PC')
#                 pedir=False
#         elif opcion==2:
#             print('Ya no sigue jugando el jugador')
#             while suma(cartasPC)<=suma(cartasJugador):
#                 pedirNumero(cartasPC)
#
#             if ganador():
#                 print('Ha ganado el Jugador')
#             else:
#                 print('Ha ganado el PC')
#             pedir = False
#
#         elif opcion ==3:
#             print(f'Cartas del PC {cartasPC} - {suma(cartasPC)}')
#             print(f'Cartas del Jugador {cartasJugador} - {suma(cartasJugador)}')
#
#
#         elif opcion ==4:
#             break
#
#     print(f'Cartas del PC {cartasPC} - {suma(cartasPC)}')
#     print(f'Cartas del Jugador {cartasJugador} - {suma(cartasJugador)}')
#
#     repetir = int(input('Repetir- 1 , Salir -0'))
#     if repetir== 0:
#         salir=False
#     else:
#         cartasPC=[]
#         cartasJugador=[]
#         pedir = True
# ----------------------------------------------------------------------------------------



valor_cartas = [2,3,4,5,6,7,8,10,'J','Q','K','AS']

valor_num_cartas = {2:2, 3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,
                    'J':10,'Q':10,'K':10, 'AS':11}


def repartir_carta(mazo):
    tam_mazo = len(mazo)
    rand_index = random.randint(0,tam_mazo-1)
    #elegimos una carta y la sacamos del mazo
    carta = mazo.pop(rand_index)
    return carta

def iniciar_partida():
    mazo_cartas = [carta for carta in valor_cartas for j in range(4)]

    mano_jugador = []
    mano_casa = []
    for j in range(2):
        mano_jugador.append(repartir_carta(mazo_cartas))
        mano_casa.append(repartir_carta(mazo_cartas))
    return mano_jugador,mano_casa, mazo_cartas

def suma_cartas(mano):
    sumatotal =0
    for carta in mano:
        sumatotal += valor_num_cartas[carta]
    if 'AS' in mano:
        num_ases = sum([1  for j in mano if j== 'AS'])
        contador = 0
        while contador<num_ases and sumatotal>21:
            sumatotal -= 10
            contador += 1
    return sumatotal

def sigueJugando(mano_jugador,mano_casa):
    if suma_cartas(mano_jugador)<=21:
        return True

    return False

def determinar_ganador(mano_j,mano_c):
    if suma_cartas(mano_c)>21 or suma_cartas(mano_j)<=21 and suma_cartas(mano_j)>suma_cartas(mano_c) :
        return 'El Jugador'
    else:
        return 'La Casa'
continuar = True
while True and continuar:
    print('Bienvenido al black-jack')
    # iniciar la partida- reparte manos de jugador, casa y resetea el mazo
    mano_jugador,mano_casa, mazo_cartas = iniciar_partida()


    while sigueJugando(mano_jugador,mano_casa):
        print()
        print('Tus cartas: ', mano_jugador, suma_cartas(mano_jugador))
        print('Cartas Casa: ', mano_casa, suma_cartas(mano_casa))
        print()
        print('¿Quiere Pedir Carta (P) or Plantarte (S)?')
        if suma_cartas(mano_jugador) !=21:

            pide_o_planta = input('Pedir carta o plantarse')
            if pide_o_planta == 'P':
                mano_jugador.append(repartir_carta(mazo_cartas))
            elif pide_o_planta == 'S':
                while suma_cartas(mano_casa)<= suma_cartas(mano_jugador):
                    mano_casa.append(repartir_carta(mazo_cartas))
                break # salimos del bucle y se determina el ganador
        else:
            while suma_cartas(mano_casa) <=21:
                mano_casa.append(repartir_carta(mazo_cartas))
            break  # salimos del bucle y se determina el ganador




    print()
    print('Tus cartas: ', mano_jugador, suma_cartas(mano_jugador))
    print('Cartas Casa: ', mano_casa, suma_cartas(mano_casa))
    print()


    # determinar el ganador
    ganador = determinar_ganador(mano_jugador,mano_casa)
    print(f'------------------------\n| Ganador--> {ganador} |\n------------------------')

    if input('Salir->E') == 'E':
        continuar =False