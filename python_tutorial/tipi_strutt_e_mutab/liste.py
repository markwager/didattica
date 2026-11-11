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