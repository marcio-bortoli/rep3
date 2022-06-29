listaclientes = []

def imprimirClientes():
    print("-- Relatório de Clientes ---")
    print("----------------------------")
    print("CPF            Nome")
    print("----------------------------")
    for i in range(len(listaclientes)):
        print(listaclientes[i]["cpf"]+"  "+listaclientes[i]["nome"])
    print("----------------------------")      
    while True:
        try: 
            while int(input("Informe [9] para sair: ")) == 9:
                break
        except:
            print("Opção informada é inválida.")
            continue
        else:
            break                

def cadastrarCliente():
    print("--- C L I E N T E ---")
    nome = input("Informe o nome...: ")        
    cpf = input("Informe o CPF.....: ")   
    idade = input("Informe a idade.: ")
    sexo = input("Informe Sexo[M/F]: ")
    listaclientes.append({"nome":nome,"cpf":cpf,"idade":idade,"sexo":sexo})
    print("Cliente salvo com sucesso")
    
def main():
    opcao = 1
    while (opcao in (1,2,9)):
        print("--- C L I E N T E ---")
        print("1 - Cadastro")
        print("2 - Imprimir")
        print("9 - Sair    ")
        opcao = int(input("Informe a opcao:"))
        if (opcao == 1):
            cadastrarCliente()
        elif (opcao == 2):
            imprimirClientes()
        elif (opcao == 9):
            break
        else:
            print("Opção inválida")

main()

