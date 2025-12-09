import pygame
import sys
import random
import json

pygame.init()

caminho_combinacao = "utils/combinacoes_vencedoras.json"
caminho_pontos = "utils/multiplicador_pontos.json"

combinacoes_possiveis = []
pontuacoes = []

# abrir arquivos - combinacoes possíveis
with open(caminho_combinacao, "r") as file:
    combinacoes = json.load(file)

     # gerar lista de combinacoes
    for i in range(len(combinacoes)):
        combinacoes_possiveis.append(combinacoes["combinacao{}".format(i+1)])

with open(caminho_pontos, "r") as file:
    pontos = json.load(file)

    #gera lista dos pontos
    for i in range(len(pontos)):
        pontuacoes.append(pontos["combinacao{}".format(i+1)])

#################################################################################

def gerar_pontuacao(jogada_escolhida, saldo_inserido):
    if jogada_escolhida in combinacoes_possiveis:
        for indice, elemento in enumerate(combinacoes_possiveis):
            if jogada_escolhida == elemento:
                #return indice
                multiplicador_ponto = pontuacoes[indice]
                return saldo_inserido * multiplicador_ponto # retorna o saldo final do jogador na aposta


print(combinacoes_possiveis)
print(pontuacoes)
#gerar_pontuacao([3, 3, 3], 5)


#caminho = "../utils/combinacoes_vencedoras.json"

class Maquina:

    def __init__(self):
        self.jogada_vencedora = 0
        self.contador = 0
        self.combinacao_escolhida = [] # depois testar com 0

    def zerar_maquina(self):
        self.contador = 0
        self.jogada_vencedora = 0
        self.combinacao_escolhida = []
        self.saldo_inserido = 0

    def gerar_jogada_perdedora(self):
        lista = [1, 2, 3]
        lista_nova = random.sample(lista, len(lista))
        #print(lista_nova)
        return lista_nova

    def gerar_jogada_vencedora(self):
        self.jogada_vencedora = random.randint(1, 4)
        return self.jogada_vencedora
    
    def escolher_combinacao(self, caminho = "utils/combinacoes_vencedoras.json"):
        """
        Essa função escolhe a combinação que o usuário receberá na jogada em que for vencedor
        """
        with open(caminho, "r") as file:
            combinacoes = json.load(file) # combinações agora é um dicionario em python
            combinacao = random.choice([combinacoes["combinacao1"], combinacoes["combinacao2"], combinacoes["combinacao3"]]) # escolhe a combinação
            self.combinacao_escolhida = combinacao
            return combinacao

    def gerador_de_aposta(self, caminho = "utils/combinacoes_vencedoras.json"): # combina as jogadas
        self.gerar_jogada_vencedora()
        self.escolher_combinacao(caminho)

    def jogada(self, caminho = "utils/combinacoes_vencedoras.json"):
        todas_combinacoes = []
        #print(self.jogada_vencedora, self.combinacao_escolhida)

        self.gerador_de_aposta(caminho) # aqui ja alterou a configuração da máquina

        while self.contador < self.jogada_vencedora:

            self.contador += 1
            todas_combinacoes.append(self.gerar_jogada_perdedora())

        # jogada vencedora
        todas_combinacoes.append(self.combinacao_escolhida)
        #print("Lista: {}".format(todas_combinacoes))
        self.zerar_maquina()
        return todas_combinacoes
    
    def aposta(self):
        rodada = self.jogada()
        return rodada               # retorna a lista com as combinacoes perdedoras e a ganhadora por último. Chamar essa função no front, pfv não esquecer!


m  = Maquina()
print(m.jogada())


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
        
'''''''''
user = Jogador("Tester", 2)
print(f"Saldo atual: {user.saldo}")
user.apostar()
print(f"Saldo após a aposta: {user.saldo} e Saldo inserido: {user.saldo_inserido}")
'''''''''

# user = Jogador('Tester', 100)
# user.apostar()


# Config da tela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Exemplo de Telas")

#imagens
simbolos_imgs = [
    pygame.image.load("java.png"),
    pygame.image.load("javascript.png"),
    pygame.image.load("py.png")
]

simbolos_imgs = [
    pygame.transform.scale(img, (100, 100))
    for img in simbolos_imgs
]
imgs_atual=[
    random.choice(simbolos_imgs),
    random.choice(simbolos_imgs),
    random.choice(simbolos_imgs)
]

#painel
pygame.draw.rect(tela, (200, 0, 0), (80, 130, 450, 150), border_radius=20)   
pygame.draw.rect(tela, (255, 255, 0), (80, 130, 450, 150), 8, border_radius=20) 

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (50, 100, 255)

# Fonte
fonte = pygame.font.Font(None, 40)

tela_atual = "menu" 

def caixa_imgs(x, y, img):
    # fundo branco
    pygame.draw.rect(tela, (255, 255, 255), (x, y, 110, 110), border_radius=10)
    # borda preta
    pygame.draw.rect(tela, (0, 0, 0), (x, y, 110, 110), 5, border_radius=10)
    # imagem dentro com margem
    tela.blit(img, (x + 5, y + 5))

def desenhar_botao(texto, x, y, largura, altura):
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()

    # Verificar se o mouse está em cima do botão
    if x < mouse[0] < x + largura and y < mouse[1] < y + altura:
        cor = (150, 150, 255)
        if clique[0] == 1:
            return True
    else:
        cor = azul

    pygame.draw.rect(tela, cor, (x, y, largura, altura))
    texto_render = fonte.render(texto, True, preto)
    tela.blit(texto_render, (x + 10, y + 10))

    return False
maquina=Maquina()
jogador=Jogador('Player 1',100)

while True:
    tela.fill(branco)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #tela1
    if tela_atual == "menu":
        if desenhar_botao("Iniciar", 250, 300, 120, 60):
            tela_atual = "segunda"
            pygame.time.delay(200)

        texto1 = fonte.render("Bem vindo ao jogo!", True, preto)
        tela.blit(texto1, (200, 50))

    #tela2
    elif tela_atual == "segunda":
        texto2 = fonte.render("CAÇA-NÍQUEL", True, preto)
        tela.blit(texto2, (200,50))
        
        tela.blit(imgs_atual[0], (100, 150))
        tela.blit(imgs_atual[1], (250, 150))
        tela.blit(imgs_atual[2], (400, 150))
        
        caixa_imgs(100, 150, imgs_atual[0])
        caixa_imgs(250, 150, imgs_atual[1])
        caixa_imgs(400, 150, imgs_atual[2])
        
        if desenhar_botao("Girar", 250, 300, 120, 50):
            rodada=maquina.aposta()
            ultima=rodada[-1]
            for i in range(15):
                imgs_atual=[
                    random.choice(simbolos_imgs),
                    random.choice(simbolos_imgs),
                    random.choice(simbolos_imgs)
                ]
            pygame.time.delay(200)
        if desenhar_botao("Voltar", 250, 350, 120, 50):
            tela_atual = "menu"
            pygame.time.delay(200)
            imgs_atual=[simbolos_imgs[i-1] for i in ultima]
            
    pygame.display.update()
