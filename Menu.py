from Cama import Cama
from Medicamento import Medicamento

class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.test,
            '4':self.salir
        }
    def lanzarMenu(self,manejadorCama,manejadorMedicamento):
        #Menu opciones
        i=str(len(self.__opciones))
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1 para dar alta a un paciente.')
            print('-Ingrese 2 para listar datos de pacientes con diagnostico.')
            print('-Ingrese 3 para ejecutar test.')
            print('-Ingrese 4 para salir.')
            opcion=input('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion=='1' or opcion=='3':
                ejecutar(manejadorCama,manejadorMedicamento)
            elif opcion=='2':
                ejecutar(manejadorCama)
            else:
                ejecutar()
    def opcion1(self,manejadorCama,manejadorMedicamento):
        nombre=input('Ingrese nombre y apellido paciente:\n')
        manejadorCama.darAltaPaciente(nombre,manejadorMedicamento)
    def opcion2(self,manejadorCama):
        diagnostico=input('Ingrese diagnostico:\n')
        manejadorCama.mostrarPacientesDiagnostico(diagnostico)
    def test(self,manejadorCama,manejadorMedicamento):
        manejadorMedicamento.test()
        manejadorCama.test(manejadorMedicamento)
        cama=Cama()
        medicamento=Medicamento()
        cama.test()
        medicamento.test()
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')