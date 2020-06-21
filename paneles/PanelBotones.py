from tkinter import *
from tkinter import ttk
from modelo.figuras.Cuadrilatero import Cuadrilatero
from modelo.figuras.Circulo import Circulo
from acciones.ControladorAcciones import ControladorAcciones

class PanelBotones:
        
    def __init__(self, ventana):
        control = ControladorAcciones(ventana)
        
        ttk.Label(ventana.ventana, text='posicion x:').place(x=25,y=20)
        pos_x = ttk.Entry(ventana.ventana, width=10)
        pos_x.place(x=25,y=45)
        
        ttk.Label(ventana.ventana, text='posicion y:').place(x=25,y=70)
        pos_y = ttk.Entry(ventana.ventana, width=10)
        pos_y.place(x=25,y=95)
        
        ttk.Label(ventana.ventana, text='grosor:').place(x=25,y=120)
        grosor = ttk.Entry(ventana.ventana, width=10)
        grosor.place(x=25,y=145)
        
        ttk.Label(ventana.ventana, text='color:').place(x=25,y=170)
        color = ttk.Entry(ventana.ventana, width=10)
        color.place(x=25,y=195)
        
        ttk.Label(ventana.ventana, text='ancho:').place(x=25,y=220)
        ancho = ttk.Entry(ventana.ventana, width=10)
        ancho.place(x=25,y=245)
        
        ttk.Label(ventana.ventana, text='alto:').place(x=25,y=270)
        alto = ttk.Entry(ventana.ventana, width=10)
        alto.place(x=25,y=295)
        
        ttk.Label(ventana.ventana, text='radio:').place(x=25,y=320)
        radio = ttk.Entry(ventana.ventana, width=10)
        radio.place(x=25,y=345)
        
        'Botones'
        
        btn_exit = ttk.Button(ventana.ventana, text='Salir', command=ventana.ventana.destroy)
        btn_exit.place(x=610,y=320)
        btn_erase = ttk.Button(ventana.ventana, text='Borrar todo', command=control.borrar_todo)
        btn_erase.place(x=525,y=320)
        
        btn_erase_last = ttk.Button(ventana.ventana, text='Borrar último', command=control.borrar_ultimo)
        btn_erase_last.place(x=525,y=360)
        
        btn_c = ttk.Button(ventana.ventana, text='Circulo', command=control.circulo)
        btn_c.place(x=225,y=320)
        
        btn_cuad = ttk.Button(ventana.ventana, text='Cuadrilatero', command=control.cuadrilatero)
        btn_cuad.place(x=125,y=320)
        
        btn_cuad = ttk.Button(ventana.ventana, text='Crear', command = lambda: control.asignar_cuad(pos_x.get(),pos_y.get(),grosor.get(),color.get(),alto.get(),ancho.get()))
        btn_cuad.place(x=125,y=360)
        
        btn_circ = ttk.Button(ventana.ventana, text='Crear', command = lambda: control.asignar_circ(pos_x.get(),pos_y.get(),grosor.get(),color.get(),radio.get()))
        btn_circ.place(x=225,y=360)
        
        btn_lin = ttk.Button(ventana.ventana, text='Linea', command=control.linea)
        btn_lin.place(x=325,y=320)
        
        btn_linc = ttk.Button(ventana.ventana, text='Crear', command = lambda: control.asignar_lin(in_x.get(),in_y.get(),fi_x.get(),fi_y.get(),color_i.get()))
        btn_linc.place(x=325,y=360)
        
        btn_arc = ttk.Button(ventana.ventana, text='Arco', command=control.arco)
        btn_arc.place(x=425,y=320)
        
        btn_arcc = ttk.Button(ventana.ventana, text='Crear', command = lambda: control.asignar_lin(in_x.get(),in_y.get(),fi_x.get(),fi_y.get(),color_i.get()))
        btn_arcc.place(x=425,y=360)
        
        'Líneas y arcos'
        
        ttk.Label(ventana.ventana, text='inicial x:').place(x=575,y=20)
        in_x = ttk.Entry(ventana.ventana, width=10)
        in_x.place(x=575,y=45)
        
        ttk.Label(ventana.ventana, text='inicial y:').place(x=575,y=70)
        in_y = ttk.Entry(ventana.ventana, width=10)
        in_y.place(x=575,y=95)
        
        ttk.Label(ventana.ventana, text='final x:').place(x=575,y=120)
        fi_x = ttk.Entry(ventana.ventana, width=10)
        fi_x.place(x=575,y=145)
        
        ttk.Label(ventana.ventana, text='final y:').place(x=575,y=170)
        fi_y = ttk.Entry(ventana.ventana, width=10)
        fi_y.place(x=575,y=195)
        
        ttk.Label(ventana.ventana, text='color:').place(x=575,y=220)
        color_i = ttk.Entry(ventana.ventana, width=10)
        color_i.place(x=575,y=245)
        