def numero_entrada (decimal):
    if decimal <= 0:
        return "0"
    
    binario = ""

    while decimal > 0:
        residuo = int (decimal % 2)
        decimal = int (decimal // 2)
        binario = str(residuo) + binario
    return (binario)


decimal = int(input("Escribe el numero que deseas convertir a binario: "))
binario = numero_entrada (decimal)
print (f"El numero {decimal} en binario es {binario}")


Valor_numerico = int(input("Escribe el numero binario que deseas convertir a decimal: "))
valor_str = str(Valor_numerico)
Numero_decimal = 0
for posicion, valor_str in enumerate(valor_str[::-1]) :
    Numero_decimal += int (valor_str) * 2 ** posicion

print (f"El numero binario {Valor_numerico} en numero decimal es {Numero_decimal}")