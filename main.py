# типа поставить на авто ослеживание 
# след автобус через ...  типа все в стопку .. сортировки 
# время на сборы .. выход .. отправление 



import json ,time
from datetime import datetime


from C190 import C190
from C119 import C119
#from C189 import C189

from Stack import Stack
from Console import Console

from Alarm import Alarm

from Loca import Loca

import os
#os.chdir("./scripts3/AVTOBUS")
os.chdir("./projects3/AVTOBUS")

import androidhelper 

droid = androidhelper.Android()



now = datetime.now()
#now = datetime.strptime("2025-01-12 4:00","%Y-%m-%d %H:%M" ) 
#now = datetime.strptime("2025-01-13 09:30","%Y-%m-%d %H:%M" ) 


loc = Loca()
l   = loc.get_area()
print("Locale",l[0],l[1]*1000)
droid.ttsSpeak(l[0])
droid.ttsSpeak( str(round(l[1]*1000)))

l = l[0]

if l == "dacha":
    way = "fa"
    #way = "fg"
    
if l == "dom" or l == "gorod":
    way = "fg"
    #way = "fg"
    
if l == "dacha" or l == "dom" or l == "gorod":

    b190   = C190(  now )
    b119   = C119(  now )
    #b189  = C189(  now )
    stack  = Stack( now )

    stack.add( b190.all( way ) ) # b190.next("FG") типа вывод всех след  from far away 
    stack.add( b119.all( way ) )  

res = stack.res()
#res  = stack.all()

console = Console( res , now , way )
console.display(3)
#console.display()


print()


if len(res)==0: 
    print("Нет следования")
    droid.ttsSpeak("Нет следования")

if len(res)>0:
    
    alarm = Alarm(   res[0] , way )
    
    while True:
        
        now = datetime.now()
        print( alarm.hint( ) )
        t = alarm.chek( now )
        #print(t)
        if t["go_dl"]<-10:
            break
        
        if t["sbor_dl"] <= 25 and t["sbor_dl"] > 0 :
            droid.ttsSpeak(f"Сбор через {t['sbor_dl']}" )
           
        if t["go_dl"] <= 15 and t["go_dl"] > 0 :
            droid.ttsSpeak(f"Выход через {t['go_dl']}" )   
        
        time.sleep(60)
        
    
    
    #print( alarm.hint( ) )
    
    #alarm.chek( now )
    
    #now = datetime.strptime("2025-01-13 09:31","%Y-%m-%d %H:%M" ) 
    #alarm.chek( now )
    #print()
    #print(res[0])
        


# на ютуб - боевые проекты на питоне 
# далле отдых и битва на расписание  -- расписание и подготовленность это клево 
# но самое клевое что будут результатв 

# Типа идея - сервера таймеров 
# В который задачи на таймеры послыть - и окружение по уведомлениям - там - тг - музыка ... звуки голос.. и тд 

