# queremos ingresar una encomienda

# 1) Definir las clases (defino las propiedades) == tablas
# 2) Definir las funciones
# agregar encomienda.
# calcular el precio de envio.
# 3) UI (no tengo)
# 4) agrupacion
from Encomienda import Encomienda
from EncomiendaServicio import EncomiendaServicio

# OOP Programacion orientada a objecto.  Interface
# SRP Responsabilidad de principio simple.
# KISS Kept it simple stupid
# SOLID = es mas complicado.


enc = Encomienda()  # propiedades (modelo)
enc_s = EncomiendaServicio()  # solo funciones (servicio).

enc_s.agregar_encomienda(enc)
total = enc_s.calcular(enc)
enc_s.mostrar(enc)
print("el destino: ", enc.destino)   # $enc->destino
print("el total es ", total)
