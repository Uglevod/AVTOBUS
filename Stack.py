# тут первая заливка и потом сортировка при второй заливке 


import json, time
from datetime import datetime, timedelta


class Stack():
    
    def __init__( self, now = datetime.strptime("3333-01-01 00:00","%Y-%m-%d %H:%M" )  ):
        
        self.mass = []
        self.now  = now
        
    def first(self,m1 ):
        
        self.mass.extend( m1 )
        
    def add(self, m2  ):
        
        self.mass.extend( m2 )
        
    def res(self):
        
        self.mass.sort( key=lambda x: x["go2"] )
        
        def ch(line):
            
            #if self.now > line["go2"]:
            if self.now > ( line["go"] + timedelta(minutes=5)) :
                return False  
            return True
        
        return list( filter(ch, self.mass))
    
    def all(self):
        
        self.mass.sort( key=lambda x: x["go2"] )

        
        return self.mass