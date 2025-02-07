
niveles2 =[]
def nivel_seguro(nivel):
    resultado=[]
    analisis=[]
    salida= False
    for n in range(1,len(nivel)+1):
        if n != len(nivel):
            diferencia= nivel[n]-nivel[n-1]
            analisis.append(diferencia)
    # print(nivel,analisis)
    # print(analisis)
    salida_ascendente = [True if n < 0 and -3<=n<0 else False for n in analisis]
    salida_descendente = [True if n > 0 and 0<n<=3 else False for n in analisis]
    # print(salida_ascendente,salida_descendente)

    if all(salida_ascendente) or all(salida_descendente):
       salida = True
    else:
        salida = False
        niveles2.append(nivel)

    return  salida

def nivel_seguro2(nivel):
    resultado=[]
    analisis=[]
    salida = False

    for n in range(1,len(nivel)+1):
        if n != len(nivel):
            diferencia= nivel[n]-nivel[n-1]
            analisis.append(diferencia)
    # print(nivel,analisis)

    salida_ascendente = [True if n < 0 and -3 <= n < 0 else False for n in analisis]
    salida_descendente = [True if n > 0 and 0 < n <= 3 else False for n in analisis]

    if all(salida_ascendente) or all(salida_descendente):
        salida = True
    else:
        print(analisis)
        analisis2 = [n  for n in analisis if 0<n<=3]
        analisis3 = [n  for n in analisis if -3<=n<0]
        analisis4 = [n  for n in analisis if n==0]
        print(analisis2,analisis3,analisis4)
        # print(len(analisis2),len(analisis3),len(analisis4))
        # print(len(analisis))
        # print(len(analisis2)== len(analisis)-1,len(analisis3)== len(analisis)-1)
        # print(len(analisis3)<=1,len(analisis4)<=1)
        print(len(analisis2)== len(analisis)-1 or len(analisis3)== len(analisis)-1 ) and (len(analisis3)<=1 or len(analisis4)<=1)
        if (len(analisis2)== len(analisis)-1 or len(analisis3)== len(analisis)-1 ) and (len(analisis3)<=1 or len(analisis4)<=1):
            salida=True
            print('TRUE')
        else:
            print('FALSE')
            salida=False

    return  salida


with open('day_2.txt', 'r') as c:
    niveles=[]
    nivelesSeguros= dict()
    total_niveles_seguros = 0
    total_niveles_seguros2 = 0
    MAX_DIFERENCE = 3
    lineas = c.readlines()
    for i,l in enumerate(lineas):
        lineas[i] = l.replace('\n','')

    for j in range(0,len(lineas)):
        niveles.append(lineas[j])

    todos_los_niveles = []
    for i in range(0,len(niveles)):
        # print(niveles[i])
        todos_los_niveles.append(niveles[i])
    # print(todos_los_niveles[0])


    for nivel in todos_los_niveles:
        # print(nivel)
        numero = nivel.split(' ')
        for n in range(0, len(numero)):
            numero[n] = int(numero[n])
        # print(f'[*****] EL nivel: {numero}, ¿es seguro? {"SI" if nivel_seguro(numero)else "NO"}')
        print(f'{"[*****]" if nivel_seguro2(numero) else ""}El nivel: {numero}, ¿es seguro? {"SI----------------------------------------------------" if nivel_seguro2(numero)else "NO"}')
        if nivel_seguro(numero)==True:
            total_niveles_seguros +=1

        if nivel_seguro2(numero):
            total_niveles_seguros2 +=1


print(f'El total de niveles seguros es de {total_niveles_seguros}')
print(f'El total de niveles seguros parte 2 es de {total_niveles_seguros2}')#577


