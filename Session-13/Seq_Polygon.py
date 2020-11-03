from Polygon import Polygon
class Seq_Polygon:
    def __init__(self, num):
        self.vertices = num
        
    
    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 3 or s >=self.vertices:
                raise IndexError
            else:
                return Seq_Polygon._maxeffpolygon(s)
    
    def __len__(self):
        return self.vertices
    
    @staticmethod
    def _maxeffpolygon(c):
        max_ratio = 0
        radius = 5
        for i in range(3,c+1):
            pol = Polygon(i, radius)
            #print(pol.area())
            r = pol.area()/pol.perimeter()
            #print(r)
            if r > max_ratio:
                max_ratio = r
                side_len = i
        return f'Polygon having max efficiency is having side:{side_len} and the ratio is:{max_ratio:0.3f}\n'
            
    def __repr__(self):
        return f'This polygon sequence is called with number of vertices for largest polygon:{self.vertices}'
    

p = Seq_Polygon(11)
print(p[5], p[7], p[9])