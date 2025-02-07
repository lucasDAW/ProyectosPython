# https://adventofcode.com/2024/day/25

cerraduras=[]
llaves = []


CLAVE_LLAVES = '.'*5
CLAVE_CERRADURAS = '#'*5



def contadorclave(elemento):
    '''Metodo que devuelve el total de # de cada elemento sea cerradura o llave'''
    totalesestrellas = [0, 0, 0, 0, 0]
    for i in range(len(elemento)):

        for j in range(len(elemento[i])):
            if elemento[i][j]=="#":
               totalesestrellas[j]+=1
    for i in range(len(totalesestrellas)):
        totalesestrellas[i]=totalesestrellas[i]-1

    return totalesestrellas


with open('../code_chronicle.txt', 'r') as c:
    lineas = c.readlines()

    final = 0
    salto = 7
    totalelementos = 0
    while final <= len(lineas):
        if final ==len(lineas):#linea final
            elemento = []
            elemento = lineas[final - 7:final+1]
            for i, e in enumerate(elemento):
                elemento[i] = e.replace('\n', '')
            totalelementos += 1
            if elemento[0] == CLAVE_LLAVES:
                llaves.append(elemento)
            elif elemento[0] == CLAVE_CERRADURAS:
                cerraduras.append(elemento)
        else:

            if lineas[final] =='\n':
                elemento = []
                elemento=lineas[final-7:final]

                for i,e in enumerate(elemento):
                    elemento[i]=e.replace('\n','')
                totalelementos +=1
                if elemento[0]==CLAVE_LLAVES:
                    llaves.append(elemento)
                elif elemento[0] == CLAVE_CERRADURAS:
                    cerraduras.append(elemento)
                else:
                    print('No es ni cerradura y ni llave')

        final+=1





def totalUtiles(llaves,cerraduras):
    cerraduras_contador = []
    llaves_contador = []

    for llave in llaves:
        llaves_contador.append(contadorclave(llave))
    for cerradura in cerraduras:
        cerraduras_contador.append(contadorclave(cerradura))

    totalUtiles = 0
    for l in llaves_contador:
        sumaasteriscos = [0,0,0,0,0]
        for c in cerraduras_contador:

            for i in range(0,5):
                sumaasteriscos[i]=l[i]+c[i]
            if sumaasteriscos[0]<=5 and sumaasteriscos[1]<=5 and sumaasteriscos[2]<=5 and sumaasteriscos[3]<=5 and sumaasteriscos[4]<=5:
                # print(f'La llave:{l}-encaja con la cerradura: {c}')
                index_llave = llaves_contador.index(l)
                index_cerradura = cerraduras_contador.index(c)
                figurallave = llaves[index_llave]
                figuracerradura = cerraduras[index_cerradura]
                cadena = ['CERRADURA' + ' ' * 6 + 'LLAVE']
                for z in range(0, 7):
                    cadena.append(figurallave[z] + ' ' * 10 + figuracerradura[z])
                cadena.append('-------------------------------------')
                for ca in cadena:
                    print(ca)


                totalUtiles +=1
    return totalUtiles

print(f'Llaves funciona: {totalUtiles(llaves,cerraduras)}')