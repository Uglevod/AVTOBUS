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

#import os
#os.chdir("./scripts3/AVTOBUS")

now = datetime.now()
#now = datetime.strptime("2025-01-12 4:00","%Y-%m-%d %H:%M" ) 
#now = datetime.strptime("2025-01-13 09:30","%Y-%m-%d %H:%M" ) 

b190   = C190(  now )
b119   = C119(  now )
#b189  = C189(  now )
stack  = Stack( now )

way = "fa"
#way = "fg"
#way = "fk"
#stack.add( b190.next( way ) ) # b190.next("FG") типа вывод всех след  from far away 
#stack.add( b119.next( way ) )  

stack.add( b190.all( way ) ) # b190.next("FG") типа вывод всех след  from far away 
stack.add( b119.all( way ) )  

res = stack.res()
#res  = stack.all()

console = Console( res , now , way )
console.display(3)
#console.display()


print()


if len(res)==0: print("Нет следования")

if len(res)>0:
    
    alarm = Alarm(   res[0] , way )
    
    while True:
        
        now = datetime.now()
        print( alarm.hint( ) )
        t = alarm.chek( now )
        #print(t)
        
        if t["go_dl"]<-10:
            break
        
         
        time.sleep(60)
        
    
  

