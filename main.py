
# ==========================================
# RADAR DE FLUXO
# Sistema de Orquestração de Ordens de Serviço
# ==========================================

ordens = []


# ------------------------------------------
# CADASTRAR UMA ORDEM DE SERVIÇO
# ------------------------------------------

def cadastrar_os():

    print("\n===== CADASTRO DE O.S. =====")

    numero = int(input("Número da O.S.: "))
    tipo = input("Tipo de serviço: ")

    print("\nPrioridade:")
    print("1 - Baixa")
    print("2 - Média")
    print("3 - Alta")

    prioridade = int(input("Escolha a prioridade: "))

    prazo = int(input("Quantos dias faltam para o prazo? "))

    tempo = float(input("Tempo estimado de serviço (horas): "))

    pecas = input("As peças estão disponíveis? (s/n): ")

    if pecas.lower() == "s":
        pecas_disponiveis = True
    else:
        pecas_disponiveis = False

    ordem = {
        "numero": numero,
        "tipo": tipo,
        "prioridade": prioridade,
        "prazo": prazo,
        "tempo": tempo,
        "pecas": pecas_disponiveis
    }

    ordens.append(ordem)

    print("\nO.S. cadastrada com sucesso!")


# ------------------------------------------
# CALCULAR SCORE DA O.S.
# ------------------------------------------

def calcular_score(ordem):

    score = 0

    # Prioridade
    score += ordem["prioridade"] * 10

    # Urgência do prazo
    if ordem["prazo"] <= 1:
        score += 30

    elif ordem["prazo"] <= 3:
        score += 20

    elif ordem["prazo"] <= 5:
        score += 10

    # Serviços demorados
    if ordem["tempo"] >= 15:
        score += 5

    return score


# ------------------------------------------
# MOSTRAR A FILA
# ------------------------------------------

def mostrar_fila():

    print("\n===== FILA DE O.S. =====")

    if len(ordens) == 0:

        print("Nenhuma O.S. cadastrada.")

        return

    # Ordena as O.S. pelo score
    fila = sorted(
        ordens,
        key=calcular_score,
        reverse=True
    )

    for posicao, ordem in enumerate(fila, start=1):

        score = calcular_score(ordem)

        if ordem["pecas"]:

            status = "LIBERADA"

        else:

            status = "BLOQUEADA - aguardando peças"

        print("\n--------------------------")

        print(f"{posicao}º - O.S. {ordem['numero']}")

        print(f"Serviço: {ordem['tipo']}")

        print(f"Prioridade: {ordem['prioridade']}")

        print(f"Dias restantes: {ordem['prazo']}")

        print(f"Tempo estimado: {ordem['tempo']} horas")

        print(f"Score: {score}")

        print(f"Status: {status}")


# ------------------------------------------
# ANALISAR CAPACIDADE
# ------------------------------------------

def analisar_capacidade():

    print("\n===== ANÁLISE DE CAPACIDADE =====")

    tempo_total = 0

    for ordem in ordens:

        if ordem["pecas"]:

            tempo_total += ordem["tempo"]

    # Capacidade simplificada
    capacidade = 44

    print(f"Tempo planejado: {tempo_total:.1f} horas")

    print(f"Capacidade disponível: {capacidade} horas")

    if tempo_total > capacidade:

        print("⚠️ ALERTA: capacidade ultrapassada!")

    else:

        utilizacao = (tempo_total / capacidade) * 100

        print(f"Utilização: {utilizacao:.1f}%")

        if utilizacao >= 80:

            print("⚠️ Atenção: capacidade próxima da saturação.")


# ------------------------------------------
# MENU PRINCIPAL
# ------------------------------------------

def menu():

    while True:

        print("\n")
        print("==============================")
        print("       RADAR DE FLUXO")
        print("==============================")

        print("1 - Cadastrar O.S.")
        print("2 - Mostrar fila")
        print("3 - Analisar capacidade")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":

            cadastrar_os()

        elif opcao == "2":

            mostrar_fila()

        elif opcao == "3":

            analisar_capacidade()

        elif opcao == "0":

            print("\nEncerrando Radar de Fluxo...")

            break

        else:

            print("\nOpção inválida!")


# Iniciar o programa
menu()

