
numero = 'MCDXCII'
romanos = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
rom = ['M', 'D', 'C', 'L', 'X', 'V', 'I', ' ']
MAX_VALUE = 3999
MIN_VALUE = 0
num_decimal = 0
prev=0
contador = 0

for n in reversed(numero):
    valor = romanos[n]


    if valor<prev:
        num_decimal -=valor
    else:
        num_decimal +=valor
    prev = valor
    contador+=1

print(num_decimal)

decimal = 1492
roma = ''
totalM = int(decimal/1000)
decimal -= totalM*1000
totalCM =int(decimal/900)
decimal -= totalCM*900
totalD = int(decimal/500)
decimal -= totalD*500
totalCD = int(decimal/400)
decimal -= totalCD*400
totalXC = int(decimal/90)
decimal -= totalXC*90
totalC = int(decimal/100)
decimal -= totalC*100
totalL = int(decimal/50)
decimal -= totalC*50
totalX = int(decimal/10)
decimal -= totalX*10
totalV = int(decimal/5)
decimal -= totalV*5
totalIV = int(decimal/4)
decimal -= totalIV*4
totalI = decimal
decimal -= totalI
print(decimal)


roma = 'M'*totalM+'CM'*totalCM+totalD*'D'+totalCD*'CD'+'C'*totalC+'XC'*totalXC+'L'*totalL+'V'*totalV+'IV'*totalIV+'I'*totalI
print(roma)


exit()
continuar = True
while continuar:
    opcion = int(input("""Introduzca una opcion:
    1- Número Romano a Número Decimal.
    2- Número Decimal a Número Romano."""))

    if opcion == 1:
        total = 0
        numeroRomano = str(input('Introduzca numero romano: '))
        numero = numeroRomano + ' '

        for i in range(0, len(numero)):
            if numero[i] in rom:
                n = numero[i]
                if n == 'M':  # 1000
                    total += 1000
                if n == 'C':
                    total += 100
                if n == 'D':  # 500
                    total += 500
                if n == 'L':  # 50
                    total += 50
                if n == 'X':  # 10
                    total += 10
                if n == 'V':  # 5
                    total += 5
                if n == 'I':
                    total += 1
                if n == 'C' and numero[i + 1] == 'M':
                    total -= 100 * 2
                if n == 'C' and numero[i + 1] == 'D':
                    total -= 100 * 2
                if n == 'X' and numero[i + 1] == 'C':
                    total -= 10 * 2
                if n == 'X' and numero[i + 1] == 'L':
                    total -= 10 * 2
                if n == 'I' and numero[i + 1] == 'V':
                    total -= 1 * 2
                if n == 'I' and numero[i + 1] == 'X':
                    total -= 1 * 2
            else:
                print('No se reconoce caracter romano')

        if total>MAX_VALUE or total<MIN_VALUE or not numeroRomano:
            print('El número no se puede representar')
        else:
            print(f'El número  {numeroRomano} es equivalente a {total}')
    elif opcion == 2:
        numerodecimal = int(input('Introduzca número decimal: '))
        if numerodecimal<MAX_VALUE and numerodecimal>MIN_VALUE:

            num = numerodecimal
            numero_romano = ''
            totalM = int(numerodecimal/1000)
            if totalM>0:
                numero_romano = numero_romano + totalM*'M'
                numerodecimal -= totalM*1000

            totalC = int(numerodecimal/100)
            if totalC ==9:
                numero_romano += 'CM'
                numerodecimal -=900
            elif totalC >=5:
                numerodecimal -=(100*totalC)
                numero_romano += 'D'+'C'*(totalC-5)
            elif totalC==4:
                numero_romano += 'CD'
                numerodecimal -=400
            elif totalC>=1:
                numero_romano += 'C'*(totalC)
                numerodecimal -=totalC*100
            totalX = int(numerodecimal / 10)
            if totalX == 9:
                numero_romano += 'XC'
                numerodecimal -= 90
            elif totalX >= 5:
                numerodecimal -= (10 * totalX-5)
                numero_romano += 'L' + 'X' * (totalX-5)
            elif totalX == 4:
                numero_romano += 'XL'
                numerodecimal -= 40
            elif totalX >= 1:
                numero_romano += 'X' + 'I'*(totalX-1)
                numerodecimal -= totalX * 10

            if numerodecimal == 9:
                numero_romano += 'IX'
                numerodecimal -= 9

            else:

                if numerodecimal>=5:
                   numerodecimal-=5
                   numero_romano +='V'+'I'*numerodecimal
                else:
                    numero_romano +='I'*numerodecimal
                    numerodecimal -=numerodecimal


            print(f'El número  {num} es equivalente a {numero_romano}')
        else:
            print('El número no se puede representar')


    else:
        print('opcion no contemplada')
        opcion = int(input("""Introduzca una opcion:
                1- Número Decimal a Número romano.
                2- Número Romano a Número Decimal."""))

    num = False
    while num == False:
        try:

            continuar = int(input('Salir --> 0, Continuar --> 1'))
            num = True
        except ValueError as e:
            num = False
