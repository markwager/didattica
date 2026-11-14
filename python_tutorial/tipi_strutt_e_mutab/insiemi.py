#gli insiemi sono oggetti mutabili

baseball_teams = {'Dodgers', 'Giants', 'Padres', 'Rockies'}
football_teams = {'Giants', 'Eagles', 'Cardinals', 'Cowboys'}

#print(baseball_teams[0]) genera un errore

baseball_teams.add('Yankees') #per l'aggiunta di un unico elemento
football_teams.update(['Patriots', 'Jets']) #per varie aggiunte
print(baseball_teams)
print(football_teams)
#con i print si possono osservare elementi in insiemi che possono essere stampati in modo diverso
#questo perchè l'ordine non è definito dal linguaggio
baseball_teams.remove('Giants') #per l'eliminazione di un elemento

print(baseball_teams.union({1, 2})) #
print(baseball_teams.intersection(football_teams))
print(baseball_teams.difference(football_teams))
print({'Padres', 'Yankees'}.issubset(baseball_teams))

#questi sono equivalenti
print(baseball_teams | {1, 2})
print(baseball_teams & football_teams)
print(baseball_teams - football_teams)
print({'Padres', 'Yankees'} <= baseball_teams)

