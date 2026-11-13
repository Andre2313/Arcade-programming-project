import os

# caminho do ficheiro dos jogadores (pasta data)
PASTA_DO_PROGRAMA = os.path.dirname(os.path.abspath(__file__))
CAMINHO_JOGADORES = os.path.join(PASTA_DO_PROGRAMA, "..", "data", "jogadores.csv")

lista_de_jogadores = []


# lê os jogadores do ficheiro e põe na lista
def carregar_jogadores():
    # se o ficheiro não existir, cria com o cabeçalho
    if not os.path.exists(CAMINHO_JOGADORES):
        ficheiro = open(CAMINHO_JOGADORES, "w", encoding="utf-8")
        ficheiro.write("username\n")
        ficheiro.close()
        return

    ficheiro = open(CAMINHO_JOGADORES, "r", encoding="utf-8")
    linhas = ficheiro.readlines()
    ficheiro.close()

    for linha in linhas[1:]:  # salta a primeira linha
        nome = linha.strip()
        if nome != "" and nome not in lista_de_jogadores:
            lista_de_jogadores.append(nome)


# guarda um jogador no fim do ficheiro
def guardar_jogador(nome):
    ficheiro = open(CAMINHO_JOGADORES, "a", encoding="utf-8")  # a = acrescentar
    ficheiro.write(nome + "\n")
    ficheiro.close()


# escreve o ficheiro outra vez, com os jogadores que estão na lista
def guardar_todos_os_jogadores():
    ficheiro = open(CAMINHO_JOGADORES, "w", encoding="utf-8")  # w = apagar e escrever de novo
    ficheiro.write("username\n")
    for jogador in lista_de_jogadores:
        ficheiro.write(jogador + "\n")
    ficheiro.close()


# Menu principal
def menu_principal():
    carregar_jogadores()  # lê os jogadores do ficheiro
    jogador_atual = ""  # ainda não escolheu ninguém

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
    elif "," in nome:  # a vírgula é o separador do csv
        print("O nome de utilizador não pode ter vírgulas.")
    elif nome in lista_de_jogadores:
        print("Já existe um jogador com esse nome.")
        criar_jogador()
    else:
        lista_de_jogadores.append(nome)
        guardar_jogador(nome)  # guarda no ficheiro
        print(f"Jogador {nome} criado.")


# Escolher o jogador
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


# Eliminar um jogador e os seus dados
def eliminar_jogador(jogador_atual):
    if len(lista_de_jogadores) == 0:
        print("Ainda não há jogadores para eliminar.")
        return jogador_atual

    print("\nLista de jogadores")
    print("__")
    for jogador in lista_de_jogadores:
        print(f" - {jogador}")
    print("__")

    while True:
        escolhido = input("Introduza o jogador que quer eliminar (Enter para voltar): ").strip()
        if escolhido == "":
            return jogador_atual
        elif escolhido in lista_de_jogadores:
            break
        else:
            print("Este jogador não faz parte da lista de jogadores.")

    resposta = input(f"Tem a certeza que quer eliminar {escolhido} e os seus dados? (s/n): ").strip().lower()
    if resposta == "s":
        lista_de_jogadores.remove(escolhido)  # tira da lista
        guardar_todos_os_jogadores()  # atualiza o ficheiro
        # mais tarde: apagar aqui também as partidas deste jogador
        print(f"Jogador {escolhido} eliminado.")
        if escolhido == jogador_atual:
            jogador_atual = ""  # já não há jogador selecionado
    else:
        print("Nada foi eliminado.")
    return jogador_atual


# Menu dos jogadores
def menu_jogadores(jogador_atual):
    while True:
        print("""
=== Jogadores ===
1 - Criar jogador
2 - Selecionar jogador
3 - Eliminar jogador
0 - Voltar""")
        opcao = input("Opção: ")
        if opcao == "1":
            criar_jogador()
        elif opcao == "2":
            novo = selecionar_jogador()
            if novo != "":  # só muda se escolheu alguém
                jogador_atual = novo
        elif opcao == "3":
            jogador_atual = eliminar_jogador(jogador_atual)
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
            break  # volta ao menu principal
        else:
            print("Opção inválida.")


menu_principal()
