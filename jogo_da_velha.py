# Example file showing a basic pygame "game loop"
import pygame # importa a biblioteca pygame para script

# pygame setup configuração
pygame.init() # inicio do jogo
pygame.font.init() # Inicialização do pacote de fontes no pygame

screen = pygame.display.set_mode((600, 600)) # modo de configuração do jogo
pygame.display.set_caption('Jogo da Velha') # definir legenda do jogo
clock = pygame.time.Clock() #biblioteca de tempo

fonte_quadrinhos = pygame.font.SysFont('Comic Sans MS', 100) # Importa fonte
running = True # A variável booleana que pode acompanhar uma chamada
personagem_X = fonte_quadrinhos.render('X', True, 'Red') # Criar personagem X
personagem_O = fonte_quadrinhos.render('O', True, 'Blue') # Criar personagem Y

jogador_atual = personagem_X # Inicializa o jogo com X 

rodadas = 0 # Cor do fundo do cenário
tabuleiro_desenhado = False
coordenada_X = 0
coordenada_Y = 0
q1 = ''
q2 = ''
q3 = ''
q4 = ''
q5 = ''
q6 = ''
q7 = ''
q8 = ''
q9 = ''

def desenha_tabuleiro(espessura, cor):
    
    # Desenhar Tabuleiro    
    # Linhas Verticais
    #                              origem     destino
    #                             (x   y)    (y   x)
    pygame.draw.line(screen, cor,(200, 0), (200, 600), espessura) 
    pygame.draw.line(screen, cor,(400, 0), (400, 600), espessura)
    
    # Linhas Horizontais
    pygame.draw.line(screen, cor,(0, 200), (600, 200), espessura)
    pygame.draw.line(screen, cor,(0, 400), (600, 400), espessura)

def faz_jogada():
    
    # Primeira linha
   # posição dos personagens no tabuleiro (X=O, Y)
    global q1,q2,q3,q4,q5,q6,q7,q8,q9
    status = True

    if q1== '' and coordenada_X > 0 and coordenada_X < 200 and coordenada_Y < 200:
        screen.blit(jogador_atual,(60,30)) # primeiro
        q1 = jogador_atual

    elif q2== '' and coordenada_X >= 200 and coordenada_X < 400 and coordenada_Y < 200:
        screen.blit(jogador_atual,(260,30)) # segundo
        q2 = jogador_atual

    elif q3== '' and coordenada_X >= 400 and coordenada_Y < 200:
        screen.blit(jogador_atual,(460,30)) # terceiro
        q3 = jogador_atual

   # Segunda Linha
    elif q4== '' and coordenada_X < 200 and coordenada_Y >= 200 and coordenada_Y < 400:
        screen.blit(jogador_atual,(60,230)) # quarta
        q4 = jogador_atual

    elif q5== '' and coordenada_X >= 200 and coordenada_X < 400 and coordenada_Y >= 200 and coordenada_Y < 400:
        screen.blit(jogador_atual,(260,230)) # quinto
        q5 = jogador_atual

    elif q6== '' and coordenada_X >= 400 and coordenada_Y >= 200 and coordenada_Y < 400:
        screen.blit(jogador_atual,(460,230)) # sexto
        q6 = jogador_atual

   # Terceira linha
    elif q7== '' and coordenada_X < 200 and coordenada_Y >= 400:
        screen.blit(jogador_atual,(60,430)) # setimo
        q7 = jogador_atual

    elif q8== '' and  coordenada_X >= 200 and coordenada_X < 400 and coordenada_Y >= 400:
        screen.blit(jogador_atual,(260,430)) # oitavo
        q8 = jogador_atual

    elif q9== '' and coordenada_X >= 400 and coordenada_Y >= 400:
        screen.blit(jogador_atual,(460,430)) # nono 
        q9 = jogador_atual 
    else:
        status = False     
    return status      
  

while running:
    # poll for events (começo do evento)
       # pygame.QUIT event means the user clicked X to close your window
       # Evento pygame.QUIT significa que o usuário clicou no X para fechar sua janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Clicou')   
            click_pos = pygame.mouse.get_pos() # a posição do mouse quando houver o evento click
            print('eixo X:', click_pos[0])
            print('eixo Y:', click_pos[1])
            coordenada_X = click_pos[0]
            coordenada_Y = click_pos[1]
            if(rodadas >= 9):
                screen.fill('black')
                rodadas = 0
                coordenada_X = 0
                coordenada_Y = 0
                tabuleiro_desenhado = False
            if(faz_jogada()):
                rodadas = rodadas + 1
                if jogador_atual == personagem_X:
                   jogador_atual = personagem_O
                else:
                     jogador_atual = personagem_X
            
                      
                  
    
    if tabuleiro_desenhado == False:
       desenha_tabuleiro(5,'yellow') 
       q1 = ''
       q2 = ''
       q3 = ''
       q4 = ''
       q5 = ''
       q6 = ''
       q7 = ''
       q8 = ''
       q9 = ''
       tabuleiro_desenhado = True

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit() 
# (!) diferente