from tkinter import *
from tkinter import ttk
from modelo.figuras.Cuadrilatero import Cuadrilatero
from modelo.figuras.Circulo import Circulo
from modelo.figuras.Linea import Linea
from modelo.figuras.Arco import Arco


'''
Circulo : posx, posy, grosor, color, radio
Rectángulo : posx, posy, grosor, color, ancho, alto
Linea: inicial_x, inicial_y , final_x, final_y, color
Arco: inicial_x, inicial_y , final_x, final_y, color     
'''


class ControladorAcciones:
    def __init__(self,ventana):
        self.ventana = ventana 
        self.list = []
        
    def asignar_lin(self,ix,iy,fx,fy,col):
        self.ix = float(ix)
        self.iy = float(iy)
        self.fx = float(fx)
        self.fy = float(fy)
        self.col = col
        print("Línea creada")
        
    def asignar_cuad(self,x,y,g,col,h,w):
        self.x = float(x)
        self.y = float(y)
        self.g = float(g)
        self.col = col
        self.h = float(h)
        self.w = float(w)
        print("Cuadrilátero creado")
        
    def asignar_circ(self,x,y,g,col,r):
        self.x = float(x)
        self.y = float(y)
        self.g = float(g)
        self.col = col
        self.r = float(r)
        print("Círculo creado")
        
    def linea(self):
        self.lin = Linea(self.ix,self.iy,self.fx,self.fy,self.col)
        print("creado")
        self.list.append(self.lin)
        self.lin.dibujar(self.ventana.canvas)
        
    def arco(self):
        self.arc = Arco(self.ix,self.iy,self.fx,self.fy,self.col)
        print("creado")
        self.list.append(self.arc)
        self.arc.dibujar(self.ventana.canvas)
        
    
    def circulo(self):
        self.circ = Circulo(self.x,self.y,self.g,self.col,self.r)
        print("creado")  
        self.list.append(self.circ)
        self.circ.dibujar(self.ventana.canvas)
        
    def cuadrilatero(self):
        self.c = Cuadrilatero(self.x,self.y,self.g,self.col,self.h,self.w)
        print(type(self.c))
        self.list.append(self.c)
        print("creado")
        self.c.dibujar(self.ventana.canvas)
        
    def borrar_todo(self):
        self.ventana.canvas.delete("all")
        self.lista = []
        
    def borrar_ultimo(self):
        if(len(self.list)>0):     
            if(type(self.list[-1])==type(self.c)):
                self.c.eliminar(self.ventana.canvas)
                self.list.pop()
            elif(type(self.list[-1])==type(self.circ)):
                self.circ.eliminar(self.ventana.canvas)
                self.list.pop()
            elif(type(self.list[-1])==type(self.lin)):
                self.lin.eliminar(self.ventana.canvas)
                self.list.pop()
            elif(type(self.list[-1])==type(self.arc)):
                self.arc.eliminar(self.ventana.canvas)
                self.list.pop()
            print("objeto eliminado")
        