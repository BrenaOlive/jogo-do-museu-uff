print("--------------------------------------------------")
print("Bem vindo ao Mistério no Museu\n")


def jogo_escolha():
    while True:
        try:
            opcao =int(input( "Escolha a entrada do museu por onde você deseja começar a partida \n"
                "1 - Frente \n"
                "2 - Serviço \n"
                "3 - Telhado \n\n"))
           
            match opcao:
                case 1:
                    jogoFrente()
                    break
                case 2:
                    jogoServico()
                    break
                case 3:
                    jogoTelhado()
                    break
                case _:
                    print("ESCOLHA UMA OPÇÃO VÁLIDA!\n")
        
        except ValueError:
            print("Digite apenas as opções acima \n")

        
def jogoFrente():
    tentativas = 3
    print("------------------------------------------------")
    print("\nVocê está na frente do museu e quer seguir pelo caminho mas a porta está bloqueada e você precisa desvendar um mistério para seguir. Você tem:", tentativas, "tentativas.\n")
    
    while tentativas > 0:
        try:
            valores = input("Digite 2 valores inteiros e 1 valor decimal separados por espaço:\n\n ").split()

            if len(valores) != 3:
                raise ValueError

            a = int(valores[0])
            b = int(valores[1])
            c = float(valores[2])


            if (294%a == 0 and 294//a == b and abs(c - (b / a)) < 0.0001):
                print("\nParabéns!\nVocê segue para a segunda etapa.|=\n")
                return segundaEtapa("frente", 4 - tentativas)
            else:
                tentativas -= 1
                print("\nERROU, você possue:",tentativas,"restantes\n")

        except ValueError:
            tentativas -= 1
            print("\nEntrada inválida!")
            print("\nTentativas restantes:", tentativas, "\n")

    print("\nSuas tentativas acabaram e você perdeu!\n")

def jogoServico():
    tentativas = 3
    print("\nVocê está na área de serviço do museu e quer seguir pelo caminho mas a porta está bloqueada e você precisa desvendar um mistério para seguir. Você tem:", tentativas, "tentativas.\n")

    while tentativas > 0:
        try:
            valores = input("\nDigite 2 números inteiros:\n\n ").split()

            if len(valores) != 2:
                raise ValueError

            a = int(valores[0])
            b = int(valores[1])

            if b != 0 and a % b == 0 and b % 2 != 0 and (a + b) > 50:
                print("\nParabéns! Você avançou!\n")
                segundaEtapa("servico", 4 - tentativas)
                return
            else:
                tentativas -= 1
                print("\nErrou! Restam:\n", tentativas)

        except ValueError:
            tentativas -= 1
            print("\nEntrada inválida! Restam:", tentativas)

    print("\nVocê perdeu!\n")

def jogoTelhado():
    tentativas = 3
    print("\nVocê está no telhado do museu e quer seguir pelo caminho mas a porta está bloqueada e você precisa desvendar um mistério para seguir. Você tem:", tentativas, "tentativas.\n")

    while tentativas > 0:
        try:
            valores = input("Digite 3 números decimais:\n\n ").split()

            if len(valores) != 3:
                raise ValueError

            x = float(valores[0])
            y = float(valores[1])
            z = float(valores[2])

            if (x + y > z and x + z > y and y + z > x) and not (x == y == z):
                print("\nParabéns! Você avançou!\n")
                segundaEtapa("telhado", 4 - tentativas)
                return
            else:
                tentativas -= 1
                print("\nErrou! Restam:\n", tentativas)

        except ValueError:
            tentativas -= 1
            print("\nEntrada inválida! Restam:\n", tentativas)

    print("\nVocê perdeu!\n")      

def segundaEtapa(entrada, tentativa_usada):
    itens_validos = {'lanterna','chave','corda'}

    while True:
        escolha = input("\nEscolha dois itens (lanterna chave corda):\n\n").lower().split()

        if(len(escolha)!= 2):
            input("\nDigite apenas 2 itens da lista.\n")
            continue

        if (escolha[0] == escolha [1]):
            print("\nOs itens não podem ser repetidos.\n")
            continue

        if(escolha[0] not in itens_validos or escolha[1] not in itens_validos):
            print("\nDigite somente itens que estejam na lista.\n")
            continue
            
        break

    itens_escolhidos = set(escolha)
    terceiraEtapa(entrada, tentativa_usada, itens_escolhidos)

def terceiraEtapa(entrada, tentativa_usada, itens_escolhidos):
    combinacoes = {
        "frente": {"lanterna", "chave"},
        "servico": {"chave", "corda"},
        "telhado": {"lanterna", "corda"}
    }
    
    print("\nVocê acaba de entrar em uma sala escura e a sua frente está localizado um cofre, mas ele está bloqueado por uma viga!\n")
    print("Suas opções de itens são", " e ".join(itens_escolhidos), "será que você conseguiu?\n" )
    if itens_escolhidos != combinacoes[entrada]:
        print("Final: Você não conseguiu! O final foi ruim\n")
        return

    if tentativa_usada == 1:
        finais = {
            "frente": "Você abriu o cofre e foi excelente supremo",
            "servico": "Você abriu o cofre e foi perfeito supremo",
            "telhado": "Você abriu o cofre e foi ninja supremo"
        }
        print("Final:", finais[entrada])

    elif tentativa_usada == 2:
        finais = {
            "frente": "excelente",
            "servico": "perfeito",
            "telhado": "ninja"
        }
        print("Final:", finais[entrada])

    else:
        print("Final: neutro")

   
while True:
    jogo_escolha()
    jogar_novamente = input("Deseja jogar novamente? (sim/nao): ").lower()

    if jogar_novamente != "sim":
        print("Encerrando jogo...")
        break



