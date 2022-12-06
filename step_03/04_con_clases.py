from cryptoconverter.model import ParCriptos, ErrorConsulta
from cryptoconverter.view04 import CriptoVista

vista = CriptoVista()
vista.intro()

par = ParCriptos(vista.criptoDe, vista.criptoA)
try:
    tasa = par.valor(vista.cantidad)
    vista.mostrar(tasa)
except ErrorConsulta as e:
    vista.error(e)
