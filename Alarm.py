# ставим сюда будильник 
# До начала сборов [######_____] 
# До выхода [######_____] 
# До отход автобуса [######_____] 
# До выхода [######_____] 
# до начала сбора 5 минут - отдохни . 
# tts - Начало сбора ..музонч - ТТс до выхода 10 - 5 минут - проверье комплект 
# Выход - буззер 


import json, time
from datetime import datetime, timedelta


class Alarm():
    def __init__( self , res , way ):
        
        self.way = way # для подсказок - что собрать особенно важно 
        self.res = res 
        
        f         = open( "taiming.json" )
        tj  = json.loads(f.read() )
        f.close()
        
        self.ff = { "sbor":-50 , "go":-30 , "go2":0  , "goal":25 }
        
        for t in tj:
            
            if way == "fa":
                if t["bus"] == res["bus"] and t["way"] == "fa":
                    self.ff = t
                    
            if way == "fg":
                if t["bus"] == res["bus"] and t["way"] == "fg":
                    self.ff = t
        
        
    
    def hint ( self ):
        
        hint_fa=[
            "Взять документы",
            "Взять ключи",
            "Взять Карты и наличные",
            "Взять часы , телефоны и повер банк",
            "Взять воду",
            "Взять вещи на стирку"
        ]
         
        hint_fg=[
            "Взять документы",
            "Взять ключи",
            "Взять карты и наличные",
            "Взять часы , nелефоны и повер банк",
            "Взять воду",
            "Взять стираные вещи",
            "Поход в магазин"
        ]
        
        hint_def= [
            "Взять документы",
            "Взять ключи",
            "Взять Карты и наличные",
            "Взять часы , телефоны и повер банк",
            "Взять воду"
        ]
        
        if self.way == "fa" : return hint_fa
        if self.way == "fg" : return hint_fg
        
        return hint_def
    
    def  chek( self, now   ):
        
        #print(self.ff)
        
        sbor_dl  = round((self.res["sbor"]-now).total_seconds()//60)
        sbor_dlf = self.ff["go"] - self.ff["sbor"]
        
        go_dl  = round(( self.res["go"] - now).total_seconds()//60)
        go_dlf = self.ff["go2"] - self.ff["go"] 
        
        
        pro_sbor =  ( 100/sbor_dlf ) * ( abs(sbor_dlf) - abs(sbor_dl) )
        
        print( f"На сборы {sbor_dlf}, Сборы через {sbor_dl}, Осталось на сборы { abs(sbor_dlf) - abs(sbor_dl) } ({ 100 - pro_sbor}%)"  )
        
        print( f"Выход через {go_dl} минут.   "  ) #Осталось на путь до автобуса {go_dlf}.
        print( f"Затем на путь до остановки: {go_dlf} минут.   "  ) #Осталось на путь до автобуса {go_dlf}.
        print( f"-----------------------------------------"  )
        
        return { "sbor_dl":sbor_dl , "go_dl":go_dl } 
        
        
    def run(self,now):
        pass
        