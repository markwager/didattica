#metodo usato per trovare radice reali di molte funzioni
#in questo caso si fa riferimento alla ricerca di radici reali di una funzione polinomiale in una variabile
#Newton-Raphson per la radice quadrata
#trova un x tale che la differenza fra x**2 - k e 0
#sia minore di epsilon
k=int(input("Inserisci intero: "))
epsilon = 0.01
guess = k/2
num_guess=0
while abs(guess**2 - k) >= epsilon:
    guess = guess - (guess**2 - k)/(2*guess)
    num_guess+=1 
print("Il numero di tentativi è: ", num_guess)
print('La radice quadrata di ', k, 'è circa', guess)