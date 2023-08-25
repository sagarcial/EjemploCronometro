from unidad_tiempo import UnidadTiempo

class minuto(UnidadTiempo):
    def __init__(self):
        super().__init__()
        self.valor = 0
        self.tope=60