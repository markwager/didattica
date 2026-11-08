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

x=float(input("Inserisci un float: "))
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
# In[]
x=int(input("Inserisci un intero: "))
if x<0:
    x=abs(x)
epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, x)
ans = (high + low)/2 #guess la metto a metà
while abs(ans**2 - x) >= epsilon:
    print('basso =', low, 'alto =', high, 'ans =', ans)
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('numero di congetture =', num_guesses)
print(ans, 'è vicino alla radice quadrata di', x)

# In[]

x=int(input("Inserisci un intero: "))
epsilon = 0.01
num_guesses = 0
low = 0
if x<0:
    low=x
high = max(1, x)
ans = (high + low)/2 #guess la metto a metà
while abs(ans**3 - x) >= epsilon:
    print('basso =', low, 'alto =', high, 'ans =', ans)
    num_guesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('numero di congetture =', num_guesses)
print(ans, 'è vicino alla radice cubica di', x)

# %%
