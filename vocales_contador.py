def vocales_contar(palabra):
    vocales = {"a","e","i","o","u"}
    resultado = {}
    palabra = palabra.replace(" ","").replace(",","").replace("-","").lower()
    for letra in palabra:
        if letra in vocales:
            if not resultado.get(letra):
                resultado[letra] = 0
            resultado [letra] += 1 
            
    return resultado