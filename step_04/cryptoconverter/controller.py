from cryptoconverter.view import CriptoVista
from cryptoconverter.model import ParCriptos, ErrorConsulta

class CriptoController:
    def __init__(self):
        self.vista = CriptoVista()
        self.model = None

    def execute(self):
        self.vista.intro()
        self.model = ParCriptos(self.vista.criptoDe, self.vista.criptoA)
        try:
            tasa = self.model.valor(self.vista.cantidad)
            self.vista.mostrar(tasa)
        except ErrorConsulta as e:
            vista.error(e)