# queremos ingresar una encomienda

# 1) Definir las clases (defino las propiedades) == tablas
# 2) Definir las funciones
# agregar encomienda.
# calcular el precio de envio.
# 3) UI (no tengo)
# 4) agrupacion
from Encomienda import Encomienda

# OOP Programacion orientada a objecto.  Interface
# SRP Responsabilidad de principio simple.
# KISS Kept it simple stupid
# SOLID = es mas complicado.


enc = Encomienda()

enc.agregar_encomienda()
total = enc.calcular()
enc.mostrar()
print("el destino: ", enc.destino)   # $enc->destino
print("el total es ", total)
