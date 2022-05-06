

class planAhorro:
    __codigo = 0
    __modelo = ''
    __version_veh = ''
    __valor_vehiculo = 0
    cant_cuotas = 60
    cuotas_licitacion = 10
    def __init__(self, c, m, ver, v):
        self.__codigo = c
        self.__modelo = m
        self.__version_veh = ver
        self.__valor_vehiculo = v
    def __str__(self):
        return "Codigo: %d, Modelo: %s, Version de vehiculo: %s, Valor de vehiculo: %d, Cantidad de cuotas: %d, Cuotas para licitar: %d" % (self.__codigo, self.__modelo, self.__version_veh, self.__valor_vehiculo, self.get_cantCuotas(), self.get_cuotasLic())
    def get_codigo(self):
        return self.__codigo
    def get_modelo(self):
        return self.__modelo
    def get_version(self):
        return self.__version_veh
    @classmethod
    def get_cantCuotas(cls):
        return cls.cant_cuotas
    @classmethod
    def get_cuotasLic(cls):
        return cls.cuotas_licitacion
    def actualizar_valor(self,v):
        self.__valor_vehiculo = v
    def valor_cuota(self):
        return ((self.__valor_vehiculo/self.get_cantCuotas()) + (self.__valor_vehiculo * 0.10))
    def lici(self):
        return (self.get_cuotasLic() * self.__valor_vehiculo)
    