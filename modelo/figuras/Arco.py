from modelo.figuras.FiguraL import FiguraL
import math


class Arco(FiguraL):
    def dibujar(self, lienzo):
        self.arc = lienzo.create_arc(self.posIX,self.posIY,self.posFX,self.posFY,fill=self.color)
        
    def __init__(self,posix,posiy,posfx,posfy,color):
        FiguraL.__init__(self,posix,posiy,posfx,posfy,color)

    def calcularLongitud(self):
        return (math.tan((self.posfx-self.posix))/180)*math.pi
    
    def eliminar(self,lienzo):
        lienzo.delete(self.arc)