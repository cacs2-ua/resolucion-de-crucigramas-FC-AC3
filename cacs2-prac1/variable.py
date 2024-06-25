from dominio import *
from restriccion import *
from copy import deepcopy

class Word:
    def __init__(self, value="-", name=0, 
                 initial_pos=(0, 0), final_pos=(0, 0), 
                 length=0, orientation="horizontal", 
                 feasibles=None, pounds=None, restrictions=None):
        self.value = value
        self.name = name
        self.initial_pos = initial_pos
        self.final_pos = final_pos
        self.length = length
        self.orientation = orientation
        
        self.feasibles = feasibles if feasibles is not None else []
        self.pounds = pounds if pounds is not None else {}
        self.restrictions = restrictions if restrictions is not None else {}
        
    def __eq__(self, other):
        if isinstance(other, Word):
            return (self.value == other.value and
                    self.name == other.name and
                    self.initial_pos == other.initial_pos and
                    self.final_pos == other.final_pos and
                    self.length == other.length and
                    self.orientation == other.orientation and
                    self.feasibles == other.feasibles and
                    self.pounds == other.pounds and
                    self.restrictions == other.restrictions)
        return False
    
    def __repr__(self):
        return (f"Word(value={self.value}, name={self.name}, initial_pos={self.initial_pos}, "
                f"final_pos={self.final_pos}, length={self.length}, orientation={self.orientation}, "
                f"feasibles={self.feasibles}, pounds={self.pounds}, restrictions={self.restrictions})")
