def numero_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
print(not numero_par(12))
print(not numero_par(13))