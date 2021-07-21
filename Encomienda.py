class Encomienda:
    destino: str
    alto: int
    ancho: int  # type hinting
    largo: int

    def agregar_encomienda(self) -> None:
        self.destino = input("Ingrese el destino")
        self.alto = int(input("ingrese alto"))
        self.ancho = int(input("ingrese ancho"))
        self.largo = int(input("ingrese largo"))

    def calcular(self) -> int:
        return self.alto * self.ancho * self.largo

    def mostrar(self) -> None:
        print("destino:{} alto:{}".format(self.destino,self.alto))



    def calculo_completo(self) -> int:
        # todo: falta implementar el codigo (to do tareas por hacer)
        pass
