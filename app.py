class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self.saldo:
            print("Saldo insuficiente para saque.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def consultar_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")

def main():
    print("Bem-vindo ao Sistema Bancário!")
    nome = input("Digite seu nome para criar uma conta: ")
    conta = ContaBancaria(nome)

    while True:
        print("\nEscolha uma opção:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Consultar saldo")
        print("4 - Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor para depósito: R$"))
            conta.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor para saque: R$"))
            conta.sacar(valor)
        elif opcao == '3':
            conta.consultar_saldo()
        elif opcao == '4':
            print("Obrigado por usar o Sistema Bancário. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
