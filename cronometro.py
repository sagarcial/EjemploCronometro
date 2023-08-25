from hora import hora
from segundo import segundo
from minuto import minuto

class Cronometro():
    def __init__(self):
        self.hora = hora()
        self.minuto = minuto()
        self.segundo = segundo()
    def avanzar(self):
        self.segundo.avanzar()
        if self.segundo.valor ==0:
            self.minuto.avanzar()
            if self.minuto.valor ==0:
             self.hora.avanzar()