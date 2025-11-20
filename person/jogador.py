#classe principal do jogador

class Jogador:

    def __init__(self, nome: str, saldo: int): # construção da classe recebendo o nome e o saldo inicial do jogador
        self.nome = nome
        self.saldo = saldo # por enquanto, a varíavel receberá int
        self.saldo_inserido = 0

    def alterar_saldo(self):
        self.saldo -= self.saldo_inserido

    def validar_aposta(self, saldo_inserido = 0): # < -- FUNÇÃO EM TESTE -- >
        self.saldo_inserido = int(input('Insira o valor da aposta: ')) # esse número deve vir do próprio front como um inteiro ou objeto de classe para poder ser chamado no backend e fazer a lógica

        #verificador de saldo inserido
        while self.saldo_inserido > self.saldo:
            self.saldo_inserido = int(input('Valor mais alto que o permitido. Insira novamente'))

        self.alterar_saldo()
        
'''
user = Jogador("Tester", 2)
print(f"Saldo atual: {user.saldo}")
user.apostar()
print(f"Saldo após a aposta: {user.saldo} e Saldo inserido: {user.saldo_inserido}")
'''

# user = Jogador('Tester', 100)
# user.apostar()
