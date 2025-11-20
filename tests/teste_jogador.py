from person.jogador import Jogador

# instanciado a classe
jogador = Jogador("Tester", 100)

# teste para alterar o saldo
def alterador_de_saldo(valor_para_alterar):
	"""
	Para testar, use: alterador_de_saldo(coloque aqui dentro, o valor que deseja alterar do jogador)
	"""
	jogador.saldo_inserido = valor_para_alterar
	jogador.alterar_saldo()
	print("O novo saldo do jogador é de: {}".format(jogador.saldo))
	
	
def teste_apostar(saldo_inserido = 0):
	jogador.validar_aposta()
	print("Novo saldo do jogador após a aposta: {}".format(jogador.saldo))
	
teste_apostar()
