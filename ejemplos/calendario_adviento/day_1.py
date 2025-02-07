# https://adventofcode.com/2024/day/1#part2
with open('day_1.txt', 'r') as c:
    fila1 = []
    fila2 = []
    diferencias= []
    lineas = c.readlines()
    for i,l in enumerate(lineas):
        lineas[i] = l.replace('\n','')
        fila1.append(int(lineas[i].split('   ')[0]))
        fila2.append(int(lineas[i].split('   ')[1]))
# parte 1
    # ordenarmos las lista
    fila1.sort()
    fila2.sort()


    for f in range(0,len(fila1)):
        if fila1[f]>fila2[f]:
            diferencias.append(fila1[f]-fila2[f])
        else:
            diferencias.append(fila2[f]-fila1[f])

    print(f'El numero a introducir es {sum(diferencias)}')
    # parte 2
    numero_apariciones=dict()
    for numero in fila1:
        total_apariciones = 0
        for n2 in fila2:
            if numero == n2:
                total_apariciones +=1
                apa = {numero:total_apariciones}
                numero_apariciones.update(apa)

resultado = 0
for clave in numero_apariciones:
    # print(clave)
    # print(numero_apariciones[clave])
    resultado += clave*numero_apariciones[clave]
print(f'El resultado final es {resultado}')

