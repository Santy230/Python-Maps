from google import lugares_cerca
from os import system

def limpiarPantalla():  #LIMPIA LA CONSOLA
    system('cls')


def Comida():   #MENU COMIDAS
    limpiarPantalla()
    print("-------------MENU QUE COMO---------------")
    opc = input(f"1)Pedir Comida\n"
                "2)Cocinar\n"
                "3)Volver\n"
                "4)salir\n"
                "-----------------------------------------\n ")
    if int(opc)==1:
        limpiarPantalla()
        lugares_cerca()
    if int(opc)==2:
        pass
        #def recipes:
    if int(opc)==3:
        pass
    if int(opc)==4:
        exit()


Comida()