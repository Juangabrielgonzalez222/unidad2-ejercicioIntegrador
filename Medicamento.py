class Medicamento:
    __idCama=0
    __idMedicamento=0
    __nombreComercial='',
    __monodroga='' 
    __presentacion=''
    __cantidadAplicada=0
    __precioTotal=0.0
    def __init__(self,idCama=0,idMedicamento=0,nombreComercial='',monodroga='' ,presentacion='',cantidadAplicada=0,precioTotal=0.0):
        self.__idCama=idCama
        self.__idMedicamento=idMedicamento
        self.__nombreComercial=nombreComercial
        self.__monodroga=monodroga
        self.__presentacion=presentacion
        self.__cantidadAplicada=cantidadAplicada
        self.__precioTotal=precioTotal
    def getNombre(self):
        return self.__nombreComercial
    def getMonodroga(self):
        return self.__monodroga
    def getPresentacion(self):
        return self.__presentacion
    def getCantidad(self):
        return self.__cantidadAplicada
    def getPrecio(self):
        return self.__precioTotal
    def verificarCama(self,numero):
        return self.__idCama==numero
    def calcularPrecioTotal(self):
        return self.__cantidadAplicada*self.__precioTotal
    def test(self):
        print('Comienza test Medicamento')
        medicamento=Medicamento(2,5,'Pentotal','Penicilina','ampolla 20ml',4,2750.0)
        print('Nombre:{}, Monodrogra:{}, Presentacion:{}, Cantidad:{}, Precio:{}'.format(medicamento.getNombre(),medicamento.getMonodroga(),medicamento.getPresentacion(),medicamento.getCantidad(),medicamento.getPrecio()))
        print(medicamento.verificarCama(2))
        print(medicamento.calcularPrecioTotal())
        print('Fin test Medicamento. \n')