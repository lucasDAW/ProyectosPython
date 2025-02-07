# cadenaejemplo ="""MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX"""
# matriz = cadenaejemplo.split('\n')
# # print(matriz)
# palabra = "XMAS"
# # print(cadenaejemplo)
# total_encontradas=0
# print('+++++++++++++++++++++++ MI MATRIZ +++++++++++++++++++++++ ')
# for m in matriz:
#     print(m)
# print('+++++++++++++++++++++++ FIN MI MATRIZ +++++++++++++++++++++++ ')
# for i in range(0,len(matriz)):
#     for j in range(0,len(matriz[i])):
#
#         c = matriz[i][j]
#         if c =='S' or c == 'X':
#             #encontramos S o X de la palabra XMASS
#             if c =='S':
#                 pass
#
# def buscar_alrededor(celda,i,j,matriz):
#     c=matriz[i-1][j-1]+' '+matriz[i-1][j]+' '+matriz[i-1][j+1]+'\n'
#     c+=matriz[i][j-1]+' '+matriz[i][j]+' '+matriz[i][j+1]+'\n'
#     c+=matriz[i+1][j-1]+' '+matriz[i+1][j]+' '+matriz[i+1][j+1]+'\n'
#     print(c)
#     array_busqueda = [matriz[i-1][j-1],matriz[i-1][j],matriz[i-1][j+1],
#                       matriz[i][j-1],matriz[i][j+1],
#                       matriz[i+1][j-1],matriz[i+1][j],matriz[i+1][j+1]]
#     if celda=='S' or celda=='M':
#         if 'A' in array_busqueda:
#             print('poss')
#
#
#
#
# print(matriz[2][5])
# buscar_alrededor(matriz[2][5],2,5,matriz)
# """
# MMMSXXMASM
# MSAM+MSMSA
# AMXSXMAAMM
# """

import re

# Parse the grid into a dictionary of (y,x):c
data = open("day_4.txt").readlines()
H, W = len(data), len(data[0])-1
grid = {(y,x):data[y][x] for y in range(H) for x in range(W)}

# Part 1 - Find anything that says 'XMAS'
TARGET = "XMAS"
DELTAS = [(dy,dx) for dy in [-1,0,1] for dx in [-1,0,1] if (dx!=0 or dy!=0)]
count = 0

for y, x in grid:
    for dy,dx in DELTAS:
        candidate = "".join(grid.get((y+dy*i, x+dx*i),"") for i in range(len(TARGET)))
        count += candidate == TARGET

print("Part 1:", count)

# Part 2 - Find an MAS 'X'...
count = 0
for y, x in grid:
    if grid[y,x]=="A":
        lr = grid.get((y-1,x-1),"")+grid.get((y+1,x+1),"")
        rl = grid.get((y-1,x+1),"")+grid.get((y+1,x-1),"")
        count += {lr, rl} <= {"MS", "SM"}
print("Part 2:", count)