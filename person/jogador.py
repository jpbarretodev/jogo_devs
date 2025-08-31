#classe principal do jogador

class Jogador:

    def __init__(self, nome: str, saldo: int): # construção da classe recebendo o nome e o saldo inicial do jogador
        self.nome = nome
        self.saldo = saldo # por enquanto, a varíavel receberá int

    def verificar_saldo(self):
        if self.saldo <= 0:
            return False
        else:
            return True

    def apostar(self):
        if self.verificar_saldo() == True:
            print("Ok")
        else:
            print("Você perdeu por estar sem saldo!")

    def alterar_saldo(self):
        
        pass

user = Jogador("Tester", 100)