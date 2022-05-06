import csv,numpy as np

from Cama import Cama

class ManejadorCama:
    __dimension=0
    __cantidad=0
    __incremento=0
    __camas=None
    def __init__(self,dimension=3,incremento=5):
        self.__camas=np.empty(dimension,dtype=Cama)
        self.__incremento=incremento
        self.__dimension=dimension
        self.__cantidad=0
    def agregarCama(self,cama):
        if type(cama)==Cama:
            if self.__cantidad==self.__dimension:
                self.__dimension+=self.__incremento
                self.__camas.resize(self.__dimension)
            self.__camas[self.__cantidad]=cama
            self.__cantidad+=1
        else:
            print('Error, no se pudo agregar una cama al arreglo, el tipo de datos es incorrecto.')
    def cargarDesdeArchivo(self):
        nombreArchivo='camas.csv'
        archivo=open(nombreArchivo)
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                self.agregarCama(Cama(int(fila[0]),int(fila[1]),bool(fila[2]),fila[3],fila[4],fila[5],fila[6]))
        archivo.close()
        print('Fin de la carga desde: ',nombreArchivo)
    def buscarPaciente(self,nombre):
        resultado=-1
        bandera=True
        i=0
        while i<self.__cantidad and bandera:
            if self.__camas[i].comprobarNombre(nombre):
                bandera=not bandera
                resultado=i
            else:
                i+=1
        return resultado
    def darAltaPaciente(self,nombre,manejadorMedicamento):
        iPaciente=self.buscarPaciente(nombre)
        if iPaciente!=-1:
            print('Ingrese a continuacion fecha del alta:')
            dia=input('Ingrese dia:\n')
            mes=input('Ingrese mes:\n')
            año=input('Ingrese año:\n')
            fecha='{}/{}/{}'.format(dia,mes,año)
            self.__camas[iPaciente].establecerFechaAlta(fecha)
            print('Paciente:{}        Cama:{:5}        Habitacion:{}'.format(self.__camas[iPaciente].getNombre(),self.__camas[iPaciente].getIdCama(),self.__camas[iPaciente].getHabitacion()))
            print('Diagnostico:{}                fecha de Internacion:{}'.format(self.__camas[iPaciente].getDiagnostico(),self.__camas[iPaciente].getFechaInternacion()))
            print('Fecha de alta:{}'.format(self.__camas[iPaciente].getFechaAlta()))
            manejadorMedicamento.mostrarDeudaPaciente(self.__camas[iPaciente].getIdCama())
            self.__camas[iPaciente].darAlta()
        else:
            print('No se encontro el paciente')
    def mostrarPacientesDiagnostico(self,diagnostico):
        for i in range(self.__cantidad):
            if self.__camas[i].getEstado():
                if self.__camas[i].getDiagnostico()==diagnostico:
                    print(self.__camas[i])
    def test(self,manejadorMedicamento):
        print('Comienza test ManejadorCama')
        manejador=ManejadorCama()
        manejador.cargarDesdeArchivo()
        manejador.agregarCama(Cama(7,150,True,'Fernandez, Emiliano','Apendicitis','27/04/2020',None))
        print(manejador.buscarPaciente('Fernandez, Emiliano'))
        manejador.mostrarPacientesDiagnostico('Apendicitis')
        manejador.darAltaPaciente('Perez, Luis',manejadorMedicamento)
        print('Fin test ManejadorCama. \n')