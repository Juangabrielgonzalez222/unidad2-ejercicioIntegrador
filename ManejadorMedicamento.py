import csv

from Medicamento import Medicamento

class ManejadorMedicamento:
    __listaMedicamentos=[]
    def __init__(self):
        self.__listaMedicamentos=[]
    def agregarMedicamento(self,medicamento):
        if type(medicamento)==Medicamento:
            self.__listaMedicamentos.append(medicamento)
        else:
            print('Error, no se pudo agregar un medicamento a la lista, el tipo de datos es incorrecto.')
    def cargarDesdeArchivo(self):
        nombreArchivo='medicamentos.csv'
        archivo=open(nombreArchivo)
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                self.agregarMedicamento(Medicamento(int(fila[0]),int(fila[1]),fila[2],fila[3],fila[4],int(fila[5]),float(fila[6])))
        archivo.close()
        print('Fin de la carga desde: ',nombreArchivo)
    def mostrarDeudaPaciente(self,numeroCama):
        print('{:30} {:^15} {:^10} {:^10}'.format('Medicamento/monodroga','Presentacion','Cantidad','Precio'))
        acumularPrecioFinal=0
        for medicamento in self.__listaMedicamentos:
            if medicamento.verificarCama(numeroCama):
                print('{:30} {:^15} {:^10d} {:^10}'.format(medicamento.getNombre()+'/'+medicamento.getMonodroga(),medicamento.getPresentacion(),medicamento.getCantidad(),medicamento.getPrecio()))
                acumularPrecioFinal+=medicamento.calcularPrecioTotal()
        print('Total adeudado:{:41} {:^10} '.format('',acumularPrecioFinal))
    def test(self):
        print('Comienza test ManejadorMedicamento')
        manejador=ManejadorMedicamento()
        manejador.cargarDesdeArchivo()
        manejador.agregarMedicamento(Medicamento(2,5,'Pentotal','Penicilina','ampolla 20ml',4,2750.0))
        manejador.mostrarDeudaPaciente(2)
        print('Fin test ManejadorMedicamento. \n')