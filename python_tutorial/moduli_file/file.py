name_handle=open("kids", "w") #crea un file di nome kids e ci si può scrivere sopra
for i in range(2):
    name=input("Inserisci nome: ")
    name_handle.write(name+"\n")
name_handle.close()