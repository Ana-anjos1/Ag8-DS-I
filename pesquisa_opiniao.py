# Pesquisa de Opinião - TudoWeb

TOTAL_ENTREVISTADOS = 50

quantidade_excelente = 0
quantidade_ruim = 0

print("=" * 50)
print("PESQUISA DE OPINIÃO - TUDOWEB")
print("=" * 50)

for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\n--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")

    while True:
        nome = input("Digite o nome: ").strip()
        if nome:
            break
        print("O nome não pode ficar em branco.")

    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade > 0:
                break
            print("A idade deve ser maior que zero.")
        except ValueError:
            print("Digite uma idade válida.")

    while True:
        try:
            opiniao = int(input(
                "Opinião sobre o atendimento:\n"
                "1 - EXCELENTE\n"
                "2 - BOM\n"
                "3 - RUIM\n"
                "Digite sua opção: "
            ))

            if opiniao in (1, 2, 3):
                break

            print("Opção inválida. Digite 1, 2 ou 3.")
        except ValueError:
            print("Digite apenas o número da opção.")

    if opiniao == 1:
        quantidade_excelente += 1
    elif opiniao == 3:
        quantidade_ruim += 1

print("\n" + "=" * 50)
print("RESULTADO DA PESQUISA")
print("=" * 50)
print(f'Quantidade de respostas "EXCELENTE": {quantidade_excelente}')
print(f'Quantidade de respostas "RUIM": {quantidade_ruim}')
print("=" * 50)