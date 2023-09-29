class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.saques_restantes = 3
        self.extrato = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +{valor} reais")
            print(f"Depósito de {valor} reais realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def saque(self, valor):
        if self.saques_restantes > 0:
            if valor <= 500 and valor <= self.saldo:
                self.saldo -= valor
                self.saques_restantes -= 1
                self.extrato.append(f"Saque: -{valor} reais")
                print(f"Saque de {valor} reais realizado com sucesso.")
            elif valor > 500:
                print("O limite máximo por saque é de 500 reais.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Você atingiu o limite diário de saques.")

    def imprimir_extrato(self):
        print("\nExtrato:")
        for item in self.extrato:
            print(item)
        print(f"Saldo atual: {self.saldo} reais")
        print(f"Saques restantes hoje: {self.saques_restantes}")

# Exemplo de uso
conta = ContaBancaria(1000)

while True:
    print("\nEscolha uma opção:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Imprimir Extrato")
    print("4. Sair")

    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        conta.deposito(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        conta.saque(valor)
    elif opcao == "3":
        conta.imprimir_extrato()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")
