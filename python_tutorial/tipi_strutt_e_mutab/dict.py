#un dizionario è una coppia chiave-valore
#sono come le liste, ma si indicizzano tramite chiavi

month_numbers = {'Gen':1, 'Feb':2, 'Mar':3, 'Apr':4, 'Mag':5, 1:'Gen', 2:'Feb', 3:'Mar', 4:'Apr', 5:'Mag'}
#come chiave posso mettere numeri, stringhe e tuple e booleani
#come elemento qualsiasi cosa

for k in month_numbers:
    print("Il mese", k, "con il numero", month_numbers[k])

# In[]

capitals = {'Francia': 'Parigi', 'Spagna': 'Madrid', 'Grecia': 'Atene'}
citta=[]

for val in capitals.values(): #itera sui valori del dizionario
    citta.append(val)
print(citta, "è la lista delle capitali")

# In[]

capitals = {'Francia': 'Parigi', 'Spagna': 'Madrid', 'Grecia': 'Atene'}
paesi=[]
citta=[]

for k, v in capitals.items():
    print("La capitale della", k, "è", v)
    paesi.append(k)
    citta.append(v)
print(paesi)
print(citta)

# In[]

#comprensione di dizionario
# {chiave: valore for id1, id2 in iterabile if test}

number_to_word = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 10: 'ten'}
word_to_number={w: d for d, w in number_to_word.items()} #crea un diz che inverte la mappatura del diz di prima
print(word_to_number)