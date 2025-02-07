import itertools


def fuerza_bruta(contrasenia, long_max=6):
    c = "abcdefghijklmnopqrstuvwxyz0123456789"

    for longitud in range(1, long_max + 1):
        print(f"Longitud {longitud}...")
        for intento in itertools.product(c, repeat=longitud):
            intento_s = ''.join(intento)
            if intento_s == contrasenia:
                return intento_s
    return None

passwrod= 'hfydHH8f'
encuentrada = fuerza_bruta(passwrod,long_max=9)
print(encuentrada)