import os
import re

MENU="""
    1.- ver todos los Productos
    2.- Agregar Productos
    3.- Editar Productos
    4.- Sacar Cuenta
    5.- Historial de Pagos
    6.- Salir
"""

productos=[]

def pause_cls(): # pausa hasta tocar un tecla y borra toda lo que esta en consola
    os.system("pause")      # esto funciona si trabajas py en la terminal de windows
    os.system("cls")

#terminar la funcion mañana
def Ver_Productos():
    a_productos=open('Productos_/producto_info.txt','r')
    informacion_a_p=a_productos.read()
    a_P=re.split(r'\n',informacion_a_p)
    for i in a_P:
        print(re.split(r',',i))
        #productos.append(i)

    # if len(productos) == len(precios):
    #     print("listas de productos y precios iguales :)\n\n")
    #     print(f"productos -> {len(productos)}")
    #     print(f"precios -> {len(precios)}")
    #     pause_cls()
    # print("\tPRODC.\tPRECIO")
    # for produc,precio in zip(productos,precios): #obtenemos los valores en cada iteración de las listas
    #     print(f"1.-\t{produc}\t{precio}")
    pause_cls()


if __name__=="__main__":
    pause_cls()
    opc_menu=0
    # doble bucle para 
    # el 1° para que el MENU nuca se cierre, ya que la tienda esta abierta 12/7 Hrs
    # el 2° para validar q no se ingrese letras
    while (True):  
        opc_valida=True
        while(opc_valida):
            # se valida si se ingresa un numero
            try:
                print(MENU) 
                opc_menu = int(input("\t - elige una opcion : "))
            except:
                print("\n\n__________________________________________________________")
                print("Alparecer ingreso letras ...\nPorfavor intente de nuevo.\nIngrese del 1-5\n\n\t . . . ")
                pause_cls()
            else:
                opc_valida=False
        # seleciona del 1-5
        if(opc_menu==1):
            Ver_Productos()
        elif(opc_menu==2):
            print("Agregar")
        elif(opc_menu==3):
            print("Editar Productos")
        elif(opc_menu==4):
            print("Sacar Cuenta")
        elif(opc_menu==5):
            print("Historial de Pago")
        elif(opc_menu==6):
            break
        else:
            print("la opc. no existe")
