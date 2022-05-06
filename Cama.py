class Cama:
    __idCama=0
    __habitación=0
    __estado=False
    __nombreApellido=None
    __diagnostico=''
    __fechaInternacion=''
    __fechaAlta=None
    def __init__(self,idCama=0,habitación=0,estado=False,nombreApellido=None,diagnostico='',fechaInternacion='',fechaAlta=None):
        self.__idCama=idCama
        self.__habitación=habitación
        self.__estado=estado
        self.__nombreApellido=nombreApellido
        self.__diagnostico=diagnostico
        self.__fechaInternacion=fechaInternacion
        self.__fechaAlta=fechaAlta
    def getNombre(self):
        return self.__nombreApellido
    def getEstado(self):
        return self.__estado
    def getIdCama(self):
        return self.__idCama
    def getHabitacion(self):
        return self.__habitación
    def getDiagnostico(self):
        return self.__diagnostico
    def getFechaAlta(self):
        return self.__fechaAlta
    def getFechaInternacion(self):
        return self.__fechaInternacion
    def comprobarNombre(self,nombre):
        return self.__nombreApellido==nombre
    def establecerFechaAlta(self,alta):
        self.__fechaAlta=alta
    def darAlta(self):
        self.__estado=not self.__estado
        self.__nombreApellido=None
        self.__diagnostico=''
        self.__fechaInternacion=''
    def __str__(self):
        return 'Nombre y apellido:{}, Diagnostico:{}, Fecha de Internacion:{}'.format(self.__nombreApellido,self.__diagnostico,self.__fechaInternacion)
    def test(self):
        print('Comienza test Cama')
        cama=Cama(7,150,True,'Fernandez, Emiliano','Hepatitis','27/04/2020',None)
        print(cama.comprobarNombre('Fernandez, Emiliano'))
        cama.establecerFechaAlta('30/05/2020')
        print('Nombre:{}, Estado:{}, Id:{}, Diagnostico:{}, Habitacion:{}, FechaAlta:{}, FechaInternacion:{} '.format(cama.getNombre(),cama.getEstado(),cama.getIdCama(),cama.getDiagnostico(),cama.getHabitacion(),cama.getFechaAlta(),cama.getFechaInternacion()))
        print(cama)
        cama.darAlta()
        print('Fin test Cama. \n')