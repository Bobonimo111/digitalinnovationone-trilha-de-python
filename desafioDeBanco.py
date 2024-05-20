Extrato = ""
saldo = 00
saldo += 1000
opcao = -1
saques = 0
while (opcao != 0) :
    print("="*20)
    print("BEM VINDO AO BANCO")
    print("SELECIONE")
    print("DEPOSITO (1)")
    print("SAQUE (2)")
    print("EXTRATO (3)")
    print("SAIR (0)")
    entrada = int(input())

    opcao = 0 if entrada == 0 else ""
    if(entrada == 1):
        valor = int(input("VALOR DEPOSITO: "))
        if(valor > 0):
            saldo += valor
            print("valor adicionado a conta, pressione enter") 
            Extrato += "DEPOSITO : R$" + str(valor) + ".00\n"
        else:
            print("valor invalido,pressione enter")
        input()
    elif(entrada == 2):
        valor = int(input("VALOR SAQUE: "))
        if(valor > saldo):
            print("SALDO INSUFICIENTE, PRESCIONE ENTER")
            input()
        elif(saques >= 1500):
            print("limete diario excedido,PRESCIONE ENTER")
            input()
        elif(valor > 500):
            print("valor maior que o permitido,PRESCIONE ENTER")
            input()
        
        else:
            saques += valor
            saldo -= valor
            Extrato += "SAQUE : R$" + str(valor) + ".00\n"
            input("SAQUE REALIZADO COM SUCESSO, PRESCIONE ENTER")
    elif(entrada == 3):
        print(Extrato)
        print("SALDO : R$" + str(saldo)+ ".00")
        input("PRESCIONE ENTER")
    elif(entrada != 0 ):
        input("VALOR INVALIDO E TENTE NOVAMENTE,PRESCIONE ENTER")