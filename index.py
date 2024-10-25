from funciones.opciones import *

opcion=0

productos=[]
precio=[]
stock_min=[]
stock_act=[]

while(opcion!=9):
    
    menu()
    
    try:
        opcion = int(input("Ingrese la opcion que desee: "))
            
    
        #Mostrar
        if opcion==1:

            Mostrar_productos(productos,precio,stock_act)
        
        #Alta productos
        elif opcion==2:

            prod_alta=Agregar_producto()
            
            productos.append(prod_alta[0])
            precio.append(prod_alta[1])
            stock_min.append(prod_alta[2])
            stock_act.append(prod_alta[3])
            
            print("\nProducto Agregado.")
        
        #Eliminar Productos
        elif opcion==3:
            
            Eliminar_producto(productos,precio,stock_min,stock_act)
        
        #Modificar Productos
        elif opcion==4:
            Modificar_producto(productos,precio,stock_min,stock_act)
        
        #Buscar Productos
        elif opcion==5:
            Buscar_producto(productos,precio,stock_min,stock_act)
        
        #Productos bajo stock
        elif opcion==6:
            
            Bajo_stk(productos,precio,stock_min,stock_act)
        
        elif opcion==9:
            print("\n\tSaliendo del programa")
        
        else:
            print("\n\tOpcion invalida")
    
    except ValueError:

        print("\nPor favor, ingrese un número entero válido.")