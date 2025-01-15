
import json, time
from datetime import datetime, timedelta


class C119():
    def __init__( self , now ):
        
        self.now = now
         
        self.dt  = self.now.strftime("%Y-%m-%d")
        
        file      = "119.json"
        
        f         = open( file )
        self.j119 = json.loads(f.read() )
        f.close()
        
        #print(self.now.isoweekday())
        
        self.wh = False  # выходные 
        self.wk = True 
        if self.now.isoweekday()==7 or self.now.isoweekday()==6:
            self.wh = True
            self.wk = False
            
        file = "taiming.json"
        f    = open( file )
        tj   = json.loads(f.read() )
        f.close()
            
        self.fa = { "sbor":-20 , "go":5   , "go2":15 , "goal":45 }
        self.fg = { "sbor":-50 , "go":-30 , "go2":0  , "goal":25 }
        
        
        for t in tj:
            
            if t["bus"] == "119" and t["way"]=="fa":
                self.fa = t
            
            if t["bus"] == "119" and t["way"]=="fg":
                self.fg = t
                
                
        
        
        self.ff  = {   }
        
        self.way = [   ]
         
        
        
                
    def next( self , dest ):
        # список следующих//  с разницей для направления .. в зависимости от направ - фарм строки 
        # { bus:119 sbor go go2 goal } # от кпп отход по факту типа +15 выход +5
        # есть еще рабочие не рабочие  
        res = [] 
        
         
        if dest == "fa": 
            self.way = self.j119['fa']
            self.ff  = self.fa

        if dest == "fg": 
            self.way = self.j119['fg']
            self.ff  = self.fg
        
        for i in self.way:
            
            base = datetime.strptime( self.dt+" "+i["bs"] ,f"%Y-%m-%d %H:%M" )
                
            sbor = base + timedelta( minutes = self.ff["sbor"] )
                
            go   = base + timedelta( minutes = self.ff["go"]   )
                
            go2  = base + timedelta( minutes = self.ff["go2"]  )
                
            goal = base + timedelta( minutes = self.ff["goal"] )
            
            
            sres = {    
                                        "bus"  : "119",
                                        "base" : base,
                                        "sbor" : sbor,
                                        "go"   : go,
                                        "go2"  : go2,
                                        "goal" : goal,
                                        "cm"   : "work" if not i["wh"] else ""
                                } 
            
            
            if True:#self.now < go2:
                
                #if i["wh"] == True and  self.wh == True  and i["wk"]== self.wk ==  : 
                
                if  self.wh == True and i["wh"] == True   : 
                    
                    res.append( sres )  
                    
                if  self.wk == True and i["wk"] == True   : 
                    
                    res.append( sres )  
                    
                    
                    
                    #print( self.wh ,i["wh"] , self.wk , i["wk"] )
                
            #print( str(base) ,self.wh ,i["wh"] , self.wk , i["wk"] )
                
                
                
            
            
            
            
            
             
        
        return res
    
    def all(self, dest = "fa"):
        return self.next(dest)
 
        