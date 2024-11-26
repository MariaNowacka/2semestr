import numpy as np
class Vector:
    def __init__(self,arg=3):
        self.v=list(np.zeros(arg))
    
    def __str__(self):
        '''funkcja print
           output : wektor '''
        return str(self.v)

v1=Vector(2)
print(v1)

