import pygame

pygame.init() # inicializar



tamanho_da_tela = (800,800)
tela = pygame.display.set_mode(tamanho_da_tela) # Cria a tela do jogo e guarda na variável
pygame.display.set_caption("Jogo do Bloco") # Titulo do jogo

tamanho_da_bola = 15
bola = pygame.Rect(100, 500, tamanho_da_bola, tamanho_da_bola) # Esse Rect é uma classe para criar o retagulo

tamanho_do_jogador = 100
#                  Esquerda, Topo, largura,    altura
jogador = pygame.Rect(0,750, tamanho_do_jogador, 15)

qtd_bloco_por_linha = 8
qtd_linha_de_bloco = 5
qtd_de_blocos = qtd_bloco_por_linha * qtd_linha_de_bloco

def criar_blocos(qtd_linha_de_bloco, qtd_bloco_por_linha): # Criar os blocos e devolver a lista com todos os blocos
    altura_da_tela = tamanho_da_tela[1]
    largura_da_tela = tamanho_da_tela[0]
    largura_do_bloco = largura_da_tela / 8 - 5
    altura_do_bloco = 15
    blocos =  []  
# Criar blocos
    for j in range(qtd_linha_de_bloco):
        for i in range(qtd_bloco_por_linha):
            #Cria o bloco
            # bloco = pygame.Rect(0, 0, largura_do_bloco, altura_do_bloco) # Cria os blocos um encima do outro
            bloco = pygame.Rect(i * (largura_do_bloco + 5), j *(altura_do_bloco +10) , largura_do_bloco, altura_do_bloco) # aqui ele cria os blocos separados com 5 de distancia
            #adiciona o bloco na lista de blocos
            blocos.append(bloco)


    return blocos #Criar blocos


cores = {"branca": (255,255,255),
        "preta": (0,0,0),
        "amarela" : (255, 255, 0),
        "azul" : (0,0,255),
        "verde": (0,255,0),
        "rosaaloma": (255,0,255),
        "amareloaloma": (228,245,11),
        "azulzinho": (2,219,248)
        }

fim_de_jogo = False
pontuacao = 0
movimento_da_bola = [1,1] # Feito com lista pois é preciso mudar o movimento durante o jogo
# Criar as funções do jogo


# Desenhar na tela - criado uma função para chamar a função durante o codigo
def desenhar_inicio_do_jogo():
    tela.fill(cores["preta"])
    pygame.draw.rect(tela, cores["rosaaloma"], jogador) # Desenhar o jogador # Esse rect é uma função desenhar na tela
    pygame.draw.rect(tela,cores["amareloaloma"], bola)


def desenhar_blocos_natela(bloco):
    for bloco in blocos:
        pygame.draw.rect(tela, cores["azulzinho"], bloco)




# Criar as regras do jogo
def movimentar_jogador(evento): # Precisa receber  como parâmetro a telca que o usuario clicou
    if evento.type == pygame.KEYDOWN:
        print("Andou com o jogador") # teste de setas
        if evento.key == pygame.K_RIGHT: # Seta para esquerda
            if (jogador.x + tamanho_do_jogador) < tamanho_da_tela[0]:
                jogador.x = jogador.x + 5
        if evento.key == pygame.K_LEFT: # Seta para direita
            if jogador.x > 0:
                jogador.x = jogador.x - 5

def movimentar_bola(bola):
    movimento = movimento_da_bola
    bola.x = bola.x + movimento[0]
    bola.y = bola.y + movimento[1]

    if bola.x <= 0:
        movimento[0] = -movimento[0]
    if bola.y <= 0:
        movimento[1] = -movimento[1]
    if bola.x + tamanho_da_bola >= tamanho_da_tela[0]:
        movimento[0] = - movimento[0]
    if bola.y + tamanho_da_bola >= tamanho_da_tela[1]:
            movimento[1] = -movimento[1]
    
    



    return movimento





blocos = criar_blocos(qtd_linha_de_bloco, qtd_bloco_por_linha) # variável que recebe a criação dos blocos "def criar_blocos(qtd_bloco_linha, qtd_linha_bloco):"


# Criar o loop do jogo
while not fim_de_jogo:
    desenhar_inicio_do_jogo()
    desenhar_blocos_natela(blocos)
    for evento in pygame.event.get():    
        if evento.type == pygame.QUIT:
            fim_de_jogo = True

        movimentar_jogador(evento)
        novimento_bole_return = movimentar_bola(bola)

    pygame.time.wait(1) # Atualizar a tela a cada milissegundo - espera 1 milissegundo entre cada quadro
    pygame.display.flip()

pygame.quit()
