import time
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_formatted_text():
    text = """
:::    :::     :::     :::        :::         ::::::::  :::       :::     :::     :::   :::   ::::::::  ::::::::::: ::::::::::: :::   ::: 
:+:    :+:   :+: :+:   :+:        :+:        :+:    :+: :+:       :+:   :+: :+:   :+:   :+:  :+:    :+:     :+:         :+:     :+:   :+: 
+:+    +:+  +:+   +:+  +:+        +:+        +:+    +:+ +:+       +:+  +:+   +:+   +:+ +:+   +:+            +:+         +:+      +:+ +:+  
+#++:++#++ +#++:++#++: +#+        +#+        +#+    +:+ +#+  +:+  +#+ +#++:++#++:   +#++:    +#+            +#+         +#+       +#++:   
+#+    +#+ +#+     +#+ +#+        +#+        +#+    +#+ +#+ +#+#+ +#+ +#+     +#+    +#+     +#+            +#+         +#+        +#+    
#+#    #+# #+#     #+# #+#        #+#        #+#    #+#  #+#+# #+#+#  #+#     #+#    #+#     #+#    #+#     #+#         #+#        #+#    
###    ### ###     ### ########## ##########  ########    ###   ###   ###     ###    ###      ########  ###########     ###        ###     
"""
    print(text)

def introducao():
    print("Você está prestes a começar um jogo pelo qual não deveria começar!")
    time.sleep(2)
    print("Aceite os termos do jogo abaixo.")
    time.sleep(2)
    print("прими условия, чтобы мы могли начать эту дерьмовую игру")

def começar():
    escolha = ""
    while escolha != "s" and escolha != "n":
        print("Aceitar termos? (s/n)")
        escolha = input().lower()
        limpar_terminal()
    return escolha

def escolha_caminho():
    escolha = ""
    while escolha != "1" and escolha != "2" and escolha != "3":
        print("Qual caminho você escolhe? (1, 2 ou 3)")
        escolha = input()
        limpar_terminal()
    return escolha

def verificar_começar(escolha):
    if escolha == "s":
        print("Então podemos começar!")
        time.sleep(2)
        limpar_terminal()
    elif escolha == "n":
        print("Infelizmente você não tem sangue frio para esse jogo!")
        exit()  

def verificar_caminho(escolha):
    if escolha == "1":
        print("Você avança pelo caminho 1")
        time.sleep(2)
        print("Você encontra uma caverna escura...")
        time.sleep(2)
        print("O que você faz?")
        time.sleep(2)
        print("1. Entra na caverna.")
        print("2. Segue na estrada que tem ao lado da entrada da caverna.")
        escolha_caverna = input()
        limpar_terminal()
        if escolha_caverna == "1":
            print("Ao entrar na caverna você e recebido por um feral que se alimenta de humanos...")
            time.sleep(2)
            print("Mas você não tem nenhuma arma para se defender...")
            time.sleep(2)
            print("Infelizmente o feral te devora.")
            time.sleep(2)
            print("GAME OVER")
            return False
        elif escolha_caverna == "2":
            print("Você segue pela estrada...")
            time.sleep(2)
            print("O final da estrada é um abismo...")
            time.sleep(2)
            print("Você tenta retornar, mas os ferais que sairam da caverna estão correndo em sua direção...")
            time.sleep(2)
            print("Você se desespera e acaba caindo.")
            time.sleep(2)
            print("GAME OVER")
            return False
        else:
            print("Opção inválida!")
            return False
    elif escolha == "2":
        print("Você avança pelo caminho 2...")
        time.sleep(2)
        limpar_terminal()
        print("Você encontra um portal misterioso.")
        time.sleep(2)
        print("1. Entrar no portal")
        print("2. Ignorar o portal e continuar pela trilha")
        escolha_portal = input()
        limpar_terminal()
        if escolha_portal == "1":
            print("Você entra no portal e é recebido por uma bruxa...")
            time.sleep(2)
            print("Ela irá te guiar...")
            time.sleep(2)
            print("Mas antes ela pergunta...")
            time.sleep(2)
            print("Vamos fazer um pacto?")
            time.sleep(2)
            print("1. Fazer o pacto.")
            print("2. Não fazer o pacto.")
            escolha_bruxa = input()
            limpar_terminal()
            if escolha_bruxa == "1":
                print("Esse pacto que você fez com a bruxa ele nunca mais te deixará sair desse jogo e sua vida estará vagando por HALLOWAY CITY para sempre.")
                time.sleep(2)
                print("Você é só mais um dos que não lerão os termos desse jogo e agora está preso aqui!")
                time.sleep(2)
                print("GAME OVER")
                return False
            elif escolha_bruxa == "2":
                print("Não fazer o pacto te da um poder sobre a bruxa...")
                time.sleep(2)
                print("A unica forma dela sair de guia desse portal e ela realizando o pacto...")
                time.sleep(2)
                print("Como você foi esperto!")
                time.sleep(2)
                print("Agora ela será obrigada a te guiar para fora desse portal")
                time.sleep(2)
                print("E lá vamos nós...")
                time.sleep(2)
                print("No fim do portal encotramos uma floresta sombria e uma trilha para montanha")
                print("1. Floresta sombria.")
                print("2. Trilha para montanha.")
                escolha_floresta_trilha = input()
                limpar_terminal()
                if escolha_floresta_trilha == "1":
                    print("A floresta pertence ao Mortiferoth, o Devorador de Almas!")
                    time.sleep(2)
                    print("Infelizmente a unica forma de sair dessa floresta e vendendo sua alma para ele...")
                    time.sleep(2)
                    print("Mas você conhece aquela bruxa que faria de tudo para sair daquele portal...")
                    time.sleep(2)
                    print("Você então negocia um acordo entre a bruxa e o Mortiferoth...")
                    time.sleep(2)
                    print("Nesse acordo eles fazem um pacto de alma e liberam a sua alma desse jogo...")
                    time.sleep(2)
                    print("Assim você poderá voltar pra casa em segurança!")
                    print("MEUS PARABÉNS VOCÊ SAIU COM VIDA DESSE JOGO!!!")
                    return False
                elif escolha_floresta_trilha == "2":
                    print("A trilha para montanha possui um guardião chamado Vorágine, o senhor do caos")
                    time.sleep(2)
                    print("Ele causou desordem na sua mente e fez você se jogar da montanha.")
                    time.sleep(2)
                    print("GAME OVER")
                    return False
            else:
                print("Opção inválida!")
                return False
        elif escolha_portal == "2":
            print("Você decide ignorar o portal e continuar em frente...")
            time.sleep(2)
            print("Você cometeu um grande erro ao ignorar esse portal... ")
            time.sleep(2)
            print("Nesse caminho você encontrou um Gnomo que o amaldiçoou a viver preso com os ferais...")
            time.sleep(2)
            print("Viverá eternamente servindo de alimento para os ferais!!")
            time.sleep(2)
            print("GAME OVER")
            return False
        else:
            print("Opção inválida!")
            return False
    elif escolha == "3":
        print("Você escolhe o caminho 3...")
        time.sleep(2)
        limpar_terminal()
        print("Você se depara com Dracus, o Desperto das Trevas.")
        time.sleep(2)
        print("O que você faz?")
        time.sleep(2)
        print("1. Procura por artefatos mágicos ao redor")
        print("2. Aproxima-se de Dracus")
        escolha_dracus = input()
        limpar_terminal()
        if escolha_dracus == "1":
            print("O chão está cheio de artefatos...")
            time.sleep(2)
            print("Esse aqui deve servir...")
            time.sleep(2)
            print("📿")
            time.sleep(2)
            print("Esse artefato mata Dracus e te concede a volta para casa")
            time.sleep(2)
            print("Você conseguiu sair desse jogo!!!")
            time.sleep(2)
            print("Excelente você está livre do para seguir a sua vida!!!")
            return False
        elif escolha_dracus == "2":
            print("Dracus te puxa e te leva para as trevas...")
            time.sleep(2)
            print("Ele te condena a viver 100 mil anos nas trevas...")
            time.sleep(2)
            print("GAME OVER")
            return False
        else:
            print("Opção inválida!")
            return False
    else:
        print("Opção inválida!")
        return False

def resetar_jogo():
    while True:
        print("Deseja jogar novamente? (s/n)")
        escolha = input().lower()
        if escolha == "s":
            limpar_terminal()
            main()
        elif escolha == "n":
            print("Obrigado por jogar!")
            exit()
        else:
            print("Opção inválida!")

def main():
    print_formatted_text()
    introducao()
    escolha_começar = começar()
    verificar_começar(escolha_começar)
    caminho_escolhido = escolha_caminho()
    while not verificar_caminho(caminho_escolhido):
        caminho_escolhido = escolha_caminho()
    resetar_jogo()

if __name__ == "__main__":
    main()
