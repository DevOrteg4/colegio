class Fecha():
    def __init__(self,dia,mes,anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio
    
    def mostrarFecha(self):
        return str(self.dia)+"/"+str(self.mes)+"/"+str(self.anio)