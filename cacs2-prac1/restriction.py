from dominio import *
from variable import *
from copy import deepcopy

class Restriction:
    def __init__ (self, word_restricted = None, word_restrainer = None,
                  x_coordinate = 0, y_coordinate = 0,
                  letter_of_restriction = "-"):
        if word_restricted is None:
            word_restricted = Word()
        self.word_restricted = word_restricted
        
        if word_restrainer is None:
            word_restrainer = Word()
        self.word_restrainer = word_restrainer
        
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.letter_of_restriction = letter_of_restriction
    
    def set_word_restricted(self, word_restricted):
        self.word_restricted = word_restricted
    
    def get_word_restricted(self):
        return self.word_restricted
    
    def set_word_restrainer(self, word_restrainer):
        self.word_restrainer = word_restrainer
    
    def get_word_restrainer(self):
        return self.word_restrainer
    
    def set_x_coordinate(self, x_coordinate):
        self.x_coordinate = x_coordinate
    
    def get_x_coordinate(self):
        return self.x_coordinate
    
    def set_y_coordinate(self, y_coordinate):
        self.y_coordinate = y_coordinate
    
    def get_y_coordinate(self):
        return self.y_coordinate

    def set_letter_of_restriction(self, letter_of_restriction):
        self.letter_of_restriction = letter_of_restriction
    
    def get_letter_of_restriction(self):
        return self.letter_of_restriction
    
    def __eq__(self, other):
        if isinstance(other, Restriction):
            return (self.word_restricted == other.word_restricted and
                    self.word_restrainer == other.word_restrainer and
                    self.x_coordinate == other.x_coordinate and
                    self.y_coordinate == other.y_coordinate and
                    self.letter_of_restriction == other.letter_of_restriction)
        return False

    def __repr__(self):
        return (f"Restriction(word_restricted={self.word_restricted}, "
                f"word_restrainer={self.word_restrainer}, "
                f"x_coordinate={self.x_coordinate}, "
                f"y_coordinate={self.y_coordinate}, "
                f"letter_of_restriction='{self.letter_of_restriction}')")