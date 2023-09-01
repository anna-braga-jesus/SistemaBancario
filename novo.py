menu = """
[d] Depósito
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("O valor informado é inválido. Verifique e tente novamente!")

    elif opcao == "s":
        float(input("Informe o valor do saque:"))

        #Condições
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você excedeu o saldo! Verifique e tente novamente!")
        elif excedeu_limite:
            print("Operação falhou! Você excedeu o limite de saque diário!")
        elif excedeu_saques:
            print( "Limite de saque excedido!")
        
        elif valor > 0:
            saldo -= valor
            extrato+= (f"Saque: R${valor:.2f}\n")
            numero_saques += 1

        else:
            print("O valor informado é inválido. Verifique e tente novamente.")


    elif opcao == "e":
        print("\n===================Extrato=====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}\n")
        print("================== Obrigada pela preferência! ============================")
    
    elif opcao == 'q':
        break
    
    else: print("Não foi possível concluir a opção. Verifique e tente novamente.")

