# Representa el crucigrama: medidas y matriz correspondiente a las celdas
class Tablero:    
    def __init__(self, FILS=None, COLS=None, file_path=None):
        if file_path:
            self.load_from_file(file_path)
        else:
            self.ancho = COLS
            self.alto = FILS    
            self.tablero = [['-' for _ in range(self.ancho)] for _ in range(self.alto)]
                 
    def load_from_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        self.alto = len(lines)
        self.ancho = len(lines[0].strip())
        self.tablero = []
        
        for line in lines:
            self.tablero.append(list(line.strip()))
            
    def set_from_file(self, file_path):
        self.load_from_file(file_path)
        
    def __str__(self):
        salida=""
        for f in range(self.alto):            
            for c in range(self.ancho):
                salida += self.tablero[f][c]                
            salida += "\n"
        return salida
       
    def reset(self):
        for f in range(self.alto):
            for c in range(self.ancho):
                self.tablero[f][c]='-'        
       
    def getAncho(self):
        return self.ancho
    
    def getAlto(self):
        return self.alto
    
    def getCelda(self, fila, col):
        return self.tablero[fila][col]
    
    def setCelda(self, fila, col, val):
        self.tablero[fila][col]=val    
    