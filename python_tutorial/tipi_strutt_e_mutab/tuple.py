#le stringhe sono immutabili come le stringhe
t1=()
t2=("cya", 12, 2.8)
t3=(10,)
t4=(t2,20)
t5=(12,34)
print(t1)
print(t2)
print(t4)

#come le stringhe, supportano:

#concatenazione
print(t5+t3)

#ripetizione
print(3*t2)

#indicizzazione
print(t2[1])

#slicing
print(t2[:2])

# In[]

def inters(t1,t2):
    ris=()
    for i in t1:
        if i in t2:
            ris+=(i,)

    return ris

t1=(1,2,3,4,5)
t2=(22,2,8,9,3,1)

print(inters(t1,t2))

