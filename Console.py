

import json, time
from datetime import datetime, timedelta


class Console():
    def __init__( self , res , now , way ):
        
        self.res = res
        
        self.now = now
        
        
        self.z  = ""
        self.z2 = ""
        
        if way == "fa" : 
            self.z  = "От КПП1 до Железногорска"
            self.z2 = "в город"
        
        if way == "fg" : 
            self.z = "Из Железногорска до КПП1"
            self.z2 = "на КПП1"
        
    def display(self, n = 99):
        
        print(self.z)
        print(self.now)
        print()
        
        ddl = {}
        
        
        
        for c,i in enumerate( self.res ):
            
            base = i['base'].strftime("%H:%M")
            
            sbor = i['sbor'].strftime("%H:%M")
            go   = i['go'  ].strftime("%H:%M")
            go2  = i['go2' ].strftime("%H:%M")
            goal = i['goal'].strftime("%H:%M")
            
            sbor_dl = round(( i['sbor'] - self.now ).total_seconds() // 60 )
            go_dl   = round(( i['go'  ] - self.now ).total_seconds() // 60 )
            go2_dl  = round(( i['go2' ] - self.now ).total_seconds() // 60 )
            goal_dl = round(( i['goal'] - self.now ).total_seconds() // 60 )
            
            cm = f" ({ i['cm'] })." if len(i["cm"])>0 else "."
            
            if c == 0:
                
                #print( f"{c:<2} {base} { i['bus'] } Сбор c {sbor}. Выход до {go}. Отправка в {go2}. Приезд в {goal} {cm} ")
                print( f"{c:<2} {base} { i['bus'] } Старт сбор через {sbor_dl}. Выход через {go_dl}. Aвтобуса отходит через {go2_dl}. Приезд {self.z2} через {goal_dl}. ")
                print()
                print( f"{c:<2} {base} { i['bus'] } Старт сбор с {sbor}. Выход до {go}. Aвтобуса отходит в {go2}. Приезд {self.z2} в {goal}{cm} ")
            
                ddl = {
                        "bus"     : i['bus'],
                        "base" : base,
                        "sbor_dl" : sbor_dl,
                        "go_dl"   : go_dl,
                        "go2_dl"  : go2_dl,
                        "goal_dl" : goal_dl,
                        "cm"      : i['cm']
                    }
            else:
                
                print( f"{c:<2} {base} {i['bus']} Старт сбор c {sbor}. Выход до {go}. Aвтобуса отходит в {go2}. Приезд {self.z2} в {goal}{cm} " )
                
            if c+2 > n:
                break
         
        return ddl