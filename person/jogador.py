#classe principal do jogador

class Jogador:

    def __init__(self, nome: str, saldo: int): # construção da classe recebendo o nome e o saldo inicial do jogador
        self.nome = nome
        self.saldo = saldo # por enquanto, a varíavel receberá int
        self.saldo_inserido = 0

    def verificar_saldo(self):
        if self.saldo <= 0:
            return False
        else:
            return True

    def apostar(self): # < -- FUNÇÃO EM TESTE -- >
        if self.verificar_saldo() == True:
            self.saldo_inserido = int(input("Insira o valor da aposta: ")) # SOMENTE PARA TESTE, DESENROLAR DEPOIS COM A GALERA DO FRONT

            while self.saldo_inserido > self.saldo or self.saldo_inserido <= 0 :
                self.saldo_inserido = int(input("Insira o valor da aposta novamente: "))
            self.saldo -= self.saldo_inserido # diminui o saldo do usuário mediante inserção do saldo de aposta            

        else:
            print("Você perdeu por estar sem saldo!")

    def alterar_saldo(self):
        pass

'''
user = Jogador("Tester", 2)
print(f"Saldo atual: {user.saldo}")
user.apostar()
print(f"Saldo após a aposta: {user.saldo} e Saldo inserido: {user.saldo_inserido}")
'''