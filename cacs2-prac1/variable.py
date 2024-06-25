from dominio import *
from restriccion import *
from copy import deepcopy

class Word:

    def __init__(self, value = "-", name = 0, 
                 initial_pos = (0, 0), final_pos = (0, 0), 
                 length = 0, orientation = "horizontal", 
                 feasibles = None, pounds = None, restrictions = None):
        self.value = value
        self.name = name
        self.initial_pos = initial_pos
        self.final_pos = final_pos
        self.length = length
        self.orientation = orientation
        
        if feasibles is None:
            feasibles = []
        self.feasibles = feasibles
        
        if pounds is None:
            pounds = {}
        self.pounds = pounds # Hash Table
        
        if restrictions is None:
            restrictions = {}
        self.restrictions = restrictions # Hash Table