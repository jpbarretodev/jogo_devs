#classe principal do jogador

class Jogador:

    def __init__(self, nome: str, saldo: int): # construção da classe recebendo o nome e o saldo inicial do jogador
        self.nome = nome
        self.saldo = saldo # por enquanto, a varíavel receberá int

    @staticmethod
    def verificar_saldo(saldo_atual, saldo_para_verificacao):
        if saldo_para_verificacao > saldo_atual:
            return False
        else:
            return True

    def ganhar_saldo(self, saldo_ganho):
        self.saldo += saldo_ganho
        pass

    def perder_saldo(self, saldo_apostado):
        self.saldo -= saldo_apostado
        pass

    def apostar(self):
        """
        Essa função retorna um booleano permitindo ou não que o usuário faça a aposta. Quando a função retornar False, o usuário perdeu.
        """
        # Faz a verificação do saldo do Jogador
        if self.saldo > 0:
            aposta = int(input("Insira o valor da aposta: "))

            while self.verificar_saldo(self.saldo, aposta) != True:
                aposta = int(input("Valor maior que o saldo. Insira um valor dentro da possibilidade: "))
            else:
                print(f"Valor apostado {aposta}") # trocar para retornar o saldo e/ou um booleano
    
        elif self.saldo <= 0: # Obs: dar uma olhada com carinho aqui nessa condição
            return False
        
    