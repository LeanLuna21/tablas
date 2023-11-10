###### ESTE PROGRAMA LE DA LA CHANCE AL USUARIO DE CREAR UN ARCHIVO QUE CONTENGA LA TABLA DE UN NUMERO N. 
###### ADEMAS, LE DA LA CHANCE DE LEER ALGUNA TABLA YA EXISTENTE, Y DE NO EXISITR EL ARCHIVO, LE CONSULTA AL USUARIO SI DESEA CREARLO.

# FX PARA QUE EL USUARIO INDIQUE SI QUIERE REALIZAR OTRA OPERACION
def continuar_operando():
    print('¿Desea realizar otra operación? (y/n)')
    decision = input('').lower()
    if decision == 'yes' or decision == 'y':
        main()
    else:
        print('Ok. Nos vemos pronto. ¡Adiós!')
        quit()

# FX QUE CREA EL TXT CON LA TABLA DEL NUMERO INTRODUCIDO POR EL USUARIO. 
def crear_fichero(num):
    nombre_fichero = 'tabla-'+str(num)+'.txt'
    try:
        doc = open(nombre_fichero,'w')
    except Exception as err:
        print('Ha ocurrido el siguiente problema:',err)
        
    # EN EL RANGO DEL 0 AL 10, ESCRIBIMOS EN EL DOC CADA ITERACION CON SU MULTIPLICACION
    for i in range(11):
        doc.write(f' \n{num} * {i} = {num*i}')  
    doc.write('\n'+'---------------'+'\n')
    print('¡Fichero creado con éxito!')
    doc.close()

# FX QUE AGREGA EL FICHERO EN CASO DE NO EXISTIR
def agregar_fichero(num):
    print('¿Desea crear el fichero inexistente? (y/n)')
    option = input('').lower()
    if option == 'y':
        # LLAMAMOS A LA FX QUE CREA EL FICHERO
        crear_fichero(num)
    else:
        print('OK.')    

# FX PARA EVALUAR SI EL NUM ELEGIDO ES VALIDO Y CREAR EL FICHERO
def multiplicacion ():
    num = input('Ingrese un número: ')
    try:
        num = int(num)
    except Exception: 
        print('Por favor ingrese un número.')

    # LLAMAMOS A LA FX QUE CREA EL FICHERO    
    crear_fichero(num)
    # CONSULTAMOS SI DESEA HACER OTRA OPERACION
    continuar_operando()

# FX PARA MOSTRAR UNA LINEA EN ESPECIFICO INDICADA POR EL USUARIO
def leer_linea(num):
    fichero = "tabla-"+str(num)+".txt"
    with open(fichero,"r") as doc:
        elements = doc.readlines()
        n = int(input("Introduzca linea a leer: "))
        print(elements[n+1])
 
# FX QUE MUESTRA LA TABLA DEL NUMERO INTRODUCIDO POR EL USUARIO
def mostrar_fichero():
    num = input('¿Qué número desea ver?: ')
    try:
        num = int(num)
    except Exception as err: 
        print('Ha ocurrido un error:',err)
    
    fichero = 'tabla-'+str(num)+'.txt'
    try:
        doc = open(fichero,'r')
    except FileNotFoundError:
        print('No hay tablas definidas para el numero solicitado.')
        agregar_fichero(num)
    else:
        # CONSULTAMOS AL USUARIO SI QUIERE VER ALGUNA LINEA ESPECIFICA, SINO DEVOLVEMOS LA TABLA COMPLETA
        print("¿Desea leer alguna linea en especial? (y/n) ")
        option = input("").lower()
        if option == "y":
            # SI LA RESPUESTA ES 'SI' LLAMAMOS A LA FX ENCARGADA DE MOSTRAR LA LINEA SOLICITADA 
            leer_linea(num)
        else:
            # SINO MOSTRAMOS LA TABLA COMPLETA
            print(f'Esta es la tabla del {num}:')
            tablas = doc.readlines() #readlines devuelve una lista con cada una de las lineas del txt
            for i in tablas:
                print (i)
    # CONSULTAMOS SI DESEA HACER OTRA OPERACION        
    continuar_operando()

# FUNCION SOLO PARA MOSTRAR EL MENU DE OPCIONES - RETORNA LA OPCION ELEGIDA POR EL USUARIO
def show_menu():
    print('''------------------------------------------------

Bienvenido a Tablas.exe.
Elija una de las siguientes tareas a realizar...

1- Crear tabla de multiplicar 
2- Mostrar tabla de multiplicar
3- Salir

-------------------------------------------------
          ''')
    option= input('Ingrese una opcion: ')
    return option


# FX QUE VA A EVALUAR LA OPCION QUE DESEA REALIZAR EL USUARIO  
def main():
    # MOSTRAMOS EL MENU DE OPCIONES Y EVALUAMOS LA OPCION ELEGIDA
    option = show_menu()
    if option == '1':
        multiplicacion()
    elif option == '2':
        mostrar_fichero()
    elif option == '3':
        print('¡Adiós!')
        quit()
    else: 
        print('Opción invalida. Elija una de las opciones disponibles') 
        continuar_operando()
    
# ACA ARRANCA EL PROGRAMA PRINCIPAL 
if __name__ == '__main__':
    main()
