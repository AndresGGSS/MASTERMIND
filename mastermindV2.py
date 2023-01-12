
from cgitb import text
from doctest import master
from tkinter import*
import tkinter as tk
import tkinter
import tkinter.messagebox
import random
import pickle
from datetime import datetime
from wsgiref.validate import validator
from fpdf import FPDF
import webbrowser


colors = ["blue","red","yellow","green","saddle brown","orange"]
letters = ["A","B","C","D","E","F"]
numbers = [1,2,3,4,5,6]
simbols = ["*","+","/","-",">","<"]
def validate_spaces(lista):
    """
    It returns True if all the elements in the list are non-empty lists, and False otherwise
    
    :param lista: list of lists of strings
    :return: a boolean value.
    """
    for elementos in lista:
        if elementos == []:
            return False
    return True
def validate_list(lista):
    """
    It returns True if all the elements in the list are integers, and False otherwise
    
    :param lista: a list of numbers
    :return: True or False
    """
    for numeros in lista:
        if type(numeros) != int:
            return False
    return True
# > This class creates a window that displays the game's title and a button that allows the user to
# start the game.
class ventana_principal: #La ventana de incio del juego. 
    
    def __init__(self,master):
        self.master = master
        self.canvas = Canvas(master,width=2000,height=1000,highlightthickness=0, relief='ridge',
                             bg = "#050834")
        self.canvas.place(x=0,y=0) #Tamaño y posición del canvas en el tkinter.

        self.label_titulo = Label(self.canvas, text='MASTERMIND GAME',font=('Games',45), fg='white', bg = "#050834") 
        self.label_titulo.place(x=278,y=50,width=450,height=50) #Titulo de la pantalla.

        self.Button_mostrar1 = Button(self.canvas, text = '¡Jugar!', fg = 'white',
                                    font=('Games',15), command = self.ventana2 , bg = 'lightskyblue', highlightbackground = 'blue', highlightthickness = 30)
        self.Button_mostrar1.place(x=400,y=150,width=200,height=40) #Botón para ir a la pantalla de juego

        self.Button_mostrar2 = Button(self.canvas, text = 'Configurar partida', fg='white',
                                    font=('Games',15), command = self.ventana3, bg = 'lightskyblue', highlightbackground = 'orange', highlightthickness = 30)
        self.Button_mostrar2.place(x=400,y=200,width=200,height=40) #Botón para ir a la pantalla de configurar juego

        self.Button_mostrar2 = Button(self.canvas, text = 'Top 10 resumen', fg='white',
                                    font=('Games',15), command = self.ventana4, bg = 'lightskyblue', highlightbackground = 'red', highlightthickness = 30)
        self.Button_mostrar2.place(x=400,y=250,width=200,height=40) #Botón para ir a la pantalla de top 10 resumen

        self.Button_mostrar2 = Button(self.canvas, text = 'Top 10 detalle', fg='white',
                                    font=('Games',15), command = self.ventana5, bg = 'lightskyblue', highlightbackground = 'green', highlightthickness = 30)
        self.Button_mostrar2.place(x=400,y=300,width=200,height=40) #Botón para ir a la pantalla de top 10 resumen

        self.Button_mostrar2 = Button(self.canvas, text = 'Ayuda', fg='white',
                                    font=('Games',15), command = self.ventana6, bg = 'lightskyblue', highlightbackground = 'saddle brown', highlightthickness = 30)
        self.Button_mostrar2.place(x=400,y=350,width=200,height=40) #Botón para ir a la pantalla de ayuda

        self.Button_mostrar2 = Button(self.canvas, text = 'Acerca de', fg='white',
                                    font=('Games',15), command = self.ventana7, bg = 'lightskyblue',  highlightbackground = 'yellow', highlightthickness = 30)
        self.Button_mostrar2.place(x=400,y=400,width=200,height=40) #Botón para ir a la pantalla de ayuda
        

        self.Button_mostrar2 = Button(self.canvas, text = 'Salir', fg='black',
                                    font=('Games',15), command = self.salir, bg = 'lightskyblue',  highlightbackground = 'white', highlightthickness = 30)
        self.Button_mostrar2.place(x=400,y=450,width=200,height=40) #Botón para ir a la pantalla de ayuda

    def ventana2(self):
        ventana_juego(self.master)#Me genera la ventana de juego.
    
    def ventana3(self):
        ventana_configuracion(self.master)#Me genera la ventana de configuracion del juego

    def ventana4(self):
        ventana_top_10_resumen(self.master)#Me genera la pantalla de top 10 resumen
    
    def ventana5(self):
        ventana_top_10_detalle(self.master)#Me genera la pantalla de top 10 detalle
    
    def ventana6(self):
        path = 'https://www.canva.com/design/DAFQRZIoaoM/HahuzSqGXEClW4KeonqsUw/view?utm_content=DAFQRZIoaoM&utm_campaign=designshare&utm_medium=link&utm_source=publishpresent'
        webbrowser.open_new(path)
    
    def ventana7(self):
        ventana_acerca_de(self.master)#Me genera la pantalla de acerca de
    
    def salir(self):
        self.master.destroy()#Me cierra el juego.

# > This class creates a window for the game.
class ventana_juego:#Ventana de juego.
    def __init__(self, master):
        self.master = master
        self.canvas = Canvas(master,width=1000,height=700,highlightthickness=0, relief='ridge',
                             bg = 'gray25')
        self.canvas.place(x=0,y=0) #Tamaño y posición del canvas.

        #Variables para usar en funciones
        self.lista = [[],[],[],[]]
        self.booleano = False
        self.contador = 0
        self.h = 0
        self.m = 0
        self.s = 0
        self.contador2 = 0
        self.validador = 0
        self.contador3 = 0
        self.jugadas = []
        self.calificadas = []
        self.lista_de_horas = []
        self.contador4 = 0
        self.acumulador1 = 0
        self.acumulador2 = 0
        self.acumulador3 = 0
        self.x = True
        # TENGO QUE GUARDAR ESTO
        self.listatotal = [[],[],[],[]]
        self.lista_copia = [[],[],[],[]]
        self.lista_cont_copia = []
        self.lista_de_contadores = []
        self.indice = 0
        self.sub_indice = 0
        self.indice_copia = 0
        self.sub_indice_copia = 0
        self.grado_dificultad = 0

        self.label_titulo = Label(self.canvas, text='MasterMind',font=('Games',45), fg='red', bg = 'dimgray') 
        self.label_titulo.place(x=278,y=5,width=450,height=50) #Titulo de la pantalla.

        self.label_titulo_jugador = Label(self.canvas, text='Jugador:',font=('Games',15), fg='white', bg = 'gray25') 
        self.label_titulo_jugador.place(x=530,y=620,width=200,height=20) #Titulo de la entrada

        self.inicio_juego = Button(self.canvas, text ='INICIAR JUEGO',font=('Games',15) ,highlightbackground = '#25D55F', highlightthickness = 30, command = self.start)
        self.inicio_juego.place(x = 330, y = 500,width = 350, height = 50) #Iniciar juego

        self.nombre = tkinter.StringVar()
        self.entrada_nombre = Entry(self.canvas, background = 'white', bg = 'white', fg = 'black' , textvariable = self.nombre) #Entrada del nombre del jugador
        self.entrada_nombre.place(x=600,y=650,width=300,height=30)
        self.entrada_nombre.bind("<Leave>",self.validate_name)

    def data(self):
        """
        It loads the data from the file and assigns it to the variables.
        """
        datos = open("mastermind2022configuración.dat","rb")
        self.lista_datos = pickle.load(datos)
        self.dificultad = self.lista_datos[0]
        self.cronometro = self.lista_datos[1]
        self.posicion = self.lista_datos[5]
        self.combinacion = self.lista_datos[6]
        if self.dificultad == 4:
            if self.grado_dificultad == 0:
                self.h1 = self.lista_datos[7][0]
                self.m1 = self.lista_datos[7][1]
                self.s1 = self.lista_datos[7][2]
            elif self.grado_dificultad == 1:
                self.h1 = self.lista_datos[7][3]
                self.m1 = self.lista_datos[7][4]
                self.s1 = self.lista_datos[7][5]
            else:
                self.h1 = self.lista_datos[7][6]
                self.m1 = self.lista_datos[7][7]
                self.s1 = self.lista_datos[7][8]
        else:
            self.h1 = self.lista_datos[2]
            self.m1 = self.lista_datos[3]
            self.s1 = self.lista_datos[4]

    def dificult(self):
        """
        It creates a label with the difficulty level of the game, depending on the value of the variable
        "dificultad" (which is set by the user in the main menu)
        """
        if self.dificultad == 1:
            self.facil = Label(self.canvas, text='NIVEL: Fácil',font=('Games',15), fg='white', bg = 'gray25')
            self.facil.place(x = 10, y = 10,width = 150, height = 50)
            self.validador = 8
        elif self.dificultad == 2:
            self.medio = Label(self.canvas, text='NIVEL: Medio',font=('Games',15), fg='white', bg = 'gray25')
            self.medio.place(x = 10, y = 10,width = 150, height = 50)
            self.validador = 7
        elif self.dificultad == 3:
            self.dificil = Label(self.canvas, text='NIVEL: Dificil',font=('Games',15), fg='white', bg = 'gray25')
            self.dificil.place(x = 10, y = 10,width = 150, height = 50)
            self.validador = 6
        else:
            if self.grado_dificultad == 0:
                self.facil = Label(self.canvas, text='NIVEL: Fácil',font=('Games',15), fg='white', bg = 'gray25')
                self.facil.place(x = 10, y = 10,width = 150, height = 50)
                self.validador = 8
            elif self.grado_dificultad == 1:
                self.medio = Label(self.canvas, text='NIVEL: Medio',font=('Games',15), fg='white', bg = 'gray25')
                self.medio.place(x = 10, y = 10,width = 150, height = 50)
                self.validador = 7
            else:
                self.dificil = Label(self.canvas, text='NIVEL: Dificil',font=('Games',15), fg='white', bg = 'gray25')
                self.dificil.place(x = 10, y = 10,width = 150, height = 50)
                self.validador = 6

    def posiciones(self):
        #DERECHA
        if self.posicion == 1:
            #Colores
            if self.combinacion == 1:
                self.circle1 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle1.create_oval(0,50,50,0, fill = colors[0], outline = "")
                self.circle1.place(x = 850, y = 110)
                self.circle1.bind("<Button-1>",self.drag_start)
                self.circle1.bind("<B1-Motion>",self.drag_motion)
                self.circle1.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle1.bind("<B1-Motion>",self.change_colors_right)

                self.circle2 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle2.create_oval(0,50,50,0, fill = colors[1], outline = "")
                self.circle2.place(x = 850, y = 170)
                self.circle2.bind("<Button-1>",self.drag_start)
                self.circle2.bind("<B1-Motion>",self.drag_motion)
                self.circle2.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle2.bind("<B1-Motion>",self.change_colors_right)

                self.circle3 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle3.create_oval(0,50,50,0, fill = colors[2], outline = "")
                self.circle3.place(x = 850, y = 230)
                self.circle3.bind("<Button-1>",self.drag_start)
                self.circle3.bind("<B1-Motion>",self.drag_motion)
                self.circle3.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle3.bind("<B1-Motion>",self.change_colors_right)

                self.circle4 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle4.create_oval(0,50,50,0, fill = colors[3], outline = "")
                self.circle4.place(x = 850, y = 290)
                self.circle4.bind("<Button-1>",self.drag_start)
                self.circle4.bind("<B1-Motion>",self.drag_motion)
                self.circle4.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle4.bind("<B1-Motion>",self.change_colors_right)

                self.circle5 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle5.create_oval(0,50,50,0, fill = colors[4], outline = "")
                self.circle5.place(x = 850, y = 350)
                self.circle5.bind("<Button-1>",self.drag_start)
                self.circle5.bind("<B1-Motion>",self.drag_motion)
                self.circle5.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle5.bind("<B1-Motion>",self.change_colors_right)

                self.circle6 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle6.create_oval(0,50,50,0, fill = colors[5], outline = "")
                self.circle6.place(x = 850, y = 410)
                self.circle6.bind("<Button-1>",self.drag_start)
                self.circle6.bind("<B1-Motion>",self.drag_motion)
                self.circle6.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle6.bind("<B1-Motion>",self.change_colors_right)
            #Letras
            elif self.combinacion  == 2:
                self.circle1 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle1.create_oval(0,50,50,0, fill = "gray25")
                self.circle1.place(x = 850, y = 110)
                self.circle1_text = tk.Label(self.circle1, text = "A", fg = "white", bg = "gray25")
                self.circle1_text.place(x = 18, y = 15)
                self.circle1.bind("<Button-1>",self.drag_start)
                self.circle1.bind("<B1-Motion>",self.drag_motion)
                self.circle1.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle1.bind("<B1-Motion>",self.change_colors_right)

                self.circle2 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle2.create_oval(0,50,50,0, fill = "gray25")
                self.circle2.place(x = 850, y = 170)
                self.circle2_text = tk.Label(self.circle2, text = "B", fg = "white", bg = "gray25")
                self.circle2_text.place(x = 18, y = 15)
                self.circle2.bind("<Button-1>",self.drag_start)
                self.circle2.bind("<B1-Motion>",self.drag_motion)
                self.circle2.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle2.bind("<B1-Motion>",self.change_colors_right)

                self.circle3 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle3.create_oval(0,50,50,0, fill = "gray25")
                self.circle3.place(x = 850, y = 230)
                self.circle3_text = tk.Label(self.circle3, text = "C", fg = "white", bg = "gray25")
                self.circle3_text.place(x = 18, y = 15)
                self.circle3.bind("<Button-1>",self.drag_start)
                self.circle3.bind("<B1-Motion>",self.drag_motion)
                self.circle3.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle3.bind("<B1-Motion>",self.change_colors_right)

                self.circle4 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle4.create_oval(0,50,50,0, fill = "gray25")
                self.circle4.place(x = 850, y = 290)
                self.circle4_text = tk.Label(self.circle4, text = "D", fg = "white", bg = "gray25")
                self.circle4_text.place(x = 18, y = 15)
                self.circle4.bind("<Button-1>",self.drag_start)
                self.circle4.bind("<B1-Motion>",self.drag_motion)
                self.circle4.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle4.bind("<B1-Motion>",self.change_colors_right)
 
                self.circle5 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle5.create_oval(0,50,50,0, fill = "gray25")
                self.circle5.place(x = 850, y = 350)
                self.circle5_text = tk.Label(self.circle5, text = "E", fg = "white", bg = "gray25")
                self.circle5_text.place(x = 18, y = 15)
                self.circle5.bind("<Button-1>",self.drag_start)
                self.circle5.bind("<B1-Motion>",self.drag_motion)
                self.circle5.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle5.bind("<B1-Motion>",self.change_colors_right)

                self.circle6 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle6.create_oval(0,50,50,0, fill = "gray25")
                self.circle6.place(x = 850, y = 410)
                self.circle6_text = tk.Label(self.circle6, text = "F", fg = "white", bg = "gray25")
                self.circle6_text.place(x = 18, y = 15)
                self.circle6.bind("<Button-1>",self.drag_start)
                self.circle6.bind("<B1-Motion>",self.drag_motion)
                self.circle6.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle6.bind("<B1-Motion>",self.change_colors_right)
            #Numeros
            elif self.combinacion == 3:
                self.circle1 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle1.create_oval(0,50,50,0, fill = "gray25")
                self.circle1.place(x = 850, y = 110)
                self.circle1_text = tk.Label(self.circle1, text = "1", fg = "white", bg = "gray25")
                self.circle1_text.place(x = 18, y = 15)
                self.circle1.bind("<Button-1>",self.drag_start)
                self.circle1.bind("<B1-Motion>",self.drag_motion)
                self.circle1.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle1.bind("<B1-Motion>",self.change_colors_right)

                self.circle2 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle2.create_oval(0,50,50,0, fill = "gray25")
                self.circle2.place(x = 850, y = 170)
                self.circle2_text = tk.Label(self.circle2, text = "2", fg = "white", bg = "gray25")
                self.circle2_text.place(x = 18, y = 15)
                self.circle2.bind("<Button-1>",self.drag_start)
                self.circle2.bind("<B1-Motion>",self.drag_motion)
                self.circle2.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle2.bind("<B1-Motion>",self.change_colors_right)

                self.circle3 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle3.create_oval(0,50,50,0, fill = "gray25")
                self.circle3.place(x = 850, y = 230)
                self.circle3_text = tk.Label(self.circle3, text = "3", fg = "white", bg = "gray25")
                self.circle3_text.place(x = 18, y = 15)
                self.circle3.bind("<Button-1>",self.drag_start)
                self.circle3.bind("<B1-Motion>",self.drag_motion)
                self.circle3.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle3.bind("<B1-Motion>",self.change_colors_right)

                self.circle4 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle4.create_oval(0,50,50,0, fill = "gray25")
                self.circle4.place(x = 850, y = 290)
                self.circle4_text = tk.Label(self.circle4, text = "4", fg = "white", bg = "gray25")
                self.circle4_text.place(x = 18, y = 15)
                self.circle4.bind("<Button-1>",self.drag_start)
                self.circle4.bind("<B1-Motion>",self.drag_motion)
                self.circle4.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle4.bind("<B1-Motion>",self.change_colors_right)

                self.circle5 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle5.create_oval(0,50,50,0, fill = "gray25")
                self.circle5.place(x = 850, y = 350)
                self.circle5_text = tk.Label(self.circle5, text = "5", fg = "white", bg = "gray25")
                self.circle5_text.place(x = 18, y = 15)
                self.circle5.bind("<Button-1>",self.drag_start)
                self.circle5.bind("<B1-Motion>",self.drag_motion)
                self.circle5.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle5.bind("<B1-Motion>",self.change_colors_right)

                self.circle6 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle6.create_oval(0,50,50,0, fill = "gray25")
                self.circle6.place(x = 850, y = 410)
                self.circle6_text = tk.Label(self.circle6, text = "6", fg = "white", bg = "gray25")
                self.circle6_text.place(x = 18, y = 15)
                self.circle6.bind("<Button-1>",self.drag_start)
                self.circle6.bind("<B1-Motion>",self.drag_motion)
                self.circle6.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle6.bind("<B1-Motion>",self.change_colors_right)
            else:
                self.circle1 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle1.create_oval(0,50,50,0, fill = "gray25")
                self.circle1.place(x = 850, y = 110)
                self.circle1_text = tk.Label(self.circle1, text = "*", fg = "white", bg = "gray25")
                self.circle1_text.place(x = 18, y = 15)
                self.circle1.bind("<Button-1>",self.drag_start)
                self.circle1.bind("<B1-Motion>",self.drag_motion)
                self.circle1.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle1.bind("<B1-Motion>",self.change_colors_right)

                self.circle2 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle2.create_oval(0,50,50,0, fill = "gray25")
                self.circle2.place(x = 850, y = 170)
                self.circle2_text = tk.Label(self.circle2, text = "+", fg = "white", bg = "gray25")
                self.circle2_text.place(x = 18, y = 15)
                self.circle2.bind("<Button-1>",self.drag_start)
                self.circle2.bind("<B1-Motion>",self.drag_motion)
                self.circle2.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle2.bind("<B1-Motion>",self.change_colors_right)

                self.circle3 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle3.create_oval(0,50,50,0, fill = "gray25")
                self.circle3.place(x = 850, y = 230)
                self.circle3_text = tk.Label(self.circle3, text = "/", fg = "white", bg = "gray25")
                self.circle3_text.place(x = 18, y = 15)
                self.circle3.bind("<Button-1>",self.drag_start)
                self.circle3.bind("<B1-Motion>",self.drag_motion)
                self.circle3.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle3.bind("<B1-Motion>",self.change_colors_right)

                self.circle4 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle4.create_oval(0,50,50,0, fill = "gray25")
                self.circle4.place(x = 850, y = 290)
                self.circle4_text = tk.Label(self.circle4, text = "-", fg = "white", bg = "gray25")
                self.circle4_text.place(x = 18, y = 15)
                self.circle4.bind("<Button-1>",self.drag_start)
                self.circle4.bind("<B1-Motion>",self.drag_motion)
                self.circle4.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle4.bind("<B1-Motion>",self.change_colors_right)

                self.circle5 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle5.create_oval(0,50,50,0, fill = "gray25")
                self.circle5.place(x = 850, y = 350)
                self.circle5_text = tk.Label(self.circle5, text = ">", fg = "white", bg = "gray25")
                self.circle5_text.place(x = 18, y = 15)
                self.circle5.bind("<Button-1>",self.drag_start)
                self.circle5.bind("<B1-Motion>",self.drag_motion)
                self.circle5.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle5.bind("<B1-Motion>",self.change_colors_right)

                self.circle6 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle6.create_oval(0,50,50,0, fill = "gray25")
                self.circle6.place(x = 850, y = 410)
                self.circle6_text = tk.Label(self.circle6, text = "<", fg = "white", bg = "gray25")
                self.circle6_text.place(x = 18, y = 15)
                self.circle6.bind("<Button-1>",self.drag_start)
                self.circle6.bind("<B1-Motion>",self.drag_motion)
                self.circle6.bind("<ButtonRelease-1>",self.call_back_rigth)
                self.circle6.bind("<B1-Motion>",self.change_colors_right)


            #ESPACIOS EN BLANCO QUE TOMAN LOS COLORES
            self.white_space1 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space1.create_oval(0,50,50,0, fill = "white", outline = "")
            self.white_space1.place(x = 200,y = 410)

            self.white_space2 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space2.create_oval(0,50,50,0, fill = "white", outline = "")
            self.white_space2.place(x = 260, y = 410)

            self.white_space3 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space3.create_oval(0,50,50,0, fill = "white", outline = "")
            self.white_space3.place(x = 320,y = 410)

            self.white_space4 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space4.create_oval(0,50,50,0, fill = "white", outline = "")
            self.white_space4.place(x = 380,y = 410)

            self.white_space5 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space5.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space5.place(x = 200,y = 350)

            self.white_space6 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space6.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space6.place(x = 240,y = 350)

            self.white_space7 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space7.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space7.place(x = 280,y = 350)

            self.white_space8 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space8.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space8.place(x = 320,y = 350)

            self.white_space9 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space9.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space9.place(x = 200,y = 310)

            self.white_space10 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space10.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space10.place(x = 240,y = 310)

            self.white_space11 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space11.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space11.place(x = 280,y = 310)

            self.white_space12 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space12.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space12.place(x = 320,y = 310)

            self.white_space13 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space13.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space13.place(x = 200,y = 270)

            self.white_space14 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space14.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space14.place(x = 240,y = 270)

            self.white_space15 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space15.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space15.place(x = 280,y = 270)

            self.white_space16= tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space16.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space16.place(x = 320,y = 270)

            self.white_space17 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space17.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space17.place(x = 200,y = 230)

            self.white_space18 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space18.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space18.place(x = 240,y = 230)

            self.white_space19 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space19.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space19.place(x = 280,y = 230)

            self.white_space20 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space20.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space20.place(x = 320,y = 230)

            self.white_space21 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space21.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space21.place(x = 200,y = 190)

            self.white_space22 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space22.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space22.place(x = 240,y = 190)

            self.white_space23 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space23.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space23.place(x = 280,y = 190)

            self.white_space24 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space24.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space24.place(x = 320,y = 190)

            self.white_space25 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space25.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space25.place(x = 200,y = 150)

            self.white_space26 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space26.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space26.place(x = 240,y = 150)

            self.white_space27 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space27.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space27.place(x = 280,y = 150)

            self.white_space28 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space28.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space28.place(x = 320,y = 150)

            self.white_space29 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space29.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space29.place(x = 200,y = 110)

            self.white_space30 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space30.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space30.place(x = 240,y = 110)

            self.white_space31 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space31.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space31.place(x = 280,y = 110)

            self.white_space32 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space32.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space32.place(x = 320,y = 110)

            self.white_space33 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space33.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space33.place(x = 200,y = 70)

            self.white_space34 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space34.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space34.place(x = 240,y = 70)

            self.white_space35 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space35.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space35.place(x = 280,y = 70)

            self.white_space36 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space36.create_oval(0,30,30,0, fill = "gray25",outline = "")
            self.white_space36.place(x = 320,y = 70)

            #Calificadores

            self.calificador = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador.place(x = 380,y = 373)

            self.calificador1 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador1.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador1.place(x = 380,y = 350)

            self.calificador2 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador2.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador2.place(x = 360,y = 373)

            self.calificador3 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador3.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador3.place(x = 360,y = 350)

            self.calificador4 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador4.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador4.place(x = 360,y = 310)

            self.calificador5 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador5.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador5.place(x = 380,y = 333)

            self.calificador6 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador6.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador6.place(x = 380,y = 310)

            self.calificador7 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador7.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador7.place(x = 360,y = 333)

            self.calificador8 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador8.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador8.place(x = 360,y = 293)

            self.calificador9 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador9.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador9.place(x = 360,y = 270)

            self.calificador10 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador10.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador10.place(x = 380,y = 270)

            self.calificador11 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador11.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador11.place(x = 380,y = 293)

            self.calificador12 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador12.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador12.place(x = 380,y = 230)

            self.calificador13 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador13.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador13.place(x = 360,y = 253)

            self.calificador14 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador14.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador14.place(x = 360,y = 230)

            self.calificador15 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador15.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador15.place(x = 380,y = 253)

            self.calificador16 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador16.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador16.place(x = 360,y = 190)

            self.calificador17= tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador17.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador17.place(x = 360,y = 213)

            self.calificador18 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador18.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador18.place(x = 380,y = 190)

            self.calificador19 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador19.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador19.place(x = 380,y = 213)

            self.calificador20 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador20.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador20.place(x = 380,y = 173)
    
            self.calificador21 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador21.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador21.place(x = 360,y = 173)

            self.calificador22 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador22.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador22.place(x = 380,y = 150)

            self.calificador23 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador23.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador23.place(x = 360,y = 150)

            self.calificador24 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador24.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador24.place(x = 360,y = 110)

            self.calificador25 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador25.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador25.place(x = 360,y = 133)

            self.calificador26 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador26.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador26.place(x = 380,y = 110)

            self.calificador27 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador27.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador27.place(x = 380,y = 133)

            self.calificador28 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador28.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador28.place(x = 360,y = 70)

            self.calificador29 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador29.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador29.place(x = 360,y = 93)

            self.calificador30 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador30.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador30.place(x = 380,y = 70)

            self.calificador31 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador31.create_oval(0,10,10,0, fill = "gray25",outline = "")
            self.calificador31.place(x = 380,y = 93)
        #Izquierda
        else:
            #Colores
            if self.combinacion  == 1:
                self.circle1 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle1.create_oval(0,50,50,0, fill = colors[0], outline = "")
                self.circle1.place(x = 100, y = 110)
                self.circle1.bind("<Button-1>",self.drag_start)
                self.circle1.bind("<B1-Motion>",self.drag_motion)
                self.circle1.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle1.bind("<B1-Motion>",self.change_colors_left)

                self.circle2 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle2.create_oval(0,50,50,0, fill = colors[1], outline = "")
                self.circle2.place(x = 100, y = 170)
                self.circle2.bind("<Button-1>",self.drag_start)
                self.circle2.bind("<B1-Motion>",self.drag_motion)
                self.circle2.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle2.bind("<B1-Motion>",self.change_colors_left)

                self.circle3 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle3.create_oval(0,50,50,0, fill = colors[2], outline = "")
                self.circle3.place(x = 100, y = 230)
                self.circle3.bind("<Button-1>",self.drag_start)
                self.circle3.bind("<B1-Motion>",self.drag_motion)
                self.circle3.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle3.bind("<B1-Motion>",self.change_colors_left)

                self.circle4 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle4.create_oval(0,50,50,0, fill = colors[3], outline = "")
                self.circle4.place(x = 100, y = 290)
                self.circle4.bind("<Button-1>",self.drag_start)
                self.circle4.bind("<B1-Motion>",self.drag_motion)
                self.circle4.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle4.bind("<B1-Motion>",self.change_colors_left)

                self.circle5 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle5.create_oval(0,50,50,0, fill = colors[4], outline = "")
                self.circle5.place(x = 100, y = 350)
                self.circle5.bind("<Button-1>",self.drag_start)
                self.circle5.bind("<B1-Motion>",self.drag_motion)
                self.circle5.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle5.bind("<B1-Motion>",self.change_colors_left)

                self.circle6 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle6.create_oval(0,50,50,0, fill = colors[5], outline = "")
                self.circle6.place(x = 100, y = 410)
                self.circle6.bind("<Button-1>",self.drag_start)
                self.circle6.bind("<B1-Motion>",self.drag_motion)
                self.circle6.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle6.bind("<B1-Motion>",self.change_colors_left)
            #Letras
            elif self.combinacion == 2:
                self.circle1 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle1.create_oval(0,50,50,0, fill = "gray25")
                self.circle1.place(x = 100, y = 110)
                self.circle1_text = tk.Label(self.circle1, text = "A", fg = "white", bg = "gray25")
                self.circle1_text.place(x = 18, y = 15)
                self.circle1.bind("<Button-1>",self.drag_start)
                self.circle1.bind("<B1-Motion>",self.drag_motion)
                self.circle1.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle1.bind("<B1-Motion>",self.change_colors_left)

                self.circle2 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle2.create_oval(0,50,50,0, fill = "gray25")
                self.circle2.place(x = 100, y = 170)
                self.circle2_text = tk.Label(self.circle2, text = "B", fg = "white", bg = "gray25")
                self.circle2_text.place(x = 18, y = 15)
                self.circle2.bind("<Button-1>",self.drag_start)
                self.circle2.bind("<B1-Motion>",self.drag_motion)
                self.circle2.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle2.bind("<B1-Motion>",self.change_colors_left)

                self.circle3 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle3.create_oval(0,50,50,0, fill = "gray25")
                self.circle3.place(x = 100, y = 230)
                self.circle3_text = tk.Label(self.circle3, text = "C", fg = "white", bg = "gray25")
                self.circle3_text.place(x = 18, y = 15)
                self.circle3.bind("<Button-1>",self.drag_start)
                self.circle3.bind("<B1-Motion>",self.drag_motion)
                self.circle3.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle3.bind("<B1-Motion>",self.change_colors_left)

                self.circle4 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle4.create_oval(0,50,50,0, fill = "gray25")
                self.circle4.place(x = 100, y = 290)
                self.circle4_text = tk.Label(self.circle4, text = "D", fg = "white", bg = "gray25")
                self.circle4_text.place(x = 18, y = 15)
                self.circle4.bind("<Button-1>",self.drag_start)
                self.circle4.bind("<B1-Motion>",self.drag_motion)
                self.circle4.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle4.bind("<B1-Motion>",self.change_colors_left)

                self.circle5 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle5.create_oval(0,50,50,0, fill = "gray25")
                self.circle5.place(x = 100, y = 350)
                self.circle5_text = tk.Label(self.circle5, text = "E", fg = "white", bg = "gray25")
                self.circle5_text.place(x = 18, y = 15)
                self.circle5.bind("<Button-1>",self.drag_start)
                self.circle5.bind("<B1-Motion>",self.drag_motion)
                self.circle5.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle5.bind("<B1-Motion>",self.change_colors_left)

                self.circle6 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle6.create_oval(0,50,50,0, fill = "gray25")
                self.circle6.place(x = 100, y = 410)
                self.circle6_text = tk.Label(self.circle6, text = "F", fg = "white", bg = "gray25")
                self.circle6_text.place(x = 18, y = 15)
                self.circle6.bind("<Button-1>",self.drag_start)
                self.circle6.bind("<B1-Motion>",self.drag_motion)
                self.circle6.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle6.bind("<B1-Motion>",self.change_colors_left)
            #Numeros
            elif self.combinacion == 3:
                self.circle1 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle1.create_oval(0,50,50,0, fill = "gray25")
                self.circle1.place(x = 100, y = 110)
                self.circle1_text = tk.Label(self.circle1, text = "1", fg = "white", bg = "gray25")
                self.circle1_text.place(x = 18, y = 15)
                self.circle1.bind("<Button-1>",self.drag_start)
                self.circle1.bind("<B1-Motion>",self.drag_motion)
                self.circle1.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle1.bind("<B1-Motion>",self.change_colors_left)

                self.circle2 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle2.create_oval(0,50,50,0, fill = "gray25")
                self.circle2.place(x = 100, y = 170)
                self.circle2_text = tk.Label(self.circle2, text = "2", fg = "white", bg = "gray25")
                self.circle2_text.place(x = 18, y = 15)
                self.circle2.bind("<Button-1>",self.drag_start)
                self.circle2.bind("<B1-Motion>",self.drag_motion)
                self.circle2.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle2.bind("<B1-Motion>",self.change_colors_left)

                self.circle3 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle3.create_oval(0,50,50,0, fill = "gray25")
                self.circle3.place(x = 100, y = 230)
                self.circle3_text = tk.Label(self.circle3, text = "3", fg = "white", bg = "gray25")
                self.circle3_text.place(x = 18, y = 15)
                self.circle3.bind("<Button-1>",self.drag_start)
                self.circle3.bind("<B1-Motion>",self.drag_motion)
                self.circle3.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle3.bind("<B1-Motion>",self.change_colors_left)

                self.circle4 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle4.create_oval(0,50,50,0, fill = "gray25")
                self.circle4.place(x = 100, y = 290)
                self.circle4_text = tk.Label(self.circle4, text = "4", fg = "white", bg = "gray25")
                self.circle4_text.place(x = 18, y = 15)
                self.circle4.bind("<Button-1>",self.drag_start)
                self.circle4.bind("<B1-Motion>",self.drag_motion)
                self.circle4.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle4.bind("<B1-Motion>",self.change_colors_left)

                self.circle5 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle5.create_oval(0,50,50,0, fill = "gray25")
                self.circle5.place(x = 100, y = 350)
                self.circle5_text = tk.Label(self.circle5, text = "5", fg = "white", bg = "gray25")
                self.circle5_text.place(x = 18, y = 15)
                self.circle5.bind("<Button-1>",self.drag_start)
                self.circle5.bind("<B1-Motion>",self.drag_motion)
                self.circle5.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle5.bind("<B1-Motion>",self.change_colors_left)

                self.circle6 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle6.create_oval(0,50,50,0, fill = "gray25")
                self.circle6.place(x = 100, y = 410)
                self.circle6_text = tk.Label(self.circle6, text = "6", fg = "white", bg = "gray25")
                self.circle6_text.place(x = 18, y = 15)
                self.circle6.bind("<Button-1>",self.drag_start)
                self.circle6.bind("<B1-Motion>",self.drag_motion)
                self.circle6.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle6.bind("<B1-Motion>",self.change_colors_left)
            else:
                self.circle1 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle1.create_oval(0,50,50,0, fill = "gray25")
                self.circle1.place(x = 100, y = 110)
                self.circle1_text = tk.Label(self.circle1, text = "*", fg = "white", bg = "gray25")
                self.circle1_text.place(x = 18, y = 15)
                self.circle1.bind("<Button-1>",self.drag_start)
                self.circle1.bind("<B1-Motion>",self.drag_motion)
                self.circle1.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle1.bind("<B1-Motion>",self.change_colors_left)

                self.circle2 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle2.create_oval(0,50,50,0, fill = "gray25")
                self.circle2.place(x = 100, y = 170)
                self.circle2_text = tk.Label(self.circle2, text = "+", fg = "white", bg = "gray25")
                self.circle2_text.place(x = 18, y = 15)
                self.circle2.bind("<Button-1>",self.drag_start)
                self.circle2.bind("<B1-Motion>",self.drag_motion)
                self.circle2.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle2.bind("<B1-Motion>",self.change_colors_left)

                self.circle3 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle3.create_oval(0,50,50,0, fill = "gray25")
                self.circle3.place(x = 100, y = 230)
                self.circle3_text = tk.Label(self.circle3, text = "/", fg = "white", bg = "gray25")
                self.circle3_text.place(x = 18, y = 15)
                self.circle3.bind("<Button-1>",self.drag_start)
                self.circle3.bind("<B1-Motion>",self.drag_motion)
                self.circle3.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle3.bind("<B1-Motion>",self.change_colors_left)

                self.circle4 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle4.create_oval(0,50,50,0, fill = "gray25")
                self.circle4.place(x = 100, y = 290)
                self.circle4_text = tk.Label(self.circle4, text = "-", fg = "white", bg = "gray25")
                self.circle4_text.place(x = 18, y = 15)
                self.circle4.bind("<Button-1>",self.drag_start)
                self.circle4.bind("<B1-Motion>",self.drag_motion)
                self.circle4.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle4.bind("<B1-Motion>",self.change_colors_left)

                self.circle5 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle5.create_oval(0,50,50,0, fill = "gray25")
                self.circle5.place(x = 100, y = 350)
                self.circle5_text = tk.Label(self.circle5, text = ">", fg = "white", bg = "gray25")
                self.circle5_text.place(x = 18, y = 15)
                self.circle5.bind("<Button-1>",self.drag_start)
                self.circle5.bind("<B1-Motion>",self.drag_motion)
                self.circle5.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle5.bind("<B1-Motion>",self.change_colors_left)

                self.circle6 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                self.circle6.create_oval(0,50,50,0, fill = "gray25")
                self.circle6.place(x = 100, y = 410)
                self.circle6_text = tk.Label(self.circle6, text = "<", fg = "white", bg = "gray25")
                self.circle6_text.place(x = 18, y = 15)
                self.circle6.bind("<Button-1>",self.drag_start)
                self.circle6.bind("<B1-Motion>",self.drag_motion)
                self.circle6.bind("<ButtonRelease-1>",self.call_back_left)
                self.circle6.bind("<B1-Motion>",self.change_colors_left)

            #Espacios en blanco
            self.white_space1 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space1.create_oval(0,50,50,0, fill = "white", outline = "")
            self.white_space1.place(x = 570,y = 410)

            self.white_space2 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space2.create_oval(0,50,50,0, fill = "white", outline = "")
            self.white_space2.place(x = 630, y = 410)

            self.white_space3 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space3.create_oval(0,50,50,0, fill = "white", outline = "")
            self.white_space3.place(x = 690,y = 410)

            self.white_space4 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space4.create_oval(0,50,50,0, fill = "white", outline = "")
            self.white_space4.place(x = 750,y = 410)

            self.white_space5 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space5.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space5.place(x = 645,y = 350)

            self.white_space6 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space6.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space6.place(x = 685,y = 350)

            self.white_space7 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space7.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space7.place(x = 725,y = 350)

            self.white_space8 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space8.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space8.place(x = 765,y = 350)

            self.white_space9 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space9.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space9.place(x = 645,y = 310)

            self.white_space10 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space10.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space10.place(x = 685,y = 310)

            self.white_space11 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space11.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space11.place(x = 725,y = 310)

            self.white_space12 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space12.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space12.place(x = 765,y = 310)

            self.white_space13 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space13.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space13.place(x = 645,y = 270)

            self.white_space14 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space14.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space14.place(x = 685,y = 270)

            self.white_space15 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space15.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space15.place(x = 725,y = 270)

            self.white_space16= tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space16.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space16.place(x = 765,y = 270)

            self.white_space17 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space17.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space17.place(x = 645,y = 230)

            self.white_space18 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space18.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space18.place(x = 685,y = 230)

            self.white_space19 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space19.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space19.place(x = 725,y = 230)

            self.white_space20 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space20.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space20.place(x = 765,y = 230)

            self.white_space21 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space21.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space21.place(x = 645,y = 190)

            self.white_space22 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space22.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space22.place(x = 685,y = 190)

            self.white_space23 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space23.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space23.place(x = 725,y = 190)

            self.white_space24 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space24.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space24.place(x = 765,y = 190)

            self.white_space25 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space25.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space25.place(x = 645,y = 150)

            self.white_space26 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space26.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space26.place(x = 685,y = 150)

            self.white_space27 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space27.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space27.place(x = 725,y = 150)

            self.white_space28 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space28.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space28.place(x = 765,y = 150)

            self.white_space29 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space29.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space29.place(x = 645,y = 110)

            self.white_space30 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space30.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space30.place(x = 685,y = 110)

            self.white_space31 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space31.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space31.place(x = 725,y = 110)

            self.white_space32 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space32.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space32.place(x = 765,y = 110)

            self.white_space33 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space33.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space33.place(x = 645,y = 70)

            self.white_space34 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space34.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space34.place(x = 685,y = 70)

            self.white_space35 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space35.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space35.place(x = 725,y = 70)

            self.white_space36 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.white_space36.create_oval(0,30,30,0, fill = "gray25", outline = "")
            self.white_space36.place(x = 765,y = 70)

            #Calificadores
            self.calificador = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador.place(x = 605,y = 373)

            self.calificador1 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador1.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador1.place(x = 605,y = 350)

            self.calificador2 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador2.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador2.place(x = 625,y = 373)

            self.calificador3 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador3.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador3.place(x = 625,y = 350)

            self.calificador4 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador4.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador4.place(x = 625,y = 310)

            self.calificador5 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador5.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador5.place(x = 605,y = 333)

            self.calificador6 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador6.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador6.place(x = 605,y = 310)

            self.calificador7 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador7.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador7.place(x = 625,y = 333)

            self.calificador8 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador8.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador8.place(x = 625,y = 293)

            self.calificador9 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador9.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador9.place(x = 625,y = 270)

            self.calificador10 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador10.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador10.place(x = 605,y = 270)

            self.calificador11 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador11.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador11.place(x = 605,y = 293)

            self.calificador12 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador12.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador12.place(x = 605,y = 230)

            self.calificador13 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador13.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador13.place(x = 625,y = 253)

            self.calificador14 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador14.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador14.place(x = 625,y = 230)

            self.calificador15 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador15.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador15.place(x = 605,y = 253)

            self.calificador16 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador16.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador16.place(x = 625,y = 190)

            self.calificador17= tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador17.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador17.place(x = 625,y = 213)

            self.calificador18 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador18.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador18.place(x = 605,y = 190)

            self.calificador19 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador19.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador19.place(x = 605,y = 213)

            self.calificador20 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador20.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador20.place(x = 605,y = 173)

            self.calificador21 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador21.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador21.place(x = 625,y = 173)

            self.calificador22 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador22.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador22.place(x = 605,y = 150)

            self.calificador23 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador23.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador23.place(x = 625,y = 150)

            self.calificador24 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador24.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador24.place(x = 625,y = 110)

            self.calificador25 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador25.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador25.place(x = 625,y = 133)

            self.calificador26 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador26.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador26.place(x = 605,y = 110)

            self.calificador27 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador27.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador27.place(x = 605,y = 133)

            self.calificador28 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador28.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador28.place(x = 625,y = 70)

            self.calificador29 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador29.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador29.place(x = 625,y = 93)

            self.calificador30 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador30.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador30.place(x = 605,y = 70)

            self.calificador31 = tk.Canvas(self.canvas, width = 10, height = 10, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
            self.calificador31.create_oval(0,10,10,0, fill = "gray25", outline = "")
            self.calificador31.place(x = 605,y = 93)

        self.white_spaces = [self.white_space5,self.white_space6,self.white_space7,self.white_space8,self.white_space9,self.white_space10,self.white_space11,self.white_space12,self.white_space13, self.white_space14,self.white_space15,self.white_space16,self.white_space17,self.white_space18,self.white_space19,self.white_space20,self.white_space21,self.white_space22,self.white_space23,self.white_space24,self.white_space25,self.white_space26,self.white_space27,self.white_space28,self.white_space29,self.white_space30,self.white_space31,self.white_space32,self.white_space33,self.white_space34,self.white_space35,self.white_space36]
        self.calificadores = [self.calificador,self.calificador1,self.calificador2,self.calificador3,self.calificador4,self.calificador5,self.calificador6,self.calificador7,self.calificador8,self.calificador9,self.calificador10,self.calificador11,self.calificador12,self.calificador13,self.calificador14,self.calificador15,self.calificador16,self.calificador17,self.calificador18,self.calificador19,self.calificador20,self.calificador21,self.calificador22,self.calificador23,self.calificador24,self.calificador25,self.calificador26,self.calificador27,self.calificador28,self.calificador29,self.calificador30,self.calificador31]
        self.lista_espacios = [self.white_space1,self.white_space2,self.white_space3,self.white_space4]
    #Mover widgets
    def drag_start(self,event):
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y
    def drag_motion(self,event):

        widget = event.widget
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        widget.place(x = x, y = y)
    #Volver a posicion original
    def call_back_rigth(self,event):
        self.x = True
        widget = event.widget
        if widget == self.circle1:
            self.circle1.place(x = 850,y = 110)
        elif widget == self.circle2:
            self.circle2.place(x = 850,y = 170)
        elif widget == self.circle3:
            self.circle3.place(x = 850,y = 230)
        elif widget == self.circle4:
            self.circle4.place(x = 850,y = 290)
        elif widget == self.circle5:
            self.circle5.place(x = 850,y = 350)
        elif widget == self.circle6:
            self.circle6.place(x = 850,y = 410)
    #Volver a posicion original
    def call_back_left(self,event):
        self.x = True
        widget = event.widget
        if widget == self.circle1:
            self.circle1.place(x = 100,y = 110)
        elif widget == self.circle2:
            self.circle2.place(x = 100,y = 170)
        elif widget == self.circle3:
            self.circle3.place(x = 100,y = 230)
        elif widget == self.circle4:
            self.circle4.place(x = 100,y = 290)
        elif widget == self.circle5:
            self.circle5.place(x = 100,y = 350)
        elif widget == self.circle6:
            self.circle6.place(x = 100,y = 410)
    #Cambiar elementos de los espacios en blanco del lado derecho
    def change_colors_right(self,event):
        widget = event.widget
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        widget.place(x=x,y=y)
        if x in range(190,210) and y in range(370,470):
            if self.x == True:
                self.lista_de_contadores.append(0)
                self.indice = self.lista_de_contadores[len(self.lista_de_contadores) - 1]
            if self.combinacion == 1:
                if widget == self.circle1:
                    self.white_space1.create_oval(0,50,50,0, fill = "blue", outline = "")
                    self.lista.pop(0)
                    self.lista.insert(0,"blue")
                    if self.x == True:
                        self.listatotal[0].append("blue")
                        self.x = False
                elif widget == self.circle2:
                    self.white_space1.create_oval(0,50,50,0, fill = "red", outline = "")
                    self.lista.pop(0)
                    self.lista.insert(0,"red")
                    if self.x == True:
                        self.listatotal[0].append("red")
                        self.x = False
                elif widget == self.circle3:
                    self.white_space1.create_oval(0,50,50,0, fill = "yellow", outline = "")
                    self.lista.pop(0)
                    self.lista.insert(0,"yellow")
                    if self.x == True:
                        self.listatotal[0].append("yellow")
                        self.x = False
                elif widget == self.circle4:
                    self.white_space1.create_oval(0,50,50,0, fill = "green", outline = "")
                    self.lista.pop(0)
                    self.lista.insert(0,"green")
                    if self.x == True:
                        self.listatotal[0].append("green")
                        self.x = False
                elif widget == self.circle5:
                    self.white_space1.create_oval(0,50,50,0, fill = "saddle brown", outline = "")
                    self.lista.pop(0)
                    self.lista.insert(0,"saddle brown")
                    if self.x == True:
                        self.listatotal[0].append("saddle brown")
                        self.x = False
                elif widget == self.circle6:
                    self.white_space1.create_oval(0,50,50,0, fill = "orange", outline = "")
                    self.lista.pop(0)
                    self.lista.insert(0,"orange")
                    if self.x == True:
                        self.listatotal[0].append("orange")
                        self.x = False
            elif self.combinacion == 2:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space1, text = "A", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,"A")
                    if self.x == True:
                        self.listatotal[0].append("A")
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space1, text = "B", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,"B")
                    if self.x == True:
                        self.listatotal[0].append("B")
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space1, text = "C", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,"C")
                    if self.x == True:
                        self.listatotal[0].append("C")
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space1, text = "D", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,"D")
                    if self.x == True:
                        self.listatotal[0].append("D")
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space1, text = "E", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,"E")
                    if self.x == True:
                        self.listatotal[0].append("E")
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space1, text = "F", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,"F")
                    if self.x == True:
                        self.listatotal[0].append("F")
                        self.x = False
            elif self.combinacion == 3:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space1, text = 1, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,1)
                    if self.x == True:
                        self.listatotal[0].append(1)
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space1, text = 2, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,2)
                    if self.x == True:
                        self.listatotal[0].append(2)
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space1, text = 3, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,3)
                    if self.x == True:
                        self.listatotal[0].append(3)
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space1, text = 4, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,4)
                    if self.x == True:
                        self.listatotal[0].append(4)
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space1, text = 5, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,5)
                    if self.x == True:
                        self.listatotal[0].append(5)
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space1, text = 6, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,6)
                    if self.x == True:
                        self.listatotal[0].append(6)
                        self.x = False
            else:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space1, text = "*", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,"*")
                    if self.x == True:
                        self.listatotal[0].append("*")
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space1, text = "+", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,"+")
                    if self.x == True:
                        self.listatotal[0].append("+")
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space1, text = "/", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,"/")
                    if self.x == True:
                        self.listatotal[0].append("/")
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space1, text = "-", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,"-")
                    if self.x == True:
                        self.listatotal[0].append("-")
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space1, text = ">", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,">")
                    if self.x == True:
                        self.listatotal[0].append(">")
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space1, text = "<", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,"<")
                    if self.x == True:
                        self.listatotal[0].append("<")
                        self.x = False
        elif x in range(250,267) and y in range(370,470):
            #Segundo
            if self.x == True:
                self.lista_de_contadores.append(1)
                self.indice = self.lista_de_contadores[len(self.lista_de_contadores) - 1]
            if self.combinacion == 1:
                if widget == self.circle1:
                    self.white_space2.create_oval(0,50,50,0, fill = "blue", outline = "")
                    self.lista.pop(1)
                    self.lista.insert(1,"blue")
                    if self.x == True:
                        self.listatotal[1].append("blue")
                        self.x = False
                elif widget == self.circle2:
                    self.white_space2.create_oval(0,50,50,0, fill = "red", outline = "")
                    self.lista.pop(1)
                    self.lista.insert(1,"red")
                    if self.x == True:
                        self.listatotal[1].append("red")
                        self.x = False
                elif widget == self.circle3:
                    self.white_space2.create_oval(0,50,50,0, fill = "yellow", outline = "")
                    self.lista.pop(1)
                    self.lista.insert(1,"yellow")
                    if self.x == True:
                        self.listatotal[1].append("yellow")
                        self.x = False
                elif widget == self.circle4:
                    self.white_space2.create_oval(0,50,50,0, fill = "green", outline = "")
                    self.lista.pop(1)
                    self.lista.insert(1,"green")
                    if self.x == True:
                        self.listatotal[1].append("green")
                        self.x = False
                elif widget == self.circle5:
                    self.white_space2.create_oval(0,50,50,0, fill = "saddle brown", outline = "")
                    self.lista.pop(1)
                    self.lista.insert(1,"saddle brown")
                    if self.x == True:
                        self.listatotal[1].append("saddle brown")
                        self.x = False
                elif widget == self.circle6:
                    self.white_space2.create_oval(0,50,50,0, fill = "orange", outline = "")
                    self.lista.pop(1)
                    self.lista.insert(1,"orange")
                    if self.x == True:
                        self.listatotal[1].append("orange")
                        self.x = False
            elif self.combinacion == 2:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space2, text = "A", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,"A")
                    if self.x == True:
                        self.listatotal[1].append("A")
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space2, text = "B", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,"B")
                    if self.x == True:
                        self.listatotal[1].append("B")
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space2, text = "C", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,"C")
                    if self.x == True:
                        self.listatotal[1].append("C")
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space2, text = "D", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,"D")
                    if self.x == True:
                        self.listatotal[1].append("D")
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space2, text = "E", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,"E")
                    if self.x == True:
                        self.listatotal[1].append("E")
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space2, text = "F", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,"F")
                    if self.x == True:
                        self.listatotal[1].append("F")
                        self.x = False
            elif self.combinacion == 3:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space2, text = 1, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,1)
                    if self.x == True:
                        self.listatotal[1].append(1)
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space2, text = 2, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,2)
                    if self.x == True:
                        self.listatotal[1].append(2)
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space2, text = 3, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,3)
                    if self.x == True:
                        self.listatotal[1].append(3)
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space2, text = 4, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,4)
                    if self.x == True:
                        self.listatotal[1].append(4)
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space2, text = 5, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,5)
                    if self.x == True:
                        self.listatotal[1].append(5)
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space2, text = 6, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,6)
                    if self.x == True:
                        self.listatotal[1].append(6)
                        self.x = False
            else:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space2, text = "*", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,"*")
                    if self.x == True:
                        self.listatotal[1].append("*")
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space2, text = "+", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,"+")
                    if self.x == True:
                        self.listatotal[1].append("+")
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space2, text = "/", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,"/")
                    if self.x == True:
                        self.listatotal[1].append("/")
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space2, text = "-", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,"-")
                    if self.x == True:
                        self.listatotal[1].append("-")
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space2, text = ">", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,">")
                    if self.x == True:
                        self.listatotal[1].append(">")
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space2, text = "<", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,"<")
                    if self.x == True:
                        self.listatotal[1].append("<")
                        self.x = False
        elif x in range(315,325) and y in range(370,470):
            #Tercero
            if self.x == True:
                self.lista_de_contadores.append(2)
                self.indice = self.lista_de_contadores[len(self.lista_de_contadores) - 1]
            if self.combinacion == 1:
                if widget == self.circle1:
                    self.white_space3.create_oval(0,50,50,0, fill = "blue", outline = "")
                    self.lista.pop(2)
                    self.lista.insert(2,"blue")
                    if self.x == True:
                        self.listatotal[2].append("blue")
                        self.x = False
                elif widget == self.circle2:
                    self.white_space3.create_oval(0,50,50,0, fill = "red", outline = "")
                    self.lista.pop(2)
                    self.lista.insert(2,"red")
                    if self.x == True:
                        self.listatotal[2].append("red")
                        self.x = False
                elif widget == self.circle3:
                    self.white_space3.create_oval(0,50,50,0, fill = "yellow", outline = "")
                    self.lista.pop(2)
                    self.lista.insert(2,"yellow")
                    if self.x == True:
                        self.listatotal[2].append("yellow")
                        self.x = False
                elif widget == self.circle4:
                    self.white_space3.create_oval(0,50,50,0, fill = "green", outline = "")
                    self.lista.pop(2)
                    self.lista.insert(2,"green")
                    if self.x == True:
                        self.listatotal[2].append("green")
                        self.x = False
                elif widget == self.circle5:
                    self.white_space3.create_oval(0,50,50,0, fill = "saddle brown", outline = "")
                    self.lista.pop(2)
                    self.lista.insert(2,"saddle brown")
                    if self.x == True:
                        self.listatotal[2].append("saddle brown")
                        self.x = False
                elif widget == self.circle6:
                    self.white_space3.create_oval(0,50,50,0, fill = "orange", outline = "")
                    self.lista.pop(2)
                    self.lista.insert(2,"orange")
                    if self.x == True:
                        self.listatotal[2].append("orange")
                        self.x = False
            elif self.combinacion == 2:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space3, text = "A", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,"A")
                    if self.x == True:
                        self.listatotal[2].append("A")
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space3, text = "B", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,"B")
                    if self.x == True:
                        self.listatotal[2].append("B")
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space3, text = "C", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,"C")
                    if self.x == True:
                        self.listatotal[2].append("C")
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space3, text = "D", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,"D")
                    if self.x == True:
                        self.listatotal[2].append("D")
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space3, text = "E", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,"E")
                    if self.x == True:
                        self.listatotal[2].append("E")
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space3, text = "F", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,"F")
                    if self.x == True:
                        self.listatotal[2].append("F")
                        self.x = False
            elif self.combinacion == 3:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space3, text = 1, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,1)
                    if self.x == True:
                        self.listatotal[2].append(1)
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space3, text = 2, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,2)
                    if self.x == True:
                        self.listatotal[2].append(2)
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space3, text = 3, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,3)
                    if self.x == True:
                        self.listatotal[2].append(3)
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space3, text = 4, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,4)
                    if self.x == True:
                        self.listatotal[2].append(4)
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space3, text = 5, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,5)
                    if self.x == True:
                        self.listatotal[2].append(5)
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space3, text = 6, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,6)
                    if self.x == True:
                        self.listatotal[2].append(6)
                        self.x = False
            else:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space3, text = "*", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,"*")
                    if self.x == True:
                        self.listatotal[2].append("*")
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space3, text = "+", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,"+")
                    if self.x == True:
                        self.listatotal[2].append("+")
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space3, text = "/", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,"/")
                    if self.x == True:
                        self.listatotal[2].append("/")
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space3, text = '-', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,"-")
                    if self.x == True:
                        self.listatotal[2].append("-")
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space3, text = '>', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,">")
                    if self.x == True:
                        self.listatotal[2].append(">")
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space3, text = "<", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,"<")
                    if self.x == True:
                        self.listatotal[2].append("<")
                        self.x = False
        elif x in range(375,395) and y in range(370,470):
            #Cuarto
            if self.x == True:
                self.lista_de_contadores.append(3)
                self.indice = self.lista_de_contadores[len(self.lista_de_contadores) - 1]
            if self.combinacion == 1:
                if widget == self.circle1:
                    self.white_space4.create_oval(0,50,50,0, fill = "blue", outline = "")
                    self.lista.pop(3)
                    self.lista.insert(3,"blue")
                    if self.x == True:
                        self.listatotal[3].append("blue")
                        self.x = False
                elif widget == self.circle2:
                    self.white_space4.create_oval(0,50,50,0, fill = "red", outline = "")
                    self.lista.pop(3)
                    self.lista.insert(3,"red")
                    if self.x == True:
                        self.listatotal[3].append("red")
                        self.x = False
                elif widget == self.circle3:
                    self.white_space4.create_oval(0,50,50,0, fill = "yellow", outline = "")
                    self.lista.pop(3)
                    self.lista.insert(3,"yellow")
                    if self.x == True:
                        self.listatotal[3].append("yellow")
                        self.x = False
                elif widget == self.circle4:
                    self.white_space4.create_oval(0,50,50,0, fill = "green", outline = "")
                    self.lista.pop(3)
                    self.lista.insert(3,"green")
                    if self.x == True:
                        self.listatotal[3].append("green")
                        self.x = False
                elif widget == self.circle5:
                    self.white_space4.create_oval(0,50,50,0, fill = "saddle brown", outline = "")
                    self.lista.pop(3)
                    self.lista.insert(3,"saddle brown")
                    if self.x == True:
                        self.listatotal[3].append("saddle brown")
                        self.x = False
                elif widget == self.circle6:
                    self.white_space4.create_oval(0,50,50,0, fill = "orange", outline = "")
                    self.lista.pop(3)
                    self.lista.insert(3,"orange")
                    if self.x == True:
                        self.listatotal[3].append("orange")
                        self.x = False
            elif self.combinacion == 2:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space4, text = "A", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,"A")
                    if self.x == True:
                        self.listatotal[3].append("A")
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space4, text = "B", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,"B")
                    if self.x == True:
                        self.listatotal[3].append("B")
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space4, text = "C", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,"C")
                    if self.x == True:
                        self.listatotal[3].append("C")
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space4, text = "D", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,"D")
                    if self.x == True:
                        self.listatotal[3].append("D")
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space4, text = "E", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,"E")
                    if self.x == True:
                        self.listatotal[3].append("E")
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space4, text = "F", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,"F")
                    if self.x == True:
                        self.listatotal[3].append("F")
                        self.x = False
            elif self.combinacion == 3:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space4, text = 1, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,1)
                    if self.x == True:
                        self.listatotal[3].append(1)
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space4, text = 2, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,2)
                    self.listatotal[3].append(2)
                    if self.x == True:
                        self.listatotal[3].append(2)
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space4, text = 3, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,3)
                    if self.x == True:
                        self.listatotal[3].append(3)
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space4, text = 4, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,4)
                    if self.x == True:
                        self.listatotal[3].append(4)
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space4, text = 5, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,5)
                    if self.x == True:
                        self.listatotal[3].append(5)
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space4, text = 6, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,6)
                    if self.x == True:
                        self.listatotal[3].append(6)
                        self.x = False
            else:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space4, text = '*', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,"*")
                    if self.x == True:
                        self.listatotal[3].append("*")
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space4, text = '+', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,"+")
                    if self.x == True:
                        self.listatotal[3].append("+")
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space4, text = '/', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,"/")
                    if self.x == True:
                        self.listatotal[3].append("/")
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space4, text = '-', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,"-")
                    if self.x == True:
                        self.listatotal[3].append("-")
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space4, text = '>', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,">")
                    if self.x == True:
                        self.listatotal[3].append(">")
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space4, text = '<', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,"<")
                    if self.x == True:
                        self.listatotal[3].append("<")
                        self.x = False

    def change_colors_left(self,event):
        widget = event.widget
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        widget.place(x=x,y=y)
        if x in range(550,620) and y in range(395,475):
            if self.x == True:
                self.lista_de_contadores.append(0)
                self.indice = self.lista_de_contadores[len(self.lista_de_contadores) - 1]
            if self.combinacion == 1:
                if widget == self.circle1:
                    self.white_space1.create_oval(0,50,50,0, fill = "blue", outline = "")
                    self.lista.pop(0)
                    self.lista.insert(0,"blue")
                    if self.x == True:
                        self.listatotal[0].append("blue")
                        self.x = False
                elif widget == self.circle2:
                    self.white_space1.create_oval(0,50,50,0, fill = "red", outline = "")
                    self.lista.pop(0)
                    self.lista.insert(0,"red")
                    if self.x == True:
                        self.listatotal[0].append("red")
                        self.x = False
                elif widget == self.circle3:
                    self.white_space1.create_oval(0,50,50,0, fill = "yellow", outline = "")
                    self.lista.pop(0)
                    self.lista.insert(0,"yellow")
                    if self.x == True:
                        self.listatotal[0].append("yellow")
                        self.x = False
                elif widget == self.circle4:
                    self.white_space1.create_oval(0,50,50,0, fill = "green", outline = "")
                    self.lista.pop(0)
                    self.lista.insert(0,"green")
                    if self.x == True:
                        self.listatotal[0].append("green")
                        self.x = False
                elif widget == self.circle5:
                    self.white_space1.create_oval(0,50,50,0, fill = "saddle brown", outline = "")
                    self.lista.pop(0)
                    self.lista.insert(0,"saddle brown")
                    if self.x == True:
                        self.listatotal[0].append("saddle brown")
                        self.x = False
                elif widget == self.circle6:
                    self.white_space1.create_oval(0,50,50,0, fill = "orange", outline = "")
                    self.lista.pop(0)
                    self.lista.insert(0,"orange")
                    if self.x == True:
                        self.listatotal[0].append("orange")
                        self.x = False
            elif self.combinacion == 2:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space1, text = "A", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,"A")
                    if self.x == True:
                        self.listatotal[0].append("A")
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space1, text = "B", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,"B")
                    if self.x == True:
                        self.listatotal[0].append("B")
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space1, text = "C", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,"C")
                    if self.x == True:
                        self.listatotal[0].append("C")
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space1, text = "D", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,"D")
                    if self.x == True:
                        self.listatotal[0].append("D")
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space1, text = "E", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,"E")
                    if self.x == True:
                        self.listatotal[0].append("E")
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space1, text = "F", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,"F")
                    if self.x == True:
                        self.listatotal[0].append("F")
                        self.x = False
            elif self.combinacion == 3:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space1, text = 1, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,1)
                    if self.x == True:
                        self.listatotal[0].append(1)
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space1, text = 2, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,2)
                    if self.x == True:
                        self.listatotal[0].append(2)
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space1, text = 3, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,3)
                    if self.x == True:
                        self.listatotal[0].append(3)
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space1, text = 4, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,4)
                    if self.x == True:
                        self.listatotal[0].append(4)
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space1, text = 5, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,5)
                    if self.x == True:
                        self.listatotal[0].append(5)
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space1, text = 6, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,6)
                    if self.x == True:
                        self.listatotal[0].append(6)
                        self.x = False
            else:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space1, text = '*', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,'*')
                    if self.x == True:
                        self.listatotal[0].append("*")
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space1, text = '+', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,'+')
                    if self.x == True:
                        self.listatotal[0].append('+')
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space1, text = '/', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,'/')
                    if self.x == True:
                        self.listatotal[0].append('/')
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space1, text = '-', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,'-')
                    if self.x == True:
                        self.listatotal[0].append('-')
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space1, text = '>', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,'>')
                    if self.x == True:
                        self.listatotal[0].append('>')
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space1, text = '<', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(0)
                    self.lista.insert(0,'<')
                    if self.x == True:
                        self.listatotal[0].append('<')
                        self.x = False
        elif x in range(630,680) and y in range(395,475):
            if self.x == True:
                self.lista_de_contadores.append(1)
                self.indice = self.lista_de_contadores[len(self.lista_de_contadores) - 1]
            if self.combinacion == 1:
                if widget == self.circle1:
                    self.white_space2.create_oval(0,50,50,0, fill = "blue", outline = "")
                    self.lista.pop(1)
                    self.lista.insert(1,"blue")
                    if self.x == True:
                        self.listatotal[1].append("blue")
                        self.x = False
                elif widget == self.circle2:
                    self.white_space2.create_oval(0,50,50,0, fill = "red", outline = "")
                    self.lista.pop(1)
                    self.lista.insert(1,"red")
                    if self.x == True:
                        self.listatotal[1].append("red")
                        self.x = False
                elif widget == self.circle3:
                    self.white_space2.create_oval(0,50,50,0, fill = "yellow", outline = "")
                    self.lista.pop(1)
                    self.lista.insert(1,"yellow")
                    if self.x == True:
                        self.listatotal[1].append("yellow")
                        self.x = False
                elif widget == self.circle4:
                    self.white_space2.create_oval(0,50,50,0, fill = "green", outline = "")
                    self.lista.pop(1)
                    self.lista.insert(1,"green")
                    if self.x == True:
                        self.listatotal[1].append("green")
                        self.x = False
                elif widget == self.circle5:
                    self.white_space2.create_oval(0,50,50,0, fill = "saddle brown", outline = "")
                    self.lista.pop(1)
                    self.lista.insert(1,"saddle brown")
                    if self.x == True:
                        self.listatotal[1].append("saddle brown")
                        self.x = False
                elif widget == self.circle6:
                    self.white_space2.create_oval(0,50,50,0, fill = "orange", outline = "")
                    self.lista.pop(1)
                    self.lista.insert(1,"orange")
                    if self.x == True:
                        self.listatotal[1].append("orange")
                        self.x = False
            elif self.combinacion == 2:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space2, text = "A", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,"A")
                    if self.x == True:
                        self.listatotal[1].append("A")
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space2, text = "B", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,"B")
                    if self.x == True:
                        self.listatotal[1].append("B")
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space2, text = "C", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,"C")
                    if self.x == True:
                        self.listatotal[1].append("C")
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space2, text = "D", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,"D")
                    if self.x == True:
                        self.listatotal[1].append("D")
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space2, text = "E", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,"E")
                    if self.x == True:
                        self.listatotal[1].append("E")
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space2, text = "F", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,"F")
                    if self.x == True:
                        self.listatotal[1].append("F")
                        self.x = False
            elif self.combinacion == 3:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space2, text = 1, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,1)
                    if self.x == True:
                        self.listatotal[1].append(1)
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space2, text = 2, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,2)
                    if self.x == True:
                        self.listatotal[1].append(2)
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space2, text = 3, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,3)
                    if self.x == True:
                        self.listatotal[1].append(3)
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space2, text = 4, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,4)
                    if self.x == True:
                        self.listatotal[1].append(4)
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space2, text = 5, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,5)
                    if self.x == True:
                        self.listatotal[1].append(5)
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space2, text = 6, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,6)
                    if self.x == True:
                        self.listatotal[1].append(6)
                        self.x = False
            else:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space2, text = '*', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,'*')
                    if self.x == True:
                        self.listatotal[1].append('*')
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space2, text = '+', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,'+')
                    if self.x == True:
                        self.listatotal[1].append('+')
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space2, text = '/', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,'/')
                    if self.x == True:
                        self.listatotal[1].append('/')
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space2, text = '-', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,'-')
                    if self.x == True:
                        self.listatotal[1].append('-')
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space2, text = '>', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,'>')
                    if self.x == True:
                        self.listatotal[1].append('>')
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space2, text = '<', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(1)
                    self.lista.insert(1,'<')
                    if self.x == True:
                        self.listatotal[1].append('<')
                        self.x = False
        elif x in range(690,740) and y in range(395,475):
            if self.x == True:
                self.lista_de_contadores.append(2)
                self.indice = self.lista_de_contadores[len(self.lista_de_contadores) - 1]
            if self.combinacion == 1:
                if widget == self.circle1:
                    self.white_space3.create_oval(0,50,50,0, fill = "blue", outline = "")
                    self.lista.pop(2)
                    self.lista.insert(2,"blue")
                    if self.x == True:
                        self.listatotal[2].append("blue")
                        self.x = False
                elif widget == self.circle2:
                    self.white_space3.create_oval(0,50,50,0, fill = "red", outline = "")
                    self.lista.pop(2)
                    self.lista.insert(2,"red")
                    if self.x == True:
                        self.listatotal[2].append("red")
                        self.x = False
                elif widget == self.circle3:
                    self.white_space3.create_oval(0,50,50,0, fill = "yellow", outline = "")
                    self.lista.pop(2)
                    self.lista.insert(2,"yellow")
                    if self.x == True:
                        self.listatotal[2].append("yellow")
                        self.x = False
                elif widget == self.circle4:
                    self.white_space3.create_oval(0,50,50,0, fill = "green", outline = "")
                    self.lista.pop(2)
                    self.lista.insert(2,"green")
                    if self.x == True:
                        self.listatotal[2].append("green")
                        self.x = False
                elif widget == self.circle5:
                    self.white_space3.create_oval(0,50,50,0, fill = "saddle brown", outline = "")
                    self.lista.pop(2)
                    self.lista.insert(2,"saddle brown")
                    if self.x == True:
                        self.listatotal[2].append("saddle brown")
                        self.x = False
                elif widget == self.circle6:
                    self.white_space3.create_oval(0,50,50,0, fill = "orange", outline = "")
                    self.lista.pop(2)
                    self.lista.insert(2,"orange")
                    if self.x == True:
                        self.listatotal[2].append("orange")
                        self.x = False
            elif self.combinacion == 2:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space3, text = "A", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,"A")
                    if self.x == True:
                        self.listatotal[2].append("A")
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space3, text = "B", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,"B")
                    if self.x == True:
                        self.listatotal[2].append("B")
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space3, text = "C", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,"C")
                    if self.x == True:
                        self.listatotal[2].append("C")
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space3, text = "D", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,"D")
                    if self.x == True:
                        self.listatotal[2].append("D")
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space3, text = "E", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,"E")
                    if self.x == True:
                        self.listatotal[2].append("E")
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space3, text = "F", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,"F")
                    if self.x == True:
                        self.listatotal[2].append("F")
                        self.x = False
            elif self.combinacion == 3:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space3, text = 1, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,1)
                    if self.x == True:
                        self.listatotal[2].append(1)
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space3, text = 2, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,2)
                    if self.x == True:
                        self.listatotal[2].append(2)
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space3, text = 3, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,3)
                    if self.x == True:
                        self.listatotal[2].append(3)
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space3, text = 4, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,4)
                    if self.x == True:
                        self.listatotal[2].append(4)
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space3, text = 5, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,5)
                    if self.x == True:
                        self.listatotal[2].append(5)
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space3, text = 6, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,6)
                    if self.x == True:
                        self.listatotal[2].append(6)
                        self.x = False
            else:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space3, text = '*', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,'*')
                    if self.x == True:
                        self.listatotal[2].append('*')
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space3, text = '+', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,'+')
                    if self.x == True:
                        self.listatotal[2].append('+')
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space3, text = '/', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,'/')
                    if self.x == True:
                        self.listatotal[2].append('/')
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space3, text = '-', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,'-')
                    if self.x == True:
                        self.listatotal[2].append('-')
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space3, text = '>', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,'>')
                    if self.x == True:
                        self.listatotal[2].append('>')
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space3, text = '<', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(2)
                    self.lista.insert(2,'<')
                    if self.x == True:
                        self.listatotal[2].append('<')
                        self.x = False
        elif x in range(750,800) and y in range(395,475):
            if self.x == True:
                self.lista_de_contadores.append(3)
                self.indice = self.lista_de_contadores[len(self.lista_de_contadores) - 1]
            if self.combinacion == 1:
                if widget == self.circle1:
                    self.white_space4.create_oval(0,50,50,0, fill = "blue", outline = "")
                    self.lista.pop(3)
                    self.lista.insert(3,"blue")
                    if self.x == True:
                        self.listatotal[3].append("blue")
                        self.x = False
                elif widget == self.circle2:
                    self.white_space4.create_oval(0,50,50,0, fill = "red", outline = "")
                    self.lista.pop(3)
                    self.lista.insert(3,"red")
                    if self.x == True:
                        self.listatotal[3].append("red")
                        self.x = False
                elif widget == self.circle3:
                    self.white_space4.create_oval(0,50,50,0, fill = "yellow", outline = "")
                    self.lista.pop(3)
                    self.lista.insert(3,"yellow")
                    if self.x == True:
                        self.listatotal[3].append("yellow")
                        self.x = False
                elif widget == self.circle4:
                    self.white_space4.create_oval(0,50,50,0, fill = "green", outline = "")
                    self.lista.pop(3)
                    self.lista.insert(3,"green")
                    if self.x == True:
                        self.listatotal[3].append("green")
                        self.x = False
                elif widget == self.circle5:
                    self.white_space4.create_oval(0,50,50,0, fill = "saddle brown", outline = "")
                    self.lista.pop(3)
                    self.lista.insert(3,"saddle brown")
                    if self.x == True:
                        self.listatotal[3].append("saddle brown")
                        self.x = False
                elif widget == self.circle6:
                    self.white_space4.create_oval(0,50,50,0, fill = "orange", outline = "")
                    self.lista.pop(3)
                    self.lista.insert(3,"orange")
                    if self.x == True:
                        self.listatotal[3].append("orange")
                        self.x = False
            elif self.combinacion == 2:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space4, text = "A", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,"A")
                    if self.x == True:
                        self.listatotal[3].append("A")
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space4, text = "B", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,"B")
                    if self.x == True:
                        self.listatotal[3].append("B")
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space4, text = "C", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,"C")
                    if self.x == True:
                        self.listatotal[3].append("C")
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space4, text = "D", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,"D")
                    if self.x == True:
                        self.listatotal[3].append("D")
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space4, text = "E", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,"E")
                    if self.x == True:
                        self.listatotal[3].append("E")
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space4, text = "F", fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,"F")
                    if self.x == True:
                        self.listatotal[3].append("F")
                        self.x = False
            elif self.combinacion == 3:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space4, text = 1, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,1)
                    if self.x == True:
                        self.listatotal[3].append(1)
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space4, text = 2, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,2)
                    if self.x == True:
                        self.listatotal[3].append(2)
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space4, text = 3, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,3)
                    if self.x == True:
                        self.listatotal[3].append(3)
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space4, text = 4, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,4)
                    if self.x == True:
                        self.listatotal[3].append(4)
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space4, text = 5, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,5)
                    if self.x == True:
                        self.listatotal[3].append(5)
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space4, text = 6, fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,6)
                    if self.x == True:
                        self.listatotal[3].append(6)
                        self.x = False
            else:
                if widget == self.circle1:
                    self.circle_text = tk.Label(self.white_space4, text = '*', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,'*')
                    if self.x == True:
                        self.listatotal[3].append('*')
                        self.x = False
                elif widget == self.circle2:
                    self.circle_text = tk.Label(self.white_space4, text = '+', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,'+')
                    if self.x == True:
                        self.listatotal[3].append('+')
                        self.x = False
                elif widget == self.circle3:
                    self.circle_text = tk.Label(self.white_space4, text = '/', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,'/')
                    if self.x == True:
                        self.listatotal[3].append('/')
                        self.x = False
                elif widget == self.circle4:
                    self.circle_text = tk.Label(self.white_space4, text = '-', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,'-')
                    if self.x == True:
                        self.listatotal[3].append('-')
                        self.x = False
                elif widget == self.circle5:
                    self.circle_text = tk.Label(self.white_space4, text = '>', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,'>')
                    if self.x == True:
                        self.listatotal[3].append('>')
                        self.x = False
                elif widget == self.circle6:
                    self.circle_text = tk.Label(self.white_space4, text = '<', fg = "Black", bg = "white")
                    self.circle_text.place(x = 18, y = 15)
                    self.lista.pop(3)
                    self.lista.insert(3,'<')
                    if self.x == True:
                        self.listatotal[3].append('<')
                        self.x = False
    #Validad nombre de usuario
    def validate_name(self,event):
        self.nombre1 = self.nombre.get()
        if len(self.nombre1) > 2 and len(self.nombre1) <= 30 and self.nombre1.isspace() == False:
            self.entrada_nombre.destroy()
            self.label_jugador = Label(self.canvas, text = self.nombre1, font=('Games',15), fg='white', bg = 'gray25')
            self.label_jugador.place(x=600,y=650,width=300,height=30)
            self.booleano = True
            return self.booleano 
        else:
            tkinter.messagebox.showinfo("MASTERMIND","ERROR DEBE ESCRIBIR UN NOMBRE DE ENTRE 4 y 40 CARACTERES")
    #Iniciar el juego
    def start(self):
        if self.booleano == True:
            now = datetime.now()
            self.date = [now.year,now.month,now.day]
            self.hour = [now.hour,now.minute]
            self.data()
            self.posiciones()
            self.dificult()
            if self.cronometro == 1 or self.cronometro == 3 or self.cronometro == 4:
                self.chronometer()

            if self.combinacion == 1:
                self.combinations = random.choices(colors, k = 4)
            elif self.combinacion == 2:
                self.combinations = random.choices(letters, k = 4)
            elif self.combinacion == 3:
                self.combinations = random.choices(numbers, k = 4)
            else:
                self.combinations = random.choices(simbols, k = 4)
            print(self.combinations)

            self.inicio_juego.destroy()

            self.calificar = Button(self.canvas, text ='CALIFICAR',font=('Games',15) ,highlightbackground = '#F0FF00', highlightthickness = 30, command = self.qualify_play)
            self.calificar.place(x = 150, y = 480,width = 150, height = 50)

            self.deshacer = Button(self.canvas, text ='DESHACER',font=('Games',15) ,highlightbackground = '#F0FF00', highlightthickness = 30, command = self.des_hacer)
            self.deshacer.place(x = 350, y = 515,width = 150, height = 50)

            self.rehacer = Button(self.canvas, text ='REHACER',font=('Games',15) ,highlightbackground = '#F0FF00', highlightthickness = 30, command = self.re_hacer)
            self.rehacer.place(x = 550, y = 515,width = 150, height = 50)
            
            self.cancelar_juego = Button(self.canvas, text ='CANCELAR JUEGO',font=('Games',15) ,highlightbackground = '#FF0000', highlightthickness = 30, command = self.go_back)
            self.cancelar_juego.place(x = 150, y = 550,width = 150, height = 50)

            self.guardar_juego = Button(self.canvas, text ='GUARDAR JUEGO',font=('Games',15) ,highlightbackground = '#FF8F00', highlightthickness = 30, command = self.save_game)
            self.guardar_juego.place(x = 750, y = 480,width = 150, height = 50)

            self.cargar_juego = Button(self.canvas, text ='CARGAR JUEGO',font=('Games',15) ,highlightbackground = '#0C00FF', highlightthickness = 30, command = self.load_game)
            self.cargar_juego.place(x = 750, y = 550,width = 150, height = 50)
        else:
            tkinter.messagebox.showinfo("MASTERMIND","ERROR DEBE REGISTRAR EL NOMBRE DEL JUGADOR") 

    def go_back(self):
        self.canvas_atras = Canvas(width=1000,height=700,highlightthickness=0, relief='ridge',
                             bg = 'gray25')
        self.canvas_atras.place(x = 0, y = 0)

        self.label = Label(self.canvas_atras, text='¿ESTÁ SEGURO DE CANCELAR EL JUEGO (SI o NO) ?',font=('Games',25), fg='red', bg = 'dimgray') 
        self.label.place(x=170,y=300,width=650,height=50) #Titulo de la pantalla.

        self.calificar = Button(self.canvas_atras, text ='SI',font=('Games',15) ,highlightbackground = '#F0FF00', highlightthickness = 30, command = self.go_back1 )
        self.calificar.place(x = 150, y = 500,width = 150, height = 50)

        self.cargar_juego = Button(self.canvas_atras, text ='NO',font=('Games',15) ,highlightbackground = '#0C00FF', highlightthickness = 30, command = self.negation)
        self.cargar_juego.place(x = 750, y = 500,width = 150, height = 50)
    
    def go_back1(self):
        self.canvas_atras.destroy()
        self.canvas.destroy()
    
    def negation(self):
        self.canvas_atras.destroy()

    def to_blink(self):
        self.label_perder.config(fg='red')
        self.label_perder.config(fg='white')
        self.to_blink()

    def loss(self):
        self.canvas.destroy()
        self.canvas_loss = Canvas(width=1000,height=700,highlightthickness=0, relief='ridge',
                             bg = 'gray25')
        self.canvas_loss.place(x = 0, y = 0)

        self.label_perder = Label(self.canvas_loss, text="PERDIO",font=('Games',25), fg='red', bg = 'gray25') 
        self.label_perder.place(x=130,y=300,width=750,height=50) #Titulo de la pantalla.

        self.calificar = Button(self.canvas_loss, text ='SALIR',font=('Games',15) ,highlightbackground = '#F0FF00', highlightthickness = 30, command = self.salir)
        self.calificar.place(x = 150, y = 500,width = 150, height = 50)

        self.cargar_juego = Button(self.canvas_loss, text ='REINICIAR',font=('Games',15) ,highlightbackground = '#0C00FF', highlightthickness = 30, command = self.reiniciar)
        self.cargar_juego.place(x = 750, y = 500,width = 150, height = 50)

    def salir(self):
        self.canvas_loss.destroy()
        self.canvas.destroy()

    def win(self):
        if self.cronometro == 1 or self.cronometro == 3 or self.cronometro == 4:
            if self.dificultad == 4:
                if self.grado_dificultad == 0:
                    self.dificultad = 1
                elif self.grado_dificultad == 1:
                    self.dificultad = 2
                else:
                    self.dificultad = 3
                lista_de_datos = [self.h,self.m,self.s,self.dificultad,self.nombre1,self.jugadas,self.date,self.hour,self.lista_de_horas]
                settings = open("mastermind2022top10.dat","ab")
                pickle.dump(lista_de_datos,settings)
                settings.close()
                self.dificultad = 4
            else:
                lista_de_datos = [self.h,self.m,self.s,self.dificultad,self.nombre1,self.jugadas,self.date,self.hour,self.lista_de_horas]
                settings = open("mastermind2022top10.dat","ab")
                pickle.dump(lista_de_datos,settings)
                settings.close()

        if self.dificultad == 4:
            self.lista = [[],[],[],[]]
            self.booleano = True
            self.contador = 0
            self.h = 0
            self.m = 0
            self.s = 0
            self.contador2 = 0
            self.validador = 0
            self.contador3 = 0
            self.jugadas = []
            self.calificadas = []
            self.lista_de_horas = []
            self.contador4 = 0
            self.acumulador1 = 0
            self.acumulador2 = 0
            self.acumulador3 = 0
            self.x = True
            self.listatotal = [[],[],[],[]]
            self.lista_copia = [[],[],[],[]]
            self.lista_cont_copia = []
            self.lista_de_contadores = []
            self.indice = 0
            self.sub_indice = 0
            self.indice_copia = 0
            self.sub_indice_copia = 0
            if self.grado_dificultad == 0:
                self.grado_dificultad = 1
            elif self.grado_dificultad == 1:
                self.grado_dificultad = 2
            self.circle1.destroy()
            self.circle2.destroy()
            self.circle3.destroy()
            self.circle4.destroy()
            self.circle5.destroy()
            self.circle6.destroy()
            self.white_space1.destroy()
            self.white_space2.destroy()
            self.white_space3.destroy()
            self.white_space4.destroy()
            self.white_space5.destroy()
            self.white_space6.destroy()
            self.white_space7.destroy()
            self.white_space8.destroy()
            self.white_space9.destroy()
            self.white_space10.destroy()
            self.white_space11.destroy()
            self.white_space12.destroy()
            self.white_space13.destroy()
            self.white_space14.destroy()
            self.white_space15.destroy()
            self.white_space16.destroy()
            self.white_space17.destroy()
            self.white_space18.destroy()
            self.white_space19.destroy()
            self.white_space20.destroy()
            self.white_space21.destroy()
            self.white_space22.destroy()
            self.white_space23.destroy()
            self.white_space24.destroy()
            self.white_space25.destroy()
            self.white_space26.destroy()
            self.white_space27.destroy()
            self.white_space28.destroy()
            self.white_space29.destroy()
            self.white_space30.destroy()
            self.white_space31.destroy()
            self.white_space32.destroy()
            self.white_space33.destroy()
            self.white_space34.destroy()
            self.white_space35.destroy()
            self.white_space36.destroy()
            self.calificador.destroy()
            self.calificador1.destroy()
            self.calificador2.destroy()
            self.calificador3.destroy()
            self.calificador4.destroy()
            self.calificador5.destroy()
            self.calificador6.destroy()
            self.calificador7.destroy()
            self.calificador8.destroy()
            self.calificador9.destroy()
            self.calificador10.destroy()
            self.calificador11.destroy()
            self.calificador12.destroy()
            self.calificador13.destroy()
            self.calificador14.destroy()
            self.calificador15.destroy()
            self.calificador16.destroy()
            self.calificador17.destroy()
            self.calificador18.destroy()
            self.calificador19.destroy()
            self.calificador20.destroy()
            self.calificador21.destroy()
            self.calificador22.destroy()
            self.calificador23.destroy()
            self.calificador24.destroy()
            self.calificador25.destroy()
            self.calificador26.destroy()
            self.calificador27.destroy()
            self.calificador28.destroy()
            self.calificador29.destroy()
            self.calificador30.destroy()
            self.calificador31.destroy()
            try:
                self.horas.destroy()
                self.horas_numeros.destroy()
                self.minutos.destroy()
                self.minutos_numeros.destroy()
                self.segundos.destroy()
                self.segundos_numeros.destroy()
            except:
                pass
            self.start()
        else:
            self.canvas.destroy()
            self.canvas_loss = Canvas(width=1000,height=700,highlightthickness=0, relief='ridge',
                                bg = 'gray25')
            self.canvas_loss.place(x = 0, y = 0)

            self.label_perder = Label(self.canvas_loss, text="¡JUEGO TERMINADO: G A N Ó!",font=('Games',25), fg='red', bg = 'gray25') 
            self.label_perder.place(x=130,y=300,width=750,height=50) #Titulo de la pantalla.

            self.calificar = Button(self.canvas_loss, text ='SALIR',font=('Games',15) ,highlightbackground = '#F0FF00', highlightthickness = 30, command = self.salir)
            self.calificar.place(x = 150, y = 500,width = 150, height = 50)

            self.cargar_juego = Button(self.canvas_loss, text ='REINICIAR',font=('Games',15) ,highlightbackground = '#0C00FF', highlightthickness = 30, command = self.reiniciar)
            self.cargar_juego.place(x = 750, y = 500,width = 150, height = 50)

    def reiniciar(self):
        self.canvas_loss.destroy()
        ventana_juego(self.master)

    def menu(self):
        self.canvas_perder.destroy()
        self.canvas.destroy()

    def time(self):
        self.s += 1
        if self.s == 60:
            self.m += 1
            self.minutos_numeros.config(text = str(self.m))
            self.s = 0
            if self.m == 60:
                self.h += 1
                self.horas_numeros.config(text = str(self.h))
                self.m = 0
        self.segundos_numeros.config(text = str(self.s))
        if self.cronometro == 3:
            if self.h1 == self.h and self.m1 == self.m and self.s1 == self.s:
                self.canvas.destroy()
                self.canvas_perder = Canvas(width=1000,height=700,highlightthickness=0, relief='ridge',
                             bg = 'gray25')
                self.canvas_perder.place(x = 0, y = 0)

                self.label_perder = Label(self.canvas_perder, text="JUEGO TERMINADO: TIEMPO DE LA ÚLTIMA JUGADA EXCEDIDO",font=('Games',25), fg='red', bg = 'gray25') 
                self.label_perder.place(x=130,y=300,width=750,height=50) #Titulo de la pantalla.

                self.cancelar_juego = Button(self.canvas_perder, text ="SALIR",font=('Games',15) ,highlightbackground = '#FF0000', highlightthickness = 30, command = self.menu)
                self.cancelar_juego.place(x = 350, y = 500,width = 150, height = 50)
                return

        if self.cronometro == 4:
            if self.h1 == self.h and self.m1 == self.m and self.s1 == self.s:
                self.canvas.destroy()
                self.canvas_perder = Canvas(width=1000,height=700,highlightthickness=0, relief='ridge',
                             bg = 'gray25')
                self.canvas_perder.place(x = 0, y = 0)

                self.label_perder = Label(self.canvas_perder, text="JUEGO TERMINADO: TIEMPO DE JUEGO EXCEDIDO",font=('Games',25), fg='red', bg = 'gray25') 
                self.label_perder.place(x=130,y=300,width=750,height=50) #Titulo de la pantalla.

                self.cancelar_juego = Button(self.canvas_perder, text ="SALIR",font=('Games',15) ,highlightbackground = '#FF0000', highlightthickness = 30, command = self.menu)
                self.cancelar_juego.place(x = 350, y = 500,width = 150, height = 50)
                return

        self.segundos_numeros.after(1000,self.time)

    def chronometer(self):
        if self.cronometro == 1 or self.cronometro == 3 or self.cronometro == 4:

            self.horas = Label(self.canvas, text='Horas',font=('Games',15), fg='white', bg = 'gray25')
            self.horas.place(x = 150, y = 600,width = 150, height = 50)
            self.horas_numeros = Label(self.canvas, text= self.h ,font=('Games',15), fg='white', bg = 'gray25')
            self.horas_numeros.place(x = 150, y = 650,width = 150, height = 50)

            self.minutos = Label(self.canvas, text='Minutos',font=('Games',15), fg='white', bg = 'gray25')
            self.minutos.place(x = 250, y = 600,width = 150, height = 50)
            self.minutos_numeros = Label(self.canvas, text= self.m ,font=('Games',15), fg='white', bg = 'gray25')
            self.minutos_numeros.place(x = 250, y = 650,width = 150, height = 50)

            self.segundos = Label(self.canvas, text='Segundos',font=('Games',15), fg='white', bg = 'gray25')
            self.segundos.place(x = 351, y = 600,width = 150, height = 50)
            self.segundos_numeros = Label(self.canvas, text= self.s ,font=('Games',15), fg='white', bg = 'gray25')
            self.segundos_numeros.place(x = 351, y = 650,width = 150, height = 50)

            self.time()
        else:
            pass

    def des_hacer(self):
# The above code is the undo function. It is undoing the last move made by the user.
        try:
            self.indice = self.lista_de_contadores[len(self.lista_de_contadores) - 1]
            self.sub_indice = self.listatotal[self.indice]
            if len(self.sub_indice) == 1:
                self.lista_copia[self.indice].append(self.sub_indice[len(self.sub_indice) - 1])
                self.listatotal[self.indice].pop()
                self.lista_cont_copia.append(self.indice)
                self.lista_de_contadores.pop(len(self.lista_de_contadores) - 1)
                self.lista.pop(self.indice)
                self.lista.insert(self.indice,[])
                if self.combinacion == 2 or self.combinacion == 3 or self.combinacion == 4:
                    if self.indice== 0:
                        self.white_space1 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                        self.white_space1.create_oval(0,50,50,0, fill = "white", outline = "")
                        if self.posicion == 1:
                            self.white_space1.place(x = 200,y = 410)
                        else:
                            self.white_space1.place(x = 570,y = 410)
                    elif self.indice == 1:
                        self.white_space2 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                        self.white_space2.create_oval(0,50,50,0, fill = "white", outline = "")
                        if self.posicion == 1:
                            self.white_space2.place(x = 260, y = 410)
                        else:
                            self.white_space2.place(x = 630, y = 410)
                    elif self.indice == 2:
                        self.white_space3 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                        self.white_space3.create_oval(0,50,50,0, fill = "white", outline = "")
                        if self.posicion == 1:
                            self.white_space3.place(x = 320,y = 410)
                        else:
                            self.white_space3.place(x = 690,y = 410)
                    else:
                        self.white_space4 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                        self.white_space4.create_oval(0,50,50,0, fill = "white", outline = "")
                        if self.posicion == 1:
                            self.white_space4.place(x = 380,y = 410)
                        else:
                            self.white_space4.place(x = 750,y = 410)
                else:
                    if self.indice == 0:
                        self.white_space1.create_oval(0,50,50,0, fill = "white", outline = "")
                    elif self.indice == 1:
                        self.white_space2.create_oval(0,50,50,0, fill = "white", outline = "")
                    elif self.indice == 2:
                        self.white_space3.create_oval(0,50,50,0, fill = "white", outline = "")
                    else:
                        self.white_space4.create_oval(0,50,50,0, fill = "white", outline = "")
            else:
                self.lista_copia[self.indice].append(self.sub_indice[len(self.sub_indice) - 1])
                self.sub_indice.pop(len(self.sub_indice) - 1)
                self.sub_indice = self.sub_indice[len(self.sub_indice) - 1]
                self.lista_cont_copia.append(self.indice)
                self.lista_de_contadores.pop(len(self.lista_de_contadores) - 1)
                if self.combinacion == 2 or self.combinacion == 3 or self.combinacion == 4:
                    if self.indice == 0:
                        self.circle2_text = tk.Label(self.white_space1, text = self.sub_indice, fg = "Black", bg = "white")
                        self.circle2_text.place(x = 18, y = 15)
                        self.lista.pop(self.indice)
                        self.lista.insert(self.indice,self.sub_indice)
                    elif self.indice == 1:
                        self.circle2_text = tk.Label(self.white_space2, text = self.sub_indice, fg = "Black", bg = "white")
                        self.circle2_text.place(x = 18, y = 15)
                        self.lista.pop(self.indice)
                        self.lista.insert(self.indice,self.sub_indice)
                    elif self.indice == 2:
                        self.circle2_text = tk.Label(self.white_space3, text = self.sub_indice, fg = "Black", bg = "white")
                        self.circle2_text.place(x = 18, y = 15)
                        self.lista.pop(self.indice)
                        self.lista.insert(self.indice,self.sub_indice)
                    else:
                        self.circle2_text = tk.Label(self.white_space4, text = self.sub_indice, fg = "Black", bg = "white")
                        self.circle2_text.place(x = 18, y = 15)
                        self.lista.pop(self.indice)
                        self.lista.insert(self.indice,self.sub_indice)
                else:
                    if self.indice == 0:
                        self.white_space1.create_oval(0,50,50,0, fill = self.sub_indice, outline = "")
                        self.lista.pop(self.indice)
                        self.lista.insert(self.indice,self.sub_indice)
                    elif self.indice == 1:
                        self.white_space2.create_oval(0,50,50,0, fill = self.sub_indice, outline = "")
                        self.lista.pop(self.indice)
                        self.lista.insert(self.indice,self.sub_indice)
                    elif self.indice == 2:
                        self.white_space3.create_oval(0,50,50,0, fill = self.sub_indice, outline = "")
                        self.lista.pop(self.indice)
                        self.lista.insert(self.indice,self.sub_indice)
                    else:
                        self.white_space4.create_oval(0,50,50,0, fill = self.sub_indice, outline = "")
                        self.lista.pop(self.indice)
                        self.lista.insert(self.indice,self.sub_indice)
        except:
           tkinter.messagebox.showinfo("MASTERMIND","ERROR NO HAY MOVIMIENTOS PREVIOS")
    
    def re_hacer(self):
# The above code is the undo function. It is used to undo the last move made by the user.
        try:
            self.indice_copia = self.lista_cont_copia[len(self.lista_cont_copia) - 1]
            self.sub_indice_copia = self.lista_copia[self.indice_copia]
            self.sub_indice_copia = self.sub_indice_copia[len(self.sub_indice_copia) - 1]
            self.lista_de_contadores.append(self.indice_copia)
            self.lista_cont_copia.pop(len(self.lista_cont_copia) - 1)
            self.listatotal[self.indice_copia].append(self.sub_indice_copia)
            self.lista_copia[self.indice_copia].pop(len(self.lista_copia[self.indice_copia]) - 1)
            if self.combinacion == 2 or self.combinacion == 3 or self.combinacion == 4:
                    if self.indice_copia == 0:
                        self.circle2_text = tk.Label(self.white_space1, text = self.sub_indice_copia, fg = "Black", bg = "white")
                        self.circle2_text.place(x = 18, y = 15)
                        self.lista.pop(self.indice_copia)
                        self.lista.insert(self.indice_copia,self.sub_indice_copia)
                    elif self.indice_copia == 1:
                        self.circle2_text = tk.Label(self.white_space2, text = self.sub_indice_copia, fg = "Black", bg = "white")
                        self.circle2_text.place(x = 18, y = 15)
                        self.lista.pop(self.indice_copia)
                        self.lista.insert(self.indice_copia,self.sub_indice_copia)
                    elif self.indice_copia == 2:
                        self.circle2_text = tk.Label(self.white_space3, text = self.sub_indice_copia, fg = "Black", bg = "white")
                        self.circle2_text.place(x = 18, y = 15)
                        self.lista.pop(self.indice_copia)
                        self.lista.insert(self.indice_copia,self.sub_indice_copia)
                    else:
                        self.circle2_text = tk.Label(self.white_space4, text = self.sub_indice_copia, fg = "Black", bg = "white")
                        self.circle2_text.place(x = 18, y = 15)
                        self.lista.pop(self.indice_copia)
                        self.lista.insert(self.indice_copia,self.sub_indice_copia)
            else:
                if self.indice_copia == 0:
                    self.white_space1.create_oval(0,50,50,0, fill =  self.sub_indice_copia, outline = "")
                    self.lista.pop(self.indice_copia)
                    self.lista.insert(self.indice_copia,self.sub_indice_copia)
                elif self.indice_copia == 1:
                    self.white_space2.create_oval(0,50,50,0, fill = self.sub_indice_copia, outline = "")
                    self.lista.pop(self.indice_copia)
                    self.lista.insert(self.indice_copia,self.sub_indice_copia)
                elif self.indice_copia == 2:
                    self.white_space3.create_oval(0,50,50,0, fill = self.sub_indice_copia, outline = "")
                    self.lista.pop(self.indice_copia)
                    self.lista.insert(self.indice_copia,self.sub_indice_copia)
                else:
                    self.white_space4.create_oval(0,50,50,0, fill = self.sub_indice_copia, outline = "")
                    self.lista.pop(self.indice_copia)
                    self.lista.insert(self.indice_copia,self.sub_indice_copia)
        except:
            tkinter.messagebox.showinfo("MASTERMIND","ERROR NO HAY MOVIMIENTOS PREVIOS")

    def qualify_play(self):
# The above code is validating if the user has filled all the spaces, if the user has filled all the
# spaces, the code will check if the user has won or not, if the user has won, the code will call the
# win function, if the user has not won, the code will check if the user is playing with colors or
# numbers, if the user is playing with colors, the code will place the colors in the white spaces, if
# the user is playing with numbers, the code will place the numbers in the white spaces, after that,
# the code will check if the user has
        if validate_spaces(self.lista):
            self.contador += 1
            if self.cronometro == 3:
                self.h = 0
                self.m = 0
                self.s = 0
            self.jugadas.append(self.lista)
            if self.lista_de_horas:
                datos1 = self.lista_de_horas[self.contador4]
                self.acumulador1 = self.acumulador1 + datos1[0]
                self.acumulador2 = self.acumulador2 + datos1[1]
                self.acumulador3 = self.acumulador3 + datos1[2]
                horas = abs(self.acumulador1 - self.h)
                minutos = abs(self.acumulador2 - self.m)
                segundos = abs(self.acumulador3 - self.s)
                self.contador4 += 1
                datson = [horas,minutos,segundos]
                self.lista_de_horas.append(datson)
            else:
                datos = [self.h,self.m,self.s]
                self.lista_de_horas.append(datos)
            self.listatotal = [[],[],[],[]]
            self.lista_copia = [[],[],[],[]]
            self.lista_cont_copia = []
            self.lista_de_contadores = []
            self.indice = 0
            self.sub_indice = 0
            self.indice_copia = 0
            self.sub_indice_copia = 0
            lista = self.lista
            copia_lista = lista
            if self.lista == self.combinations:
                self.win()
            else:
                if self.combinacion == 1:
                    self.white_spaces[self.contador2].create_oval(0,30,30,0, fill = lista[0] , outline = "")
                    self.white_space1.create_oval(0,50,50,0, fill = "white", outline = "")
                    self.contador2 += 1
                    self.white_spaces[self.contador2].create_oval(0,30,30,0, fill = lista[1] , outline = "")
                    self.white_space2.create_oval(0,50,50,0, fill = "white", outline = "")
                    self.contador2 += 1
                    self.white_spaces[self.contador2].create_oval(0,30,30,0, fill = lista[2] , outline = "")
                    self.white_space3.create_oval(0,50,50,0, fill = "white", outline = "")
                    self.contador2 += 1
                    self.white_spaces[self.contador2].create_oval(0,30,30,0, fill = lista[3] , outline = "")
                    self.white_space4.create_oval(0,50,50,0, fill = "white", outline = "")
                    self.contador2 += 1
                elif self.combinacion == 2 or self.combinacion == 3 or self.combinacion == 4:
                    self.white_spaces[self.contador2].create_oval(0,30,30,0, outline = "white")
                    self.circle2_text = tk.Label(self.white_spaces[self.contador2], text = lista[0], fg = "white", bg = "gray25")
                    self.circle2_text.place(x = 8, y = 3)
                    self.white_space1 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                    self.white_space1.create_oval(0,50,50,0, fill = "white", outline = "")
                    if self.posicion == 1:
                        self.white_space1.place(x = 200,y = 410)
                    else:
                        self.white_space1.place(x = 570,y = 410)
                    self.contador2 += 1

                    self.white_spaces[self.contador2].create_oval(0,30,30,0, outline = "white")
                    self.circle2_text = tk.Label(self.white_spaces[self.contador2], text = lista[1], fg = "white", bg = "gray25")
                    self.circle2_text.place(x = 8, y = 3)
                    self.white_space2 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                    self.white_space2.create_oval(0,50,50,0, fill = "white", outline = "")
                    if self.posicion == 1:
                        self.white_space2.place(x = 260, y = 410)
                    else:
                        self.white_space2.place(x = 630, y = 410)
                    self.contador2 += 1

                    self.white_spaces[self.contador2].create_oval(0,30,30,0, outline = "white")
                    self.circle2_text = tk.Label(self.white_spaces[self.contador2], text = lista[2], fg = "white", bg = "gray25")
                    self.circle2_text.place(x = 8, y = 3)
                    self.white_space3 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                    self.white_space3.create_oval(0,50,50,0, fill = "white", outline = "")
                    if self.posicion == 1:
                        self.white_space3.place(x = 320,y = 410)
                    else:
                        self.white_space3.place(x = 690,y = 410)
                    self.contador2 += 1

                    self.white_spaces[self.contador2].create_oval(0,30,30,0, outline = "white")
                    self.circle2_text = tk.Label(self.white_spaces[self.contador2], text = lista[3], fg = "white", bg = "gray25")
                    self.circle2_text.place(x = 8, y = 3)
                    self.white_space4 = tk.Canvas(self.canvas, width = 50, height = 50, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
                    self.white_space4.create_oval(0,50,50,0, fill = "white", outline = "")
                    if self.posicion == 1:
                        self.white_space4.place(x = 380,y = 410)
                    else:
                        self.white_space4.place(x = 750,y = 410)
                    self.contador2 += 1
                self.lista = [[],[],[],[]]
                contador = 0
                lista_validadora = []
                for colores in copia_lista:
                    if colores in self.combinations:
                        while contador < 4:
                            if colores == self.combinations[contador]:
                                contador += 1
                                self.calificadores[self.contador3].create_oval(0,10,10,0, fill = "black", outline = "")
                                self.contador3 += 1
                                lista_validadora.append(colores)
                                self.calificadas.append("black")
                                break
                            else:
                                if not colores in lista_validadora:
                                    contador += 1
                                    self.calificadores[self.contador3].create_oval(0,10,10,0, fill = "white", outline = "")
                                    self.contador3 += 1
                                    lista_validadora.append(colores)
                                    self.calificadas.append("white")
                                    break
                                else:
                                    self.calificadores[self.contador3].create_oval(0,10,10,0, outline = "white")
                                    self.contador3 += 1
                                    contador += 1
                                    self.calificadas.append("outline")
                    else:
                        self.calificadores[self.contador3].create_oval(0,10,10,0, outline = "white")
                        self.contador3 += 1
                        contador += 1
                        self.calificadas.append("outline")
                if self.contador == self.validador:
                    self.loss()          
        else:
            tkinter.messagebox.showinfo("MASTERMIND","ERROR HAY CASILLAS BLANCAS TODAVIA")
            
    def load_game(self):
# The above code is loading the data from the file "mastermind2022juegoactual.dat" and then it is
# assigning the data to the variables that are going to be used in the game.
        datos = open("mastermind2022juegoactual.dat","rb")
        lista_de_datos = pickle.load(datos)
        del self.nombre1
        del self.booleano
        del self.dificultad
        del self.cronometro
        del self.h1
        del self.m1
        del self.s1
        del self.posicion
        del self.combinacion
        del self.contador
        del self.contador2
        del self.contador3
        del self.jugadas
        del self.calificadas
        del self.combinations
        del self.h
        del self.m
        del self.s
        del self.contador4
        del self.lista_de_horas
        del self.acumulador1
        del self.acumulador2
        del self.acumulador3
        del self.date
        del self.hour
        del self.lista
        del self.listatotal
        del self.lista_de_contadores
        del self.lista_copia
        del self.lista_cont_copia
        del self.indice
        del self.sub_indice
        del self.indice_copia
        del self.sub_indice_copia
        del self.grado_dificultad
        self.lista = lista_de_datos[25]
        self.listatotal = lista_de_datos[26]
        self.lista_copia = lista_de_datos[27]
        self.lista_de_contadores = lista_de_datos[28]
        self.lista_cont_copia = lista_de_datos[29]
        self.indice = lista_de_datos[30]
        self.sub_indice = lista_de_datos[31]
        self.indice_copia = lista_de_datos[32]
        self.sub_indice_copia = lista_de_datos[33]
        self.grado_dificultad = lista_de_datos[34]
        self.nombre1 = lista_de_datos[0]
        self.label_jugador.config(text = lista_de_datos[0])
        self.booleano = lista_de_datos[1]
        self.dificultad = lista_de_datos[2]
        self.dificult()
        self.cronometro = lista_de_datos[3]
        self.h1 = lista_de_datos[4]
        self.m1 = lista_de_datos[5]
        self.s1 = lista_de_datos[6]
        self.posicion = lista_de_datos[7]
        self.circle1.destroy()
        self.circle2.destroy()
        self.circle3.destroy()
        self.circle4.destroy()
        self.circle5.destroy()
        self.circle6.destroy()
        self.white_space1.destroy()
        self.white_space2.destroy()
        self.white_space3.destroy()
        self.white_space4.destroy()
        self.white_space5.destroy()
        self.white_space6.destroy()
        self.white_space7.destroy()
        self.white_space8.destroy()
        self.white_space9.destroy()
        self.white_space10.destroy()
        self.white_space11.destroy()
        self.white_space12.destroy()
        self.white_space13.destroy()
        self.white_space14.destroy()
        self.white_space15.destroy()
        self.white_space16.destroy()
        self.white_space17.destroy()
        self.white_space18.destroy()
        self.white_space19.destroy()
        self.white_space20.destroy()
        self.white_space21.destroy()
        self.white_space22.destroy()
        self.white_space23.destroy()
        self.white_space24.destroy()
        self.white_space25.destroy()
        self.white_space26.destroy()
        self.white_space27.destroy()
        self.white_space28.destroy()
        self.white_space29.destroy()
        self.white_space30.destroy()
        self.white_space31.destroy()
        self.white_space32.destroy()
        self.white_space33.destroy()
        self.white_space34.destroy()
        self.white_space35.destroy()
        self.white_space36.destroy()
        self.calificador.destroy()
        self.calificador1.destroy()
        self.calificador2.destroy()
        self.calificador3.destroy()
        self.calificador4.destroy()
        self.calificador5.destroy()
        self.calificador6.destroy()
        self.calificador7.destroy()
        self.calificador8.destroy()
        self.calificador9.destroy()
        self.calificador10.destroy()
        self.calificador11.destroy()
        self.calificador12.destroy()
        self.calificador13.destroy()
        self.calificador14.destroy()
        self.calificador15.destroy()
        self.calificador16.destroy()
        self.calificador17.destroy()
        self.calificador18.destroy()
        self.calificador19.destroy()
        self.calificador20.destroy()
        self.calificador21.destroy()
        self.calificador22.destroy()
        self.calificador23.destroy()
        self.calificador24.destroy()
        self.calificador25.destroy()
        self.calificador26.destroy()
        self.calificador27.destroy()
        self.calificador28.destroy()
        self.calificador29.destroy()
        self.calificador30.destroy()
        self.calificador31.destroy()
        self.combinacion = lista_de_datos[8]
        self.posiciones()
        self.contador = lista_de_datos[9]
        self.contador2 = lista_de_datos[10]
        self.contador3 = lista_de_datos[11]
        self.jugadas = lista_de_datos[12]
        self.calificadas = lista_de_datos[13]
        self.combinations = lista_de_datos[14]
        self.h = lista_de_datos[15]
        self.m = lista_de_datos[16]
        self.s = lista_de_datos[17]
        self.contador4 = lista_de_datos[18]
        self.lista_de_horas = lista_de_datos[19]
        self.acumulador1 = lista_de_datos[20]
        self.acumulador2 = lista_de_datos[21]
        self.acumulador3 = lista_de_datos[22]
        self.date = lista_de_datos[23]
        self.hour  = lista_de_datos[24]
        try:
            self.horas.destroy()
            self.horas_numeros.destroy()
            self.minutos.destroy()
            self.minutos_numeros.destroy()
            self.segundos.destroy()
            self.segundos_numeros.destroy()
        except:
            pass
        self.chronometer()
        jugadas = lista_de_datos[12]
        clasificadas = lista_de_datos[13]
        lista = []
        for juego in jugadas:
            for colores in juego:
                lista.append(colores)
        contador = 0
        for color in lista:
            if self.combinacion == 1:
                self.white_spaces[contador].create_oval(0,30,30,0, fill = color , outline = "")
                contador += 1
            elif self.combinacion == 2 or self.combinacion == 3 or self.combinacion == 4:
                    self.white_spaces[contador].create_oval(0,30,30,0, outline = "white")
                    self.circle3_text = tk.Label(self.white_spaces[contador], text = color, fg = "white", bg = "gray25")
                    self.circle3_text.place(x = 8, y = 3)
                    contador += 1
        contador1 = 0
        for clasificados in clasificadas:
            if clasificados == "outline":
                self.calificadores[contador1].create_oval(0,10,10,0, outline = "white")
                contador1 += 1
            elif clasificados == "white":
                self.calificadores[contador1].create_oval(0,10,10,0, fill = "white", outline = "")
                contador1 += 1
            elif clasificados == "black":
                self.calificadores[contador1].create_oval(0,10,10,0, fill = "black", outline = "")
                contador1 += 1
        contador2 = 0
        for colores in self.lista:
            if colores == []:
                contador2 += 1
            else:
                if self.combinacion == 1:
                    self.lista_espacios[contador2].create_oval(0,50,50,0, fill = colores, outline = "")
                    contador2 += 1
                else:
                    self.circle3_text = tk.Label(self.lista_espacios[contador2], text = colores , fg = "Black", bg = "white")
                    self.circle3_text.place(x = 18, y = 15)
                    contador2 += 1

    def save_game(self):
# Saving the current game.
        lista_de_datos = [self.nombre1,self.booleano,self.dificultad,self.cronometro,self.h1,self.m1,self.s1,self.posicion,self.combinacion,self.contador,self.contador2,self.contador3,self.jugadas,self.calificadas,self.combinations,self.h,self.m,self.s,self.contador4,self.lista_de_horas,self.acumulador1,self.acumulador2,self.acumulador3,self.date,self.hour,self.lista,self.listatotal,self.lista_copia,self.lista_de_contadores,self.lista_cont_copia,self.indice,self.sub_indice,self.indice_copia,self.sub_indice_copia,self.grado_dificultad]
        print(len(lista_de_datos))
        settings = open("mastermind2022juegoactual.dat","wb")
        pickle.dump(lista_de_datos,settings)
        settings.close()

# This class is used to create a window that allows the user to configure the program.
class ventana_configuracion:

    def __init__(self,master):
        self.master = master
        self.canvas = Canvas(master,width=2000,height=1000,highlightthickness=0, relief='ridge',
                             bg = 'gray25')
        self.canvas.place(x=0,y=0)

        #Variables para que las funciones, funcionen
        self.seleccionar_dificultad1 = tk.IntVar()
        self.seleccion_reloj1 = tk.IntVar()
        self.seleccion_posicicon = tk.IntVar()
        self.seleccion_combinacion = tk.IntVar()
        self.horas_entradas = tk.IntVar()
        self.dificultad = 0
        self.cronometro = 0
        self.p = 0
        self.h = ""
        self.m = ""
        self.s = ""
        self.lista_de_tiempos = ["","","","","","","","",""]
        self.combinacion = 0

        self.label_titulo = Label(self.canvas, text='CONFIGURAR',font=('Games',45), fg='white', bg = 'gray25') 
        self.label_titulo.place(x=278,y=10,width=450,height=50) #Titulo de la pantalla.

        self.seleccionar_dificultad = Label(self.canvas, text= '1. Nivel de dificultad:', bg = 'gray25') 
        self.seleccionar_dificultad.place(x = 50, y = 50) #Titulo de la pantalla.

        self.dificultad_facil = Radiobutton(self.canvas, text = "Fácil (8 jugadas, combinaciónde 4 elementos de 6)", bg = 'gray25', 
                                                    variable = self.seleccionar_dificultad1, value = 1, command = self.seleccion_dificultad)
        self.dificultad_facil.place(x = 200, y = 70)

        self.dificultad_medio = Radiobutton(self.canvas, text = "Medio (7 jugadas, combinación de 4 elementos de 6)", bg = 'gray25',
                                                    variable = self.seleccionar_dificultad1, value = 2, command = self.seleccion_dificultad)
        self.dificultad_medio.place(x = 200, y = 90)

        self.dificultad_dificil = Radiobutton(self.canvas, text = "Difícil (6 jugadas, combinación de 4 elementos de 6)", bg = 'gray25',
                                                    variable = self.seleccionar_dificultad1, value = 3, command = self.seleccion_dificultad)
        self.dificultad_dificil.place(x = 200, y = 110)

        self.dificultad_multinivel = Radiobutton(self.canvas, text = "Multinivel", bg = 'gray25',
                                                    variable = self.seleccionar_dificultad1, value = 4, command = self.seleccion_dificultad)
        self.dificultad_multinivel.place(x = 200, y = 130)

        #TIEMPO
        self.reloj = Label(self.canvas, text= '2. Reloj:', bg = 'gray25') 
        self.reloj.place(x = 50, y = 180) #Titulo de la pantalla.

        self.reloj_si = Radiobutton(self.canvas, text = "Si", bg = 'gray25', variable = self.seleccion_reloj1, value = 1, command = self.seleccionar_reloj)
        self.reloj_si.place(x = 120, y = 180)

        self.reloj_no = Radiobutton(self.canvas, text = "No", bg = 'gray25', variable = self.seleccion_reloj1, value = 2, command = self.seleccionar_reloj)
        self.reloj_no.place(x = 120, y = 200)

        self.cronometro_por_jugada = Radiobutton(self.canvas, text = "Cronómetro por jugada", bg = 'gray25', variable = self.seleccion_reloj1, value = 3, command = self.seleccionar_reloj)
        self.cronometro_por_jugada.place(x = 120, y = 220)

        self.cronometro_por_juego = Radiobutton(self.canvas, text = "Cronómetro por juego", bg = 'gray25',variable = self.seleccion_reloj1, value = 4, command = self.seleccionar_reloj)
        self.cronometro_por_juego.place(x = 120, y = 240)

        self.horas = Label(self.canvas, text = "Horas", bg = 'gray25', borderwidth = 1, relief = "solid")
        self.horas.place(x = 250, y = 300 , width = 100, height = 20)

        self.minutos = Label(self.canvas, text = "Minutos", bg = 'gray25', borderwidth = 1, relief = "solid")
        self.minutos.place(x = 350, y = 300 , width = 100, height = 20)

        self.segundos = Label(self.canvas, text = "Segundos", bg = 'gray25', borderwidth = 1, relief = "solid")
        self.segundos.place(x = 450, y = 300 , width = 100, height = 20)

        self.h_4 = Label(self.canvas, text = "00", bg = 'gray25', borderwidth = 1, relief = "solid")
        self.h_4.place(x = 250, y = 320 , width = 100, height = 50)

        self.m_4 = Label(self.canvas, text = "00", bg = 'gray25', borderwidth = 1, relief = "solid")
        self.m_4.place(x = 350, y = 320 , width = 100, height = 50)

        self.s_4 = Label(self.canvas, text = "00", bg = 'gray25', borderwidth = 1, relief = "solid")
        self.s_4.place(x = 450, y = 320 , width = 100, height = 50)

        # POSICIONES
        self.posicion = Label(self.canvas, text= '3. Posición del panel de elementos:', bg = 'gray25') 
        self.posicion.place(x = 50, y = 380) #Titulo de la pantalla.

        self.derecha =  Radiobutton(self.canvas, text = "Derecha", bg = 'gray25', variable = self.seleccion_posicicon, value = 1, command = self.seleccionar_posicion)
        self.derecha.place(x = 300, y = 380)

        self.izquierda =  Radiobutton(self.canvas, text = "Izquierda", bg = 'gray25', variable = self.seleccion_posicicon, value = 2, command = self.seleccionar_posicion)
        self.izquierda.place(x = 300, y = 400)

        #COMBINACIONES
        self.combinaciones = Label(self.canvas, text= '4. Panel de elementos para usar en la combinación:', bg = 'gray25') 
        self.combinaciones.place(x = 50, y = 440)

        #COLORES
        self.colores =  Radiobutton(self.canvas, text = "Colores", bg = 'gray25', variable = self.seleccion_combinacion, value = 1, command = self.seleccionar_combinacion)
        self.colores.place(x = 100, y = 480)

        self.color1 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.color1.create_oval(0,30,30,0, fill = "blue", outline = "")
        self.color1.place(x = 200,y = 480)

        self.color2 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.color2.create_oval(0,30,30,0, fill = "orange", outline = "")
        self.color2.place(x = 270,y = 480)

        self.color3 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.color3.create_oval(0,30,30,0, fill = "red", outline = "")
        self.color3.place(x = 340,y = 480)

        self.color4 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.color4.create_oval(0,30,30,0, fill = "green", outline = "")
        self.color4.place(x = 410,y = 480)

        self.color5 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.color5.create_oval(0,30,30,0, fill = "saddle brown", outline = "")
        self.color5.place(x = 480,y = 480)

        self.color6 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.color6.create_oval(0,30,30,0, fill = "yellow", outline = "")
        self.color6.place(x = 550,y = 480)

        #LETRAS
        self.letras =  Radiobutton(self.canvas, text = "Letras", bg = 'gray25', variable = self.seleccion_combinacion, value = 2, command = self.seleccionar_combinacion)
        self.letras.place(x = 100, y = 540)

        self.letra1 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.letra1.create_oval(0,30,30,0, fill = "gray25")
        self.letra1_text = tk.Label(self.letra1, text = "A", fg = "white", bg = "gray25")
        self.letra1_text.place(x = 8, y = 5)
        self.letra1.place(x = 200,y = 540)

        self.letra2 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.letra2.create_oval(0,30,30,0, fill = "gray25")
        self.letra2_text = tk.Label(self.letra2, text = "B", fg = "white", bg = "gray25")
        self.letra2_text.place(x = 8, y = 5)
        self.letra2.place(x = 270,y = 540)

        self.letra3 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.letra3.create_oval(0,30,30,0, fill = "gray25")
        self.letra3_text = tk.Label(self.letra3, text = "C", fg = "white", bg = "gray25")
        self.letra3_text.place(x = 8, y = 5)
        self.letra3.place(x = 340,y = 540)

        self.letra4 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.letra4.create_oval(0,30,30,0, fill = "gray25")
        self.letra4_text = tk.Label(self.letra4, text = "D", fg = "white", bg = "gray25")
        self.letra4_text.place(x = 8, y = 5)
        self.letra4.place(x = 410,y = 540)

        self.letra5 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.letra5.create_oval(0,30,30,0, fill = "gray25")
        self.letra5_text = tk.Label(self.letra5, text = "E", fg = "white", bg = "gray25")
        self.letra5_text.place(x = 8, y = 5)
        self.letra5.place(x = 480,y = 540)

        self.letra6 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.letra6.create_oval(0,30,30,0, fill = "gray25")
        self.letra6_text = tk.Label(self.letra6, text = "F", fg = "white", bg = "gray25")
        self.letra6_text.place(x = 8, y = 5)
        self.letra6.place(x = 550,y = 540)

        #NUMEROS
        self.numeros =  Radiobutton(self.canvas, text = "Números", bg = 'gray25', variable = self.seleccion_combinacion, value = 3 , command = self.seleccionar_combinacion)
        self.numeros.place(x = 100, y = 600)

        self.numero1 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.numero1.create_oval(0,30,30,0, fill = "gray25")
        self.numero1_text = tk.Label(self.numero1, text = 1, fg = "white", bg = "gray25")
        self.numero1_text.place(x = 8, y = 5)
        self.numero1.place(x = 200,y = 600)

        self.numero2 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.numero2.create_oval(0,30,30,0, fill = "gray25")
        self.numero2_text = tk.Label(self.numero2, text = 2, fg = "white", bg = "gray25")
        self.numero2_text.place(x = 8, y = 5)
        self.numero2.place(x = 270,y = 600)

        self.numero3 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.numero3.create_oval(0,30,30,0, fill = "gray25")
        self.numero3_text = tk.Label(self.numero3, text = 3, fg = "white", bg = "gray25")
        self.numero3_text.place(x = 8, y = 5)
        self.numero3.place(x = 340,y = 600)

        self.numero4 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.numero4.create_oval(0,30,30,0, fill = "gray25")
        self.numero4_text = tk.Label(self.numero4, text = 4, fg = "white", bg = "gray25")
        self.numero4_text.place(x = 8, y = 5)
        self.numero4.place(x = 410,y = 600)

        self.numero5 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.numero5.create_oval(0,30,30,0, fill = "gray25")
        self.numero5_text = tk.Label(self.numero5, text = 5, fg = "white", bg = "gray25")
        self.numero5_text.place(x = 8, y = 5)
        self.numero5.place(x = 480,y = 600)

        self.numero6 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.numero6.create_oval(0,30,30,0, fill = "gray25")
        self.numero6_text = tk.Label(self.numero6, text = 6, fg = "white", bg = "gray25")
        self.numero6_text.place(x = 8, y = 5)
        self.numero6.place(x = 550,y = 600)

        #
        self.simbolos =  Radiobutton(self.canvas, text = "Símbolos", bg = 'gray25', variable = self.seleccion_combinacion, value = 4 , command = self.seleccionar_combinacion)
        self.simbolos.place(x = 100, y = 660)

        self.simbolos1 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.simbolos1.create_oval(0,30,30,0, fill = "gray25")
        self.simbolos1_text = tk.Label(self.simbolos1, text = "*", fg = "white", bg = "gray25")
        self.simbolos1_text.place(x = 8, y = 5)
        self.simbolos1.place(x = 200,y = 660)

        self.simbolos2 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.simbolos2.create_oval(0,30,30,0, fill = "gray25")
        self.simbolos2_text = tk.Label(self.simbolos2, text = "+", fg = "white", bg = "gray25")
        self.simbolos2_text.place(x = 8, y = 5)
        self.simbolos2.place(x = 270,y = 660)

        self.simbolos3 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.simbolos3.create_oval(0,30,30,0, fill = "gray25")
        self.simbolos3_text = tk.Label(self.simbolos3, text = "/", fg = "white", bg = "gray25")
        self.simbolos3_text.place(x = 8, y = 5)
        self.simbolos3.place(x = 340,y = 660)

        self.simbolos4 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.simbolos4.create_oval(0,30,30,0, fill = "gray25")
        self.simbolos4_text = tk.Label(self.simbolos4, text = "-", fg = "white", bg = "gray25")
        self.simbolos4_text.place(x = 8, y = 5)
        self.simbolos4.place(x = 410,y = 660)

        self.simbolos5 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.simbolos5.create_oval(0,30,30,0, fill = "gray25")
        self.simbolos5_text = tk.Label(self.simbolos5, text = ">", fg = "white", bg = "gray25")
        self.simbolos5_text.place(x = 8, y = 5)
        self.simbolos5.place(x = 480,y = 660)

        self.simbolos6 = tk.Canvas(self.canvas, width = 30, height = 30, bg = "gray25", bd = 0, highlightthickness = 0, relief ="ridge")
        self.simbolos6.create_oval(0,30,30,0, fill = "gray25")
        self.simbolos6_text = tk.Label(self.simbolos6, text = "<", fg = "white", bg = "gray25")
        self.simbolos6_text.place(x = 8, y = 5)
        self.simbolos6.place(x = 550,y = 660)


        self.salir1 = Button(self.canvas, text = "GUARDAR CONFIGURACIÓN" ,highlightbackground = '#25D55F', highlightthickness = 30, command = self.salir)
        self.salir1.place(x = 650, y = 580, width = 300, height = 30)

        self.salir3 = Button(self.canvas, text = "SALIR" ,highlightbackground = '#FF0000', highlightthickness = 30, command = self.salir2)
        self.salir3.place(x = 650, y = 620, width = 300, height = 30)

        #VALORES INCIALES
        self.seleccionar_dificultad1.set(1)
        self.seleccion_reloj1.set(1)
        self.seleccion_posicicon.set(1)
        self.seleccion_combinacion.set(1)
    
    def salir2(self):
        self.canvas.destroy()
    
    def seleccion_dificultad(self):
        seleccion = self.seleccionar_dificultad1.get()
        if seleccion == 1:
            self.dificultad = seleccion
        elif seleccion == 2:
            self.dificultad = seleccion
        elif seleccion == 3:
            self.dificultad = seleccion
        else:
            self.dificultad = seleccion

    def seleccionar_reloj(self):
        seleccion = self.seleccion_reloj1.get()
        dificultad = self.seleccionar_dificultad1.get()
        if seleccion == 1:
            self.cronometro = seleccion
            self.horas = Label(self.canvas, text = "Horas", bg = 'gray25', borderwidth = 1, relief = "solid")
            self.horas.place(x = 250, y = 300 , width = 100, height = 20)

            self.minutos = Label(self.canvas, text = "Minutos", bg = 'gray25', borderwidth = 1, relief = "solid")
            self.minutos.place(x = 350, y = 300 , width = 100, height = 20)

            self.segundos = Label(self.canvas, text = "Segundos", bg = 'gray25', borderwidth = 1, relief = "solid")
            self.segundos.place(x = 450, y = 300 , width = 100, height = 20)

            self.h_4 = Label(self.canvas, text = "00", bg = 'gray25', borderwidth = 1, relief = "solid")
            self.h_4.place(x = 250, y = 320 , width = 100, height = 50)

            self.m_4 = Label(self.canvas, text = "00", bg = 'gray25', borderwidth = 1, relief = "solid")
            self.m_4.place(x = 350, y = 320 , width = 100, height = 50)

            self.s_4 = Label(self.canvas, text = "00", bg = 'gray25', borderwidth = 1, relief = "solid")
            self.s_4.place(x = 450, y = 320 , width = 100, height = 50)
        elif seleccion == 2:
            self.cronometro = seleccion
            self.label = Label(self.canvas, bg = 'gray25')
            self.label.place(x = 150, y = 270 , width = 500, height = 110)
        elif seleccion == 3:
            self.cronometro = seleccion
            if dificultad == 4:
                self.horas = Label(self.canvas, text = "Horas", bg = 'gray25', borderwidth = 1, relief = "solid")
                self.horas.place(x = 250, y = 270 , width = 100, height = 20)

                self.minutos = Label(self.canvas, text = "Minutos", bg = 'gray25', borderwidth = 1, relief = "solid")
                self.minutos.place(x = 350, y = 270 , width = 100, height = 20)

                self.segundos = Label(self.canvas, text = "Segundos", bg = 'gray25', borderwidth = 1, relief = "solid")
                self.segundos.place(x = 450, y = 270 , width = 100, height = 20)

                self.facil = Label(self.canvas, text = "Nivel Fácil", bg = 'gray25', borderwidth = 1, relief = "solid")
                self.facil.place(x = 150, y = 290 , width = 100, height = 30)

                self.medio = Label(self.canvas, text = "Nivel Medio", bg = 'gray25', borderwidth = 1, relief = "solid")
                self.medio.place(x = 150, y = 320 , width = 100, height = 30)

                self.dificil = Label(self.canvas, text = "Nivel Difícil", bg = 'gray25', borderwidth = 1, relief = "solid")
                self.dificil.place(x = 150, y = 350 , width = 100, height = 30)

                self.h_1 = Entry(self.canvas, textvariable =  self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.h_1.place(x = 250, y = 290 , width = 100, height = 30)
                self.h_1.bind("<Leave>",self.validar_entradas)

                self.m_1 = Entry(self.canvas, textvariable =  self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.m_1.place(x = 350, y = 290 , width = 100, height = 30)
                self.m_1.bind("<Leave>",self.validar_entradas)

                self.s_1 = Entry(self.canvas, textvariable =  self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.s_1.place(x = 450, y = 290 , width = 100, height = 30)
                self.s_1.bind("<Leave>",self.validar_entradas)

                self.h_2 = Entry(self.canvas, textvariable =  self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.h_2.place(x = 250, y = 320 , width = 100, height = 30)
                self.h_2.bind("<Leave>",self.validar_entradas)

                self.m_2 = Entry(self.canvas, textvariable =  self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.m_2.place(x = 350, y = 320 , width = 100, height = 30)
                self.m_2.bind("<Leave>",self.validar_entradas)

                self.s_2 = Entry(self.canvas, textvariable =  self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.s_2.place(x = 450, y = 320 , width = 100, height = 30)
                self.s_2.bind("<Leave>",self.validar_entradas)

                self.h_3 = Entry(self.canvas, textvariable = self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.h_3.place(x = 250, y = 350 , width = 100, height = 30)
                self.h_3.bind("<Leave>",self.validar_entradas)

                self.m_3 = Entry(self.canvas, textvariable = self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.m_3.place(x = 350, y = 350 , width = 100, height = 30)
                self.m_3.bind("<Leave>",self.validar_entradas)

                self.s_3 = Entry(self.canvas, textvariable = self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.s_3.place(x = 450, y = 350 , width = 100, height = 30)
                self.s_3.bind("<Leave>",self.validar_entradas)

            else:
                self.horas = Label(self.canvas, text = "Horas", bg = 'gray25', borderwidth = 1, relief = "solid")
                self.horas.place(x = 250, y = 300 , width = 100, height = 20)

                self.minutos = Label(self.canvas, text = "Minutos", bg = 'gray25', borderwidth = 1, relief = "solid")
                self.minutos.place(x = 350, y = 300 , width = 100, height = 20)

                self.segundos = Label(self.canvas, text = "Segundos", bg = 'gray25', borderwidth = 1, relief = "solid")
                self.segundos.place(x = 450, y = 300 , width = 100, height = 20)

                self.h_4 = Entry(self.canvas, textvariable = self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.h_4.place(x = 250, y = 320 , width = 100, height = 50)
                self.h_4.bind("<Leave>",self.validar_entradas)

                self.m_4 = Entry(self.canvas, textvariable = self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.m_4.place(x = 350, y = 320 , width = 100, height = 50)
                self.m_4.bind("<Leave>",self.validar_entradas)

                self.s_4 = Entry(self.canvas, textvariable = self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.s_4.place(x = 450, y = 320 , width = 100, height = 50)
                self.s_4.bind("<Leave>",self.validar_entradas)
        else:
            self.cronometro = seleccion
            if dificultad == 4:
                self.horas = Label(self.canvas, text = "Horas", bg = 'gray25', borderwidth = 1, relief = "solid")
                self.horas.place(x = 250, y = 270 , width = 100, height = 20)

                self.minutos = Label(self.canvas, text = "Minutos", bg = 'gray25', borderwidth = 1, relief = "solid")
                self.minutos.place(x = 350, y = 270 , width = 100, height = 20)

                self.segundos = Label(self.canvas, text = "Segundos", bg = 'gray25', borderwidth = 1, relief = "solid")
                self.segundos.place(x = 450, y = 270 , width = 100, height = 20)

                self.facil = Label(self.canvas, text = "Nivel Fácil", bg = 'gray25', borderwidth = 1, relief = "solid")
                self.facil.place(x = 150, y = 290 , width = 100, height = 30)

                self.medio = Label(self.canvas, text = "Nivel Medio", bg = 'gray25', borderwidth = 1, relief = "solid")
                self.medio.place(x = 150, y = 320 , width = 100, height = 30)

                self.dificil = Label(self.canvas, text = "Nivel Difícil", bg = 'gray25', borderwidth = 1, relief = "solid")
                self.dificil.place(x = 150, y = 350 , width = 100, height = 30)

                self.h_1 = Entry(self.canvas, textvariable =  self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.h_1.place(x = 250, y = 290 , width = 100, height = 30)
                self.h_1.bind("<Leave>",self.validar_entradas)

                self.m_1 = Entry(self.canvas, textvariable =  self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.m_1.place(x = 350, y = 290 , width = 100, height = 30)
                self.m_1.bind("<Leave>",self.validar_entradas)

                self.s_1 = Entry(self.canvas, textvariable =  self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.s_1.place(x = 450, y = 290 , width = 100, height = 30)
                self.s_1.bind("<Leave>",self.validar_entradas)

                self.h_2 = Entry(self.canvas, textvariable =  self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.h_2.place(x = 250, y = 320 , width = 100, height = 30)
                self.h_2.bind("<Leave>",self.validar_entradas)

                self.m_2 = Entry(self.canvas, textvariable =  self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.m_2.place(x = 350, y = 320 , width = 100, height = 30)
                self.m_2.bind("<Leave>",self.validar_entradas)

                self.s_2 = Entry(self.canvas, textvariable =  self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.s_2.place(x = 450, y = 320 , width = 100, height = 30)
                self.s_2.bind("<Leave>",self.validar_entradas)

                self.h_3 = Entry(self.canvas, textvariable = self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.h_3.place(x = 250, y = 350 , width = 100, height = 30)
                self.h_3.bind("<Leave>",self.validar_entradas)

                self.m_3 = Entry(self.canvas, textvariable = self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.m_3.place(x = 350, y = 350 , width = 100, height = 30)
                self.m_3.bind("<Leave>",self.validar_entradas)

                self.s_3 = Entry(self.canvas, textvariable = self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.s_3.place(x = 450, y = 350 , width = 100, height = 30)
                self.s_3.bind("<Leave>",self.validar_entradas)
            else:
                self.horas = Label(self.canvas, text = "Horas", bg = 'gray25', borderwidth = 1, relief = "solid")
                self.horas.place(x = 250, y = 300 , width = 100, height = 20)

                self.minutos = Label(self.canvas, text = "Minutos", bg = 'gray25', borderwidth = 1, relief = "solid")
                self.minutos.place(x = 350, y = 300 , width = 100, height = 20)

                self.segundos = Label(self.canvas, text = "Segundos", bg = 'gray25', borderwidth = 1, relief = "solid")
                self.segundos.place(x = 450, y = 300 , width = 100, height = 20)

                self.h_4 = Entry(self.canvas, textvariable = self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.h_4.place(x = 250, y = 320 , width = 100, height = 50)
                self.h_4.bind("<Leave>",self.validar_entradas)

                self.m_4 = Entry(self.canvas, textvariable = self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.m_4.place(x = 350, y = 320 , width = 100, height = 50)
                self.m_4.bind("<Leave>",self.validar_entradas)

                self.s_4 = Entry(self.canvas, textvariable = self.horas_entradas, bg = 'gray25', borderwidth = 1, relief = "solid")
                self.s_4.place(x = 450, y = 320 , width = 100, height = 50)
                self.s_4.bind("<Leave>",self.validar_entradas)

    def validar_entradas(self,event):
        widget = event.widget 
        if widget == self.h_1 or widget == self.h_2 or widget == self.h_3 or widget == self.h_4:
            horas = self.horas_entradas.get()
            if horas >= 0 and horas <= 2:
                if widget == self.h_1:
                    self.h_1 = Label(self.canvas, text = horas, bg = 'gray25', borderwidth = 1, relief = "solid")
                    self.h_1.place(x = 250, y = 290 , width = 100, height = 30)
                    self.lista_de_tiempos.pop(0)
                    self.lista_de_tiempos.insert(0,horas)
                elif widget == self.h_2:
                    self.h_2 = Label(self.canvas, text = horas, bg = 'gray25', borderwidth = 1, relief = "solid")
                    self.h_2.place(x = 250, y = 320 , width = 100, height = 30)
                    self.lista_de_tiempos.pop(3)
                    self.lista_de_tiempos.insert(3,horas)
                elif widget == self.h_3:
                    self.h_3 = Label(self.canvas, text = horas, bg = 'gray25', borderwidth = 1, relief = "solid")
                    self.h_3.place(x = 250, y = 350 , width = 100, height = 30)
                    self.lista_de_tiempos.pop(6)
                    self.lista_de_tiempos.insert(6,horas)
                else:
                    self.h_4 = Label(self.canvas, text = horas, bg = 'gray25', borderwidth = 1, relief = "solid")
                    self.h_4.place(x = 250, y = 320 , width = 100, height = 50)
                    self.h = horas
            else:
                tkinter.messagebox.showinfo("MASTERMIND","ERROR LAS HORAS DEBEN ESTAR ENTRE 0")
        elif widget == self.m_1 or widget == self.m_2 or widget == self.m_3 or widget == self.m_4:
            minutos = self.horas_entradas.get()
            if minutos >= 0 and minutos <= 59:
                if widget == self.m_1:
                    self.m_1 = Label(self.canvas, text = minutos, bg = 'gray25', borderwidth = 1, relief = "solid")
                    self.m_1.place(x = 350, y = 290 , width = 100, height = 30)
                    self.lista_de_tiempos.pop(1)
                    self.lista_de_tiempos.insert(1,minutos)
                elif widget == self.m_2:
                    self.m_2 = Label(self.canvas, text = minutos, bg = 'gray25', borderwidth = 1, relief = "solid")
                    self.m_2.place(x = 350, y = 320 , width = 100, height = 30)
                    self.lista_de_tiempos.pop(4)
                    self.lista_de_tiempos.insert(4,minutos)
                elif widget == self.m_3:
                    self.m_3 = Label(self.canvas, text = minutos, bg = 'gray25', borderwidth = 1, relief = "solid")
                    self.m_3.place(x = 350, y = 350 , width = 100, height = 30)
                    self.lista_de_tiempos.pop(7)
                    self.lista_de_tiempos.insert(7,minutos)
                else:
                    self.m_4 = Label(self.canvas, text = minutos, bg = 'gray25', borderwidth = 1, relief = "solid")
                    self.m_4.place(x = 350, y = 320 , width = 100, height = 50)
                    self.m = minutos
            else:
                tkinter.messagebox.showinfo("MASTERMIND","ERROR LOS MINUTOS DEBEN ESTAR ENTRE 0 Y 59")
        elif widget == self.s_1 or widget == self.s_2 or widget == self.s_3 or widget == self.s_4:
            segundos = self.horas_entradas.get()
            if segundos > 0 and segundos <= 59:
                if widget == self.s_1:
                    self.s_1 = Label(self.canvas, text = segundos, bg = 'gray25', borderwidth = 1, relief = "solid")
                    self.s_1.place(x = 450, y = 290 , width = 100, height = 30)
                    self.lista_de_tiempos.pop(2)
                    self.lista_de_tiempos.insert(2,segundos)
                elif widget == self.s_2:
                    self.s_2 = Label(self.canvas, text = segundos, bg = 'gray25', borderwidth = 1, relief = "solid")
                    self.s_2.place(x = 450, y = 320 , width = 100, height = 30)
                    self.lista_de_tiempos.pop(5)
                    self.lista_de_tiempos.insert(5,segundos)
                elif widget == self.s_3:
                    self.s_3 = Label(self.canvas, text = segundos, bg = 'gray25', borderwidth = 1, relief = "solid")
                    self.s_3.place(x = 450, y = 350 , width = 100, height = 30)
                    self.lista_de_tiempos.pop(8)
                    self.lista_de_tiempos.insert(8,segundos)
                else:
                    self.s_4 = Label(self.canvas, text = segundos, bg = 'gray25', borderwidth = 1, relief = "solid")
                    self.s_4.place(x = 450, y = 320 , width = 100, height = 50)
                    self.s = segundos
            else:
                tkinter.messagebox.showinfo("MASTERMIND","ERROR LOS SEGUNDOS DEBEN ESTAR ENTRE 0 Y 59")

    def seleccionar_posicion(self):
        seleccion = self.seleccion_posicicon.get()
        if seleccion == 1:
            self.p = seleccion
        elif seleccion == 2:
            self.p = seleccion

    def seleccionar_combinacion(self):
        seleccion = self.seleccion_combinacion.get()
        if seleccion == 1:
            self.combinacion = seleccion
        elif seleccion == 2:
            self.combinacion = seleccion
        elif seleccion == 3:
            self.combinacion = seleccion
        else:
            self.combinacion = seleccion

    def save_settings(self):
        print(self.dificultad,self.cronometro,self.h,self.m,self.s,self.p,self.combinacion,self.lista_de_tiempos)
        lista_de_datos = [self.dificultad,self.cronometro,self.h,self.m,self.s,self.p,self.combinacion,self.lista_de_tiempos]
        settings = open("mastermind2022configuración.dat","wb")
        pickle.dump(lista_de_datos,settings)
        settings.close()

    def salir(self):
        if self.cronometro == 4 or self.cronometro == 3:
            if self.dificultad == 4:
                for elementos in self.lista_de_tiempos:
                    if elementos == "":
                        tkinter.messagebox.showinfo("MASTERMIND","ERROR DEBE COMPLETAR LOS CAMPOS DE TIEMPO")
                        return
                    else:
                        self.seleccion_dificultad()
                        self.seleccionar_posicion()
                        self.seleccionar_combinacion()
                        self.save_settings()
                        self.canvas.destroy()  
            else:
                if self.h == "" and self.m == "" and self.s == "":
                    tkinter.messagebox.showinfo("MASTERMIND","ERROR DEBE COMPLETAR LOS CAMPOS DE TIEMPO")
                else:
                    self.seleccion_dificultad()
                    self.seleccionar_posicion()
                    self.seleccionar_combinacion()
                    self.save_settings()
                    self.canvas.destroy()
        else:
            self.seleccion_dificultad()
            self.seleccionar_posicion()
            self.seleccionar_combinacion()
            self.save_settings()
            self.canvas.destroy()

# It's a window that displays the top 10 scores of the game.
class ventana_top_10_resumen:

    def __init__(self,master):
        self.master = master
        self.canvas = Canvas(master,width=2000,height=1000,highlightthickness=0, relief='ridge',
                             bg = 'gray25')
        self.canvas.place(x=0,y=0)

        self.seleccionar_dificultad1 = tk.IntVar()

        self.label_titulo = Label(self.canvas, text='TOP 10 - RESUMEN',font=('Games',45), fg='red', bg = 'dimgray') 
        self.label_titulo.place(x=278,y=5,width=450,height=50) #Titulo de la pantalla.

        self.dificultad_facil = Radiobutton(self.canvas, text = "Nivel Fácil", bg = 'gray25', value = 1, variable = self.seleccionar_dificultad1, command = self.validate_dificult)
        self.dificultad_facil.place(x = 100, y = 100)

        self.dificultad_medio = Radiobutton(self.canvas, text = "Nivel Medio", bg = 'gray25', value = 2, variable = self.seleccionar_dificultad1, command = self.validate_dificult)
        self.dificultad_medio.place(x = 100, y = 120)

        self.dificultad_dificil = Radiobutton(self.canvas, text = "Nivel difícil", bg = 'gray25', value = 3, variable = self.seleccionar_dificultad1, command = self.validate_dificult)
        self.dificultad_dificil.place(x = 100, y = 140)

        self.cancelar_juego = Button(self.canvas, text ='CONSULTAR',font=('Games',15) ,highlightbackground = '#FF8F00', highlightthickness = 30, command = self.create_pdf)
        self.cancelar_juego.place(x = 250, y = 200,width = 150, height = 50)

        self.salir_juego = Button(self.canvas, text ='SALIR',font=('Games',15) ,highlightbackground = '#FF0000', highlightthickness = 30, command = self.salir)
        self.salir_juego.place(x = 550, y = 200,width = 150, height = 50)

        self.seleccionar_dificultad1.set(1)
    
    def salir(self):
        self.canvas.destroy()

    def validate_dificult(self):
        seleccion = self.seleccionar_dificultad1.get()
        if seleccion == 1:
            self.dificultad = seleccion
        elif seleccion == 2:
            self.dificultad = seleccion
        else:
            self.dificultad = seleccion

    def create_pdf(self):
        self.lista_top_10 = []
        self.lista_definitiva = []
        self.validate_dificult()
        datos = open("mastermind2022top10.dat","rb")
        self.lista = []
        while True:
            try:
                lista_de_datos = pickle.load(datos)
                self.lista.append(lista_de_datos)
            except:
                break
        if self.dificultad == 1:
            self.titule = "TOP 10: NIVEL FÁCIL"
        elif self.dificultad == 2:
            self.titule = "TOP 10: NIVEL MEDIO"
        else:
            self.titule = "TOP 10: NIVEL DIFÍCIL"
        for jugador in self.lista:
            if jugador[3] == self.dificultad:
                self.lista_top_10.append(jugador)
        if self.lista_top_10:
            dato = min(self.lista_top_10)
            self.lista_definitiva.append(dato)
            self.lista_top_10.remove(dato)
            contador1 = 0
            while self.lista_top_10 != []:
                dato = min(self.lista_top_10)
                self.lista_definitiva.append(dato)
                self.lista_top_10.remove(dato)
                contador1 += 1
                if contador1 == 10:
                    break
            pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
            pdf.add_page()
            pdf.set_font('Arial','',16)
            pdf.text(x = 10, y = 20, txt = self.titule)
            pdf.text(x = 20, y = 30, txt = 'Jugador')
            pdf.text(x = 100, y = 30, txt = 'Tiempo')
            contador = 0
            contador2 = 1
            for top in self.lista_definitiva:
                pdf.text(x = 10, y = 40 + contador, txt = str(contador2))
                pdf.text(x = 20, y = 40 + contador, txt = top[4])
                pdf.text(x = 100, y = 40 + contador, txt = str(top[0]))
                pdf.text(x = 110, y = 40 + contador, txt = str(top[1]))
                pdf.text(x = 120, y = 40 + contador, txt = str(top[2]))
                contador += 10
                contador2 += 1
            pdf.output('TOP_10_RESUMEN.pdf')
        else:
            tkinter.messagebox.showinfo("MASTERMIND","ERRO NO HAY DATOS REGISTRADOS EN ESTA CATEGORÍA")

# This class is used to create a window that shows the top 10 most popular players in the database.
class ventana_top_10_detalle:

    def __init__(self,master):
        self.master = master
        self.canvas = Canvas(master,width=2000,height=1000,highlightthickness=0, relief='ridge',
                             bg = 'gray25')
        self.canvas.place(x=0,y=0)

        self.seleccionar_dificultad1 = tk.IntVar()

        self.label_titulo = Label(self.canvas, text='TOP 10 - DETALLE',font=('Games',45), fg='red', bg = 'dimgray') 
        self.label_titulo.place(x=278,y=5,width=450,height=50) #Titulo de la pantalla.

        self.dificultad_facil = Radiobutton(self.canvas, text = "Nivel Fácil", bg = 'gray25', value = 1, variable = self.seleccionar_dificultad1, command = self.validate_dificult)
        self.dificultad_facil.place(x = 100, y = 100)

        self.dificultad_medio = Radiobutton(self.canvas, text = "Nivel Medio", bg = 'gray25', value = 2, variable = self.seleccionar_dificultad1, command = self.validate_dificult)
        self.dificultad_medio.place(x = 100, y = 120)

        self.dificultad_dificil = Radiobutton(self.canvas, text = "Nivel difícil", bg = 'gray25', value = 3, variable = self.seleccionar_dificultad1, command = self.validate_dificult)
        self.dificultad_dificil.place(x = 100, y = 140)

        self.cancelar_juego = Button(self.canvas, text ='CONSULTAR',font=('Games',15) ,highlightbackground = '#FF8F00', highlightthickness = 30, command = self.create_pdf)
        self.cancelar_juego.place(x = 250, y = 200,width = 150, height = 50)

        self.salir_juego = Button(self.canvas, text ='SALIR',font=('Games',15) ,highlightbackground = '#FF0000', highlightthickness = 30, command = self.salir)
        self.salir_juego.place(x = 550, y = 200,width = 150, height = 50)

        self.seleccionar_dificultad1.set(1)
    
    def salir(self):
        self.canvas.destroy()

    def validate_dificult(self):
        seleccion = self.seleccionar_dificultad1.get()
        if seleccion == 1:
            self.dificultad = seleccion
        elif seleccion == 2:
            self.dificultad = seleccion
        else:
            self.dificultad = seleccion

    def create_pdf(self):
        self.lista_top_10 = []
        self.lista_definitiva = []
        self.validate_dificult()
        datos = open("mastermind2022top10.dat","rb")
        self.lista = []
        while True:
            try:
                lista_de_datos = pickle.load(datos)
                self.lista.append(lista_de_datos)
            except:
                break
        if self.dificultad == 1:
            self.titule = "TOP 10: NIVEL FÁCIL"
        elif self.dificultad == 2:
            self.titule = "TOP 10: NIVEL MEDIO"
        else:
            self.titule = "TOP 10: NIVEL DIFÍCIL"
        for jugador in self.lista:
            if jugador[3] == self.dificultad:
                self.lista_top_10.append(jugador)
        if self.lista_top_10:
            dato = min(self.lista_top_10)
            self.lista_definitiva.append(dato)
            self.lista_top_10.remove(dato)
            contador1 = 0
            while self.lista_top_10 != []:
                dato = min(self.lista_top_10)
                self.lista_definitiva.append(dato)
                self.lista_top_10.remove(dato)
                contador1 += 1
                if contador1 == 10:
                    break
            pdf = FPDF(orientation = 'L', unit = 'mm', format = 'A4')
            pdf.add_page()
            pdf.set_font('Arial','',10)
            pdf.text(x = 10, y = 20, txt = self.titule)
            pdf.text(x = 20, y = 30, txt = 'JUGADOR')
            pdf.text(x = 60, y = 30, txt = 'TIEMPO')
            pdf.text(x = 130, y = 30, txt = 'COMBINACIÓN')
            pdf.text(x = 210, y = 30, txt = 'FECHA/HORA DEL JUEGO')
            pdf.text(x = 270, y = 30, txt = 'T/J')
            contador2 = 1
            contador4 = 0
            eje_y = 40
            for top in self.lista_definitiva:
                eje_y += 10
                contador4 = 0
                pdf.text(x = 10, y =  eje_y, txt = str(contador2))
                pdf.text(x = 20, y =  eje_y, txt = top[4])
                pdf.text(x = 60, y =  eje_y, txt = str(top[0]))
                pdf.text(x = 70, y =  eje_y, txt = str(top[1]))
                pdf.text(x = 80, y =  eje_y, txt = str(top[2]))
                date = top[6]
                pdf.text(x = 210, y =  eje_y, txt = str(date[2]))
                pdf.text(x = 215, y =  eje_y, txt = '/')
                pdf.text(x = 218, y =  eje_y, txt = str(date[1]))
                pdf.text(x = 223, y =  eje_y, txt = '/')
                pdf.text(x = 225, y =  eje_y, txt = str(date[0]))
                dato1 = top[7]
                pdf.text(x = 238, y =  eje_y, txt = str(dato1[0]))
                pdf.text(x = 243, y =  eje_y, txt = ':')
                pdf.text(x = 245, y =  eje_y, txt = str(dato1[1]))
                if dato1[1] > 12:
                    pdf.text(x = 250, y =  eje_y, txt = 'PM')
                elif dato1[1] <= 12:
                    pdf.text(x = 250, y =  eje_y, txt = 'AM')
                contador2 += 1
                for time in top[8]:
                    pdf.text(x = 270, y =  eje_y, txt = str(time[0]))
                    pdf.text(x = 275, y = eje_y, txt = str(time[1]))
                    pdf.text(x = 280, y =  eje_y, txt = str(time[2]))
                    jugados = top[5]
                    jugadas = jugados[contador4]
                    if validate_list(jugadas) == False:
                        pdf.text(x = 90, y =  eje_y, txt = jugadas[0])
                        pdf.text(x = 120, y =  eje_y, txt = jugadas[1])
                        pdf.text(x = 150, y =  eje_y, txt = jugadas[2])
                        pdf.text(x = 180, y =  eje_y, txt = jugadas[3])
                        eje_y+= 10
                        contador4 += 1
                    else:
                        pdf.text(x = 110, y =  eje_y, txt = str(jugadas[0]))
                        pdf.text(x = 130, y =  eje_y, txt = str(jugadas[1]))
                        pdf.text(x = 150, y =  eje_y, txt = str(jugadas[2]))
                        pdf.text(x = 170, y =  eje_y, txt = str(jugadas[3]))
                        eje_y += 10
                        contador4 += 1
            pdf.output('TOP_10_DETALLE.pdf')
        else:
            tkinter.messagebox.showinfo("MASTERMIND","ERRO NO HAY DATOS REGISTRADOS EN ESTA CATEGORÍA")

# It creates a window with a label and a button
class ventana_acerca_de:

    def __init__(self,master):
        self.master = master
        self.canvas = Canvas(master,width=2000,height=1000,highlightthickness=0, relief='ridge',
                             bg = 'gray25')
        self.canvas.place(x=0,y=0)

        self.label_titulo = Label(self.canvas, text='ACERCA DE',font=('Games',45), fg='white', bg = "#050834") 
        self.label_titulo.place(x=278,y=100,width=450,height=50) #Titulo de la pantalla.

        self.label_titulo = Label(self.canvas, text='MASTERMIND',font=('Games',45), fg='white', bg = "#050834") 
        self.label_titulo.place(x=278,y=150,width=450,height=50) #Titulo de la pantalla.

        self.label_titulo = Label(self.canvas, text='VERSION 2.0',font=('Games',45), fg='white', bg = "#050834") 
        self.label_titulo.place(x=278,y=200,width=450,height=50) #Titulo de la pantalla.

        self.label_titulo = Label(self.canvas, text='Andrés González Sirias',font=('Games',25), fg='white', bg = "#050834") 
        self.label_titulo.place(x=278,y=250,width=450,height=50) #Titulo de la pantalla.

        self.label_titulo = Label(self.canvas, text='2022',font=('Games',45), fg='white', bg = "#050834") 
        self.label_titulo.place(x=278,y=300,width=450,height=50) #Titulo de la pantalla.

        self.salir_juego = Button(self.canvas, text ='SALIR',font=('Games',15) ,highlightbackground = '#FF0000', highlightthickness = 30, command = self.salir)
        self.salir_juego.place(x = 400, y = 400,width = 150, height = 50)

    def salir(self):
        self.canvas.destroy()

window = Tk()
ventana_principal = ventana_principal(window)
window.title("MASTERMIND")
window.minsize(1000,700)
window.resizable(0, 0)
window.mainloop() 

