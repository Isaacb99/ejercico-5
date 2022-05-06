import csv
from plan import planAhorro

class manejador:
    __lista =[]
    def __init__(self):
            self.__lista = []
    def cargaArchi(self):
        archivo = open("planes.csv")
        reader = csv.reader(archivo,delimiter=';')
        for comp in reader:
            nuevo = planAhorro(int(comp[0]), comp[1], comp[2], int(comp[3]))
            self.__lista.append(nuevo)
        archivo.close
    def imprimir(self):
        for i in range(len(self.__lista)):
            print("{}".format(self.__lista[i]))
    def actualizar(self):
        for i in range(len(self.__lista)):
            print("{}   {}   {}".format(self.__lista[i].get_codigo(), self.__lista[i].get_modelo(), self.__lista[i].get_version()))
            s = int(input("ingresar nuevo valor de vehiculo"))
            self.__lista[i].actualizar_valor(s)
    def valor(self):
        v = float(input("ingrese valor a buscar"))
        for i in range(len(self.__lista)):
            valor = float(self.__lista[i].valor_cuota())
            if valor < v:
                print("{}   {}   {}".format(self.__lista[i].get_codigo(), self.__lista[i].get_modelo(), self.__lista[i].get_version()))
    def licitar(self):
        for i in range(len(self.__lista)):
            print("monto para licitar el vehiculo:{}{} = {}".format(self.__lista[i].get_modelo(), self.__lista[i].get_version(),self.__lista[i].lici()))
    def modificar(self):
        c = int(input("ingrese codigo de plan a modificar"))
        for i in range(len(self.__lista)):
            if c == self.__lista[i].get_codigo():
                v = i
        m = int(input("ingrese la nueva cantidad de cuotas para licitar"))
        planAhorro.cuotas_licitacion = m