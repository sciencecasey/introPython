'''
Created on Mar 23, 2021

@author: CaseyJayne
'''
from conda.common._logic import FALSE

class Cart:
    def __init__(self, customer: str):
        self.customer = customer
        items = []
        
    def __len__(self):
        return len(self.items)
        
    def __iadd__(self, item):
        self.items.append(item)
        return self.items
        
        
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
        return self.items
    

class Vector: 
    def __init__(self, x_comp, y_comp):
        self.x_comp = x_comp
        self.y_comp = y_comp

    def __abs__(self):
        # returns vector length
        return (self.x_comp ** 2 + self.y_comp ** 2) ** 0.5
    
    def __str__(self):
        return f'{self.x_comp}i+{self.y_comp:}j'
    
    def __print__(self):
        print(self.__str__())
        
    def __repr__(self):
        return f'Vector({self.x_comp}, {self.y_comp})'
        
    def __bool__(self):
        if self.x_comp == 0 or self.x_comp == None:
            return False
        elif self.y_comp == 0 or self.y_comp == None:
            return False 
        return True
    
    def __add__(self, vector):
        if isinstance(vector, Vector):
            x = self.x_comp + vector.x_comp
            y = self.y_comp + vector.y_comp
            return Vector(x, y)
        
        