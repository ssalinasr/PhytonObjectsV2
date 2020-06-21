from modelo.figuras.FiguraL import FiguraL
import math


class Linea(FiguraL):
    def dibujar(self, lienzo):
        self.line = lienzo.create_line(self.posIX,self.posIY,self.posFX,self.posFY,fill=self.color)

    def __init__(self,posix,posiy,posfx,posfy,color):
        FiguraL.__init__(self,posix,posiy,posfx,posfy,color)

    def calcularLongitud(self):
        return math.sqrt(((self.posfx-self.posix)**2)+((self.posfy-self.posiy)**2))

    def eliminar(self,lienzo):
        lienzo.delete(self.line)