import math
class Polygon:
    def __init__(self, e, r):
        self._edge = e
        self._radius = r
        
    @property
    def edge(self): 
          return self._edge
        
    @property
    def radius(self): 
        return self._radius
    
    
    @edge.setter
    def edge(self, side):
            if(side < 2): 
                raise ValueError("Sorry you age is below eligibility criteria")
            self._edge = side
    @radius.setter
    def radius(self, rad):
            if(rad < 0): 
                raise ValueError("Sorry you age is below eligibility criteria")
            self._radius = rad
   
    
    
    def interiorangle(self):
        return int((self._edge-2)*180/self._edge)
    
    def edgelength(self):
        self.edgelen = 2*self._radius*math.sin(math.pi/self._edge)
        return self.edgelen
    
    def apothem (self):
        self.apo = self._radius*math.cos(math.pi/self._edge)
        return self.apo
    
   
    def area(self):
        return 0.5*self._edge*self.edgelength()*self.apothem()
    
   
    def perimeter(self):
        return self._edge*self.edgelength()
    
    def __repr__(self):
        return f'{self.edge} sided polygon created having circumradius:{self.radius}'

    def __eq__(self, other):
        if self._edge == other._edge and self._radius == other._radius:
            return True
        else:
            return False
    
    def __gt__(self, other):
        if self._edge > other._edge:
            return True
        else:
            return  False
pol1 = Polygon(4,2) 
  
pol1.edge = 4
pol1.radius = 2

pol2 = Polygon(4,2) 
  
pol2.edge = 6
pol2.radius = 3
  
print(pol1>pol2)