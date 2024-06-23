from dominio import *
from restriccion import *
from copy import deepcopy

class Word:

    def __init__(self, name, initial_pos, final_pos, length, orientation, feasibles):
        self.value = "-"
        self.name = name
        self.initial_pos = initial_pos
        self.final_pos = final_pos
        self.length = length
        self.orientation = orientation
        self.feasibles = feasibles
        self.pounds = []
        self.restrictions = []