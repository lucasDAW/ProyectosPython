
nivelesOK = False
while nivelesOK==False:
    try:
        niveles = int(input('Ingrese el total de niveles: '))
        if niveles>=3:
            nivelesOK=True
    except ValueError as e:
        print('No se ha elegido el valor correcto, numero mayor de 3')

total_caracteres = niveles * 2 +1
separacion= '   '+'_'*total_caracteres

# dibujo las torres
for i in range(0,niveles+1):
    nivel = ''
    if i ==0:
        nivel+=' '*(int(total_caracteres/2))+'I'+' '*(len(separacion))+'   '+'I'+' '*(len(separacion))+'   '+'I'
    else:
        nivel+=' '*(int(total_caracteres/2)-i)
        if i==niveles:
            nivel += '#'*(i)+'I'+'#'*(i)+' '*(len(separacion)-i)+'   '+'I'+' '*(len(separacion))+'   '+'I'
        else:
            nivel += '#'*(i)+'I'+'#'*(i)+' '*(len(separacion)-i)+'   '+'I'+' '*(len(separacion))+'   '+'I'



    print(nivel)
print(f'{50*"-"}')
print(f'{int(total_caracteres/2)*" "}A{(2*total_caracteres-niveles)*" "}B{(2*total_caracteres-niveles)*" "}C')
# algoritmo de operaciones

def moverDisco(desde, hacia):
    print('Mover disco de ', desde, ' a ', hacia)

total_movimientos = 0
def moverTorre(niveles,origen,destino,intermedio):
    global  total_movimientos
    niveles = niveles
    total_movimientos = total_movimientos+1
    if niveles >= 1:
        moverTorre(niveles-1,origen,intermedio,destino)
        moverDisco(origen,destino)
        moverTorre(niveles-1,intermedio,destino,origen)

moverTorre(niveles,"A","B","C")
print(f'Total de movimientos empleados: {total_movimientos}')


############################################################################
