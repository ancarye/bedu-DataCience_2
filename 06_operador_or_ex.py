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

n = 21
print(menor_que_diez(n) or numero_par(n))