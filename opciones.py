#menu
def menu ():
    print("""
    \n\t********************** \n\t Menu de opciones \n\t**********************\n
    1.Consulta Lista de productos.
    2.Agregar un producto.
    3.Eliminar producto.
    4.Modificar producto.
    5.Buscar producto.
    9.Salir del programa.\n
    """)


#opcion 1
def Mostrar_productos(prod,precio):
    
    producto=""
    pos=0
    numero=1
    
    print("\n\tProducto | Precio")
    
    for producto in prod:

        
        print(f"\t{numero}.{producto} : ${precio[pos]}")
        pos+=1
        numero+=1
    
    if producto=="":
    
        print("\nNo hay productos disponibles. ")


#opcion 2
def Agregar_producto():

        producto=str(input("\nIngrese un nuevo producto: ")).lower()
        precio=float(input("\nIngrese el precio del producto: "))
        stock_min=int(input("\nAgregue el STOCK minimo que manejara este producto: "))
        return[producto,precio,stock_min]


#opcion 3
def Eliminar_producto(productos,precio,stock_min):
        
            prod = str(input("\nIngrese el producto a eliminar: ")).lower()
            
            if prod in productos:
            
                while True:

                    pregunte = str(input(f"\n¿Está seguro de eliminar el producto {prod}? S:si o N:no: "))
                
                    if pregunte in ["S", "s"]:

                        indice = productos.index(prod)
                        del productos[indice]
                        del precio[indice]
                        del stock_min[indice]

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
def Modificar_producto(productos,precio,stock_min):
    
    prod=str(input("\nIngrese el producto que desea modificar: ")).lower()
    
    if prod in productos:
        
        indice = productos.index(prod)
        
        print("""\n\t1. Modificar precio. \n\t2. Modificar stock minimo. \n\t3. Modificar ambos. \n\t4. Modificar todos los datos.\n""")
        
        eleccion=int(input("Ingrese la opción que desee: "))
        
        while eleccion!=[1,2,3,4]:
            
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
            
                monto=float(input("\nIngrese el nuevo monto: "))
                stk_min=int(input("\nIngrese el stock minimo: "))
                precio[indice]=monto
                stock_min[indice]=stk_min
                print("\n El precio y el stock minimo fueron modificados con éxito.")
                break
            
            elif eleccion==4:
            
                Nom_prod=str(input("\nIngrese el nuevo nombre del producto: "))
                monto=float(input("\nIngrese el nuevo monto: "))
                stk_min=int(input("\nIngrese el stock minimo: "))
                productos[indice]=Nom_prod
                precio[indice]=monto
                stock_min[indice]=stk_min
                print("\n El producto fue modificado con éxito.")
                break
            
            else:
            
                print("\n Opción inválida.")
    
    else:
    
        print("\nNo existe el producto")


#opcion 5
def Buscar_producto(productos,precio,stock_min):
    opcion=True
    
    while opcion==True:
        
        serch_product=input("\nIngrese el producto que desea buscar: ").lower()
        
        if serch_product in productos:
        
            prod=productos.index(serch_product)
            print("\n El producto encontrado es: ", productos[prod])
            print("\n El precio del producto es: $", precio[prod])
            print("\n El stock minimo del producto es: ", stock_min[prod])
        
        else:
        
            print("\n El producto no existe")
        
        consulta=input("\n¿Desea buscar otro producto? S:si o N:no : ")

        if consulta in ["N","n"]:
            opcion=False