import abc
from abc import ABCMeta

class FiguraL(object):
    __metaclass__ = ABCMeta
    def __init__(self, posix, posiy, posfx, posfy, color):
        self.posIX = posix
        self.posIY = posiy
        self.posFX = posfx
        self.posFY = posfy    
        self.color = color

    @abc.abstractmethod
    def calcularLongitud(self):
        pass

    @abc.abstractmethod
    def dibujar(self, lienzo):
        pass
    
    @abc.abstractmethod
    def eliminar(self, lienzo):
        pass