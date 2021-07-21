from Encomienda import Encomienda


class EncomiendaServicio:

    def agregar_encomienda(self,enc:Encomienda) -> None:
        enc.destino = input("Ingrese el destino")
        enc.alto = int(input("ingrese alto"))
        enc.ancho = int(input("ingrese ancho"))
        enc.largo = int(input("ingrese largo"))

    def calcular(self,enc) -> int:
        return enc.alto * enc.ancho * enc.largo

    def mostrar(self,enc) -> None:
        print("destino:{} alto:{}".format(enc.destino,enc.alto))



    def calculo_completo(self) -> int:
        # todo: falta implementar el codigo (to do tareas por hacer)
        pass
