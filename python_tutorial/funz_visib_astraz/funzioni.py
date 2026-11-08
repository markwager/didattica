def is_in(s1,s2):
    if s1 in s2:
        return True
    elif s2 in s1:
        return True
    else:
        return False

s1="ciao"
s2="ciaoccione"

print(is_in(s1,s2))

# In[]

def print_name(first_name, last_name, reverse = False):
    if reverse:
        print(last_name + ', ' + first_name)
    else:
        print(first_name, last_name)

print_name('Olga', 'Puchmajerova')
print_name('Olga', 'Puchmajerova', True)
print_name('Olga', 'Puchmajerova', reverse=True) #i nomi delle variabili se li scrivi qui dentro devono
#essere uguali ai nomi dei parametri formali
x=True
print_name('Olga', 'Puchmajerova', x)

# In[]

def mult(*arg):
    #assume che ci sia almeno un argomento
    tot=1
    for a in arg:
        tot*=a
    return tot

print(mult(5,2))
print(mult(5))

# In[]

#esempio di uso di funzione anonima lambda

x=lambda a, b: None if b==0 else a/b
print(x(4,0))
print(x(4,2)) 


# In[]

def find_last(s, sub):
    if len(sub) > len(s):
        return None
    
    i = 0
    pos_trovata = None

    # Continuiamo finché c'è abbastanza spazio per farci stare 'sub'
    while i <= len(s) - len(sub):
        
        # Estraiamo un blocco di 's' lungo quanto 'sub' e vediamo se sono uguali
        if s[i : i + len(sub)] == sub:
            pos_trovata = i
            
        i += 1  # Passiamo al carattere successivo
        
    return pos_trovata

print(find_last("ciao", "o"))       # Stampa 3
print(find_last("ciaccciao", "ci")) # Stampa 6
print(find_last("ciao", "x"))       # Stampa None

# In[]

def find_last(s, sub):
    if len(sub) > len(s):
        return None
    
    i = 0
    pos_trovata = None

    # Continuiamo finché c'è abbastanza spazio per farci stare 'sub'
    while i <= len(s) - len(sub):
        
        # Estraiamo un blocco di 's' lungo quanto 'sub' e vediamo se sono uguali
        if s[i : i + len(sub)] == sub:
            pos_trovata = i
            return pos_trovata
            
        i += 1  # Passiamo al carattere successivo
        
    return pos_trovata

print(find_last("ciao", "o"))       # Stampa 3
print(find_last("ciaccciao", "ci")) # Stampa 6
print(find_last("ciao", "x"))       # Stampa None
# %%
