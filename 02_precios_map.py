#crear constante IVA

IVA = 1.16

#Definir funcion

def aplicar_iva(precio):
    return precio * IVA

precios_sin_iva = [415, 90, 355, 385, 115, 100, 250, 660]

#uso de programacion funcional con modulo map

precios_con_iva = list(map(aplicar_iva,precios_sin_iva))

print(precios_con_iva)