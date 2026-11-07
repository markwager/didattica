#trova un'approssimazione alla radice quadrata

x=int(input("Inserisci numero intero: "))
epsilon = 0.01 #valore di tolleranza
step = epsilon**2
num_guesses = 0
ans = 0.0 #guess iniziale
while abs(ans**2 - x) >= epsilon and ans <= x: #la guess è compresa tra la distanza da x rispetto al margine ed x 
    ans += step
    num_guesses += 1
print('numero di congetture =', num_guesses)
if abs(ans**2 - x) >= epsilon:
    print('Non ho trovato la radice quadrata di', x)
else:
    print(ans, 'è vicino alla radice quadrata di', x)

# In[]

#trova un'approssimazione alla radice quadrata

x=float(input("Inserisci numero intero: "))
epsilon = 0.01 #valore di tolleranza
step = epsilon**2
num_guesses = 0
ans = 0.0 #guess iniziale
while abs(ans**2 - x) >= epsilon and ans*ans <= x: #ora funzione anche con x float 
    ans += step
    num_guesses += 1
print('numero di congetture =', num_guesses)
if abs(ans**2 - x) >= epsilon:
    print('Non ho trovato la radice quadrata di', x)
else:
    print(ans, 'è vicino alla radice quadrata di', x)
# %%
