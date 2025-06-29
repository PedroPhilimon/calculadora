while True:
    print('Menú de Opciones')
    print("===================")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicación")
    print("4.- División")    
    print("S.- Salir")
    opc=input('Ingrese Opción: ')
    if opc=='1':
        try:
            oper1=int(input('Ingrese Operando 1: '))
            try:
                oper2=int(input('Ingrese Operando 2: '))
                suma=oper1+oper2
                print('La Suma es igual a ',suma)
            except:
                print('Debe ser un entero el operando 2')
        except:
            print('Debe ser un entero el operando 1')
    elif opc=='2':
        while True:
            try:
                oper1=int(input('Ingrese Operando 1: '))
                break
            except:
                print('Debe ser un entero el operando 1')
        while True:
            try:
                oper2=int(input('Ingrese Operando 2: '))
                break
            except:
                print('Debe ser un entero el operando 2')
        resta=oper1-oper2
        print('La Resta es igual a ',resta)
    elif opc=='3':
        while True:
            try:
                oper1=int(input('Ingrese Operando 1: '))
                break
            except:
                print('Debe ser un entero el operando 1')
        while True:
            try:
                oper2=int(input('Ingrese Operando 2: '))
                break
            except:
                print('Debe ser un entero el operando 2')
        multi=oper1*oper2
        print('La Multiplicación es igual a ',multi)
    elif opc=='4':
        while True:
            try:
                oper1=int(input('Ingrese Operando 1: '))
                break
            except:
                print('Debe ser un entero el operando 1')
        while True:
            try:
                oper2=int(input('Ingrese Operando 2: '))
                if oper2==0:
                    print('El denominador no puede ser cero')
                else:
                    break
            except:
                print('Debe ser un entero el operando 2')
        divi=oper1/oper2
        print('La División es igual a ',divi)
#     try:
#            divi=oper1/oper2
#            print('La División es igual a ',divi)
#        except ZeroDivisionError:
#            print('El denominador no puede ser cero')
    elif opc=='S' or opc=='s':
        print('Hasta la vista baby')
        exit() #break
    else:
        print('Opción Incorrecta')
