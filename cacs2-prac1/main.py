import pygame
import tkinter
from tkinter import *
from tkinter.simpledialog import *
from tkinter import messagebox as MessageBox
from tablero import *
from dominio import *
from variable import *
from restriction import *
from pygame.locals import *
from copy import deepcopy

MEDIUM_PURPLE = (147, 112, 219)
DARK_PURPLE = (128, 0, 128)
WHITE = (255, 255, 255)

MARGEN=5 #ancho del borde entre celdas
MARGEN_INFERIOR=60 #altura del margen inferior entre la cuadrícula y la ventana
TAM=60  #tamaño de la celda
FILS=5 # número de filas del crucigrama
COLS=6 # número de columnas del crucigrama
RUTA_TABLERO = "Boards_Examples/mine1.txt"

LLENA='*' 
VACIA='-'


#########################################################################
# Detecta si se pulsa el botón de FC
######################################################################### 
def pulsaBotonFC(pos, anchoVentana, altoVentana):
    if pos[0]>=anchoVentana//4-25 and pos[0]<=anchoVentana//4+25 and pos[1]>=altoVentana-45 and pos[1]<=altoVentana-19:
        return True
    else:
        return False
    
######################################################################### 
# Detecta si se pulsa el botón de AC3
######################################################################### 
def pulsaBotonAC3(pos, anchoVentana, altoVentana):
    if pos[0]>=3*(anchoVentana//4)-25 and pos[0]<=3*(anchoVentana//4)+25 and pos[1]>=altoVentana-45 and pos[1]<=altoVentana-19:
        return True
    else:
        return False
    
######################################################################### 
# Detecta si se pulsa el botón de reset
######################################################################### 
def pulsaBotonReset(pos, anchoVentana, altoVentana):
    if pos[0]>=(anchoVentana//2)-25 and pos[0]<=(anchoVentana//2)+25 and pos[1]>=altoVentana-45 and pos[1]<=altoVentana-19:
        return True
    else:
        return False
    
######################################################################### 
# Detecta si el ratón se pulsa en la cuadrícula
######################################################################### 
def inTablero(pos):
    if pos[0]>=MARGEN and pos[0]<=(TAM+MARGEN)*COLS+MARGEN and pos[1]>=MARGEN and pos[1]<=(TAM+MARGEN)*FILS+MARGEN:        
        return True
    else:
        return False
    
######################################################################### 
# Busca posición de palabras de longitud tam en el almacen
######################################################################### 
def busca(almacen, tam):
    enc=False
    pos=-1
    i=0
    while i<len(almacen) and enc==False:
        if almacen[i].tam==tam: 
            pos=i
            enc=True
        i=i+1
    return pos
    
######################################################################### 
# Crea un almacen de palabras
######################################################################### 
def creaAlmacen():
    f= open('d0.txt', 'r', encoding="utf-8")
    lista=f.read()
    f.close()
    listaPal=lista.split()
    almacen=[]
   
    for pal in listaPal:        
        pos=busca(almacen, len(pal)) 
        if pos==-1: #no existen palabras de esa longitud
            dom=Dominio(len(pal))
            dom.addPal(pal.upper())            
            almacen.append(dom)
        elif pal.upper() not in almacen[pos].lista: #añade la palabra si no está duplicada        
            almacen[pos].addPal(pal.upper())           
    return almacen

######################################################################### 
# Imprime el contenido del almacen
######################################################################### 
def imprimeAlmacen(almacen):
    for dom in almacen:
        print (dom.tam)
        lista=dom.getLista()
        for pal in lista:
            print (pal, end=" ")
        print()


#########################################################################  
# Añadido por Mí
#########################################################################

def substract(a, b):
    return a - b

def is_outside_crossboard (i, j, board):
    return (i < 0 
            or  
            i >= board.alto 
            or 
            j < 0 
            or j >= board.ancho)

def is_inside_crossboard (i, j, board):
    return not is_outside_crossboard(i, j, board)

def is_solid(i, j, board):
    if is_outside_crossboard(i, j, board):
        return False
    return board.tablero[i][j] == '*'

def is_empty(i, j, board):
    if is_outside_crossboard(i, j, board):
        return False
    return board.tablero[i][j] == '-'

def has_letter(i, j, board):
    return (
        not is_empty(i, j, board) 
        and 
        not is_solid(i, j, board) 
        and 
        not is_outside_crossboard(i, j, board))   


def is_isolated(i, j, board):
    return (
              (
              is_solid(i - 1, j, board) 
              or 
              is_outside_crossboard(i - 1, j, board)
              )
              
              and
              
              (
              is_solid(i, j + 1, board) 
              or 
              is_outside_crossboard(i, j + 1, board)
              )
              
              and
              
              (
              is_solid(i + 1, j, board) 
              or 
              is_outside_crossboard(i + 1, j, board)
              )
              
              and
              
              (
              is_solid(i, j - 1, board) 
              or 
              is_outside_crossboard(i, j - 1, board)
              )
              
              and
              
              (
                  is_empty(i, j, board)
                  or
                  has_letter(i, j, board)
              )
              
             )

def initialize_1_isolated_variables(board, number_of_previous_variables = 0):
    isolated_variables_counter = number_of_previous_variables
    isolated_variable_list = []
    for i in range(board.getAlto()):
        for j in range(board.getAncho()):
            if is_isolated(i, j, board):
                isolated_variables_counter += 1
                new_isolated_variable = Word(
                                             name = isolated_variables_counter, 
                                             initial_pos = (i, j), 
                                             final_pos= (i, j),
                                             length = 1,
                                             orientation = "isolated")
                isolated_variable_list.append(new_isolated_variable)
    return isolated_variable_list

def is_right_horizontal_terminal(i, j, board):
    return (
            (
             is_solid(i, j + 1, board) 
             or 
             is_outside_crossboard(i, j + 1, board)
            )
            
            and
            (
                is_empty(i, j, board)
                or
                has_letter(i, j, board)
            )  
            )

def initialize_1_horizontal_variables(board, number_of_previous_variables = 0,
                                      horizontal_variable_list = None,
                                      list_of_variables = None):
    if horizontal_variable_list is None:
        horizontal_variable_list = []
    if list_of_variables is None:
        list_of_variables = []
    horizontal_variable_number = number_of_previous_variables
    horizontal_variable_length = 0
    for i in range(board.getAlto()):
        for j in range(board.getAncho()):
            if is_solid(i, j, board):
                continue
            horizontal_variable_length += 1
            if is_right_horizontal_terminal(i, j, board):
                if horizontal_variable_length == 1:
                    horizontal_variable_length = 0
                    continue
                horizontal_variable_number += 1
                new_horizontal_variable = (
                    Word(
                        name = horizontal_variable_number ,
                        initial_pos = (i, j - horizontal_variable_length + 1),
                        final_pos = (i, j),
                        length = horizontal_variable_length,
                        orientation = "horizontal"
                        )
                    )
                horizontal_variable_list.append(new_horizontal_variable)
                list_of_variables.append(new_horizontal_variable)
                horizontal_variable_length = 0
    return horizontal_variable_list

def is_down_vertical_terminal(i, j, board):
    return (
            (
             is_solid(i + 1, j, board) 
             or 
             is_outside_crossboard(i + 1, j, board)
            )
            
            and
            (
                is_empty(i, j, board)
                or
                has_letter(i, j, board)
            )  
            )

def initialize_1_vertical_variables(board, number_of_previous_variables = 0,
                                    vertical_variable_list = None,
                                    list_of_variables = None):
    if vertical_variable_list is None:
        vertical_variable_list = []
    if list_of_variables is None:
        list_of_variables = []
    vertical_variable_number = number_of_previous_variables
    vertical_variable_length = 0
    for j in range(board.getAncho()):
        for i in range(board.getAlto()):
            if is_solid(i, j, board):
                continue
            vertical_variable_length += 1
            if is_down_vertical_terminal(i, j, board):
                if vertical_variable_length == 1:
                    vertical_variable_length = 0
                    continue
                vertical_variable_number += 1
                new_vertical_variable = (
                    Word(
                        name = vertical_variable_number,
                        initial_pos= (i - vertical_variable_length + 1, j),
                        final_pos = (i, j),
                        length = vertical_variable_length,
                        orientation = "vertical"
                    )
                )
                vertical_variable_list.append(new_vertical_variable)
                list_of_variables.append(new_vertical_variable)
                vertical_variable_length = 0
    return vertical_variable_list

def initialize_1_horizontal_and_isolated_variables(board, number_of_previous_variables = 0,
                                                   horizontal_variable_list = None,
                                                   list_of_vertical_variables = None,
                                                   isolated_variable_list = None):
    if horizontal_variable_list is None:
        horizontal_variable_list = []
    if list_of_vertical_variables is None:
        list_of_vertical_variables = []
    if isolated_variable_list is None:
        isolated_variable_list = []
    horizontal_variable_number = number_of_previous_variables
    horizontal_variable_length = 0
    
    for i in range(board.getAlto()):
        for j in range(board.getAncho()):
            if is_solid(i, j, board):
                continue
            if is_isolated(i, j, board):
                horizontal_variable_number += 1   
                new_isolated_variable = Word(
                        name = len(isolated_variable_list) + number_of_previous_variables + 1,
                        initial_pos = (i, j),
                        final_pos = (i, j),
                        length = 1,
                        orientation = "isolated"
                    )
                isolated_variable_list.append(new_isolated_variable)
                continue
                
            horizontal_variable_length += 1
            if is_right_horizontal_terminal(i, j, board):
                if horizontal_variable_length == 1:
                    horizontal_variable_length = 0
                    continue
                horizontal_variable_number += 1
                new_horizontal_variable = (
                    Word(
                        name = len(horizontal_variable_list) + number_of_previous_variables + 1,
                        initial_pos = (i, j - horizontal_variable_length + 1),
                        final_pos = (i, j),
                        length = horizontal_variable_length,
                        orientation = "horizontal"
                        )
                    )
                horizontal_variable_list.append(new_horizontal_variable)
                list_of_vertical_variables.append(new_horizontal_variable)
                horizontal_variable_length = 0
                
    for word in isolated_variable_list:
        word.set_name(word.get_name() + len(horizontal_variable_list))
    
    list_of_vertical_variables.extend(isolated_variable_list)
    return list_of_vertical_variables


def initialize_1_vertical_and_isolated_variables(board, number_of_previous_variables = 0,
                                                   vertical_variable_list = None,
                                                   list_of_horizontal_variables = None,
                                                   isolated_variable_list = None):
    if vertical_variable_list is None:
        vertical_variable_list = []
    if list_of_horizontal_variables is None:
        list_of_horizontal_variables = []
    if isolated_variable_list is None:
        isolated_variable_list = []
    vertical_variable_number = number_of_previous_variables
    vertical_variable_length = 0
    
    for j in range(board.getAncho()):
        for i in range(board.getAlto()):
            if is_solid(i, j, board):
                continue
            if is_isolated(i, j, board):
                vertical_variable_number += 1   
                new_isolated_variable = Word(
                        name = len(isolated_variable_list) + number_of_previous_variables + 1,
                        initial_pos = (i, j),
                        final_pos = (i, j),
                        length = 1,
                        orientation = "isolated"
                    )
                isolated_variable_list.append(new_isolated_variable)
                continue
            vertical_variable_length += 1
            if is_down_vertical_terminal(i, j, board):
                if vertical_variable_length == 1:
                    vertical_variable_length = 0
                    continue
                vertical_variable_number += 1
                new_vertical_variable = (
                    Word(
                        name = len(vertical_variable_list) + number_of_previous_variables + 1,
                        initial_pos= (i - vertical_variable_length + 1, j),
                        final_pos = (i, j),
                        length = vertical_variable_length,
                        orientation = "vertical"
                    )
                )
                vertical_variable_list.append(new_vertical_variable)
                list_of_horizontal_variables.append(new_vertical_variable)
                vertical_variable_length = 0
                
    for word in isolated_variable_list:
        word.set_name(word.get_name() + len(vertical_variable_list))
    
    list_of_horizontal_variables.extend(isolated_variable_list)
    return list_of_horizontal_variables


def initialize_1_all_variables(board):
    n = board.getAlto()
    m = board.getAncho()
    list_of_variables = []
    isolated_variable_list = []
    dictionary_of_variables = {}
    
    if m >= n:
        horizontal_variable_list = []
        vertical_variable_list = []
        initialize_1_horizontal_variables(board, 0, horizontal_variable_list,
                                          list_of_variables)
        dictionary_of_variables["horizontal"] = horizontal_variable_list
        initialize_1_vertical_and_isolated_variables(board,
                                                     len(list_of_variables),
                                                     vertical_variable_list,
                                                     list_of_variables,
                                                     isolated_variable_list)
        dictionary_of_variables["vertical"] = vertical_variable_list
        dictionary_of_variables["isolated"] = isolated_variable_list
        
        
        
    else:
        vertical_variable_list = []
        horizontal_variable_list = []
        initialize_1_vertical_variables(board, 0, vertical_variable_list,
                                        list_of_variables)
        dictionary_of_variables["vertical"] = vertical_variable_list
        initialize_1_horizontal_and_isolated_variables(board,
                                                       len(list_of_variables),
                                                       horizontal_variable_list,
                                                       list_of_variables,
                                                       isolated_variable_list)
        dictionary_of_variables["horizontal"] = horizontal_variable_list
        dictionary_of_variables["isolated"] = isolated_variable_list
    
    return dictionary_of_variables

def initialize_2_all_variables(board):
    n = board.getAlto()
    m = board.getAncho()
    list_of_variables = []
    isolated_variable_list = []
    dictionary_of_variables = {}
    
    if m >= n:
        vertical_variable_list = []
        horizontal_variable_list = []
        initialize_1_vertical_variables(board, 0, vertical_variable_list,
                                        list_of_variables)
        dictionary_of_variables["vertical"] = vertical_variable_list
        initialize_1_horizontal_and_isolated_variables(board,
                                                       len(list_of_variables),
                                                       horizontal_variable_list,
                                                       list_of_variables,
                                                       isolated_variable_list)
        dictionary_of_variables["horizontal"] = horizontal_variable_list
        dictionary_of_variables["isolated"] = isolated_variable_list
        
    else:
        horizontal_variable_list = []
        vertical_variable_list = []
        initialize_1_horizontal_variables(board, 0, horizontal_variable_list,
                                          list_of_variables)
        dictionary_of_variables["horizontal"] = horizontal_variable_list
        initialize_1_vertical_and_isolated_variables(board,
                                                     len(list_of_variables),
                                                     vertical_variable_list,
                                                     list_of_variables,
                                                     isolated_variable_list)
        dictionary_of_variables["vertical"] = vertical_variable_list
        dictionary_of_variables["isolated"] = isolated_variable_list

    
    return dictionary_of_variables


def create_storage_with_hash_table(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        lista = f.read()
    
    listaPal = lista.split()
    almacen = {}
   
    for pal in listaPal:
        tam = len(pal)
        if tam not in almacen:
            dom = Dominio(tam)
            dom.addPal(pal.upper())
            almacen[tam] = dom
        elif pal.upper() not in almacen[tam].getLista():
            almacen[tam].addPal(pal.upper())
            
    return almacen

def initialize_feasibles_v1(board, storage, dictionary_of_variables):
    
    for word in dictionary_of_variables["horizontal"]:
        word.set_feasibles(storage[word.get_length()].getLista())
        
    for word in dictionary_of_variables["vertical"]:
        word.set_feasibles(storage[word.get_length()].getLista())
        
    for word in dictionary_of_variables["isolated"]:
        word.set_feasibles(storage[word.get_length()].getLista())
        
    return dictionary_of_variables

def initialize_restrictions_v1(board, hash_table_of_variables):
    restrictions = []



#########################################################################  
# Principal
#########################################################################
def main():
    root= tkinter.Tk() #para eliminar la ventana de Tkinter
    root.withdraw() #se cierra
    pygame.init()
    
    reloj=pygame.time.Clock()
    
    anchoVentana=COLS*(TAM+MARGEN)+MARGEN
    altoVentana= MARGEN_INFERIOR+FILS*(TAM+MARGEN)+MARGEN
    
    dimension=[anchoVentana,altoVentana]
    screen=pygame.display.set_mode(dimension) 
    pygame.display.set_caption("Practica 1: Crucigrama")
    
    botonFC=pygame.image.load("botonFC.png").convert()
    botonFC=pygame.transform.scale(botonFC,[50, 30])
    
    botonAC3=pygame.image.load("botonAC3.png").convert()
    botonAC3=pygame.transform.scale(botonAC3,[50, 30])
    
    botonReset=pygame.image.load("botonReset.png").convert()
    botonReset=pygame.transform.scale(botonReset,[50,30])
    
    almacen=creaAlmacen()
    game_over=False
    tablero=Tablero(FILS, COLS,RUTA_TABLERO)
    print (tablero)    
    while not game_over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:               
                game_over=True
            if event.type==pygame.MOUSEBUTTONUP:                
                #obtener posición y calcular coordenadas matriciales                               
                pos=pygame.mouse.get_pos()                
                if pulsaBotonFC(pos, anchoVentana, altoVentana):
                    print("FC")
                    res=False #aquí llamar al forward checking
                    if res==False:
                        #MessageBox.showwarning("Alerta", "No hay solución")
                        print("No hay solución")                                  
                elif pulsaBotonAC3(pos, anchoVentana, altoVentana):                    
                     print("AC3")
                elif pulsaBotonReset(pos, anchoVentana, altoVentana):                   
                    tablero.reset()
                elif inTablero(pos):
                    colDestino=pos[0]//(TAM+MARGEN)
                    filDestino=pos[1]//(TAM+MARGEN)                    
                    if event.button==1: #botón izquierdo
                        if tablero.getCelda(filDestino, colDestino)==VACIA:
                            tablero.setCelda(filDestino, colDestino, LLENA)
                        else:
                            tablero.setCelda(filDestino, colDestino, VACIA)
                    elif event.button==3: #botón derecho
                        c=askstring('Entrada', 'Introduce carácter')
                        tablero.setCelda(filDestino, colDestino, c.upper())   
            
        ##código de dibujo        
        #limpiar pantalla
        screen.fill(DARK_PURPLE)
        pygame.draw.rect(screen, MEDIUM_PURPLE, [0, 0, COLS*(TAM+MARGEN)+MARGEN, altoVentana],0)
        for fil in range(tablero.getAlto()):
            for col in range(tablero.getAncho()):
                if tablero.getCelda(fil, col)==VACIA: 
                    pygame.draw.rect(screen, WHITE, [(TAM+MARGEN)*col+MARGEN, (TAM+MARGEN)*fil+MARGEN, TAM, TAM], 0)
                elif tablero.getCelda(fil, col)==LLENA: 
                    pygame.draw.rect(screen, DARK_PURPLE, [(TAM+MARGEN)*col+MARGEN, (TAM+MARGEN)*fil+MARGEN, TAM, TAM], 0)
                else: #dibujar letra                    
                    pygame.draw.rect(screen, WHITE, [(TAM+MARGEN)*col+MARGEN, (TAM+MARGEN)*fil+MARGEN, TAM, TAM], 0)
                    fuente= pygame.font.Font(None, 70)
                    texto= fuente.render(tablero.getCelda(fil, col), True, DARK_PURPLE)            
                    screen.blit(texto, [(TAM+MARGEN)*col+MARGEN+15, (TAM+MARGEN)*fil+MARGEN+5])             
        #pintar botones        
        screen.blit(botonFC, [anchoVentana//4-25, altoVentana-45])
        screen.blit(botonAC3, [3*(anchoVentana//4)-25, altoVentana-45])
        screen.blit(botonReset, [anchoVentana//2-25, altoVentana-45])
        #actualizar pantalla
        pygame.display.flip()
        reloj.tick(40)
        if game_over==True: #retardo cuando se cierra la ventana
            pygame.time.delay(500)
    
    pygame.quit()
 
if __name__=="__main__":
    main()
 
