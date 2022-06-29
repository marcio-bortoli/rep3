import random

#Sorteando números de 0 a 50, quando sorteado
# o número 50 para encerrar o sorteio
numero = 0
while (numero != 50):
    numero = random.randrange(1, 51)
    print("Número Sorteado:", numero)

#alimenta as 10 primeiras posições de uma
#lista com números sorteados de 1 a 50.
lista = []
for i in range(0,10):
    numero = random.randrange(1,51)
    lista.append(numero)
print(lista)

#sorteia um número de 1 a 50, e pesquisa
#se o número sorteado existe na lista
achou = False
numero = random.randrange(1,51)
for i in range(0,len(lista)):
    if (lista[i] == numero):
        achou = True
if (achou):
    print("O número sorteado ",numero," consta na lista na posição ",i)
else:    
    print("O número sorteado ",numero," não consta na lista")

