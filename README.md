# AVTOBUS
Микс расписания маршрутов на ближайший ( + версия под Qpython 3L для запуска на андройде с гео)

## Данные и базовые классы
119 json и py - Данные расписания и класс который фармит расписание. 190 .. и 189 соответвенно.

Разнесение по разным классам обусловлено в разнице формирования расписания каждого маршрута.
У одно есть рейс который добавляется только в рабочий день.
У другогго маршрута с пн - сб одно расписание, а в вс полностью другое.

* Версия с 189 вынесена в отдельную ветку, т.к. при отправке из города должна быть только один пункт назначения.

## Работа

Есть время отправлений ,а так же расчитываются время на сборы и путь до остановки, на основании данных направления и маршрута.

Данные добаляются в колоду ( stack )
на выходе имеем сортированный список 

taiming.json - особый список правил, описывающий вычесления трех точек во времени относительно времени в рсписании.
Было бы все прощще - если бы не один момент.
Время обратного отправления автобуса это на 20 минут раньше чем появления его на моей остановке, а в прямом направленн нет,
по этому был применет этот универсальный подход с нужными смещениями в зависимости от направления. 

## Вывод 
Клас Console, используется для вывода списка 
+ можем задать условие по длинне списка возвращаемого колличесва вариантов

## Запускные

### PC
tdy_toD.py  - прямое направление из города на дачу.
tdy_toG.py  - обратное направление, из дачи в город.

### Android
tdy_toG_AU.py
tdy_toG_AU tts.py

Для запуска на андройде с авто определением направления на основе геолокации. С tts и без.

## Процесс
Пример вывода 
 
От КПП1 до Железногорска
2025-01-15 15:59:02.314643

0  16:00 119 Старт сбор через -20. Выход через 5. Aвтобуса отходит через 15. Приезд в город через 45. 

0  16:00 119 Старт сбор с 15:40. Выход до 16:05. Aвтобуса отходит в 16:15. Приезд в город в 16:45. 
1  17:00 119 Старт сбор c 16:40. Выход до 17:05. Aвтобуса отходит в 17:15. Приезд в город в 17:45. 
2  17:30 190 Старт сбор c 17:10. Выход до 17:35. Aвтобуса отходит в 17:45. Приезд в город в 18:15 (pnsb). 

['Взять документы', 'Взять ключи', 'Взять Карты и наличные', 'Взять часы , телефоны и повер банк', 'Взять воду', 'Взять вещи на стирку']
На сборы 25, Сборы через -20, Осталось на сборы 5 (80.0%)
Выход через 5 минут.   
Затем на путь до остановки: 10 минут.   
 
['Взять документы', 'Взять ключи', 'Взять Карты и наличные', 'Взять часы , телефоны и повер банк', 'Взять воду', 'Взять вещи на стирку']
На сборы 25, Сборы через -21, Осталось на сборы 4 (84.0%)
Выход через 4 минут.   
Затем на путь до остановки: 10 минут.   


