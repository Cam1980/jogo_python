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
personagem_O = fonte_quadrinhos.render('O', True, 'Red') # Criar personagem Y

jogador_atual = personagem_X # Inicializa o jogo com X 

rodadas = 0 # Cor do fundo do cenário
tabuleiro_desenhado = False
coordenada_X = 0
coordenada_Y = 0

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
   
    if coordenada_X > 0 and coordenada_X < 200 and coordenada_Y < 200:
        screen.blit(jogador_atual,(60,30)) # primeiro

    elif coordenada_X >= 200 and coordenada_X < 400 and coordenada_Y < 200:
        screen.blit(jogador_atual,(260,30)) # segundo

    elif coordenada_X >= 400 and coordenada_Y < 200:
        screen.blit(jogador_atual,(460,30)) # terceiro

   # Segunda Linha
    elif coordenada_X < 200 and coordenada_Y >= 200 and coordenada_Y < 400:
        screen.blit(jogador_atual,(60,230)) # quarta

    elif coordenada_X >= 200 and coordenada_X < 400 and coordenada_Y >= 200 and coordenada_Y < 400:
        screen.blit(jogador_atual,(260,230)) # quinto

    elif coordenada_X >= 400 and coordenada_Y >= 200 and coordenada_Y < 400:
        screen.blit(jogador_atual,(460,230)) # sexto

   # Terceira linha
    elif coordenada_X < 200 and coordenada_Y >= 400:
        screen.blit(jogador_atual,(60,430)) # setimo

    elif coordenada_X >= 200 and coordenada_X < 400 and coordenada_Y >= 400:
        screen.blit(jogador_atual,(260,430)) # oitavo

    elif coordenada_X >= 400 and coordenada_Y >= 400:
        screen.blit(jogador_atual,(460,430)) # nono         
  

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
            rodadas = rodadas + 1
            
            if(rodadas >= 10):
                screen.fill('black')
                rodadas = 0
                coordenada_X = 0
                coordenada_Y = 0
                tabuleiro_desenhado = False

            if rodadas != 1: # (!) diferente
                if jogador_atual == personagem_X:
                  jogador_atual = personagem_O
                else:
                    jogador_atual = personagem_X
            else:
                    jogador_atual = personagem_X  
            faz_jogada()        
    
    if tabuleiro_desenhado == False:
       desenha_tabuleiro(5,'yellow') 
       tabuleiro_desenhado = True


   

   

   


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit() 