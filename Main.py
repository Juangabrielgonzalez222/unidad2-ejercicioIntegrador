from ManejadorCama import ManejadorCama
from ManejadorMedicamento import ManejadorMedicamento
from Menu import Menu


if __name__== '__main__':
    manejadorCama=ManejadorCama()
    manejadorMedicamento=ManejadorMedicamento()
    manejadorCama.cargarDesdeArchivo()
    manejadorMedicamento.cargarDesdeArchivo()
    menu=Menu()
    menu.lanzarMenu(manejadorCama,manejadorMedicamento)
