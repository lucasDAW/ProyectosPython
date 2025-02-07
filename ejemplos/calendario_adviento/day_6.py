

import time



def esperar_segundos(n):
    time.sleep(n)


archivo = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

with open('day_6.txt', 'r') as archivotexto:
    archivo = archivotexto.read()

# print(archivo)

matriz_mapa = archivo.split('\n')
def posicion_inicial(mapa):
    xinicial=0
    yinicial=0
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j] == '^':
                xinicial = i
                yinicial= j
    return xinicial,yinicial


movimientos_posibles = [(-1,0),(0,1),(1,0),(0,-1)] # arriba, derecha, abajo, izquierda
posx,posy = posicion_inicial(matriz_mapa)
dx,dy=0,0
d=0
totalmovimientos=0
movimientos_Jugador=set()

for x in range(0,len(matriz_mapa)):
    for y in range(0,len(matriz_mapa[x])):

        while True:
            dx,dy = movimientos_posibles[d]
            possiguientex = posx + dx
            possiguientey = posy + dy
            # print(f'PosicionX:{possiguientex}, PosicionY:{possiguientey}  Dirreción: {d}')
            mov = (possiguientex,possiguientey)
            # movimientos_Jugador.add(mov)
            movimientos_Jugador.add(mov)
            if not (0<=possiguientex<len(matriz_mapa) and 0<=possiguientey<len(matriz_mapa[x])):
                if matriz_mapa[x][y]=='#':#muro
                    totalmovimientos = len(movimientos_Jugador)
                break
            if matriz_mapa[possiguientex][possiguientey] == '#' or possiguientey==x and possiguientey==y:

                d = (d+1)%4
            else:

                posx =possiguientex
                posy =possiguientey


print(totalmovimientos)
print(movimientos_Jugador)
px,py = posicion_inicial(matriz_mapa)
print(f'Posicion inicial : {px,py}')
cadenaMapa=''
for i in range(len(matriz_mapa)):
    for j in range(len(matriz_mapa[i])):
        posicion = (i,j)
        if posicion in movimientos_Jugador:
            cadenaMapa+='X'
        else:
            cadenaMapa +=matriz_mapa[i][j]
    cadenaMapa +='\n'
# print(cadenaMapa)