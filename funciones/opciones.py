#menu
def menu ():
    print("""
    \n\t********************** \n\t Menu de opciones \n\t**********************\n
    1.Consulta Lista de productos.
    2.Agregar un producto.
    3.Eliminar producto.
    4.Modificar producto.
    5.Buscar producto.
    6.Productos Bajo Stock.
    9.Salir del programa.\n
    """)


#opcion 1
def Mostrar_productos(prod,precio,stock_act):
    
    producto=""
    pos=0
    numero=1
    
    print("\n\tProducto  |  Precio  |  Stock")
    
    for producto in prod:
        
        print(f"\t{numero}.{producto}    |  ${precio[pos]} |  {stock_act[pos]} uni.")
        pos+=1
        numero+=1
    
    if producto=="":
    
        print("\nNo hay productos disponibles. ")


#opcion 2
def Agregar_producto():

        producto=str(input("\nIngrese un nuevo producto: ")).lower()
        precio=float(input("\nIngrese el precio del producto: "))
        stock_min=int(input("\nAgregue el STOCK minimo que manejara este producto: "))
        stock_act=int(input("\nIngrese la cantidad de stock disponible: "))
        return[producto,precio,stock_min,stock_act]


#opcion 3
def Eliminar_producto(productos,precio,stock_min,stock_act):
        
            prod = str(input("\nIngrese el producto a eliminar: ")).lower()
            
            if prod in productos:
            
                while True:

                    pregunte = str(input(f"\n¿Está seguro de eliminar el producto {prod}? S:si o N:no: "))
                
                    if pregunte in ["S", "s"]:

                        indice = productos.index(prod)
                        del productos[indice]
                        del precio[indice]
                        del stock_min[indice]
                        del stock_act[indice]

                        print("\nProducto eliminado con éxito.")
                        break
                        

                    elif pregunte in ["N", "n"]:

                        print("\nSe canceló la eliminación del producto.")
                        break

                    else:
                        print("\nOpción inválida.")
            else:
                print("\nEl producto no existe en la lista.\n\nVolviendo al menú principal.")


#opcion 4
def Modificar_producto(productos,precio,stock_min,stock_act):
    
    prod=str(input("\nIngrese el producto que desea modificar: ")).lower()
    
    if prod in productos:
        
        indice = productos.index(prod)
        
        print("""\n\t1. Modificar precio. \n\t2. Modificar stock minimo. \n\t3. Modificar Stock Actual. \n\t4. Modificar lod tres. \n\t5.Modificar todos los datos. \n""")
        
        eleccion=int(input("Ingrese la opción que desee: "))
        
        while eleccion!=[1,2,3,4,5]:
            
            if eleccion==1:

                monto=float(input("\nIngrese el nuevo monto: "))
                
                precio[indice]=monto
                
                print("\n El Precio fue modificado con éxito.")
                break
            
            elif eleccion==2:
            
                stk_min=int(input("\nIngrese el stock minimo: "))
                
                stock_min[indice]=stk_min
                
                print("\n El stock minimo fue modificado con éxito.")
                break
            
            elif eleccion==3:
            
                stk_act=int(input("\nIngrese el nuevo stock disponible: "))
                
                stock_act[indice]=stk_act
                
                print("\n El stock disponible fue modificado con éxito.")
                break
            
            elif eleccion==4:

                monto=float(input("\nIngrese el nuevo monto: "))
                stk_min=int(input("\nIngrese el stock minimo: "))
                stk_act=int(input("\nIngrese el nuevo stock disponible: "))
                
                precio[indice]=monto
                stock_min[indice]=stk_min
                stock_act[indice]=stk_act
                
                print("\n El precio , el stock actual y  minimo fueron modificados con éxito.")
                break

            elif eleccion==5:
            
                Nom_prod=str(input("\nIngrese el nuevo nombre del producto: "))
                monto=float(input("\nIngrese el nuevo monto: "))
                stk_min=int(input("\nIngrese el stock minimo: "))
                stk_act=int(input("\nIngrese el nuevo stock disponible: "))

                productos[indice]=Nom_prod
                precio[indice]=monto
                stock_min[indice]=stk_min
                stock_act[indice]=stk_act
                
                print("\n El producto fue modificado con éxito.")
                break
            
            else:
            
                print("\n Opción inválida.")
    
    else:
    
        print("\nNo existe el producto")


#opcion 5
def Buscar_producto(productos,precio,stock_min,stock_act):
    opcion=True
    
    while opcion==True:
        
        serch_product=input("\nIngrese el producto que desea buscar: ").lower()
        
        if serch_product in productos:
        
            prod=productos.index(serch_product)
            print("\n El Producto encontrado es: ", productos[prod])
            print("\n El Precio del producto es: $", precio[prod])
            print("\n El Stock minimo del producto es: ", stock_min[prod])
            print("\n El Stock Actual del producto es: ", stock_act[prod])
        
        else:
        
            print("\n El producto no existe")
        
        consulta=input("\n¿Desea buscar otro producto? S:si o N:no : ")

        if consulta in ["N","n"]:
            opcion=False


#opcion 6
def Bajo_stk(productos,precio,stock_min,stock_act):
    
    for prod in productos:
        
        indice = productos.index(prod)
        alerta=stock_act[indice]-stock_min[indice]
        
        if alerta>10:
            continue
        
        else:
            print(f"\nProducto:{productos[indice]}\nPrecio:${precio[indice]}\nDisponible:{stock_act[indice]}\nStock Minimo:{stock_min[indice]}\n")