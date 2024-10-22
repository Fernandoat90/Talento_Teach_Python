from funciones.opciones import *

opcion=0

productos=[]
precio=[]
stock_min=[]

while(opcion!=9):
    
    menu()
    
    try:
        opcion = int(input("Ingrese la opcion que desee: "))
            
    

        if opcion==1:

            Mostrar_productos(productos,precio)
        
        elif opcion==2:

            prod_alta=Agregar_producto()
            productos.append(prod_alta[0])
            precio.append(prod_alta[1])
            stock_min.append(prod_alta[2])
        
        elif opcion==3:
            
            Eliminar_producto(productos,precio,stock_min)
        
        elif opcion==4:
            Modificar_producto(productos,precio,stock_min)
        
        elif opcion==5:
            Buscar_producto(productos,precio,stock_min)

        elif opcion==9:
            print("\n\tSaliendo del programa")
        
        else:
            print("\n\tOpcion invalida")
    
    except ValueError:

        print("\nPor favor, ingrese un número entero válido.")