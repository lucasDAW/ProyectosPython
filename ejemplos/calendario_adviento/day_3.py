#ejemplo
# cadena = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
# expresion = 'mul\([\d]+\,[\d]+\)'
#
# import re
# multiplicacion=re.findall(expresion,cadena)
# print(multiplicacion)
# calculos = []
# total = 0
# for m in multiplicacion:
#     m=m.replace('mul(','')
#     m=m.replace(')','')
#     m = m.split(',')
#     m = [int(m) for m in m]
#     print(m)
#     total += m[0]*m[1]
# print(total)
#ejemplo hasta aqui

import re

with open('day_3.txt', 'r') as archivo:
    texto = archivo.readlines()
    cadena_total =''
    # print(len(texto))
    for t in texto:
        cadena_total +=t
    expresion = 'mul\([\d]+\,[\d]+\)'
    multiplicacion=re.findall(expresion,cadena_total)
    numerosencontrados = []

    total = 0
    for m in multiplicacion:
        m=m.replace('mul(','')
        m=m.replace(')','')
        m = m.split(',')
        m = [int(m) for m in m]
        # print(m)
        numerosencontrados.append(m)
        total += m[0]*m[1]
    print(total)
    print(numerosencontrados)
    # fin primer caso
    expresion2 = "don't\((.*?)do\(\)"
    # expresion2 = "do\((.*?)(mul\()(.*?)(?=don't)"
    multiplicacion2=re.findall(expresion2,cadena_total)
    # print(multiplicacion2)
    # print(len(multiplicacion2))
    cadena_contenido_total =''
    for m in multiplicacion2:
        # print(m)
        cadena_contenido_total +=m
    #63421760
    #89198456
    # print(cadena_contenido_total)
    #procedemos igual que en la parte 1
    expresion = 'mul\([\d]+\,[\d]+\)'
    resultados = re.findall(expresion, cadena_contenido_total)
    # print(resultados)
    numerosencontrados2 = []
    total2 = 0
    for elem in resultados:

        elemento = elem.replace('mul(','').replace(')','')
        elementos = elemento.split(',')
        elementos = [int(e) for e in elementos]
        numerosencontrados2.append(elementos)
        # print(elementos)
        total2 += elementos[0]*elementos[1]
        # print(f'elementos: {elementos[0]} x {elementos[1]} = {total2}')
    print(numerosencontrados2)
    print(f'El total de numeros es {total-total2}')
    print(f'El total de numeros es {total2}')



    print(len(numerosencontrados))#113
    print(len(numerosencontrados2))#48

    domul= []
    for elemento in numerosencontrados:
        if elemento in numerosencontrados2:
            #print(f'El elemento {elemento} esta en la lista 2')
            pass
        else:
            domul.append(elemento)
    print(domul)
    print(len(domul))
    totalmultiplos = 0
    for e in domul:
        totalmultiplos += e[0]*e[1]
    print(totalmultiplos)

    print('#############################################################################')
    cadena_completa = 'do()'
    for t in texto:
        t= t.replace('\n','')
        cadena_completa += t
    print(cadena_completa)
    # patron = "do\((.*?)don\'t\(\)"
    patron = "don\'t\((.*?)do\(\)"
    partes_do = re.findall(patron,cadena_completa)
    print(len(partes_do))
    i=0
    patronmul= "mul\([\d]+\,[\d]+\)"
    totalmul = 0
    for p in partes_do:
        i += 1
        mul = re.findall(patronmul,p)
        # print(mul)
        for m in mul:
            m = m.replace('mul(','')
            m = m.replace(')','')
            num = m.split(',')
            num =[int(x) for x in num]
            # print(num)
            # print(num[0]*num[1])
            totalmul+=num[0]*num[1]
    print(totalmul)
    print(f'Total parte 2:{total-totalmul}')





################################################################################################
    # text ="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    # # text=texto
    # # ct=''
    # # for t in text:
    # #     ct += t
    # multiplicacion=re.findall(expresion,text)
    # print(multiplicacion)
    # # calculos = []
    # totaltest = 0
    # for m in multiplicacion:
    #     m=m.replace('mul(','')
    #     m=m.replace(')','')
    #     m = m.split(',')
    #     m = [int(m) for m in m]
    #     # print(m)
    #     totaltest += m[0]*m[1]
    # print(totaltest)
    # expresion2 = "don't\(\)(.*?)do\(\)"
    # multiplicacion3=re.findall(expresion2,text)
    # #print(multiplicacion2)
    # cadena_contenido_total =''
    # for m in multiplicacion3:
    #         # print(m)
    #     cadena_contenido_total +=m
    #     #63421760
    #     #89198456
    #     # print(cadena_contenido_total)
    #     #procedemos igual que en la parte 1
    # expresion = 'mul\([\d]+\,[\d]+\)'
    # resultadostexto = re.findall(expresion, cadena_contenido_total)
    # print(resultadostexto)
    #
    # total2ejem = 0
    # for elem in resultadostexto:
    #
    #     elemento = elem.replace('mul(','').replace(')','')
    #     elementos = elemento.split(',')
    #     elementos = [int(e) for e in elementos]
    #     # print(elementos)
    #     total2ejem += elementos[0]*elementos[1]
    # print(total2ejem)
    # print(totaltest-total2ejem)

##########################################################################################
print('#############################################################################')
#
# import sys
# import re
#
# if __name__ == '__main__':
#
#     with open('day_3.txt', 'r') as f:
#         mem = f.read()
#
#     mem_clean = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', mem)
#
#     sum_mul = 0
#     for x, y in mem_clean:
#         sum_mul += int(x) * int(y)
#
#     print(f'Suma de multiplicaciones: {sum_mul}')
#
# sum_mul = 0
# do_sum = True
# for x in re.finditer(r'do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)', mem):
#     match x[0]:
#         case 'do()':
#             do_sum = True
#         case 'don\'t()':
#             do_sum = False
#         case _:
#             if do_sum:
#                 sum_mul += int(x[1]) * int(x[2])
#
# print(sum_mul)
# print(totalmultiplos-sum_mul)
print(83595109)