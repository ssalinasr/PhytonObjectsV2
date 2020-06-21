from graficos.Ventana import Ventana
from modelo.figuras.Cuadrilatero import Cuadrilatero
from modelo.figuras.Circulo import Circulo
from paneles.PanelBotones import PanelBotones
global ventana

if __name__ == '__main__':
    ventana = Ventana('MiniPaint')
    botones = PanelBotones(ventana)
    ventana.ventana.mainloop()


