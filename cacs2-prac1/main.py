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

MARGEN = 5  # ancho del borde entre celdas
MARGEN_INFERIOR = 60  # altura del margen inferior entre la cuadrícula y la ventana
TAM = 30  # tamaño de la celda
FILS = 5  # número de filas del crucigrama
COLS = 6  # número de columnas del crucigrama

#RUTA_TABLERO = "Boards_Examples/debug_forward_checking/debug_1.txt"
#RUTA_DOMINIOS = "Domains_Examples/debug_forward_checking/debug_1.txt"

RUTA_TABLERO = 'Boards_Examples/moodle_example.txt'
RUTA_DOMINIOS = 'Domains_Examples/d0.txt'

#RUTA_TABLERO = 'Boards_Examples/complex.txt'
#RUTA_DOMINIOS = 'Domains_Examples/Top3000EnglishWords.txt'

LLENA = '*'
VACIA = '-'


#########################################################################
# Detecta si se pulsa el botón de FC
#########################################################################
def pulsaBotonFC(pos, anchoVentana, altoVentana):
    if pos[0] >= anchoVentana//4-25 and pos[0] <= anchoVentana//4+25 and pos[1] >= altoVentana-45 and pos[1] <= altoVentana-19:
        return True
    else:
        return False

#########################################################################
# Detecta si se pulsa el botón de AC3
#########################################################################


def pulsaBotonAC3(pos, anchoVentana, altoVentana):
    if pos[0] >= 3*(anchoVentana//4)-25 and pos[0] <= 3*(anchoVentana//4)+25 and pos[1] >= altoVentana-45 and pos[1] <= altoVentana-19:
        return True
    else:
        return False

#########################################################################
# Detecta si se pulsa el botón de reset
#########################################################################


def pulsaBotonReset(pos, anchoVentana, altoVentana):
    if pos[0] >= (anchoVentana//2)-25 and pos[0] <= (anchoVentana//2)+25 and pos[1] >= altoVentana-45 and pos[1] <= altoVentana-19:
        return True
    else:
        return False

#########################################################################
# Detecta si el ratón se pulsa en la cuadrícula
#########################################################################


def inTablero(pos):
    if pos[0] >= MARGEN and pos[0] <= (TAM+MARGEN)*COLS+MARGEN and pos[1] >= MARGEN and pos[1] <= (TAM+MARGEN)*FILS+MARGEN:
        return True
    else:
        return False

#########################################################################
# Busca posición de palabras de longitud tam en el almacen
#########################################################################


def busca(almacen, tam):
    enc = False
    pos = -1
    i = 0
    while i < len(almacen) and enc == False:
        if almacen[i].tam == tam:
            pos = i
            enc = True
        i = i+1
    return pos

#########################################################################
# Crea un almacen de palabras
#########################################################################


def creaAlmacen():
    f = open('d0.txt', 'r', encoding="utf-8")
    lista = f.read()
    f.close()
    listaPal = lista.split()
    almacen = []

    for pal in listaPal:
        pos = busca(almacen, len(pal))
        if pos == -1:  # no existen palabras de esa longitud
            dom = Dominio(len(pal))
            dom.addPal(pal.upper())
            almacen.append(dom)
        # añade la palabra si no está duplicada
        elif pal.upper() not in almacen[pos].lista:
            almacen[pos].addPal(pal.upper())
    return almacen

#########################################################################
# Imprime el contenido del almacen
#########################################################################


def imprimeAlmacen(almacen):
    for dom in almacen:
        print(dom.tam)
        lista = dom.getLista()
        for pal in lista:
            print(pal, end=" ")
        print()


#########################################################################
# Añadido por Mí
#########################################################################

def substract(a, b):
    return a - b


def is_outside_crossboard(i, j, board):
    return (i < 0
            or
            i >= board.alto
            or
            j < 0
            or j >= board.ancho)


def is_inside_crossboard(i, j, board):
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


def initialize_1_isolated_variables(board, number_of_previous_variables=0):
    isolated_variables_counter = number_of_previous_variables
    isolated_variable_list = []
    for i in range(board.getAlto()):
        for j in range(board.getAncho()):
            if is_isolated(i, j, board):
                isolated_variables_counter += 1
                new_isolated_variable = Word(
                    name=isolated_variables_counter,
                    initial_pos=(i, j),
                    final_pos=(i, j),
                    length=1,
                    orientation="isolated")
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


def initialize_1_horizontal_variables(board, number_of_previous_variables=0,
                                      horizontal_variable_list=None,
                                      list_of_variables=None):
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
                        name=horizontal_variable_number,
                        initial_pos=(i, j - horizontal_variable_length + 1),
                        final_pos=(i, j),
                        length=horizontal_variable_length,
                        orientation="horizontal"
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


def initialize_1_vertical_variables(board, number_of_previous_variables=0,
                                    vertical_variable_list=None,
                                    list_of_variables=None):
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
                        name=vertical_variable_number,
                        initial_pos=(i - vertical_variable_length + 1, j),
                        final_pos=(i, j),
                        length=vertical_variable_length,
                        orientation="vertical"
                    )
                )
                vertical_variable_list.append(new_vertical_variable)
                list_of_variables.append(new_vertical_variable)
                vertical_variable_length = 0
    return vertical_variable_list


def initialize_1_horizontal_and_isolated_variables(board, number_of_previous_variables=0,
                                                   horizontal_variable_list=None,
                                                   list_of_vertical_variables=None,
                                                   isolated_variable_list=None):
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
                    name=len(isolated_variable_list) +
                    number_of_previous_variables + 1,
                    initial_pos=(i, j),
                    final_pos=(i, j),
                    length=1,
                    orientation="isolated"
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
                        name=len(horizontal_variable_list) +
                        number_of_previous_variables + 1,
                        initial_pos=(i, j - horizontal_variable_length + 1),
                        final_pos=(i, j),
                        length=horizontal_variable_length,
                        orientation="horizontal"
                    )
                )
                horizontal_variable_list.append(new_horizontal_variable)
                list_of_vertical_variables.append(new_horizontal_variable)
                horizontal_variable_length = 0

    for word in isolated_variable_list:
        word.set_name(word.get_name() + len(horizontal_variable_list))

    list_of_vertical_variables.extend(isolated_variable_list)
    return list_of_vertical_variables


def initialize_1_vertical_and_isolated_variables(board, number_of_previous_variables=0,
                                                 vertical_variable_list=None,
                                                 list_of_horizontal_variables=None,
                                                 isolated_variable_list=None):
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
                    name=len(isolated_variable_list) +
                    number_of_previous_variables + 1,
                    initial_pos=(i, j),
                    final_pos=(i, j),
                    length=1,
                    orientation="isolated"
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
                        name=len(vertical_variable_list) +
                        number_of_previous_variables + 1,
                        initial_pos=(i - vertical_variable_length + 1, j),
                        final_pos=(i, j),
                        length=vertical_variable_length,
                        orientation="vertical"
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




    """
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

    
    """

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


def get_initial_letters(board):
    initial_letters = {}
    for i in range(board.getAlto()):
        for j in range(board.getAncho()):
            if has_letter(i, j, board):
                initial_letters[(i, j)] = board.getCelda(i, j)
    return initial_letters


def square_belongs_to_word(i, j, word):
    if word.get_orientation() == "horizontal":
        return i == word.get_initial_pos()[0] and j >= word.get_initial_pos()[1] and j <= word.get_final_pos()[1]

    elif word.get_orientation() == "vertical":
        return j == word.get_initial_pos()[1] and i >= word.get_initial_pos()[0] and i <= word.get_final_pos()[0]

    elif word.get_orientation() == "isolated":
        return i == word.get_initial_pos()[0] and j == word.get_initial_pos()[1]


def initialize_restrictions_v1(board, initial_letters, hash_table_of_variables):
    founded = False

    for key in initial_letters:
        for word in hash_table_of_variables["horizontal"]:
            if square_belongs_to_word(key[0], key[1], word):
                new_restriction = Restriction(word, word,
                                              key[0], key[1],
                                              board.getCelda(key[0], key[1]))
                word.add_restriction(new_restriction)
                founded = True
                break

        for word in hash_table_of_variables["vertical"]:
            if square_belongs_to_word(key[0], key[1], word):
                new_restriction = Restriction(word, word,
                                              key[0], key[1],
                                              board.getCelda(key[0], key[1]))
                word.add_restriction(new_restriction)
                founded = True
                break

        for word in hash_table_of_variables["isolated"]:
            if square_belongs_to_word(key[0], key[1], word):
                new_restriction = Restriction(word, word,
                                              key[0], key[1],
                                              board.getCelda(key[0], key[1]))
                word.add_restriction(new_restriction)
                founded = True
                break
        founded = False


def count_number_of_variables(hash_table_of_variables):
    count = 0
    for key in hash_table_of_variables:
        count += len(hash_table_of_variables[key])
    return count


def count_number_of_horizontal_variables(hash_table_of_variables):
    return len(hash_table_of_variables["horizontal"])


def count_number_of_vertical_variables(hash_table_of_variables):
    return len(hash_table_of_variables["vertical"])


def count_number_of_isolated_variables(hash_table_of_variables):
    return len(hash_table_of_variables["isolated"])


def get_common_square_coordinates_from_two_variables(word_a, word_b):
    if word_a.get_orientation() == word_b.get_orientation():
        if word_a.get_orientation() == "isolated":
            if word_a.get_initial_pos() == word_b.get_initial_pos():
                return word_a.get_initial_pos()
            else:
                return None
        else:
            return None

    else:
        horizontal_word = word_a if word_a.get_orientation() == "horizontal" else word_b
        vertical_word = word_a if word_a.get_orientation() == "vertical" else word_b

        common_square = (
            horizontal_word.get_initial_pos()[0],
            vertical_word.get_initial_pos()[1]
        )

        if (
            square_belongs_to_word(common_square[0],
                                   common_square[1],
                                   horizontal_word)
            and
            square_belongs_to_word(common_square[0],
                                   common_square[1],
                                   vertical_word)
        ):
            return common_square

        else:
            return None


def ok_restriction_between_two_variables(board, word_a, word_b, feasible_b):
    result = False
    common_square = get_common_square_coordinates_from_two_variables(
        word_a, word_b)

    if common_square is None:
        result = True
        return result

    horizontal_word = word_a if word_a.get_orientation() == "horizontal" else word_b
    vertical_word = word_a if word_a.get_orientation() == "vertical" else word_b

    horizontal_word_index = abs(
        (
            common_square[1]
            -
            horizontal_word.get_initial_pos()[1]
        )
    )

    vertical_word_index = abs(
        (
            common_square[0]
            -
            vertical_word.get_initial_pos()[0]
        )
    )

    if word_a.get_orientation() == "horizontal":
        if word_a.get_value()[horizontal_word_index] == feasible_b[vertical_word_index]:
            result = True

    elif word_a.get_orientation() == "vertical":
        if word_a.get_value()[vertical_word_index] == feasible_b[horizontal_word_index]:
            result = True

    return result


def pound_reflexive_restrictions(hash_table_of_variables):
    for key in hash_table_of_variables:
        acces_variable_index = -1
        for word in hash_table_of_variables[key]:
            acces_variable_index += 1
            if len(word.get_restrictions()) == 0:
                continue
            word_checked_deep_copy = deepcopy(word)
            for restriction in word.get_restrictions()[word.get_name()]:
                restriction_value = restriction.get_letter_of_restriction()
                word_index = -1
                if word.get_orientation() == "horizontal":
                    word_index = abs(
                        (
                            restriction.get_y_coordinate()
                            -
                            word.get_initial_pos()[1]
                        )
                    )
                    
                elif word.get_orientation() == "vertical":
                    word_index = abs(
                        (
                            restriction.get_x_coordinate()
                            -
                            word.get_initial_pos()[0]
                        )
                    )
                            
                elif word.get_orientation() == "isolated":
                    word_index = 0

                list_of_feasibles = hash_table_of_variables[key][acces_variable_index].get_feasibles()
                for feasible_value in list_of_feasibles:
                    if feasible_value[word_index] != restriction_value:
                        word_checked_deep_copy.remove_feasible(feasible_value)
                
                hash_table_of_variables[key][acces_variable_index] = word_checked_deep_copy
  
def pound_reflexive_restrictions_version_2(hash_table_of_variables):
    for key in hash_table_of_variables:
        acces_variable_index = -1
        for word in hash_table_of_variables[key]:
            acces_variable_index += 1
            if len(word.get_restrictions()) == 0:
                continue
            word_checked_deep_copy = deepcopy(word)
            for restriction in word.get_restrictions()[word.get_name()]:
                restriction_value = restriction.get_letter_of_restriction()
                word_index = -1
                if word.get_orientation() == "horizontal":
                    word_index = abs(
                        (
                            restriction.get_y_coordinate()
                            -
                            word.get_initial_pos()[1]
                        )
                    )
                    
                elif word.get_orientation() == "vertical":
                    word_index = abs(
                        (
                            restriction.get_x_coordinate()
                            -
                            word.get_initial_pos()[0]
                        )
                    )
                            
                elif word.get_orientation() == "isolated":
                    word_index = 0

                list_of_feasibles = hash_table_of_variables[key][acces_variable_index].get_feasibles()
                for feasible_value in list_of_feasibles:
                    if feasible_value[word_index] != restriction_value:
                        word_checked_deep_copy.remove_feasible(feasible_value)
                
                hash_table_of_variables[key][acces_variable_index] = word_checked_deep_copy
                
                if hash_table_of_variables[key][acces_variable_index].get_feasibles() == []:
                    return False
                
    return True

def forward(board, concrete_variable, hash_table_of_variables):
    result = False
    number_of_variables_to_be_checked = 0
    orientation_to_be_checked = "-"

    if concrete_variable.get_orientation() == "horizontal":
        orientation_to_be_checked = "vertical"
        number_of_variables_to_be_checked = count_number_of_vertical_variables(
            hash_table_of_variables)

    elif concrete_variable.get_orientation() == "vertical":
        orientation_to_be_checked = "horizontal"
        number_of_variables_to_be_checked = count_number_of_horizontal_variables(
            hash_table_of_variables)
    
    elif concrete_variable.get_orientation() == "isolated":
        return True

    """
    elif concrete_variable.get_orientation() == "isolated":
        if ok_restriction_between_two_variables(board,
                                                concrete_variable,
                                                concrete_variable,
                                                concrete_variable.get_value()):
            result = True
            return result
        else:
            result = False
            return result
    """
    
    for j in range(number_of_variables_to_be_checked):
        empty = True
        variable_checked_deep_copy = deepcopy(hash_table_of_variables
                                              [orientation_to_be_checked][j])
        for feasible_value in (hash_table_of_variables
                               [orientation_to_be_checked]
                               [j].get_feasibles()):
            if ok_restriction_between_two_variables(board,
                                                    concrete_variable,
                                                    hash_table_of_variables
                                                    [orientation_to_be_checked][j],
                                                    feasible_value):
                empty = False
            else:
                variable_checked_deep_copy.remove_feasible(feasible_value)
                variable_checked_deep_copy.add_pound(
                    concrete_variable, feasible_value)
        hash_table_of_variables[orientation_to_be_checked][j] = variable_checked_deep_copy
        if empty == True:
            result = False
            return result

    result = True
    return result


def restore(board, restrainer_variable, hash_table_of_variables):
    result = False
    number_of_variables_to_be_checked = 0
    orientation_to_be_checked = "-"

    if restrainer_variable.get_orientation() == "horizontal":
        orientation_to_be_checked = "vertical"
        number_of_variables_to_be_checked = count_number_of_vertical_variables(
            hash_table_of_variables)

    elif restrainer_variable.get_orientation() == "vertical":
        orientation_to_be_checked = "horizontal"
        number_of_variables_to_be_checked = count_number_of_horizontal_variables(
            hash_table_of_variables)
    
    for j in range(number_of_variables_to_be_checked):
        hash_table_of_pounds = (hash_table_of_variables
                                [orientation_to_be_checked][j].
                                get_pounds())
        if (restrainer_variable.get_name()
            in
            hash_table_of_pounds):
            list_of_pounded_values = (hash_table_of_pounds
                                      [restrainer_variable
                                       .get_name()])
            
            checked_variable = deepcopy(
                hash_table_of_variables
                [orientation_to_be_checked][j]
            )
            
            for pounded_value in list_of_pounded_values:
                checked_variable.remove_pound(restrainer_variable,
                                               pounded_value)
                checked_variable.add_feasible(pounded_value)
                
            hash_table_of_variables[orientation_to_be_checked][j] = checked_variable

def set_word_on_board(board, word, value):
    
    if word.get_orientation() == "horizontal":
        for j in range(word.get_length()):
            board.setCelda(word.get_initial_pos()[0],
                           word.get_initial_pos()[1] + j,
                           value[j])
            
    elif word.get_orientation() == "vertical":
        for i in range(word.get_length()):
            board.setCelda(word.get_initial_pos()[0] + i,
                           word.get_initial_pos()[1],
                           value[i])
            
    elif word.get_orientation() == "isolated":
        board.setCelda(word.get_initial_pos()[0],
                       word.get_initial_pos()[1],
                       value[0])


def FC(variable_number,
       board, hash_table_of_variables,
       number_of_horizontals,
       number_of_verticals,
       number_of_isolated,
       total_number_of_variables,
       debug_flag = False):
    
    access_orientation = "-"
    access_index = -1
    
    if 0 < variable_number <= number_of_horizontals:
        access_orientation = "horizontal"
        access_index = variable_number - 1
    
    elif number_of_horizontals < variable_number <= number_of_horizontals + number_of_verticals:
        access_orientation = "vertical"
        access_index = variable_number - number_of_horizontals - 1
    
    elif number_of_horizontals + number_of_verticals < variable_number <= number_of_horizontals + number_of_verticals + number_of_isolated:
        access_orientation = "isolated"
        access_index = variable_number - number_of_horizontals - number_of_verticals  - 1
    
    for feasible_value in (hash_table_of_variables
                           [access_orientation]
                           [access_index]
                           .get_feasibles()):
        hash_table_of_variables[access_orientation][access_index].set_value(feasible_value)
        if ((hash_table_of_variables[access_orientation][access_index].get_name()) == 1
            and
            hash_table_of_variables[access_orientation][access_index].get_value() == "ASS"):
            print("") 
        if debug_flag == True:
            set_word_on_board(board,
                              hash_table_of_variables[access_orientation][access_index],
                              hash_table_of_variables[access_orientation][access_index].get_value())
        
        if variable_number == total_number_of_variables:
            return True
        else:
            if forward(board,
                    hash_table_of_variables[access_orientation][access_index],
                    hash_table_of_variables):
                
                if FC(variable_number + 1,
                      board, hash_table_of_variables,
                      number_of_horizontals,
                      number_of_verticals,
                      number_of_isolated,
                      total_number_of_variables,
                      debug_flag):
                    return True
            else:
                restore(board,
                        hash_table_of_variables[access_orientation][access_index],
                        hash_table_of_variables)
    
    return False
                    


def forward_checking(board, domains_filename, debug_flag = False):
    hash_table_of_variables = initialize_1_all_variables(board)
    hash_table_of_domains = create_storage_with_hash_table(domains_filename)
    initialize_feasibles_v1(board, hash_table_of_domains, hash_table_of_variables)
    
    initial_letters_hash_map = get_initial_letters(board)
    initialize_restrictions_v1(board, initial_letters_hash_map, hash_table_of_variables)
    
    reflexive_pound_result = pound_reflexive_restrictions_version_2(hash_table_of_variables)
    
    if reflexive_pound_result == False:
        return False
    
    variable_number = 1
    number_of_horizontals = count_number_of_horizontal_variables(hash_table_of_variables)
    number_of_verticals = count_number_of_vertical_variables(hash_table_of_variables)
    number_of_isolated = count_number_of_isolated_variables(hash_table_of_variables)
    total_number_of_variables = count_number_of_variables(hash_table_of_variables)
    
    result = FC(variable_number,
       board, hash_table_of_variables,
       number_of_horizontals,
       number_of_verticals,
       number_of_isolated,
       total_number_of_variables,
       debug_flag)
    
    return result


def store_crossboard(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    # Initialize the 2D array
    crossboard = []
    
    for line in lines:
        # Remove newline characters and convert the line to a list of characters
        row = list(line.strip())
        crossboard.append(row)
    
    return crossboard

def tablero_to_2d_array(tablero):
    alto = tablero.getAlto()
    ancho = tablero.getAncho()
    array_2d = []

    for i in range(alto):
        row = []
        for j in range(ancho):
            row.append(tablero.getCelda(i, j))
        array_2d.append(row)
    
    return array_2d

def set_up_1_for_tests(board, domains_filename,
                       hash_table_of_variables,
                       hash_table_of_domains):
    # Clear the dictionaries to ensure they are empty before updating
    hash_table_of_variables.clear()
    hash_table_of_domains.clear()

    # Update the dictionaries with the new data
    hash_table_of_variables.update(initialize_1_all_variables(board))
    hash_table_of_domains.update(create_storage_with_hash_table(domains_filename))
    initialize_feasibles_v1(board, hash_table_of_domains, hash_table_of_variables)
    
    initial_letters_hash_map = get_initial_letters(board)
    initialize_restrictions_v1(board, initial_letters_hash_map, hash_table_of_variables)
    
    reflexive_pound_result = pound_reflexive_restrictions_version_2(hash_table_of_variables)

def assign_all_restrictions(board, hash_table_of_variables):
    for key in hash_table_of_variables:
        access_variable_index = -1
        for word_restricted in hash_table_of_variables[key]:
            
            if word_restricted.get_orientation() == "isolated":
                return
            
            access_variable_index += 1
            access_orientation = "-"
            
            checked_restricted_variable = deepcopy(hash_table_of_variables
                                                   [key][access_variable_index])
            
            
            if word_restricted.get_orientation() == "horizontal":
                access_orientation = "vertical"
            
            elif word_restricted.get_orientation() == "vertical":  
                access_orientation = "horizontal"
            
            for word_restrainer in hash_table_of_variables[access_orientation]:
                common_square = get_common_square_coordinates_from_two_variables(word_restricted,
                                                                                 word_restrainer)
                if common_square != None:
                    checked_restricted_variable.add_restriction(Restriction(
                        word_restrainer,
                        word_restricted,
                        common_square[0],
                        common_square[1],
                        board.getCelda(common_square[0], common_square[1])
                    ))
        
            hash_table_of_variables[key][access_variable_index] = checked_restricted_variable
                

def initialize_hash_table_for_AC3(board, hash_table_of_variables):
    hash_table_AC3 = {}
    
    for key in hash_table_of_variables:
        for word in hash_table_of_variables[key]:
            hash_table_AC3[word.get_name()] = word
    
    return hash_table_AC3

def ok_restriction_between_two_variables_version2(board, 
                                                  word_a, feasible_a, 
                                                  word_b, feasible_b):
    result = False
    common_square = get_common_square_coordinates_from_two_variables(
        word_a, word_b)

    if common_square is None:
        result = True
        return result

    horizontal_word = word_a if word_a.get_orientation() == "horizontal" else word_b
    vertical_word = word_a if word_a.get_orientation() == "vertical" else word_b

    horizontal_word_index = abs(
        (
            common_square[1]
            -
            horizontal_word.get_initial_pos()[1]
        )
    )

    vertical_word_index = abs(
        (
            common_square[0]
            -
            vertical_word.get_initial_pos()[0]
        )
    )

    if word_a.get_orientation() == "horizontal":
        if feasible_a[horizontal_word_index] == feasible_b[vertical_word_index]:
            result = True

    elif word_a.get_orientation() == "vertical":
        if feasible_a[vertical_word_index] == feasible_b[horizontal_word_index]:
            result = True

    return result


def assign_access_orientation_and_access_index(
                        variable_number, 
                        number_of_horizontals, 
                        number_of_verticals,
                        number_of_isolated):
    
    access_orientation = "-"
    access_index = -1
    
    if 0 < variable_number <= number_of_horizontals:
        access_orientation = "horizontal"
        access_index = variable_number - 1
    
    elif number_of_horizontals < variable_number <= number_of_horizontals + number_of_verticals:
        access_orientation = "vertical"
        access_index = variable_number - number_of_horizontals - 1
    
    elif number_of_horizontals + number_of_verticals < variable_number <= number_of_horizontals + number_of_verticals + number_of_isolated:
        access_orientation = "isolated"
        access_index = variable_number - number_of_horizontals - number_of_verticals  - 1
    
    return access_orientation, access_index



def revise(board, 
           hash_table_of_variables,
           word_restricted, word_restrainer):
    revised = False
    checked_word_restricted = deepcopy(word_restricted)
    
    variable_number = word_restricted.get_name()
    number_of_horizontals = count_number_of_horizontal_variables(hash_table_of_variables)
    number_of_verticals = count_number_of_vertical_variables(hash_table_of_variables)
    number_of_isolated = count_number_of_isolated_variables(hash_table_of_variables)
    
    acces_index = assign_access_orientation_and_access_index(variable_number,
                                                             number_of_horizontals,
                                                             number_of_verticals,
                                                             number_of_isolated)[1]
    
    for feasible_value_restricted in word_restricted.get_feasibles():
        exist_compatible_in_restrainer = False
        
        for feasible_value_restrainer in word_restrainer.get_feasibles():
            if ok_restriction_between_two_variables_version2(board,
                                                             word_restrainer, feasible_value_restrainer,
                                                             word_restricted, feasible_value_restricted):   
                exist_compatible_in_restrainer = True
                break
            
        if exist_compatible_in_restrainer == False:
            checked_word_restricted.remove_feasible(feasible_value_restricted)
            revised = True
    
    hash_table_of_variables[word_restricted.get_orientation()][acces_index] = checked_word_restricted
    
    return revised
            
       
        

#########################################################################
# Principal
#########################################################################
def main():
    global TAM
    root = tkinter.Tk()  
    root.withdraw()
    pygame.init()

    reloj = pygame.time.Clock()

    
    TAM = min(600 // FILS, 600 // COLS)

    anchoVentana = COLS * (TAM + MARGEN) + MARGEN
    altoVentana = MARGEN_INFERIOR + FILS * (TAM + MARGEN) + MARGEN

    dimension = [anchoVentana, altoVentana]
    screen = pygame.display.set_mode(dimension)
    pygame.display.set_caption("Practica 1: Crucigrama")

    botonFC = pygame.image.load("botonFC.png").convert()
    botonFC = pygame.transform.scale(botonFC, [50, 30])

    botonAC3 = pygame.image.load("botonAC3.png").convert()
    botonAC3 = pygame.transform.scale(botonAC3, [50, 30])

    botonReset = pygame.image.load("botonReset.png").convert()
    botonReset = pygame.transform.scale(botonReset, [50, 30])

    almacen = creaAlmacen()
    game_over = False
    tablero = Tablero(FILS, COLS, RUTA_TABLERO)
    print(tablero)
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONUP:

                pos = pygame.mouse.get_pos()
                if pulsaBotonFC(pos, anchoVentana, altoVentana):
                    print("FC")
                    res = forward_checking(tablero, RUTA_DOMINIOS, debug_flag=True)
                    print(tablero)
                    if res == False:
                        # MessageBox.showwarning("Alerta", "No hay solución")
                        print("No hay solución")
                elif pulsaBotonAC3(pos, anchoVentana, altoVentana):
                    print("AC3")
                elif pulsaBotonReset(pos, anchoVentana, altoVentana):
                    tablero.reset()
                elif inTablero(pos):
                    colDestino = pos[0] // (TAM + MARGEN)
                    filDestino = pos[1] // (TAM + MARGEN)
                    if event.button == 1:  # botón izquierdo
                        if tablero.getCelda(filDestino, colDestino) == VACIA:
                            tablero.setCelda(filDestino, colDestino, LLENA)
                        else:
                            tablero.setCelda(filDestino, colDestino, VACIA)
                    elif event.button == 3:  # botón derecho
                        c = askstring('Entrada', 'Introduce carácter')
                        tablero.setCelda(filDestino, colDestino, c.upper())

        # código de dibujo
        # limpiar pantalla
        screen.fill(DARK_PURPLE)
        pygame.draw.rect(screen, MEDIUM_PURPLE, [0, 0, COLS * (TAM + MARGEN) + MARGEN, altoVentana], 0)
        for fil in range(tablero.getAlto()):
            for col in range(tablero.getAncho()):
                if tablero.getCelda(fil, col) == VACIA:
                    pygame.draw.rect(screen, WHITE, [(TAM + MARGEN) * col + MARGEN, (TAM + MARGEN) * fil + MARGEN, TAM, TAM], 0)
                elif tablero.getCelda(fil, col) == LLENA:
                    pygame.draw.rect(screen, DARK_PURPLE, [(TAM + MARGEN) * col + MARGEN, (TAM + MARGEN) * fil + MARGEN, TAM, TAM], 0)
                else:  # dibujar letra
                    pygame.draw.rect(screen, WHITE, [(TAM + MARGEN) * col + MARGEN, (TAM + MARGEN) * fil + MARGEN, TAM, TAM], 0)
                    fuente = pygame.font.Font(None, TAM)
                    texto = fuente.render(tablero.getCelda(fil, col), True, DARK_PURPLE)
                    text_rect = texto.get_rect(center=((TAM + MARGEN) * col + MARGEN + TAM // 2, (TAM + MARGEN) * fil + MARGEN + TAM // 2))
                    screen.blit(texto, text_rect)
        # pintar botones
        screen.blit(botonFC, [anchoVentana // 4 - 25, altoVentana - 45])
        screen.blit(botonAC3, [3 * (anchoVentana // 4) - 25, altoVentana - 45])
        screen.blit(botonReset, [anchoVentana // 2 - 25, altoVentana - 45])
        # actualizar pantalla
        pygame.display.flip()
        reloj.tick(40)
        if game_over == True:  # retardo cuando se cierra la ventana
            pygame.time.delay(500)

    pygame.quit()

if __name__ == "__main__":
    main()

