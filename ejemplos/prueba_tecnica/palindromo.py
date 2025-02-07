palabra = input('Inserte palabra: ')

def is_palindromo(p):

    p.strip()
    palabra_inversa= p[::-1]

    if palabra_inversa==p:
        print(p,' Es palíndromo')
        return True
    else:
        print(p,' No es palíndromo')
        return False
