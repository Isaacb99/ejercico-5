from manejadorPlan import manejador
import csv

class menu:
    __op = 0
    def __init__(self, p=None):
        self.__op = p
    def opciones(self):
        l = manejador()
        l.cargaArchi()
        salir = True
        while salir:
            print("/// MENU DE OPCIONES ///")
            print("opcion 1: actualizar el valor del vehiculo")
            print("opcion 2: ingresar un valor y buscar vehiculos con menor valor al ingresado")
            print("opcion 3: mostar el monto para licitar el vehiculo")
            print("opcion 4: ingresar codigo de plan y modificar la cantidad de cuotas de licitacion")
            print("opcion 5: salir del programa")
            self.__op = int(input("INGRESE OPCION"))
            if self.__op == 1:
                l.actualizar()
            elif self.__op == 2:
                l.valor()
            elif self.__op == 3:
                l.licitar()
            elif self.__op == 4:
                l.imprimir()
                l.modificar()
            else:
                salir = not salir