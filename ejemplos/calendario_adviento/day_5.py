from collections import defaultdict

archivo = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


# print(archivo)
# operamos aqui el resultado del archivo day_5.txt

with open('day_5.txt', 'r') as archivotexto:
     archivo = archivotexto.read()

orden_impresion = archivo.split('\n\n')

lista_de_impresion = orden_impresion[0].split('\n')
lista_de_impresion.pop(0)
diccionario_de_impresion = {}
derecha_orden = []
izquierda_orden = []
for oi in lista_de_impresion:

    l,r = oi.split('|')
    if l in diccionario_de_impresion:
        elementos = diccionario_de_impresion[l]
        diccionario_de_impresion[l] =elementos+','+r
    else:
        diccionario_de_impresion[l] = r



diccionario2 = defaultdict(set)
diccionario3 = defaultdict(set)
for oi in lista_de_impresion:

    l,r = oi.split('|')
    if r in diccionario2:
        elementos = diccionario2[r]
        diccionario2[r] =elementos+','+l
    else:
        diccionario2[r] = l
    diccionario3[r]=l
print(diccionario3)

filas_impresion = orden_impresion[1].split('\n')
filas_impresion.pop(-1)
fila_primero = filas_impresion[-1]

print(diccionario2)
# da el numero medio de la fila de cada fila que cumple un ordern
def recuentofilas(fila):
    numeros_filas = fila.split(',')
    resultado = []
    cumpleregla=True
    salida =0
    # 97, 13, 75, 29, 47

    for i,x in enumerate(numeros_filas):
        for j,y in enumerate(numeros_filas):
            if i<j and y in diccionario3[x]:
                cumpleregla=False

    if cumpleregla:
        salida = int(numeros_filas[len(numeros_filas)//2])

    return salida



#lista con todos los numeros medios
resultadoobtenido = [recuentofilas(fila) for fila in filas_impresion]
print(resultadoobtenido)
def suma_numeros_medios(num):
    cadenaresultado = 0
    for r in num:
        if r is not None:
            cadenaresultado+=int(r)
    return cadenaresultado

# print(diccionario_de_impresion)
print(suma_numeros_medios(resultadoobtenido))


#######################################################################################################################
# print(ej)
#
# todas_reglas, actualizacion =  ej.strip().split('\n\n')
#
# reglas=[]
# update=[]
# for r in todas_reglas.split('\n'):
#     a,b = r.split('|')
#     reglas.append((int(a),int(b)))
# for la in actualizacion.split('\n'):
#     la = list(map(int,la.split(',')))
#     # print(la)
#     update.append(la)
#
# print(reglas)
# print(update)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# def elemento(vector):# mitad del vector
#     return vector[len(vector)//2]
#
# print(update[0])
# for n in update[0]:
#     for r in reglas:
#         if(r[0] ==update[0][0]):
#             print(r)
# total = 0
# ok = True
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# print(update[0])
#
# def cumple_reglas(modificacion):
#     id = {}
#     for i , num in enumerate(modificacion):
#         id[num] = i
#     print(id)
#     for a,b in reglas:
#         if a in id and b in id and not id[a]<id[b]:
#             return False, 0
#     return True,modificacion[len(modificacion)//2]
#
#
# print(cumple_reglas(update[0]))
# total=0
# for up in update:
#     good,mid = cumple_reglas(up)
#     if good:
#         total += mid
# print(total)
#
# ###################################################################################################################################
# with open('day_5.txt', 'r') as c:
#     cadena=''
#     for t in c:
#         cadena+=t
#
#     todas_reglas, actualizacion = cadena.strip().split('\n\n')
#
#     reglas = []
#     update = []
#     for r in todas_reglas.split('\n'):
#         a, b = r.split('|')
#         reglas.append((int(a), int(b)))
#     for la in actualizacion.split('\n'):
#         la = list(map(int, la.split(',')))
#         # print(la)
#         update.append(la)
#
#     print(reglas)
#     print(update)
#
#     print(update[0])
#
#
#     def cumple_reglas(modificacion):
#         id = {}
#         for i, num in enumerate(modificacion):
#             print(i, num)
#             id[num] = i
#         print(id)
#         for a, b in reglas:
#             if a in id and b in id and not id[a] < id[b]:
#                 return False, 0
#         return True, modificacion[len(modificacion) // 2]
#
#
#     print(cumple_reglas(update[0]))
#     total = 0
#     for up in update:
#         good, mid = cumple_reglas(up)
#         if good:
#             total += mid
#     print(total)
#
