lista_de_jogadores = []


# Menu principal
def menu_principal():
    jogador_atual = ""  # ainda ninguém selecionado

    while True:
        if jogador_atual == "":
            mostrar_jogador = "nenhum"
        else:
            mostrar_jogador = jogador_atual

        print(f"""
=== Menu principal ===
Jogador atual: {mostrar_jogador}

1 - Jogadores
2 - Jogos
3 - Histórico de partidas (em desenvolvimento)
4 - Estatísticas (em desenvolvimento)
5 - Rankings (em desenvolvimento)
0 - Sair""")
        opcao = input("Opção: ")

        if opcao == "1":
            jogador_atual = menu_jogadores(jogador_atual)
        elif opcao == "2":
            if jogador_atual == "":
                print("\nTem de selecionar um jogador antes de jogar (opção 1 - Jogadores).")
            else:
                menu_jogos()
        elif opcao in ["3", "4", "5"]:
            print("\nEsta opção ainda está em desenvolvimento.")
        elif opcao == "0":
            print("Até à próxima!")
            break
        else:
            print("Opção inválida.")


# Jogadores
def criar_jogador():
    nome = input("Introduza o nome de utilizador do novo jogador: ").strip()
    if nome == "":
        print("O nome de utilizador não pode estar vazio.")
    elif nome in lista_de_jogadores:
        print("Já existe um jogador com esse nome.")
        criar_jogador()
    else:
        lista_de_jogadores.append(nome)
        print(f"Jogador {nome} criado.")


# Selecionar o jogador
def selecionar_jogador():
    if len(lista_de_jogadores) == 0:
        print("Ainda não há jogadores. Crie um jogador primeiro.")
        return ""

    print("\nLista de jogadores")
    print("__")
    for jogador in lista_de_jogadores:
        print(f" - {jogador}")
    print("__")

    while True:
        escolhido = input("Introduza o jogador que quer utilizar (Enter para voltar): ").strip()
        if escolhido == "":
            return ""
        elif escolhido in lista_de_jogadores:
            print(f"Selecionou o jogador {escolhido}.")
            return escolhido
        else:
            print("Este jogador não faz parte da lista de jogadores.")


# Submenu dos jogadores. Devolve o jogador que ficou selecionado.
def menu_jogadores(jogador_atual):
    while True:
        print("""
=== Jogadores ===
1 - Criar jogador
2 - Selecionar jogador
0 - Voltar""")
        opcao = input("Opção: ")
        if opcao == "1":
            criar_jogador()
        elif opcao == "2":
            novo = selecionar_jogador()
            if novo != "":  # só muda se tiver escolhido alguém
                jogador_atual = novo
        elif opcao == "0":
            return jogador_atual  # volta ao menu principal
        else:
            print("Opção inválida.")


# Jogos
def menu_jogos():
    while True:
        print("""
=== Jogos ===
 - Adivinha o Número (em desenvolvimento)
 - Pedra, Papel ou Tesoura (em desenvolvimento)
 - Jogo da Forca (em desenvolvimento)
 - Blackjack (em desenvolvimento)

0 - Voltar""")
        opcao = input("Opção: ")
        if opcao == "0":
            break  # sai deste ciclo e volta ao menu principal
        else:
            print("Opção inválida.")


menu_principal()
