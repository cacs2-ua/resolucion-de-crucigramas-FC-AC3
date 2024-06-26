from dominio import *
from restriction import *
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

    
    
    def set_value(self, value):
        self.value = value
    
    def get_value(self):
        return self.value
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_initial_pos(self, initial_pos):
        self.initial_pos = initial_pos
    
    def get_initial_pos(self):
        return self.initial_pos
    
    def set_final_pos(self, final_pos):
        self.final_pos = final_pos
    
    def get_final_pos(self):
        return self.final_pos
    
    def set_length(self, length):
        self.length = length
    
    def get_length(self):
        return self.length
    
    def set_orientation(self, orientation):
        self.orientation = orientation
    
    def get_orientation(self):
        return self.orientation
    
    def set_feasibles(self, feasibles):
        self.feasibles = feasibles
    
    def get_feasibles(self):
        return self.feasibles
    
    def set_pounds(self, pounds):
        self.pounds = pounds
        
    def get_pounds(self):
        return self.pounds

    def set_restrictions(self, restrictions):
        self.restrictions = restrictions
    
    def get_restrictions(self):
        return self.restrictions
    
    def add_restriction(self, restriction):
        restrainer_name = restriction.get_word_restrainer().get_name()
        if restrainer_name not in self.restrictions:
            self.restrictions[restrainer_name] = []
        self.restrictions[restrainer_name].append(restriction)
