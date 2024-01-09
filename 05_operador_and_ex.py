numero = 23

def menor_que_diez(numero):
    if numero < 10:
        return True
    else:
        return False
def numero_par(numero):
    if numero % 2 == 0:
        return True 
    else:
        return False

def numero_positivo(numero):
    if numero > 0:
        return True
    else:
        return False

numero_magico = menor_que_diez(numero) and numero_par(numero) and numero_positivo(numero)
print(numero_magico)


#menor que diez
#if numero < 10 and numero % 2 == 0 and numero > 0:
 #   numero_magico = True
#else:
 #   numero_magico = False

print(numero_magico)