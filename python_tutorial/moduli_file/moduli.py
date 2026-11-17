#un modulo è un file .py che contiene def e dichiarazioni

import circle

pi=3
print(pi) #questo è il pi nostro
print(circle.pi) #questo invece quello del modulo
print(circle.area(4))
print(circle.circumference(6))

# In[]

from circle import * #importa tutto quanto e uso per esempio solo area()

#oppure usa
from circle import area

# In[]

import calendar as cal #per scrivere solo cal.lefunzioni di calendar
#invece di scrivere calendar.qualcosa