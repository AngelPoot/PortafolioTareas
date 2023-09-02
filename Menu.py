def menu_opciones ():
    print ("selecciona una opcion:")
    print ("1. Convertir de binario a decimal")
    print ("2. Convertir de decimal a binario")
    print ("3. Multiplicacion")
    print ("4. Dividir")
    print ("5. Sumar")
    print ("6. Restar")
    print ("7. Salir")

while True:
    correcto = False
    num = 0
    while not correcto:
        try:
           menu_opciones ()
           num = int(input("Introduce el numero de la accion: "))
           correcto = True
        except ValueError:
            print ('Error, Porfavor introducir un numero entero')
    print (f'Elegiste el numero {num}' )
    opciones_multiples = int(num)
    if opciones_multiples == 1:
        Valor_numerico = int(input("Escribe el numero binario que deseas convertir a decimal: "))
        valor_str = str(Valor_numerico)
        Numero_decimal = 0
        for posicion, valor_str in enumerate(valor_str[::-1]) :
            Numero_decimal += int (valor_str) * 2 ** posicion
        print (f"El numero binario {Valor_numerico} en numero decimal es {Numero_decimal}")
    elif opciones_multiples == 2:
        def numero_entrada (decimal):
            if decimal <= 0:
                return "0"
            binario = ""
            while decimal > 0:
                residuo = int (decimal % 2)
                decimal = int (decimal // 2)
                binario = str(residuo) + binario
            return (binario)
        decimal = int(input("Escribe el numero decimal que deseas convertir a binario: "))
        binario = numero_entrada (decimal)
        print (f"El numero decimal {decimal} en numero binario es {binario}")
    elif opciones_multiples == 3:
        Multiplicacion_digito = int(input("Ingrese el primer numero "))
        Multiplicacion_digito2 = int(input("Ingrese el segundo numero "))
        resultado_multiplicacion = int(Multiplicacion_digito) * int (Multiplicacion_digito2)
        resultado = resultado_multiplicacion
        print (f'La multiplicacion de los numeros {(Multiplicacion_digito)} y {(Multiplicacion_digito2)} es {resultado}')
    elif opciones_multiples == 4:
        division_digito = int(input("Ingrese el primer numero "))
        division_digito2 = int(input("Ingrese el segundo numero "))
        resultado_division = int(division_digito) / int(division_digito2)
        residuo = int(division_digito) % int (division_digito2)
        resultado_residuo = residuo
        resultado = resultado_division
        print (f'La division de los numeros {(division_digito)} y {(division_digito2)} es {resultado} y su residuo es {residuo}')
    elif opciones_multiples == 5:
        suma_digito = int(input("Ingrese el primer numero "))
        suma_digito2 = int(input("Ingrese el segundo numero "))
        resultado_suma = int(suma_digito) + int (suma_digito2)
        resultado = resultado_suma
        print (f'La suma de los numeros {(suma_digito)} y {(suma_digito2)} es {resultado}')
    elif opciones_multiples == 6:
        resta_digito = int(input("Ingrese el primer numero "))
        resta_digito2 = int(input("Ingrese el segundo numero "))
        resultado_resta = int(resta_digito) - int(resta_digito2)
        resultado = resultado_resta
        print (f'La resta de los numeros {(resta_digito)} y {(resta_digito2)} es {resultado}')
    elif opciones_multiples == 7:
        print ("Hasta luego que tengas un excelente dia")
        break
    else:
        print ("Introducir solo numeros del 1 al 7")