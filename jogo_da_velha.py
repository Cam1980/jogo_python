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
personagem_Y = fonte_quadrinhos.render('O', True, 'Red') # Criar personagem Y
apresenta_personagem = 0 # Cor do fundo do cenário
X = 0
Y = 0

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
            X = click_pos[0]
            Y = click_pos[1]
            apresenta_personagem = apresenta_personagem + 1
            if(apresenta_personagem >= 10):
                screen.fill('black')
                apresenta_personagem = 0
    
     
    # Desenhar Tabuleiro    
    # Linhas Verticais
    #                                  origem        destino
    #                                    (x   y)    (y     x)
    pygame.draw.line(screen, 'white',(200, 0), (200, 600), 5) 
    pygame.draw.line(screen, 'white',(400, 0), (400, 600), 5)
    # Linhas Horizontais
    pygame.draw.line(screen, 'white',(0, 200), (600, 200), 5)
    pygame.draw.line(screen, 'white',(0, 400), (600, 400), 5)

   #Primeira linha
   # posição dos personagens no tabuleiro (X=O, Y)
   
    if X > 0 and X 
    < 200 and Y < 200:
        screen.blit(personagem_X,(60,30)) # primeiro

    elif X >= 200 and X < 400 and Y < 200:
        screen.blit(personagem_Y,(260,30)) # segundo

    elif X >= 400 and Y < 200:
        screen.blit(personagem_Y,(460,30)) # terceiro

   # Segunda Linha
    elif X < 200 and Y >= 200 and Y < 400:
        screen.blit(personagem_X,(60,230)) # quarta

    elif X >= 200 and X < 400 and Y >= 200 and Y < 400:
        screen.blit(personagem_Y,(260,230)) # quinto

    elif X >= 400 and Y >= 200 and Y < 400:
        screen.blit(personagem_Y,(460,230)) # sexto

   # Terceira linha
    elif X < 200 and Y >= 400:
        screen.blit(personagem_X,(60,430)) # setimo

    elif X >= 200 and X < 400 and Y >= 400:
        screen.blit(personagem_Y,(260,430)) # oitavo

    elif X >= 400 and Y >= 400:
        screen.blit(personagem_Y,(460,430)) # nono         
  

   

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit() 