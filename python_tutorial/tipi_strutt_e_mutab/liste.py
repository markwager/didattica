#le liste sono mutabili
l=["ciao fra", 6, "pazzo"]
for i in l:
    print(i)

#operazioni:

#concatenazione
l1=["ciaoo"]
print(l+l1)

#ripetizione
print(3*l)

#indicizzazione
print(l1[0])

#slicing
print(l[:1])

# In[]
Techs = ['MIT', 'Caltech']
Ivys = ['Harvard', 'Yale', 'Brown']
Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]
print(Univs)
print(Univs1)

#Univs e Univs1 non sono legate agli stessi valori!!!
print(Univs==Univs1)
print(Univs is Univs1)

#guarda che succ se faccio
Techs.append("franco")
print(Univs)
print(Univs1)
#questo concetto si chiama aliasing

# In[]

l1=[[]]*2
l2=[[],[]]
print(len(l1))
print(len(l2))

for i in range(len(l1)):
    l1[i].append(i)
    l2[i].append(i)

print(l1)
print(l2)
#questo succede perchè nella prima dichiarazione si crea una lista con due elementi dello stesso oggetto
#nel secondo si hanno invece due oggetti diversi

# In[]

def append_val(val, list_1 = []):
    list_1.append(val)
    print(list_1)

append_val(3)
append_val(4,[12])
append_val(9)

def appendi(v, l):
    l.append(v)
    print(l)

appendi(2,[])
appendi(6,[])

# In[]

#alcuni metodi usati per le liste

L=[12,3,4,3,7,8,9,12,9,1]
L.append("chipchip")
print(L.count(3))
print(L.remove(12)) #rimuove prima occorrenza di 12
print(L.index(9)) #restiuisce indice della prima occorrenza di 9
L.pop() #elimina ultimo elemento in L
L.pop(0) #elimina e restituisce elem in pos 0
L.sort()
L.reverse() 
print(L)

# In[]

def remove_dups(L1, L2):
    """Assume che L1 e L2 sono liste.
       Elimina da L1 qualsiasi elemento
           che sia presente anche in L2"""
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)
L1 = [1,2,3,4]
L2 = [1,2,5,6]
remove_dups(L1, L2)
print('L1 =', L1)

#non è una buiona idea mutare una lista su cui si itera: la rimozione/aggiunta di elementi
#inficia sulle operazioni che si fanno

#ma si può risolvere con clonazione

def remove_dups(L1, L2):
    """Assume che L1 e L2 sono liste.
       Elimina da L1 qualsiasi elemento
           che sia presente anche in L2"""
    for e1 in L1[:]:
        if e1 in L2:
            L1.remove(e1)
L1 = [1,2,3,4]
L2 = [1,2,5,6]
remove_dups(L1, L2)
print('L1 =', L1)

# In[]

#se faccio
L = [2,3,4]
L1 = [L]
L2 = L1[:]
L.append(9)
print('L1 =', L1, 'L2 =', L2)
#si modificano entrambe

# In[]

import copy
#invece con deepcopy no
L1 = [2]
L2 = [[L1]]
L3 = copy.deepcopy(L2)
L1.append(3)
print('L2 =', L2, 'L3 =', L3)
L3.append("fra")
print('L2 =', L2, 'L3 =', L3)



# %%
