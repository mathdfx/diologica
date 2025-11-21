def calcular_nivel_heroi(vitorias, derrotas):

    saldo_vitorias = vitorias - derrotas
    nivel = ""

    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    elif vitorias >= 101:
        nivel = "Imortal"
    else:
        nivel = "Ferro (Nível Base)"

    return saldo_vitorias, nivel

continuar = "S"

print("--- ⚔️ CALCULADORA DE PARTIDAS RANKEADAS ⚔️ ---")

while continuar == "S":
    
    heroi = str(input("Qual o nome do seu Herói: "))
    qtd_vitorias = int(input("Digite a quantidade de vitórias: "))
    qtd_derrotas = int(input("Digite a quantidade de derrotas: "))

    saldo_final, nivel_final = calcular_nivel_heroi(qtd_vitorias, qtd_derrotas)

    print(f"O Herói {heroi} tem de saldo de {saldo_final} está no nível de {nivel_final}")
    
    print("-" * 30)
    
    continuar = input("Deseja calcular outro herói? (S/N): ").upper()
