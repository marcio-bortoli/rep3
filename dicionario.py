import os
def dicionario_exemplo():
    dicionario = {}
    print("1 - P/ Lançar")
    print("2 - P/ Finalizar")
    status = int(input("Informa a opção: "))
    
    i = 1
    while (status == 1):
        item = input("Informar Item: ")
        dicionario[i] = item
        i = i + 1
        print("1 - P/ Lançar")
        print("2 - P/ Finalizar")
        status = int(input("Informa a opção: "))

    print("----------------POP--------------------")
    chave = input("Informe chave para exclusao: ")
    print(dicionario.pop(int(chave)))

    print("----------------------------------------")
    for dic in dicionario.items():  
        print(dic)
    
    print("---------------VALUES-------------------")
    for dic in dicionario.values():
        print(dic)

    print("---------------KEYS---------------------")
    for dic in dicionario.keys():
        print(dic)
    
dicionario_exemplo()


